# tsinghuaNet_keepalive
A toy tool for keeping your tsinghua network alive.

## Story
Network at Tsinghua University has so many pretty good features, such as static IP addresses in dormitory, stable IPv6 connection, free access to lots of paper databases (Thank you, tsinghua library!). Therefore you may want to put your computer in your dormitory as a jump server, so that you can use tsinghua network when you are outside of tsinghua.  

There are more reasons for using a jump server in tsinghua network. One day, my friend Bowen, told me he had to go to his lab at 11pm, just for checking his running experiments on the computation server. I was so confused why he did't connect to his server remotely at dormitory, and he told me the computation servers in his lab only support connections from LAN, so he has to leave his comfortable bed, put down his favorite game *Srike of Kings* and go into the cold winter night of Beijing every time he would like to check his experiments.

Bowen needs to use his working computer, which is in the same LAN as his computation server, to jump to his server. However, in most buildings, tsinghua network needs a website-based log-in after you connect to it, and you will log out automatically if you have been online for too long or you have exceeded the maximum online number of your account. Once you log out, the only way to re-login is to open the authentication website and type in your username and passport. To help Bowen get more time for watching videos on *Bilibili* and playing *Srike of Kings*, I wrote this script for checking Internet connection, and log in automantically once you log out of Tsinghua Network .

## Requirments
### Python
python 3

### Python Packages:  
**Splinter**:  
`pip install splinter`  

**Retrying**:  
`pip install retrying`

You may need to run `pip install --upgrade pip` before installing these packages.

### Web browser and its driver
This script supports **Google Chrome** and **Mozilla Firefox**. The corresponding dirvers are also required.  
* **Chromedriver** (for Google Chrome): http://chromedriver.chromium.org/downloads
* **Geckodriver** (for Mozilla Firefox): https://github.com/mozilla/geckodriver/releases

Note that you can add the driver to your \$PATH\$, or specify the path of your driver with option `-bd PATH`

## Usage

`python tsinghuaNet_keepalive.py [-h] [-u USERNAME] [-p PASSWORD] [-w WEBSITE]
                                [-t TIME_INTERVAL] [-b BROWSER]
                                [-bd BROWSER_DRIVER]`

## Test

I have tested the script on macOS Sierra 10.12, with Python 3.7.0. Please open issues if you find any bugs.

## License

MIT © Hao Li
