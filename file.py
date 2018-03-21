import os
import sys
root = '/var/www/js.dev/public_html/pisti/cards'
for item in os.listdir(root):
    fullpath = os.path.join(root, item)
    print fullpath
    os.rename(fullpath, fullpath.replace("vkard [www.imagesplitter.net]-",""))
 