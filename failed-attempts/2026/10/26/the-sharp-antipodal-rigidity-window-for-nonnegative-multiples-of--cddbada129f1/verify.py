from math import gcd

PHI70={0:1,1:1,5:-1,6:-1,7:-1,8:-1,10:1,11:1,12:1,13:1,14:1,16:-1,17:-1,18:-1,19:-1,23:1,24:1}
E=(0,1,3,11,12,13,14,23,31,40,41,42,43,51,53,54)
WEIGHTS=(2,1,2,1,1,1,2,3,3,2,1,1,1,2,1,2)

def coeff_from_dict(d):
 arr=[0]*(1+max(d));
 for i,v in d.items():arr[i]=v
 return arr

def strip(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p

def divide(f,g):
 f=strip(list(f)); g=strip(list(g));q=[0]*max(1,len(f)-len(g)+1)
 while len(f)>=len(g) and any(f):
  # monic divisor, exact integer quotient
  j=len(f)-len(g);t=f[-1]
  q[j]=t
  for i,c in enumerate(g): f[j+i]-=t*c
  strip(f)
 return strip(q), f

def phi(n):
 p=[-1]+[0]*(n-1)+[1]
 for d in range(1,n):
  if n%d==0:
   h=phi(d);p,rem=divide(p,h); assert rem==[0],(n,d,rem)
 return p
P=coeff_from_dict(PHI70)
assert phi(70)==P
assert len(P)==25 and P[-1]==1
coeff=[]
for j in range(55):
 m=[0]*(j+1);m[j]=1
 _,r=divide(m,P)
 r=r+[0]*(24-len(r))
 lam=2*r[19]+r[20]+2*r[21]+r[22]+r[23]
 coeff.append(lam)
assert coeff[:19]==[0]*19
assert coeff[19:35]==list(WEIGHTS)
assert coeff[35:54]==[0]*19
assert coeff[54]==-2
F=[0]*55
for j in E:F[j]=1
q,r=divide(F,P)
assert r==[0]
_,r2=divide(F,[1]+[0]*34+[1]);assert r2!=[0]
assert F[0]==1 and F[35]==0
assert max(E)-min(E)==54
print('VERIFY_OK: cyclotomic identity, certificate, and first exceptional witness')
print('Phi_70 =',PHI70)
print('certificate =',WEIGHTS)
print('witness E =',E)
print('quotient =',[(i,c) for i,c in enumerate(q) if c])
