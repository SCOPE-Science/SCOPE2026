import sympy as s
z=s.symbols('z')
T=1/(1-z)
verts=['00','01','10','11']
def S(b0,d0,u):
 C=max(b0,d0-u)
 expr=z**(d0+3*C)/((1-z)*(1-z**3)) - z**(u+1+4*C)/((1-z)*(1-z**4)) + z**(u+3+4*C)/((1-z**3)*(1-z**4))
 if C>b0: expr+=z**(b0+3*d0-2*u)*(1-z**(C-b0))/((1-z)*(1-z**3))
 return expr

def Sb(d0,u):
 expr=0
 if u>=d0:
  expr+=sum(z**d for d in range(d0,u+1))
 high=max(d0,u+1)
 expr+=z**(3*high-2*u)/(1-z**3)
 return expr

def Sd(b0,u):
 L=max(b0,-u)
 expr=z**(3*L)/(1-z**3)
 if -u>b0:
  expr+=sum(z**(b-2*(b+u)) for b in range(b0,-u)) # 3b +2(-b-u) = b-2u
 return expr

def spec(v,u,w):
 b0=max(0,v);d0=max(0,-w)
 expr=T*T*S(b0,d0,u)
 if v==0:expr-=T*(T-1)*Sb(d0,u)
 if w==0:expr-=T*(T-1)*Sd(b0,u)
 if v==0 and w==0:expr+=(T-1)**2*z**(2*max(0,-u))
 return z**(u-v+w)*expr/(1-z**2)
F=spec(0,0,0)
for st in verts:
 for en in verts:
  if st==en:continue
  delta={v:(1 if v==st else -1 if v==en else 0) for v in verts}
  F+=spec(delta['00'],delta['01'],delta['11'])
F+=2*z/(1-z)
F=s.cancel(F)
num,den=map(s.expand,s.fraction(F))
print('F=',s.factor(F))
print('NUM=',num);print('DEN=',s.factor(den))
series=s.series(F,z,0,22).removeO().expand()
print('coeff', [int(series.coeff(z,i)) for i in range(22)])
# brute exhaustive words length n up to 17
from itertools import product
for n in range(3,18):
 seen=set()
 for a in product((0,1),repeat=n):
  hist=[0]*8
  for i in range(n-2):hist[4*a[i]+2*a[i+1]+a[i+2]]+=1
  seen.add(tuple(hist))
 p=len(seen)
 print(n,p,int(series.coeff(z,n-2)), 'match',p==int(series.coeff(z,n-2)),flush=True)
