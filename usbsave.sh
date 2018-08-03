#!/bin/sh

#Exit on error
set -e

#Must be executed as root
mkdir -p /media/usb-typist-drive

if mount | grep /mnt/sda1 > /dev/null; then
	mount /dev/sda1 /media/usb-typist-drive/
else
    echo "drive already mounted"
fi

mkdir -p /media/usb-typist-drive/typewriter

cp $1 /media/usb-typist-drive/typewriter

umount /media/usb-typist-drive


