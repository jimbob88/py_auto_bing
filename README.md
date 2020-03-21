# py_auto_bing ![Python Shield](https://img.shields.io/badge/python-3.8.1-brightgreen)
`py_auto_bing` is a project that automatically completes the bing rewards daily searches, it currently does not complete challenges.

But why choose `py_auto_bing` over something like [this project](https://github.com/JeffHenry/Bing-Search-Bot)?
Well this project uses the latest version of python, and also works with the latest version of Bing (i.e. it still bypasses any filtration system), it also isn't limited by a set number of search terms by using [YouTube Trending](https://www.youtube.com/feed/trending), and scraping the results into a list.

If this software ever stops working feel free to drop me an [issue](https://github.com/jimbob88/py_auto_bing/issues) or an [email](https://github.com/jimbob88).

## Setting `py_auto_bing` up
  First and foremost, one needs to download a version of [python3](https://www.python.org/downloads/), I have personally tested this to work on ![Python Shield](https://img.shields.io/badge/python-3.8.1-brightgreen). 

  Next, one needs to decide whether they want to use Chrome or Firefox, if you are going to use Chrome you need to download the [Chrome WebDriver](https://chromedriver.chromium.org/downloads) and for Firefox you need the [geckodriver](https://github.com/mozilla/geckodriver/releases). Don't forget, you need to choose the version for your system, if unsure just choose win32.
  
  Then, [download py_auto_bing](https://github.com/jimbob88/py_auto_bing/archive/master.zip) and extract it to a folder.
  
  Extract the `Chrome WebDriver` or `geckodriver` file and place it in the same folder as the `main.py` of `py_auto_bing`.
  
  
## How to use py_auto_bing
#### Windows
Navigate to where you extracted `py_auto_bing`, and press <kbd>Shift + Right Click</kbd> in the folder, you should see an option in this menu open Powershell, click this and if you installed [Python to your path](https://datatofish.com/add-python-to-windows-path/), you can then type `python -m pip install -r requirements.txt --user`, to install all the modules `py_auto_bing` uses. Then type `python main.py -h`. 

#### Using the command line interface
After running the prior command one should see something like this:
```
> pythom .\main.py -h
usage: main.py [-h] -u USERNAME -p PASSWORD [-b BROWSER] [-a AGENT]

Arguments

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Your microsoft account username (generally an email adress) (default: None)
  -p PASSWORD, --password PASSWORD
                        Your microsoft account password (default: None)
  -b BROWSER, --browser BROWSER
                        Your choice of browser, any of these options: Chrome Firefox (default: Firefox)
  -a AGENT, --agent AGENT
                        Your choice of user-agent (allows you to mimic Edge), any of these options: Edge Default
                        (default: Default)
```
If one wishes to use the default configuration, with Firefox & the [Firefox User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent/Firefox) one would type the command:
```
> python main.py -u <USERNAME> -p <PASSWORD>
```
Obviously replacing `<USERNAME` & `<PASSWORD>` with one's username and password.

If you want to use Chrome / Chromium instead of Firefox, one would type:
```
> python main.py -u <USERNAME> -p <PASSWORD> -b chrome
```

If you want to use the Edge User-Agent, so as to mimic Edge and possibly get extra points:
```
> python main.py -u <USERNAME> -p <PASSWORD> -a edge
```

Wait for the program to finish its work, you should see an instance of the browser appear and login to your account then start searching for those epic trending videos ;), then close the browser instance!

Happy hacking,
Jim
