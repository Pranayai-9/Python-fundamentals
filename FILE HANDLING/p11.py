#Shelve module
from pathlib import Path
import os
import shelve
get = shelve.open('mydata')
cats = ['lol', 'pop', 'ioi']
get['cats'] = cats
get.close() 

#Reading the database
import shelve

db = shelve.open('mydata')

print(db['cats'])

db.close()
