from itertools import product
from math import comb

def gs(n,t,kappa):
 out={}
 for s in range(-n,n+1):
  if kappa<1:
   k=(n-abs(s))%2
   c=comb(n,(n+abs(s))//2) if k==0 else 2*n*comb(n-1,(n-1+abs(s))//2)
  elif kappa>1:
   k=n-abs(s);c=comb(n,abs(s))*2**(n-abs(s))
  else:
   k=None;c=comb(2*n,n+s)
  E=2*s*s-n+((kappa-1)*(n-2*k) if k is not None else 0)-2*t*s
  out[s]=(E,c)
 m=min(q[0] for q in out.values());return m,{s:c for s,(E,c) in out.items() if abs(E-m)<1e-8}

def ex(n,t,kappa):
 m=1e30;out={}
 for z in product((-1,1),repeat=2*n):
  S=sum(z);pairs=sum(z[2*i]*z[2*i+1] for i in range(n))
  E=(S*S-2*n)/2+(kappa-1)*pairs-t*S
  if E<m-1e-8:m=E;out={}
  if abs(E-m)<1e-8:
   s=S//2;out[s]=out.get(s,0)+1
 return m,out
ct=0
for n in range(1,7):
 for k in (0,.25,.75,1,1.25,2,4):
  for t in (0,.25, .75,1,1.5,2,2.5,3,3.75,4,4.25,5,6,7,8,10,12):
   a=gs(n,t,k);b=ex(n,t,k)
   assert a==b,(n,k,t,a,b)
   ct+=1
print('PASS paired-coupling exact ground-state analytic formula vs full enumeration',ct,'instances; max n',n)
