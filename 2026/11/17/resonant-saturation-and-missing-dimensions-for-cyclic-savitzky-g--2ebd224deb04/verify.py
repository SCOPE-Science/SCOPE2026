"""Exact finite verification of cyclic quadratic Savitzky-Golay BV saturation.
Standard-library only; all arithmetic is integral/Fraction.
The general theorem is proved in RESULT.md, not inferred from these tests.
"""
from fractions import Fraction
from math import isqrt

def kernel(m):
    assert m >= 2
    A = 3*m*m+3*m-1
    D = (2*m+1)*(4*m*m+4*m-3)
    weights = [3*(A-5*j*j) for j in range(-m,m+1)]
    assert sum(weights) == D
    assert sum(j*j*weights[j+m] for j in range(-m,m+1)) == 0
    return weights, D

def signs(m):
    weights,D=kernel(m)
    a=max(j for j in range(m+1) if weights[j+m]>0)
    b=min(j for j in range(m+1) if weights[j+m]<0)
    assert b in [a+1,a+2]
    return 2*a+1,b

def sharp(m,n):
    weights,D=kernel(m)
    assert n >=2*m+1
    v=[0]*n
    for j,c in zip(range(-m,m+1),weights):v[j%n]+=c
    values=[sum(abs(v[i]-v[(i-s)%n]) for i in range(n)) for s in range(1,n)]
    mx=max(values)
    s=1+values.index(mx)
    # A cyclic one-block binary input has derivative e_0-e_s.
    x=[int(1<=i<=s) for i in range(n)]
    dx=[x[(i+1)%n]-x[i] for i in range(n)]
    assert dx[0]==1 and dx[s]==-1 and sum(abs(z) for z in dx)==2
    out=[sum(v[(i-j)%n]*dx[j] for j in range(n)) for i in range(n)]
    assert sum(abs(z) for z in out)==mx
    return Fraction(mx,2*D),s

def theoretical_saturation(m,n):
    P,b=signs(m)
    return (2*P<=n<=4*b-2) or (n>=P+2*m+1)

for m in range(2,21):
    weights,D=kernel(m)
    full=Fraction(sum(abs(k) for k in weights),D)
    P,b=signs(m)
    for n in range(2*m+1, P+2*m+9):
        exact,s=sharp(m,n)
        assert (exact==full) == theoretical_saturation(m,n),(m,n,P,b,exact,full)
        assert exact <= full
    print('EXACT_SATURATION m=%d P=%d b=%d full=%s PASS' %(m,P,b,full))

# Larger-window support-geometry verification (including nonzero and zero-weight cases).
for m in range(21,121):
    weights,D=kernel(m)
    P,b=signs(m)
    support=[j for j,k in zip(range(-m,m+1),weights) if k>0]
    neg=[j for j,k in zip(range(-m,m+1),weights) if k<0]
    assert len(support)==P and len(neg)>0
    for n in range(2*m+1, P+2*m+9):
        # Check equality condition using disjoint sign supports only, independently
        # from the analytical interval formula.
        pos={j%n for j in support}
        neg_set={j%n for j in neg}
        possible=any(not(pos & {(j+s)%n for j in pos}) and
                     not(neg_set & {(j+s)%n for j in neg_set})
                     for s in range(1,n))
        assert possible == theoretical_saturation(m,n),(m,n,P,b,possible)
    if m in (21,40,60,86,100,120):print('SIGN_SUPPORT_SATURATION m=%d P=%d b=%d PASS'%(m,P,b))

# Explicit five-tap nonmonotonicity: the first full case, a strict dip, final plateau.
expected={5:Fraction(1),6:Fraction(47,35),7:Fraction(44,35),8:Fraction(47,35)}
for n,q in expected.items():
    result,_=sharp(2,n)
    assert result==q,(n,result,q)
print('FIVE_TAP_NONMONOTONE_EXACT n=5..8 PASS')
# Degenerate zero weights in the 13-point smoother at offsets +/-5.
w,D=kernel(6)
assert w[6-5]==0 and w[6+5]==0
for n in range(18,26): assert theoretical_saturation(6,n)
print('ZERO_COEFFICIENT_13_TAP_INTERVAL_PASS')
print('ALL_CYCLIC_SG_BV_EXACT_CHECKS_PASS')
