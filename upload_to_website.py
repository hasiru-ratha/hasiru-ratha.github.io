import os
import time
import git
from shutil import copyfile

fileContents1 = \
"""+++
draft = false
"""
fileContents2 = """
showonlyimage = true
+++
"""

g = git.cmd.Git(os.getcwd())

for i in range(3,10):
    srcFilePathName = 'C:/Users/Vkrishnaswam/Downloads/HasiruRathaImages/HR%d.jpeg' % i
    dstFilePathName = 'C:/Users/Vkrishnaswam/Projects/hasiru-ratha.github.io/static/img/HR%d.jpeg' % i
    copyfile(srcFilePathName, dstFilePathName)
    g.add(dstFilePathName)
    f = open('C:/Users/Vkrishnaswam/Projects/hasiru-ratha.github.io/content/portfolio/HR%d.md' % i, 'w+')
    f.write(fileContents1)
    f.write("image = \"img/HR%d.jpeg\"" % i)
    f.write(fileContents2)
    g.add('C:/Users/Vkrishnaswam/Projects/hasiru-ratha.github.io/content/portfolio/HR%d.md' % i) 


    


