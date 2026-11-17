"""Standalone exact GF(3) matrix test of reversible incidence waves.
No third-party dependencies except NumPy; all eliminations are modulo 3.
"""
import numpy as np

def add(a,b,q):
    return (a^b) if q==4 else (a+b)%q

def mul(a,b,q):
    if q!=4:return a*b%q
    # Multiply in GF(2)[t]/(t^2+t+1).
    z=0
    for i in range(2):
      for j in range(2):
       if (a>>i)&1 and (b>>j)&1:z^=1<<(i+j)
    for i in (2,):
      if z&(1<<i):z^=0b111<<(i-2)
    return z

def inv(a,q):
  for b in range(1,q):
    if mul(a,b,q)==1:return b
  raise ValueError(a)

def canonical(v,q):
  i=next(i for i,x in enumerate(v) if x)
  c=inv(v[i],q)
  return tuple(mul(x,c,q) for x in v)

def projective(q):
  return sorted({canonical((a,b,c),q) for a in range(q) for b in range(q) for c in range(q) if a or b or c})

def incidence(q):
  points=projective(q);lines=projective(q)
  v=len(points);assert v==q*q+q+1
  N=np.zeros((v,v),dtype=np.int64)
  for i,p in enumerate(points):
    for j,l in enumerate(lines):
      s=0
      for x,y in zip(p,l):s=add(s,mul(x,y,q),q)
      if s==0:N[i,j]=1
  assert np.all(N.sum(axis=0)==q+1) and np.all(N.sum(axis=1)==q+1)
  return N

def rank3(mat):
  x=np.asarray(mat,dtype=np.int64).copy()%3;m,n=x.shape;r=0
  for c in range(n):
    nz=np.flatnonzero(x[r:,c]);
    if not len(nz):continue
    k=int(nz[0])+r
    x[[r,k]]=x[[k,r]]
    if x[r,c]==2:x[r]=(x[r]*2)%3
    nz2=np.flatnonzero(x[r+1:,c])+r+1
    if len(nz2): x[nz2]=(x[nz2]-x[nz2,c,None]*x[r])%3
    r+=1
    if r==m:break
  return r

def predicted(q,t):
  v=q*q+q+1
  if q%3==2:
    return 4*int(t%4==0)+4*(v-1)*int(t%8==0)
  assert q%3==1
  k=1
  while t%3==0:t//=3;k*=3
  one=min(k,4)+(v-2)*min(k,2)
  return one*(2 if t%2==0 else 1)

def run(q):
  N=incidence(q);v=N.shape[0];nn=2*v;dim=2*nn
  A=np.zeros((nn,nn),dtype=np.int64)
  A[:v,v:]=N;A[v:,:v]=N.T
  J=np.ones((v,v),dtype=np.int64)
  np.testing.assert_array_equal((N@N.T)%3,((q%3)*np.eye(v,dtype=np.int64)+J)%3)
  T=np.zeros((dim,dim),dtype=np.int64)
  T[:nn,:nn]=A;T[:nn,nn:]=2*np.eye(nn,dtype=np.int64);T[nn:,:nn]=np.eye(nn,dtype=np.int64)
  I=np.eye(dim,dtype=np.int64);P=I.copy()
  times=([1,2,3,4,6,8] if q%3==2 else [1,2,3,6,9,18])
  ret=[]
  for t in range(1,max(times)+1):
    P=P@T%3
    if t in times:
      observed=dim-rank3((P-I)%3);want=predicted(q,t)
      assert observed==want,(q,t,observed,want)
      ret.append((t,observed))
  assert np.array_equal(P,I),('period',q)
  # Verify minimal global order via a one-time divisor reduction
  period=max(times)
  for prime in (2,3):
    if period%prime==0:
      z=I.copy()
      for _ in range(period//prime):z=z@T%3
      assert not np.array_equal(z,I)
  return {'plane_order':q,'v':v,'state_dimension':dim,'fixed_nullities':ret,'exact_operator_order':period}

if __name__=='__main__':
 for q in (2,4,5):print(run(q))
 print('ALL EXACT MATRIX TESTS PASSED')
