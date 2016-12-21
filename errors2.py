from models import *
file = None
try:
    with open('profiles.csv','r') as file:
        for line in file:
            print line
