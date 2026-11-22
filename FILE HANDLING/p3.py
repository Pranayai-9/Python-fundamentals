#Relpath()
from pathlib import Path
import os
result = os.path.relpath('C:\\Users\\ASUS\\python-fundamentals', 'C:\\Users')
print(result)

#Abspath()
from pathlib import Path
import os
result = os.path.abspath('.\\python-fundamentals')
print(result)


#Isabs() 
from pathlib import Path
import os
result = os.path.isabs('C:\\Users\\ASUS\\python-fundamentals')
print(result)
