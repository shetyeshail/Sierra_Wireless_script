# Sierra Wireless Script
## About
A script to scrape data from multiple Sierra Wireless cellular gateways from their web interface using Python and Selenium. Also to upgrade the firmware for multiple devices.    
Created this to collect firmware/model info and to upgrade firmware on multiple devices quickly due to the [ICSA-19-122-03](https://www.us-cert.gov/ics/advisories/ICSA-19-122-03) ICS advisory.

## Progress
- [X] Code to scrape model/firmware data
- [X] Code to import and run on txt file list of URLs
- [X] Code to Update firmware
- [ ] Tested successfully
- [ ] Ready to be used
#### DO NOT USE YET, INCOMPLETE AND UNTESTED!

## How To Run
1) Install Python3 from python.org or your package manager. Eg: ``sudo pacman -S python3``
2) Install pip, a package manager for Python. Eg: ``sudo pacman -S ython-pip``
3) Install selenium: ``pip install selenium``
4) Install the webdriver for whichever browser you want to use from [here](https://www.selenium.dev/documentation/en/selenium_installation/installing_webdriver_binaries/).
5) Clone this repository or download and unzip.
6) Make sure you have a urls.txt file with a list of all the IP addresses of the SiWi cellular gateways in the same folder as the script.
7) Open ``main.py`` and put in the username and password you use for all your devices in their respective fields. Save and exit.
8) Navigate to the directory/folder that you have the script in from your terminal/cmd prompt
9) Run the script with ``python ./main.py``, cross your fingers, and hope it works.
