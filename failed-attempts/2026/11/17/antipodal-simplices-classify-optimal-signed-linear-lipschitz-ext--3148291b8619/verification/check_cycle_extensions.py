"""Exact-integer bounded Lipschitz dual enumeration for odd/even cycles."""
from fractions import Fraction as F
from itertools import product
import numpy as np

def potentials(n):
    fs=[]
    for steps in product((-1,0,1), repeat=n-1):
        if abs(sum(steps))>1: continue
        pos=[0];cur=0
        for s in steps:
            cur+=s;pos.append(cur)
        fs.append(pos)
    return np.array(fs,dtype=np.int64)

def radius(w,fs):
    n=len(w)
    assert sum(w)==1
    den=np.lcm.reduce([x.denominator for x in w])
    a=np.array([int(x*den) for x in w],dtype=np.int64)
    s=fs@a
    return F(int(np.max(np.abs(den*fs-s[:,None]))),int(den))

def check(n):
    fs=potentials(n); m=n//2;target=F(n*n//4,n)
    u=[F(1,n)]*n
    assert radius(u,fs)==target,(n,'uniform')
    seen=0
    if n%2==0:
      for j in range(m):
        w=[F(0)]*n;w[j]=w[j+m]=F(1,2)
        assert radius(w,fs)==target,(n,'antipode',j)
        seen+=1
      for j in range(m):
        a=[F(1,2*m)]*m
        a[j]=-F(1,2*m);a[(j+1)%m]+=F(2,2*m)
        assert sum(a)==F(1,2)
        w=a+a
        assert radius(w,fs)>target,(n,'negative',j)
        seen+=1
      for j in range(m):
        w=[F(0)]*n;w[j]=w[(j+1)%n]=F(1,2)
        assert radius(w,fs)>target,(n,'nonantipodal',j)
        seen+=1
    else:
      for j in range(n):
        for sign in [-1,1]:
          w=u.copy();w[j]+=F(sign,4*n);w[(j+1)%n]-=F(sign,4*n)
          assert radius(w,fs)>target,(n,'oddperturb',j,sign)
          seen+=1
    D=np.array([[min((i-j)%n,(j-i)%n) for j in range(n)] for i in range(n)])
    assert all(int(v)==n*target for v in D.sum(axis=1))
    return n,len(fs),seen,str(target)

if __name__=='__main__':
 for n in range(3,13):print('EXACT_CYCLE_CASE',*check(n),flush=True)
 print('SIGNED_CYCLE_CHEBYSHEV_SIMPLEX_ALL_CHECKS_PASS')
