from socket import *
import sys

if ( len(sys.argv) <= 2 ):
    print 'usage : python %s script' % sys.argv[0]
    quit()

if len(sys.argv[1:]) == 2:
    ip = sys.argv[1]
    sport = int(sys.argv[2])
    eport = sport + 1
elif len(sys.argv[1:]) == 3:
    ip = sys.argv[1]
    sport = int(sys.argv[2])
    eport = int(sys.argv[3]) + 1
else:
    exit()
for port in range(sport, eport):
    try:
        s = socket(AF_INET, SOCK_STREAM,0)
        s.settimeout(1)
        s.connect((ip,port))
        print str(port) + ':OK'
        s.close()
    except error, msg:
         print str(port) + ':' + str(msg)
