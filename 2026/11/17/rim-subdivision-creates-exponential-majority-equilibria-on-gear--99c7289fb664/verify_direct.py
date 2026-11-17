from itertools import product
from math import comb

def majority(state, n):
  h=state[0]; x=state[1:1+n]; y=state[1+n:]
  newh=(1 if sum(x)>n/2 else (0 if sum(x)<n/2 else h))
  newx=tuple(1 if h+y[(i-1)%n]+y[i]>=2 else 0 for i in range(n))
  newy=tuple(x[i] if x[i]==x[(i+1)%n] else y[i] for i in range(n))
  return (newh,)+newx+newy

def formula(n):
  s=1
  for j in range(1,n//2+1):
   for r in range(1,min(j,(n-j)//2)+1):
    s+=n*comb(j-1,r-1)*comb(n-j-r-1,r-1)//r
  return 2*s

def predicate(state,n):
  h=state[0];x=state[1:1+n];y=state[1+n:]
  return (sum(a!=h for a in x)<=n//2 and all(not(x[(i-1)%n]!=h and x[i]==h and x[(i+1)%n]!=h) for i in range(n)) and all(y[i]==(x[i]|x[(i+1)%n] if h==0 else (x[i]&x[(i+1)%n])) for i in range(n)))

for n in range(3,10):
  if n<=8:
   cs=0
   for bits in product((0,1),repeat=2*n+1):
    f=(majority(bits,n)==bits)
    if f!=predicate(bits,n): raise AssertionError(('predicate fails',n,bits,f))
    cs+=f
   assert cs==formula(n),(n,cs,formula(n))
  else:cs=None
  print(n,cs,formula(n))
