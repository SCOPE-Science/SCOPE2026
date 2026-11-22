"""Exact, dependency-free certificate for NOR with one self-reading site on a ring.
Run with Python 3: python verify_feedback.py
All calculations use arbitrary-precision integers. No numerical tolerances.
"""
from collections import Counter

SYMS=range(4)
STATES=[(l,c) for l in SYMS for c in SYMS]
IX={p:i for i,p in enumerate(STATES)}

def allowed(l,c,r,defect):
    a,b=c&1,(c>>1)&1
    la,lb=l&1,(l>>1)&1
    ra,rb=r&1,(r>>1)&1
    return a==int(not(lb or rb or (defect and b))) and b==int(not(la or ra or (defect and a)))

def transfer(defect):
    A=[[0]*16 for _ in range(16)]
    for l in SYMS:
      for c in SYMS:
        for r in SYMS:
          if allowed(l,c,r,defect):A[IX[(l,c)]][IX[(c,r)]]=1
    return A

def mul(A,B):
    n=len(A);m=len(B[0]);k=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]
def trace(A):return sum(A[i][i] for i in range(len(A)))
def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def subtract(A,B):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(A,B)]
def add(A,B):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(A,B)]
def scale(c,A):return [[c*x for x in ar] for ar in A]
def perrin(n):
    P=[3,0,2]
    for i in range(3,n+1):P.append(P[i-2]+P[i-3])
    return P[n]
def path_mis(n):
    if n<=2:return [1,1,2][n]
    a=[1,1,2]
    for i in range(3,n+1):a.append(a[i-2]+a[i-3])
    return a[n]
def update(s,n,defect):
    v=0
    for i in range(n):
        if not ((s>>((i-1)%n))&1 or (s>>((i+1)%n))&1 or (defect and i==0 and (s&1))):v|=1<<i
    return v
A=transfer(False);D=transfer(True)
# Annihilator certificate: A q(A)=0, q(t)=t^9-2t^8+t^6+t^5-3t^4+t^3-t+1.
# The corresponding denominator is d(z)=1-2z+z^3+z^4-3z^5+z^6-z^8+z^9.
d=[1,-2,0,1,1,-3,1,0,-1,1]
# Computes q(A) and A q(A) exactly.
P=[identity(16)]
for j in range(10):P.append(mul(P[-1],A))
qA=[[0]*16 for _ in range(16)]
for j in range(10):qA=add(qA,scale(d[9-j],P[j]))
assert not any(any(row) for row in mul(A,qA)), 'Annihilator certificate failed'
# Initial coefficients of H(z)=tr((D-A)(I-zA)^(-1)), check polynomial numerator.
num=[0,-1,1,3,-5,2,2,-5,3] # N(z) coefficients from lowest to highest
B=subtract(D,A)
h=[]
for k in range(12):h.append(trace(mul(B,P[k])) if k<=10 else trace(mul(B,mul(P[10],A))))
for k in range(10):
    coeff=sum(d[j]*h[k-j] for j in range(min(9,k)+1))
    assert coeff==(num[k] if k<len(num) else 0),(k,coeff)
# Long-range recurrence and exact enumeration check.
for k in range(9,12):assert sum(d[j]*h[k-j] for j in range(10))==0

def expected_delta(n):
    # Delta_n coefficient [z^(n-1)] N(z)/d(z) computed by integer recurrence.
    hh=[]
    for k in range(n):
        value=num[k] if k<len(num) else 0
        for j in range(1,min(9,k)+1):value-=d[j]*hh[k-j]
        hh.append(value)
    return hh[n-1]

for n in range(3,13):
    count_periodic=count_fixed=count_plain=0
    for s in range(1<<n):
      t=update(s,n,True);u=update(t,n,True)
      assert update(u,n,True)==t # F^3=F
      count_periodic+=(u==s)
      count_fixed+=(t==s)
      v=update(s,n,False)
      count_plain+=(update(v,n,False)==s)
    plain=perrin(2*n) if n%2 else perrin(n)**2
    assert count_plain==plain
    assert count_periodic==plain+expected_delta(n),(n,count_periodic,expected_delta(n))
    assert count_fixed==perrin(n)-path_mis(n-3)
    assert (count_periodic-count_fixed)%2==0
    assert count_periodic==trace(mul(D,P[n-1])) if n<=11 else True
    print(n, 'plain',plain,'defect',count_periodic,'fixed',count_fixed,'two_cycles',(count_periodic-count_fixed)//2,'delta',count_periodic-plain)
print('PASS: exact annihilator, rational generating identity, no periods >2, and exhaustive counts n=3..12')
