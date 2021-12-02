# Lets-Spam
Ever felt annoyed on being added to unnecessary whatsapp groups or just angry with friends, what about a birthday spam? just clone this repo (and star too) and have fun ¯\\_(ツ)_/¯

#Lets-Spam

I have written a python script, that makes use of Selenium, web automation framework used for testing purposes (not here lmao). 
## Installation

```
pip install selenium
```
## Drivers

We need an instructions file , "drivers" to interact with the browser. For our case, you can get Chrome drivers [here](https://chromedriver.chromium.org/downloads)

To know your Chrome version , got to __Settings > About Chrome > Version__ and download the respective driver for your operating system.
Extract the __chromedriver__ file , preferably at same directory of code. 

## Code Setup

Well i have done most of things for you, but still you may have to modify the code a bit, inorder to make it work properly.
Nah! I am not talking about the _path/to/chromedriver_ , but the xpaths.

XPath in Selenium is an XML path used for navigation through the HTML structure of the page.
> Xpath =  //tag[@Attribute='Value']

Here tag can be divison tag , input tag, button tag etc. Each tag has multiple attributes like ID, name, value, class etc. [This](https://www.perfecto.io/blog/xpath-in-selenium) is a nice tutorial on Xpath in Selenium.
Anyways, all we want now is the class and id of the message typing box and send button. So it may happen in future that whatsapp change these attributes, and then you have to get the keys yourself.

## Getting the keys

[This](https://www.browserstack.com/guide/find-element-by-xpath-in-selenium) and [this](https://www.youtube.com/watch?v=JWRRmw2xRiE&ab_channel=GetSetPython) are nice tutorials for getting the attributes for an element. 

It states that:-
1. Go to the First name tab and right click >> Inspect.
2. On inspecting the web element, it will show an input tag and attributes like class and id.
3. Use the id and these attributes to construct XPath which, in turn, will locate the first name field

![image](https://user-images.githubusercontent.com/75263532/144499076-ec60f50b-a38f-4748-bdc7-fc82a2fb6cc4.png)

Plug these back into the code

## Config File
Last but not the least, you have to create a config file, if you don't want to scan QR code everytime you run the code. You have to provide a path, to store user data, so that next time chrome remember you.
```
Windows: C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Whatsapp
Linux: /home/<username>/.config/google-chrome/Whatsapp
macOS: Users/<username>/Library/Application Support/Google/Chrome/Whatsapp
```
Replace that in config.py. You may have to use double backslash for windows path.

## Note 
This script is just for educational purpose <s>and fun</s>. Any changes you make, do it at your own risk as you may end up spamming at a place where you are not supposed to 

_Speaking from Experience_ :')
