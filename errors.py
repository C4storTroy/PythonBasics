from models import *
#file = None
try:
    file = open('profiles.csv','r')
    values = file.readline().split(':')
    Profile(*values)
    print('arquiv foi aberto')
    file.close()
except IOError as error:
    print ("IOerror is %s" % error)
except TypeError as error:
    print('TypeError is %s' % error)
finally:
    if(file is not None):
        print('Closing file')
        file.close()
"""
except(IOError,TypeError) as error:
    print ("Error is %s" % error)
"""
