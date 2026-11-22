#Writing files
res = open('spam.txt', 'w')
print(res.write('Hello world\n'))
res.close()
res = open('spam.txt', 'a')
print(res.write('Hey there'))
res.close() 

res = open('spam.txt')
content = res.read()
res.close()
print(content)

