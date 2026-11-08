#!/usr/bin/env python3
"""Exact rational checks for a two-periodic fourth/fifth-order BDF theorem.

Standard-library only. Analytical all-r conclusions are proved in RESULT.md;
these finite exact tests independently check the interpolation and matrix identities.
"""
from fractions import Fraction as F
from itertools import permutations

checks = 0
def check(ok, explanation):
    global checks
    assert ok, explanation
    checks += 1

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def det(a):
    n=len(a)
    return sum(((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))*__import__('math').prod(a[i][p[i]] for i in range(n)) for p in permutations(range(n)))

def mat(k,r):
    # The current step has length 1 and the preceding step has length 1/r.
    # Older steps alternate 1, 1/r, etc.
    nodes=[F(0)]
    for i in range(k):nodes.append(nodes[-1]-(F(1) if i%2==0 else 1/r))
    alpha=[sum(-1/x for x in nodes[1:])]
    for j in range(1,k+1):
        numerator=F(1)
        denominator=F(1)
        for l in range(1,k+1):
            if l != j:numerator *= -nodes[l]
        for l in range(k+1):
            if l != j:denominator *= nodes[j]-nodes[l]
        alpha.append(numerator/denominator)
    check(sum(alpha)==0,'constant polynomial exactness')
    check(all(sum(alpha[j]*nodes[j]**m for j in range(k+1))==(1 if m==1 else 0) for m in range(k+1)), 'degree-k derivative interpolation')
    B=[-x/alpha[0] for x in alpha[1:]]
    check(sum(B)==1,'constant solution preservation')
    first=[-sum(B[j:]) for j in range(1,k)]
    return [first]+[[F(int(j==i)) for j in range(k-1)] for i in range(k-2)]

def chifour(a):
    tr=sum(a[i][i] for i in range(3))
    minors=sum(a[i][i]*a[j][j]-a[i][j]*a[j][i] for i in range(3) for j in range(i+1,3))
    return [F(1),-tr,minors,-det(a)]

for r in [F(1,30),F(1,10),F(1,3),F(1,2),F(1),F(3,2),F(2),F(3),F(7),F(10),F(30),F(101,3)]:
    a=mat(4,r)
    den=(r+2)*(3*r+2)*(4*r+1)
    expected=[r*r*(16*r*r+36*r+17)/den,
              -r*(12*r*r+19*r+8)/den,
              r*r*(2*r+1)**2/den]
    check(a[0]==expected,'BDF4 explicit difference-state matrix')
    p=mm(mat(4,1/r),a)
    q=r+1/r
    d=24*q*q+154*q+221
    aa=24*q*q+34*q-43
    bb=6*q+19
    cc=2*q+5
    check(chifour(p)==[F(1),aa/d,bb/d,-cc/d],'BDF4 monodromy polynomial')
    check(d-cc==8*(3*q*q+19*q+27),'first Jury inequality')
    check(d+aa+bb-cc==48*(q+2)**2,'second Jury inequality')
    check(d-aa+bb+cc==32*(4*q+9),'third Jury inequality')
    check(d*d-bb*d-aa*cc-cc*cc==16*(36*q**4+450*q**3+2047*q*q+3982*q+2802),'fourth Jury inequality')
    check(d>cc and d+aa+bb-cc>0 and d-aa+bb+cc>0 and d*d-bb*d-aa*cc-cc*cc>0,'strict Jury signs')

p=mm(mat(5,F(1,10)),mat(5,F(10)))
i_plus_p=[[p[i][j]+(1 if i==j else 0) for j in range(4)] for i in range(4)]
check(det(i_plus_p)==F(-8874496,44681585),'BDF5 determinant at minus-one crossing')
# Compute all four charpoly coefficients by direct interpolation at x=0,1,-1,2,3.
def pdet(x):return det([[F(x if i==j else 0)-p[i][j] for j in range(4)] for i in range(4)])
for x in [-2,-1,0,1,2,3]:
    expected=(44681585*x**4+58282373*x**3+3875537*x**2-698295*x+152460)/F(44681585)
    check(pdet(x)==expected,'BDF5 characteristic polynomial at test point')
print('PASS',checks,'exact rational assertions')
