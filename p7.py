from pathlib import Path 
import os
result = Path('C:\\Users\\ASUS\\Desktop\\product.txt')
print(os.path.getsize(result))
print(os.listdir('C:\\Users\\ASUS\\Desktop'))
totalSize = 0
for filename in os.listdir('C:\\Users\\ASUS\\Desktop'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\ASUS\\Desktop', filename))
print(totalSize)