import lexical as lx


l=lx.lexical()

with open('../parse/good.csv','r') as f:
    string=f.read()
arr=string.split('\n')
del(arr[0])
del(arr[-1])

result='tld,dot_num,avg_host,max_host,avg_path,max_path\n'
for line in arr:
    comp=line.split(',')
    hostname=comp[0]
    tld=comp[1]
    path=comp[3]
    dot_num, avg_host, max_host, avg_path, max_path=l.lexical(hostname,path)
    result+=tld+','+str(dot_num)+','+str(avg_host)+','+str(max_host)+','+str(avg_path)+','+str(max_path)+'\n'

with open('good_lexical.csv','w') as f:
    f.write(result)

with open('../parse/bad.csv','r') as f:
    string=f.read()
arr=string.split('\n')
del(arr[0])
del(arr[-1])

result='tld,dot_num,avg_host,max_host,avg_path,max_path\n'
for line in arr:
    comp=line.split(',')
    hostname=comp[0]
    tld=comp[1]
    path=comp[3]
    dot_num, avg_host, max_host, avg_path, max_path=l.lexical(hostname,path)
    result+=tld+','+str(dot_num)+','+str(avg_host)+','+str(max_host)+','+str(avg_path)+','+str(max_path)+'\n'

with open('bad_lexical.csv','w') as f:
    f.write(result)
