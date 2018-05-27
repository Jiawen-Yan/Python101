sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
sudo apt-get update

sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
sudo pip3 install Twisted==18.4.0
sudo pip3 install cffi==1.11.5 
sudo pip3 install cryptography==2.2.2 
sudo pip3 install scrapy --user
