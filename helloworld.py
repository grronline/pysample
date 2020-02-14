#!/usr/bin/env python
import os
import time
USERNAME = os.environ['USERNAME'] 
LOGINID = os.environ['LOGINID']
CMD='export NEWVALUE="WELCOME TO PYTHON"'
RETURNVALUE=os.system(CMD)
print "return value for OS command:"+RETURNVALUE

print "hello world:"+USERNAME+"LOGIID:"+LOGINID
