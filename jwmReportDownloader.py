#!/usr/bin/env python

# Copyright 2019 Simon Zigelli
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pathlib import Path
import getopt
import sys
import time
import os


def download_wait(path):
    seconds = 0
    wait_download = True
    while wait_download and seconds < 20:
        time.sleep(1)
        wait_download = False
        for file_name in os.listdir(path):
            if file_name.endswith('.crdownload'):
                wait_download = True
        seconds += 1
    return seconds


def usage():
    print("jvmReportDownloader")
    print("Copyright 2019 Simon Zigelli")
    print("")
    print("Usage: jvmReportDownloader --user=<User name> --password=<Password> --project=<Project>")
    print("")
    print("Arguments:")
    print("--user or -u        User name (required)")
    print("--password or -p    Password (required)")
    print("--project or -r     Project ID (required)")
    print("")
    print("--start-date or -s  Start date (<Year>M<Month>, e.g. 2019M03 for March 2019)")
    print("--end-date or -e    End date (<Year>M<Month>, e.g. 2019M03 for March 2019)")
    print("--directory or -d   Directory for reports-files")
    print("")
    print("--help or -h        This message")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:p:r:s:e:d:", ["help", "user=", "password=", "project=",
                                                                   "start-date=", "end-date=", "directory="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    if not opts:
        usage()
        sys.exit(0)

    user, password, project = "", "", ""
    directory = os.getcwd()
    start_month = None
    start_year = None
    end_month = None
    end_year = None

    for o, a in opts:
        if o in ("-u", "--user"):
            user = a
        elif o in ("-p", "--password"):
            password = a
        elif o in ("-r", "--project"):
            project = a
        elif o in ("-s", "--start-date"):
            if 'M' not in a:
                sys.exit(2)
            (start_year, start_month) = a.split('M')
            if not check_date(start_month, start_year):
                sys.exit(2)
        elif o in ("-e", "--end-date"):
            if 'M' not in a:
                sys.exit(2)
            (end_year, end_month) = a.split('M')
            if not check_date(end_month, end_year):
                sys.exit(2)
        elif o in ("-d", "--directory"):
            directory = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option %s" % o

    start_date, end_date = get_dates(start_month, start_year, end_month, end_year)

    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": directory,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    browser = webdriver.Chrome(options=options)

    browser.get('https://www.jwmanagement.org/en/signin')

    elem = browser.find_element_by_name('usernameOrEmail')  # Find the search box
    elem.send_keys(user)
    elem = browser.find_element_by_name('password')  # Find the search box
    elem.send_keys(password)
    elem = browser.find_element_by_tag_name('button')
    elem.click()

    WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "navbar")))

    old_file = Path(r'%s\reports.csv')
    if old_file.exists() and old_file.is_file():
        os.remove(r'%s\reports.csv')
    get_reports(browser, directory, project, start_date, end_date)

    browser.quit()


def get_dates(start_month, start_year, end_month, end_year):
    now = datetime.now()
    if start_month is None and end_month is None:
        start_month = now.month
        start_year = now.year
        end_month = start_month
        end_year = start_year
    if start_month is None and end_month is not None:
        start_month = now.month
        start_year = now.year
    if start_month is not None and end_month is None:
        end_month = start_month
        end_year = start_year
    start_date = datetime(month=int(start_month), year=int(start_year), day=1)
    end_date = datetime(month=int(end_month), year=int(end_year), day=1)
    if start_date > end_date:
        tmp = start_year
        start_date = end_date
        end_date = tmp
    return start_date, end_date


def check_date(month, year):
    if not str(year).isnumeric() or not str(month).isnumeric() or not len(str(year)) == 4 \
            or not len(str(month)) == 2 or not int(month) > 0 or not int(month) < 13:
        return False
    return True


def get_reports(browser, directory, project, start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        browser.get('https://www.jwmanagement.org/%s/reports?month=%dM%d' % (project, current_date.year,
                                                                             current_date.month))
        WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.ID, "exportReports")))
        WebDriverWait(browser, 10).until(ec.invisibility_of_element((By.CLASS_NAME, "fa-spinner")))
        elem = browser.find_element_by_id("exportReports")
        elem.click()
        download_wait(directory)
        new_file_name = r'%s\%s_%d_%02d.csv' % (directory, datetime.now().strftime("%Y%m%d"),
                                                current_date.year, current_date.month)
        old_file = Path(new_file_name)
        if old_file.exists() and old_file.is_file():
            os.remove(new_file_name)
        os.rename(r'%s\reports.csv' % directory, new_file_name)
        current_date = current_date + relativedelta(months=+1)


if __name__ == '__main__':
    main()
