
current: run-windowed

run-windowed:
	./windowed.py
	
	#gnome-terminal -x sh -c "./windowed.py; bash"

run-windowed-xnest:
	#start xnest to debug without leaving the session that you are logged in to
	#Xnest :3 -geometry 800x+600+200 -name "Xnest Test Window" 2> /dev/null
	DISPLAY=:3 ./windowed.py


copy:
	cp windowed.py /home/typist/gui/

run:
	gnome-terminal -x sh -c "./main.py; bash"

run1:
	gnome-terminal -x sh -c "./main2.py; bash"

