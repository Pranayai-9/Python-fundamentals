from pathlib import Path
import os
result = Path('C:\\Users\\ASUS\\Desktop')
print(list(result.glob('*.txt'))) 
print(list(result.glob('*.?x?')))
for file in list(result.glob('*.?x?')):
    print(file)
