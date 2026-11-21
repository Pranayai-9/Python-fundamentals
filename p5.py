from pathlib import Path
import os
result = Path('C:\\Users\\ASUS\\Desktop\\api.txt')

print(result.anchor)
print(result.parent)
print(result.drive)
print(result.stem)
print(result.suffix)

print(os.path.dirname(result))
print(os.path.basename(result)) 