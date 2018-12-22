#!/usr/bin/python
import urllib
url = raw_input("Enter url you want to download: ")
webpage = urllib.urlopen(url)
source = webpage.read()
f = open('WebPageDownload.html', 'w')
f.write(source)
f.close
#chrissiepadilla