# wled-segment-bounds-finder
Helps find position of LEDs for setting WLED segments bounds.

"I" developed this to help setting up the segments in my [WLED](https://kno.wled.ge/) devices. Initially I needed this to help with a joke. I wanted to split the christmas tree vertically, with my colors on one side and my wives on the other. However, the strings wrapped around the tree horizontally and don't fall the same every year, so I need determine where the center line is, front and back, at each level. This made it a heck of a lot easier. In the end, I could not use multiple [segments](https://kno.wled.ge/features/segments/), because only 10 are supported. I used an the [mapping](https://kno.wled.ge/advanced/mapping/) feature instead. I mapped the right side as the first 200 LEDs and the left side as the second 200 LEDs, then only needed 2 segments. This tool was still very helpful when developing the mapping definition.

Why did I quote "I" at the beginning?
Well, while I had the need/idea, and I provided all the prompts, I let ChatGPT do all the actual coding. 
Update: Well ChatGPT was being friendly the first round, but was more reluctant as I asked for new features, so, while I asked for these new features, I had to heavily modify/repair the code to make it work. 

## Installation

You can use this by just downloading the html file to your computer and opening it in your browser. You will need to use some kind of server if you want to view it on your phone. Using on a phone is extremely helpful if you are walking around.

## Usage

1. Open the html file in your browser.
2. Enter the name/IP of the WLED device. This can be the local mDNS address set in the [WLED WiFi settings](https://kno.wled.ge/features/settings/).
3. Select the before and after colors. These should be colors that are easy to tell the difference, e.g. red, blue, or green.
4. Set the current endpoint manually, or using the <<, <, > and >> buttons to move it. 
5. Setting the segment length changes the size displayed on either side of the endpoint.
6. The LED strip should update automatically when changes are made, but you can press the button if you think is has not updated.

## Web Server

I've included a simple python script to start a web server and only serve the html file. This can be used to access from your phone so you can walk around while checking segments. The server will default to port 8080.

```
python3 http-server.py
```

You can change the port number.

```
python3 http-server.py 8081
```

