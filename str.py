string="hello world from Python"
rev=string[::-1]
print(rev)
r=""
for char in rev:
    if char not in r:
        r=r+char
print(r)
letter_count={}
for char in string:
    
        letter_count[char]=letter_count.get(char,0)+1
print("count=",letter_count)
