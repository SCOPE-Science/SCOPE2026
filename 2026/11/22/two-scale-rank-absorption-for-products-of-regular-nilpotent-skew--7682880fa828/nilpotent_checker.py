"""Independent exhaustive product enumeration for regular nilpotent so_3 matrices.

The program builds each factor and product as a 3x3 matrix, independently
computes its rank by Gaussian elimination, and measures a rank-one row norm.
It compares observed counts with predictions from the theorem.
Run with Python 3: python nilpotent_checker.py
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (3,5,7,9)
        self.q=q
    def add(self,a,b):
        if self.q!=9:return (a+b)%self.q
        return (a%3+b%3)%3+3*((a//3+b//3)%3)
    def neg(self,a):
        if self.q!=9:return (-a)%self.q
        return (-a%3)+3*((-(a//3))%3)
    def mul(self,a,b):
        if self.q!=9:return (a*b)%self.q
        x,y=a%3,a//3; u,v=b%3,b//3
        return (x*u+2*y*v)%3+3*((x*v+y*u)%3)
    def inv(self,a):
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def dot(self,a,b):
        z=0
        for x,y in zip(a,b):z=self.add(z,self.mul(x,y))
        return z

def skew(v,F):
    a,b,c=v
    return (0,F.neg(c),b,c,0,F.neg(a),F.neg(b),a,0)

def mm(A,B,F):
    return tuple(F.add(F.add(F.mul(A[3*i],B[j]),F.mul(A[3*i+1],B[3+j])),F.mul(A[3*i+2],B[6+j]))
                 for i in range(3) for j in range(3))

def rank(A,F):
    rows=[list(A[i*3:(i+1)*3]) for i in range(3)]
    r=0
    for j in range(3):
        ip=next((i for i in range(r,3) if rows[i][j]),None)
        if ip is None:continue
        rows[r],rows[ip]=rows[ip],rows[r]
        s=F.inv(rows[r][j]);rows[r]=[F.mul(s,x) for x in rows[r]]
        for i in range(r+1,3):
            s=rows[i][j]
            if s:rows[i]=[F.add(rows[i][k],F.neg(F.mul(s,rows[r][k]))) for k in range(3)]
        r+=1
    return r

def state(A,F):
    r=rank(A,F)
    if r==0:return 'Z'
    if r==2:return 'D'
    assert r==1
    v=next(A[3*i:3*i+3] for i in range(3) if any(A[3*i:3*i+3]))
    s=F.dot(v,v)
    if s==0:return 'I'
    assert any(F.neg(F.mul(t,t))==s for t in range(1,F.q)),('unexpected square type',F.q,s)
    return 'R'

def transfer(c,q):
    # Exact integer one-step count transfer, no division.
    return {'D':q*(q-1)*c['D'],
            'I':(q-1)*(c['D']+2*c['R']),
            'R':(q-1)*(q*c['I']+(q-1)*c['R']),
            'Z':(q-1)*c['I']+(q*q-1)*c['Z']}

for q,kmax in [(3,5),(5,4),(7,3),(9,2)]:
    F=Field(q)
    V=[(a,b,c) for a,b,c in product(range(q),repeat=3)
       if (a,b,c)!=(0,0,0) and F.dot((a,b,c),(a,b,c))==0]
    assert len(V)==q*q-1,(q,len(V))
    fac=[skew(v,F) for v in V]
    hist=Counter(fac)
    expected={'D':q*q-1,'I':0,'R':0,'Z':0}
    for k in range(1,kmax+1):
        got=Counter()
        for M,n in hist.items():got[state(M,F)]+=n
        assert all(got[x]==expected[x] for x in ('D','I','R','Z')),(q,k,got,expected)
        assert sum(got.values())==(q*q-1)**k
        print('q=%d k=%d state_counts (D,I,R,Z)=%s OK'%(q,k,tuple(got[x] for x in ('D','I','R','Z'))))
        if k<kmax:
            nh=Counter()
            for M,n in hist.items():
                for A in fac:nh[mm(M,A,F)]+=n
            hist=nh
            expected=transfer(expected,q)
print('ALL NILPOTENT ORBIT PRODUCT TESTS PASSED')
