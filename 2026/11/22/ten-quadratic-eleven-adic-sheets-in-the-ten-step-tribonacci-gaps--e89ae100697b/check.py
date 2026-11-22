"""Reproducibility checks for the eleven-adic ten-step Tribonacci gap theorem.
Uses integer arithmetic only. Finite tests corroborate, but do not establish,
the all-depth statement proved separately by matrix and analytic arguments.
"""
from collections import Counter

P=11
Q=((0,1,0),(0,0,1),(1,1,1))

def mul(A,B,m):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%m
                       for j in range(3)) for i in range(3))

def power(A,n,m):
    R=((1,0,0),(0,1,0),(0,0,1))
    while n:
        if n&1:R=mul(R,A,m)
        A=mul(A,A,m)
        n//=2
    return R

M=power(Q,10,11**5)
X=[[M[i][j]-(i==j) for j in range(3)] for i in range(3)]
N=[[int(v)%11 for v in row] for row in X]
assert N==[[10,2,4],[4,3,6],[6,10,9]]
assert mul(tuple(map(tuple,N)),tuple(map(tuple,N)),11)==((0,0,0),)*3
assert mul(Q,tuple(map(tuple,N)),11)==tuple(tuple(7*v%11 for v in row) for row in N)

# The two initial Mahler coefficients after the constant term.
X_exact=[[43,68,81],[81,124,149],[149,230,273]]
def imul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
X2=imul(X_exact,X_exact)
X3=imul(X2,X_exact)
assert all(x%11==0 for row in X2 for x in row)
assert all(x%11==0 for row in X3 for x in row)
assert all(x%121==0 for row in imul(X2,X2) for x in row)
assert [[x//11%11 for x in row] for row in X3]==[[4,3,6],[6,10,9],[9,4,8]]
Qpow=[[1,0,0],[0,1,0],[0,0,1]]
for r in range(10):
    a=imul(Qpow,X2)[0][2]//11%11
    b=imul(Qpow,X3)[0][2]//11%11
    assert b == (6*pow(7,r,11))%11
    assert b*pow(2,-1,11)%11 == (3*pow(7,r,11))%11
    Qpow=imul(Qpow,[list(x) for x in Q])

checks=0
for k in range(1,6):
    m=11**k
    period=10*11**(k-1)
    vals=[0,0,1]
    for n in range(period+12):
        vals.append((vals[-1]+vals[-2]+vals[-3])%m)
    diffs=[(vals[n+10]-vals[n])%m for n in range(period)]
    count=Counter(diffs)
    s=1+5*sum(11**(k-2-2*j) for j in range((k-2)//2+1)) if k>=2 else 1
    assert len(count)==10*s,(k,len(count),10*s)
    assert all(x%11!=0 for x in count)
    assert len(count)==sum(len(set(diffs[r::10])) for r in range(10))
    assert len(set(x%11 for x in count))==10
    for r in range(10):
        branch=Counter(diffs[r::10]); assert len(branch)==s
        assert {a%11 for a in branch}=={4*pow(7,r,11)%11}
        if k>=2:
            for v,multiplicity in branch.items():
                # At prime-power depth, shifted-square fibers have either
                # no root, 2*11^j roots at nonzero square valuation 2j,
                # or 11^floor((k-1)/2) roots at the critical value.
                assert multiplicity in [11**((k-1)//2)]+[2*11**j for j in range((k-1)//2+1)]
        checks+=len(branch)
    # The least period is 10*11^(k-1): modulo eleven the ten branch
    # residues are pairwise distinct; the preceding 11-divisor does not work.
    if k>=2:
        preceding=10*11**(k-2)
        assert any(diffs[n]!=diffs[n+preceding] for n in range(period-preceding))
    print('depth',k,'period',period,'distinct residues',len(count),'per-branch',s)
print('Verified grouped branch-residue assertions:',checks)
