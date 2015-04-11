#!/usr/bin/env python

import os

target = open('.convert', 'r')
excel_filename = target.read().rstrip('\n')
#print excel_filename

cmd = 'zip %s -x \*.py -r *' % excel_filename

os.system(cmd)
