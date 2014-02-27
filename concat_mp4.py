#!/usr/bin/env python
# coding:utf-8

# sudo apt-get -y install gpac

import dircache, os, shlex, sys
from subprocess import Popen, PIPE, STDOUT

def concat_mp4():
    cmd = "MP4Box"
    for file in dircache.listdir("./"):
        ext = os.path.splitext(file)[1]
        if ext == ".mp4":
            cmd += " -cat " + '"' + file + '"'
    cmd += " output.mp4"
    print cmd
    # sys.exit(0)
    p = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE, shell=False)
    stdout_data, stderr_data = p.communicate()
    print stderr_data

    print "finish!!"

if __name__ == '__main__':
    concat_mp4()
