"""Check equality, configuration by configuration, of oscillation basins."""
from check_direct import update,initial_time

def ordinary(a,b,s):
    A=s&((1<<a)-1);B=s>>a
    x=A.bit_count();y=B.bit_count();out=0
    if 2*y>b: AA=(1<<a)-1
    elif 2*y<b: AA=0
    else: AA=A
    if 2*x>a: BB=(1<<b)-1
    elif 2*x<a: BB=0
    else: BB=B
    return AA|(BB<<a)

def period_ordinary(a,b,s):
    z=s; seen={};path=[]
    while z not in seen:
        seen[z]=len(path);path.append(z);z=ordinary(a,b,z)
        assert len(path)<8
    return len(path)-seen[z]

n=0
for a in range(3,9):
 for b in range(1,9):
  for s in range(1<<(a+b)):
   assert (initial_time(a,b,s)[1]==2)==(period_ordinary(a,b,s)==2),(a,b,s)
   n+=1
print('INVARIANCE PASS:',n,'initial configurations for a=3..8,b=1..8')
