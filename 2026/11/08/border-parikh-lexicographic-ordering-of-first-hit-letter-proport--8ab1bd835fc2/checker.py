from itertools import product
from scipy.integrate import quad
from math import isclose

def borders(w):
 return [i for i in range(1,len(w)+1) if w[:i]==w[-i:]]

def calc(w,s):
 m=len(w);bl=borders(w)
 def fun(z,a):
  B=sum(s**ell*z**(m-ell) for ell in bl)
  D=z**m+(1-z)*B
  C=sum((s*w[:ell].count(a)-ell)*s**ell*z**(m-ell) for ell in bl)
  return (1-z)*z**(m-1)*C/(s*D**2)
 return [1/s+quad(lambda z:fun(z,a),0,1,epsabs=2e-13)[0] for a in range(s)]

def dp(w,s,T):
 m=len(w);P=[0.0]*m;P[0]=1.0;A=[[0.0]*s for _ in range(m)];tot=[0.0]*s
 def nextstate(u,c):
  x=u+(c,)
  if x[-m:]==w:return m
  return max((k for k in range(m) if x[-k:]==w[:k]),default=0)
 nxt=[[nextstate(w[:i],c) for c in range(s)] for i in range(m)]
 for t in range(1,T+1):
  PP=[0.0]*m;AA=[[0.0]*s for _ in range(m)]
  for i in range(m):
   if P[i]<1e-300:continue
   for c in range(s):
    j=nxt[i][c]
    if j==m:
     for a in range(s):tot[a]+=(A[i][a]+P[i]*(c==a))/(s*t)
    else:
     PP[j]+=P[i]/s
     for a in range(s):AA[j][a]+=(A[i][a]+P[i]*(c==a))/s
  P,A=PP,AA
 return tot,sum(P)

for s in (2,3,4):
 for m in range(1,7 if s<4 else 6):
  for w in product(range(s),repeat=m):
   bl=borders(w)
   for a in range(s):
    for b in range(a+1,s):
     d=[w[:ell].count(a)-w[:ell].count(b) for ell in bl]
     D=next((v for v in d[::-1] if v),0)
     for z in (0.10,.34,.71,.97,1.0):
      P=sum(di*s**ell*z**(m-ell) for ell,di in zip(bl,d))
      assert (P>0)-(P<0)==(D>0)-(D<0),(s,m,w,a,b,z,bl,d,P)
print('polynomial sign checks pass')
for s,w in [(2,(0,)),(2,(0,1)),(3,(0,1)),(3,(0,1,0)),(3,(0,1,2)),(4,(0,1))]:
 a=calc(w,s);b,rem=dp(w,s,10000)
 assert rem<2e-11,(s,w,rem)
 assert max(abs(x-y) for x,y in zip(a,b))<2e-10,(s,w,a,b)
 print('dp',s,w,a,b,'remaining',rem)
print('tie case',calc((0,1,1,2,2,0),3))
