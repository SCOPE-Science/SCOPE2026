#!/usr/bin/env python3
"""Exact rational matrix-jet verification for Yule-OU clonal readout formulas.

Only the Python standard library is required. The script checks finite matrix
identities in several dimensions; the accompanying proof establishes the
universal statements for all admissible dimensions and coefficients.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product

NTEST = 0

def test(ok, message):
    global NTEST
    NTEST += 1
    if not ok:
        raise AssertionError(message)

def zero(n):
    return [[F(0) for _ in range(n)] for __ in range(n)]

def eye(n):
    a=zero(n)
    for i in range(n):a[i][i]=F(1)
    return a

def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a))] for i in range(len(a))]

def neg(a):return scale(a,F(-1))

def sub(a,b):return add(a,neg(b))

def scale(a,s):return [[s*x for x in r] for r in a]

def mul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def tr(a):return [list(r) for r in zip(*a)]

def comm(a,b):return sub(mul(a,b),mul(b,a))

def sqnorm(a):return sum((x*x for r in a for x in r),F(0))

def expcoef(a,degree):
    n=len(a)
    out=[eye(n)]
    for k in range(1,degree+1):out.append(scale(mul(out[-1],a),F(1,k)))
    return out

def clone_jets(s,w,degree=9):
    """Return coefficients of K(t)=I+2 int_0^t exp(u) exp(-Au)exp(-A^T u) du."""
    n=len(s)
    a=add(s,w)
    ea=expcoef(neg(a),degree)
    eb=expcoef(neg(tr(a)),degree)
    h=[]
    for m in range(degree+1):
        x=zero(n)
        for k in range(m+1):x=add(x,mul(ea[k],eb[m-k]))
        h.append(x)
    k=[eye(n)]
    for m in range(1,degree+1):
        x=zero(n)
        for j in range(m):x=add(x,scale(h[j],F(1,factorial(m-1-j))))
        k.append(scale(x,F(2,m)))
    return h,k

def diagonal(vals):
    a=zero(len(vals))
    for i,v in enumerate(vals):a[i][i]=F(v)
    return a

def skew(n, entries):
    o=zero(n)
    for (i,j),v in entries.items():
        assert i<j
        o[i][j]=F(v)
        o[j][i]=-F(v)
    return o

def fmat(n,k):
    s=diagonal([i+1+F(k,3) for i in range(n)])
    omega=skew(n,{(i,j):F(((i+2*j+k)%7)-3,3) for i in range(n) for j in range(i+1,n)})
    return s,omega

for dim in [2,3,4,5]:
    for case in range(7):
        s,w=fmat(dim,case)
        h,k=clone_jets(s,w)
        k1=k[1]
        k2=scale(k[2],F(2))
        k3=scale(k[3],F(6))
        t=sub(scale(k3,F(1,2)),mul(scale(k2,F(1,2)),scale(k2,F(1,2))))
        test(k[0]==eye(dim),"initial clone covariance")
        test(k1==scale(eye(dim),F(2)),"first jet")
        test(k2==scale(sub(eye(dim),scale(s,F(2))),F(2)),"second jet")
        test(t==scale(comm(w,s),F(2)),"third jet commutator")
        test(add(add(s,w),tr(add(s,w)))==scale(s,F(2)),"stationary Lyapunov")
        recovered=zero(dim)
        for i in range(dim):
            for j in range(i+1,dim):
                recovered[i][j]=t[i][j]/(2*(s[j][j]-s[i][i]))
                recovered[j][i]=-recovered[i][j]
        test(recovered==w,"simple spectrum reconstructs all antisymmetric drift")
        delta=min(abs(s[j][j]-s[i][i]) for i in range(dim) for j in range(i+1,dim))
        dw=skew(dim,{(i,j):F(1 if (i+j+case)%2==0 else -2) for i in range(dim) for j in range(i+1,dim)})
        diff3=scale(comm(dw,s),F(4))
        test(sqnorm(diff3)>=16*delta*delta*sqnorm(dw),"sharp spectral-gap Lipschitz bound")

# Check non-diagonal damping, including a noncommuting skew drift.
for s,w in [
    ([[F(3),F(1)],[F(1),F(2)]],skew(2,{(0,1):F(7,3)})),
    ([[F(5),F(1),F(0)],[F(1),F(4),F(1)],[F(0),F(1),F(3)]],skew(3,{(0,1):2,(0,2):-3,(1,2):1})),
]:
    h,k=clone_jets(s,w)
    k2=scale(k[2],F(2)); k3=scale(k[3],F(6))
    t=sub(scale(k3,F(1,2)),mul(scale(k2,F(1,2)),scale(k2,F(1,2))))
    test(t==scale(comm(w,s),F(2)),"full symmetric damping commutator identity")
    test(k2==scale(sub(eye(len(s)),scale(s,F(2))),F(2)),"full damping retrieval")

# The obstruction is exact at every time, proved by commuting exponentials;
# these Taylor checks provide independent symbolic finite-order confirmation.
for vals,i,j in [([2,2],0,1),([2,2,5],0,1),([2,3,3,4],1,2)]:
    n=len(vals)
    s=diagonal(vals); z=zero(n); w=skew(n,{(i,j):F(5,2)})
    h0,k0=clone_jets(s,z,degree=12)
    h1,k1=clone_jets(s,w,degree=12)
    for d in range(13):
        test(h0[d]==h1[d],"commuting rotation is invisible in H jet")
        test(k0[d]==k1[d],"commuting rotation is invisible in K jet")
    entropy=sum((sum((w[i][j]*w[i][j] for j in range(n)),F(0))/s[i][i] for i in range(n)),F(0))
    test(entropy>0,"invisible current still dissipates")

# Sharpness: perturb only the closest pair (first two for unit-gap diagonal S).
for dim in range(2,8):
    s=diagonal([i+1 for i in range(dim)])
    w=skew(dim,{(0,1):F(5,7)})
    test(sqnorm(scale(comm(w,s),4))==16*sqnorm(w),"constant 1/(4 delta) sharp")

print(f"VERIFY_OK exact_rational_checks={NTEST}")
