#!/bin/bash

#Exit on error
set -e

#Must be executed as root
sudo mkdir -p /media/usb-typist-drive

usbdrive=/dev/sda1

if [[ ! -e '/dev/sda1' ]] ; then
    echo 'File /dev/sda1 is not there, trying sdb1.'

	if [[ ! -e '/dev/sdb1' ]] ; then
		echo 'sdb1 not found exiting'
		exit
	else
		usbdrive=/dev/sdb1
	fi
fi

# if mountpoint -q /media/usb-typis-drive/ ; then
#     echo "drive already mounted"
# else

{
sudo mount $usbdrive /media/usb-typist-drive/ -o umask=000
} ||  {
	#If exception
	echo failed to mount
}
# fi

mkdir -p /media/usb-typist-drive/typewriter

cp $1 /media/usb-typist-drive/typewriter

sudo umount /media/usb-typist-drive


