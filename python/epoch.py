
# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime

if __name__ == "__main__":
    print datetime(*time.localtime(int(sys.argv[1]) / 1000)[:6]).strftime("%Y/%m/%d %H:%M:%S")
