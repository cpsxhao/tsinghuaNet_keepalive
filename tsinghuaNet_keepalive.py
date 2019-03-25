import os
import time
import platform
import splinter

from argparse import ArgumentParser
from retrying import retry, RetryError


parser = ArgumentParser()

parser.add_argument(
    '-u', '--username',
    help='your username for tsinghua network',
    dest='username'
)
parser.add_argument(
    '-p', '--password',
    help='your password for tsinghua network',
    dest='password'
)
parser.add_argument(
    '-w', '--website',
    help='which website to ping for checking if network is alive (DEFAULT: www.baidu.com)',
    dest='website',
    default='www.baidu.com')
parser.add_argument(
    '-t', '--time-interval',
    help='how many seconds between two pings (DEFAULT: 60)',
    type=int,
    dest='time_interval',
    default='60'
)
parser.add_argument(
    '-b', '--browser',
    help='the web browser for using, must have been installed \n\t 1) usable browser such as firefox and chrome;\n\t 2) corrsponding drivers, such as geckodriver for firefox and chromedriver for chrome, in the right version\n(DEFAULT: chrome)',
    dest='browser',
    default='chrome'
)
parser.add_argument(
    '-bd', '--browser-driver',
    help='The executable path of browser driver for use. If the driver is in PATH, this argument can be omitted.',
    dest='browser_driver',
    default=None
)


def check_alive(url='www.baidu.com'):
    # check system
    plt = platform.system()
    
    # ping a website to check if network is alive
    if plt == 'Windows':
        cmd = 'ping ' + url + ' -n 1 | find "TTL"'
    else:
        cmd = 'ping ' + url + ' -c 1 | grep "ttl"'

    exit_code = os.system(cmd)

    return True if exit_code == 0 else False


def retry_login(result):
    if check_alive(result[1].website):
        return False
    else:
        if result[0] == 0:
            print('Unknown issue. Maybe wrong username or password. Retrying ...')
        elif result[0] == 1:
            print('Cannot access http://info.tsinghua.edu.cn. Check your network connection. Retrying ...')
        elif result[0] == 2:
            print('Elements not found. Maybe you have logged into tsinghua network. Retrying ...')
        else:
            raise NotImplementedError
        return True
        



@retry(stop_max_attempt_number=5, wait_fixed=1, retry_on_result=retry_login)
def re_login(args, browser):     
    # According to Tsinghua ITS, users are recommanded to use info.tsinghua.edu.cn in both wired and wireless networks to be redirected to login page.
    browser.visit('http://info.tsinghua.edu.cn/')
    time.sleep(0.5)
    browser.reload()
    time.sleep(0.5)
    if 'university' not in browser.title and 'University' not in browser.title:
        # Cannot access http://info.tsinghua.edu.cn
        return 1, args

    try:
        browser.fill('uname', args.username)
        time.sleep(0.5)
        browser.fill('pass', args.password)
        time.sleep(0.5)
        browser.find_by_name('connect').click()
        #input("DEBUG mode. Press Enter to continue...")
        time.sleep(1)
    except splinter.exceptions.ElementDoesNotExist:
        # Elements not found. 
        return 2, args

    return 0, args


def main():

    args = parser.parse_args()
    
    while (True):
        # check if network is alive
        if check_alive(url=args.website):
            print('\n')
            time.sleep(args.time_interval)
        else:  # network is not working
            print('Lost Internet access. Trying to re-login ...')
            if args.browser_driver is None:
                browser = splinter.Browser(driver_name=args.browser, headless=True)
            else:
                browser = splinter.Browser(driver_name=args.browser, executable_path=args.browser_driver, headless=True, set_page_load_timeout=5)
            
            try:
                re_login(args, browser)
            except RetryError:
                print('Login failed.\n')
                continue
            finally:
                browser.quit()

            print('\n')
            time.sleep(max(args.time_interval - 4, 0))
            

if __name__ == '__main__':
    main()


    




