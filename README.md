Typewriter
========
A simple gui for a typewriter like experience.

This program is ment to be excecuted without a window-manager.



Dependencies
--------------------
sudo apt-get --reinstall install ttf-mscorefonts-installer python3 



Start as default on boot
Edit `~/.dmrc`

And change it to 

```
[Desktop]
Session=typist
```


Create a file named /usr/share/xsessions/typist.desktop
```

[Desktop Entry]
# Starts de 
Name=Typist
Exec=/home/pi/gui/typewriter-gui/start.sh
# Icon=
Type=Application
```

Change the line in Exec to point to your start.sh