print([1,"hello",1.1])
l = [1,1,[1,2]]
print(l[2][1])
lst=['a','b','c'] 
print(lst[1:])
week={'sunday':0,'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6}
print(week)
d={'k1':[1,2,3]} 
ans=d['k1'][1]
print(ans)
li=[1,[2,3]]
print(tuple(li))
s=set('missisippi')
s.add('x')
print(s)
print(set([1,1,2,3]))

nl=[]
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))

def fact(x):
 if x == 0:
  return 1
 return x * fact(x - 1)
x=8
print(fact(x))

n=8
d=dict()
for i in range(1,n+1):
 d[i]=i*i
print(d)

values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)

