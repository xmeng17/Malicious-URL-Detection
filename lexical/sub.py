with open('bad_lexical.csv') as f:
    string=f.read()
arr=string.split('\n')
arr=arr[:10000]
result='\n'.join(arr)
with open('bad_sub.csv','w') as f:
    f.write(result)

with open('good_lexical.csv') as f:
    string=f.read()
arr=string.split('\n')
arr=arr[:10000]
result='\n'.join(arr)
with open('good_sub.csv','w') as f:
    f.write(result)
