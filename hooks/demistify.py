#!/usr/bin/env python

import os

target = open('.convert', 'r')
excel_filename = target.read().rstrip('\n')
#print excel_filename

cmd2 = 'rm -f %s; rm -rf _rels xl docProps *.xml' % excel_filename
os.system(cmd2)

cmd = 'unzip %s' % excel_filename

os.system(cmd)



