import lexical as lx
from random import shuffle


l=lx.lexical()
result='tld,dot_num,avg_host,max_host,avg_path,max_path,class\n'
result_arr=[]

with open('../parse/good.csv','r') as f:
    string=f.read()
arr=string.split('\n')
del(arr[0])
del(arr[-1])
for line in arr:
    comp=line.split(',')
    hostname=comp[0]
    tld=comp[1]
    path=comp[3]
    dot_num, avg_host, max_host, avg_path, max_path=l.lexical(hostname,path)
    result_arr.append(tld+','+str(dot_num)+','+str(avg_host)+','+str(max_host)+','+str(avg_path)+','+str(max_path)+',good')

with open('../parse/bad.csv','r') as f:
    string=f.read()
arr=string.split('\n')
del(arr[0])
del(arr[-1])
for line in arr:
    comp=line.split(',')
    hostname=comp[0]
    tld=comp[1]
    path=comp[3]
    dot_num, avg_host, max_host, avg_path, max_path=l.lexical(hostname,path)
    result_arr.append(tld+','+str(dot_num)+','+str(avg_host)+','+str(max_host)+','+str(avg_path)+','+str(max_path)+',bad')

shuffle(result_arr)
result+='\n'.join(result_arr)

with open('lexical.csv','w') as f:
    f.write(result)