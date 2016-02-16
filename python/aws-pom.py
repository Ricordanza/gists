
# -*- coding: utf-8 -*-

import sys
import os
from datetime import datetime

template = """    <dependency>
  		<groupId>{0}</groupId>
  		<artifactId>{1}</artifactId>
  		<version>{2}</version>
  	</dependency>
"""

if __name__ == "__main__":

    argvs = sys.argv

    argc = len(argvs)

    if (argc <= 1):
        print 'usage : python %s script' % argvs[0]
        quit()

    filename_list = []
    print argvs[1]
    for root, dirs, files in os.walk(argvs[1]):
        for file in files:
            if file.endswith("pom.properties"):
                filename_list.append(os.path.join(root, file))

    dependenciy = ""
    for _ in filename_list:
        with open(_, "r") as f:
            lines = f.readlines()
            dependenciy += template.format(
                  lines[3].split("=")[1].rstrip("\n")
                , lines[4].split("=")[1].rstrip("\n")
                , lines[2].split("=")[1].rstrip("\n")
                )

    now = datetime.now()

    with open(now.strftime("%Y%m%d%H%M%S") + "%04d" % (now.microsecond // 1000) + ".txt", "w+") as w:
        w.write(dependenciy)
