import os
path = 'C:\\outcome\\examaple\\file'
if not os.path.exists(path):
    os.makedirs(path) 
print('done')

