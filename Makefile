all:
	@echo "To build GUI, run make gui"

gui:
	pyuic AptOfflineGUI.ui > AptOfflineGUI.py

html:
	man2html apt-offline.8 > apt-offline.html
	
clean:
	rm -f AptOfflineGUI.py
	rm -f *.pyc
	rm -f apt-offline.html
