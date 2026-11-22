from math import comb
from itertools import combinations,product
from collections import Counter

def qbin(n,k,q):
 if k<0 or k>n:return 0
 # Gaussian coefficients via the q-Pascal recurrence.
 d=[0]*(k+1);d[0]=1
 for i in range(1,n+1):
  for j in range(min(i,k),0,-1):d[j]=d[j]+q**(i-j)*d[j-1]
 return d[k]

def predicted(a,b,c,q=2):
 out=Counter();m=a*c
 for l in range(a+1):
  for r in range(c+1):
   h=c*l+a*r-l*r
   for d in range(b*(l+r)+1):
    t=0
    for i in range(l+1):
     for j in range(r+1):
      t+=qbin(l,i,q)*qbin(r,j,q)*(-1)**(l-i+r-j)*q**(comb(l-i,2)+comb(r-j,2))*qbin(b*(i+j),d,q)
    assert t>=0,(a,b,c,l,r,d,t)
    for e in range(h,m+1):
     out[e+d]+=qbin(a,l,q)*qbin(c,r,q)*t*qbin(m-h,e-h,q)*q**(d*(m-e))
 return out

def enumerate_rref(n):
 for d in range(n+1):
  for pivots in combinations(range(n),d):
   loc=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
   for bits in product((0,1),repeat=len(loc)):
    rows=[1<<p for p in pivots]
    for (i,j),bit in zip(loc,bits):
     if bit:rows[i]|=1<<j
    yield tuple(rows)

def direct(a,b,c):
 basis=[];n=0
 X={(u,v):i for i,(u,v) in enumerate(product(range(a),range(b)))}
 n=len(X)
 Y={(v,w):n+i for i,(v,w) in enumerate(product(range(b),range(c)))}
 n+=len(Y)
 Z={(u,w):n+i for i,(u,w) in enumerate(product(range(a),range(c)))}
 n+=len(Z)
 products=[]
 for i in range(n):
  d=[]
  for j in range(n):
   z=0
   for (u,v),ii in X.items():
    if i==ii:
     for (vv,w),jj in Y.items():
      if j==jj and v==vv:z^=1<<Z[u,w]
   d.append(z)
  products.append(d)

 def reduce(v,rows):
  for row in rows:
   p=(row&-row)
   if v&p:v^=row
  return v==0

 counts=Counter()
 for rows in enumerate_rref(n):
  good=True
  for x in rows:
   for e in range(n):
    y=0;z=0
    for i in range(n):
     if x>>i&1:y^=products[i][e];z^=products[e][i]
    if not reduce(y,rows) or not reduce(z,rows):good=False;break
   if not good:break
  if good:counts[len(rows)]+=1
 return counts
if __name__=='__main__':
 for a,b,c in [(1,1,1),(1,2,1),(2,1,1),(1,1,2),(2,1,2)]:
  pred=predicted(a,b,c); print('formula',a,b,c,sorted(pred.items()),'total',sum(pred.values()),flush=True)
  # Exhaust all vector subspaces up to dimension five.
  if a*b+b*c+a*c<=5:
   d=direct(a,b,c);print('direct',sorted(d.items()),'equal',d==pred,flush=True);assert d==pred

def direct_prime(a,b,c,q):
 n=a*b+b*c+a*c
 X={(u,v):i for i,(u,v) in enumerate(product(range(a),range(b)))}
 Y={(v,w):a*b+i for i,(v,w) in enumerate(product(range(b),range(c)))}
 Z={(u,w):a*b+b*c+i for i,(u,w) in enumerate(product(range(a),range(c)))}
 products={}
 for (u,v),ii in X.items():
  for (vv,w),jj in Y.items():
   if v==vv:products[(ii,jj)]=Z[u,w]
 counts=Counter()
 for d in range(n+1):
  for piv in combinations(range(n),d):
   loc=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
   for digits in product(range(q),repeat=len(loc)):
    rows=[[0]*n for _ in range(d)]
    for i,p in enumerate(piv):rows[i][p]=1
    for (i,j),e in zip(loc,digits):rows[i][j]=e
    def inside(vec):
     v=vec[:]
     for row,p in zip(rows,piv):
      t=v[p]
      if t:
       for k in range(n):v[k]=(v[k]-t*row[k])%q
     return not any(v)
    good=True
    for x in rows:
     for k in range(n):
      prod1=[0]*n;prod2=[0]*n
      for i,x_i in enumerate(x):
       if x_i:
        j=products.get((i,k))
        if j is not None:prod1[j]=(prod1[j]+x_i)%q
        j=products.get((k,i))
        if j is not None:prod2[j]=(prod2[j]+x_i)%q
      if not inside(prod1) or not inside(prod2):good=False;break
     if not good:break
    if good:counts[d]+=1
 return counts

if __name__=='__main__':
 for a,b,c,q in [(1,1,1,3),(1,2,1,3),(2,1,1,3)]:
  p=predicted(a,b,c,q)
  d=direct_prime(a,b,c,q)
  print('prime',a,b,c,q,sorted(p.items()),'direct',sorted(d.items()),'same',p==d,flush=True)
  assert p==d
 for a,b,c in [(2,2,1),(1,2,2),(2,2,2)]:
  for q in (2,3):
   spectrum=predicted(a,b,c,q)
   print('formula_only',a,b,c,q,[spectrum[i] for i in range(max(spectrum)+1)],'total',sum(spectrum.values()),flush=True)
