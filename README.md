# Nessus7proxy
Very quick and dirty PoC for working around the new Nessus API restrictions. 

TODO's: 
- check if page is rendered, using DOM testing examples from http://www.guguncube.com/2760/python-spynner-test-scripts
- check status of scan, use DOM testing examples. Don't start if still running.
- API interface to mimic the old v6 API for programs to access.
- Allow to run headless, without X11 (xvfb http://en.wikipedia.org/wiki/Xvfb)
- Re-create other API functions, most importantly: export functionality
