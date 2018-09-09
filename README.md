# Nessus7download
Very quick and dirty PoC for working around the new Nessus API restrictions to download report 

# Requirements:
- Python 3
- spynner
- python3-pyside, python3-qtpy (debian 9) or just install python3 pyside and pyside-qt4 bindings

To run without X11:
- install xfvb (and then run the program with xfvb-run python downloadreport.py [reportname]


# TODO's: 
- check if page is rendered, using DOM testing examples from http://www.guguncube.com/2760/python-spynner-test-scripts
- Allow to run headless, without X11 (xvfb http://en.wikipedia.org/wiki/Xvfb)
