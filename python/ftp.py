#! /usr/bin/env python

import os, os.path, sys
from ftplib import FTP
from cStringIO import StringIO
from datetime import datetime

"""
upload.py
"""

INP = 'upload.inp'
LOG = 'upload.log'

def is_ascii(fname):
    return fname.split('.').pop() in ('txt', 'htm', 'html', 'css')

def write_log(logfile, str, success):
    log = file(logfile, 'w')
    log.write( ((not success) and  'Error:\n\n' or '') + str)
    log.close()
    success or sys.exit(1)

def server_cd(ftp, path, log_name):
    if path!='HOME':
        stdout = sys.stdout
        for d in path.split('/'):
            sys.stdout = StringIO()
            try:
                ftp.dir()
            except:
                ftp.close()
                write_log(log_name, "Cannot get LIST", False)
                
            if not d in [line.split(' ').pop()
                         for line in sys.stdout.getvalue().split('\n') if line and line[0]=='d']:
                try:
                    ftp.mkd(d)
                except:
                    ftp.close()
                    write_log(log_name, "Cannot make directory on the server: " + d, False)
            try:        
                ftp.cwd(d)
            except:
                ftp.close()
                write_log(log_name, "Cannot change directory on the server: " + d, False)
                
            sys.stdout.close()
        sys.stdout = stdout
        

def put(ftp, ls, log_name):
    for fname in ls:
        fbase = os.path.basename(fname)
        (method, mode) = is_ascii(fbase) and ('storlines', 'r') or ('storbinary', 'rb')
        try:
            f = file(fname, mode)
        except:
            ftp.close()
            write_log(log_name, "Cannot open local file: " + fbase, False)
        try:
            getattr(ftp, method)("STOR " + fbase, f)
        except:
            ftp.close()
            write_log(log_name, "Cannot Transfer local file: " + fbase, False)
            
        f.close()

if __name__ == '__main__':
    dtemp = os.getenv("TEMP") or os.getenv("TMP") or "C:\\"
    log_name = os.path.join(dtemp, LOG)
    os.path.exists(log_name) and os.remove(log_name)
    inp_name = os.path.join(dtemp, INP)
    try:
        inp = file(inp_name)
    except:
        write_log(log_name, "Cannot open input file.", False)
        
    server, user, passw, path, files = eval(inp.read())
    inp.close()
    os.remove(inp_name)

    try:
        ftp = FTP(server)
    except:
        write_log(log_name, "Cannot connect to " + server, False)

    try:
        ftp.login(user, passw)
    except:
        ftp.close()
        write_log(log_name, "Cannot login: " + server, False)
        
    server_cd(ftp, path, log_name)
    put(ftp, files, log_name)
    ftp.quit()
    write_log(log_name,
              "Following files are uploaded successfully at\n%s:\n\n" % datetime.now().isoformat(' ') + \
              "\n".join(files) + "\n",
              True)
