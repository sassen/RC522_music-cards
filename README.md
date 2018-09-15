This project let's you use a 2$ RFID-RC522 to scan RFID tags and play local folders or spotify playlist using pimusicbox or any other mpd server.


It is a adapted version of [music-card](https://github.com/fsahli/music-cards) and is using [python-mpd2](https://github.com/Mic92/python-mpd2) and [SPI-Py](https://github.com/lthiery/SPI-Py)



First, you need to enable SPI for your Raspberry Pi Zero. Go to configuration settings via
```
raspi-config
```
Select Interfacing Options then SPI. Select Yes when prompted. After that, reboot your Pi, if you can't find the option you have to enable it with the config.txt
```
sudo nano /boot/config.txt
```

Find this line and change it to on:
```
dtparam=spi=on
```


Next, install Python 2.7 dev using:
```
sudo apt-get install python2.7-dev
```
Then download and install the special SPI tool for python either with git or with wget

```
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
```
or
```
wget https://github.com/lthiery/SPI-Py/archive/master.zip

unzip master.zip

cd ./SPI-Py-master
```
then install it by

```
sudo python setup.py install
```

Next you have to install python-mpd2 by pip
```
pip install python-mpd2
```
or from source here

```
wget https://github.com/Mic92/python-mpd2/archive/master.zip

unzip master.zip

cd ./python-mpd2-master

python setup.py install
```
