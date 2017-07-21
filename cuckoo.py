#!/usr/bin/python

# -*- coding: utf-8 -*-
import re
import sys

#modify by xuyuu
sys.path.insert(0, "/root/Django-1.8.4")

from cuckoo.main import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
