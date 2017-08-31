#https://askubuntu.com/questions/148383/how-to-resolve-dpkg-error-processing-var-cache-apt-archives-python-apport-2-0
#sudo dpkg -i --force-overwrite /var/cache/apt/archives/libpcre3-dev_2%3a8.38-3.1_amd64.deb

sudo dpkg -i --force-overwrite $1
sudo apt-get -f install
