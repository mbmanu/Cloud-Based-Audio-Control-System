# CLOUD-BASED AUDIO CONTOL SYSTEM
Mini project built using Raspberry Pi, MQTT service, and Adafruit Cloud.

## Setup
- [Python 3](https://www.python.org/downloads/)
- Update the Raspberry Pi and Python:
```
    $ sudo apt update
    $ sudo apt upgrade -y
    $ sudo pip3 install --upgrade setuptools
```
- Install Adafruit IO library:
```
    $ sudo pip3 install adafruit-io
```
- Install pygame library:
```
    $ pip3 install pygame
```
- In subscriber.py script, change the ADAFRUIT_IO_KEY, ADAFRUIT_IO_USERNAME, and FEED_ID as mentioned in [Adafruit IO](https://io.adafruit.com/) cloud.
```
ADAFRUIT_IO_KEY = 'YOUR_API_KEY'
ADAFRUIT_IO_USERNAME = 'YOUR_ADAFRUIT_IO_USERNAME'
FEED_ID = 'YOUR_FEED_ID'
```
## Run
```
$ python3 subscribe.py
```
Now, send any value from the feed, and the song assigned to the value will be played on the Raspberry Pi.
This can be further extended to voice-control music player by interfacing IFTTT to the Adafruit IO cloud.
