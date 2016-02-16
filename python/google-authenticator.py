#!/usr/bin/python

import hmac, base64, struct, hashlib, time, os, sys

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(h[19]) & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time())//30)

if( len(sys.argv) > 1):
  secret = sys.argv[1]

elif( os.path.exists( os.environ["HOME"] + "/.google_authenticator" )):
  f = open( os.environ["HOME"] + "/.google_authenticator" )
  secret = f.readline().replace('\n','')
else:
  print sys.argv[0] + " SECRETKEY"
  exit(-1)


#for i in xrange(1, 10):
#    print i, get_hotp_token(secret, intervals_no=i)

print get_totp_token(secret)

