#Writing and reading files
from pathlib import Path
import os
p = Path('spam.txt')
print(p.write_text('Hey there its whatsapp!!'))
print(p.read_text())

result = open(Path.cwd() / 'spam.txt') 
res = result.read()
print(result)
print(res) 