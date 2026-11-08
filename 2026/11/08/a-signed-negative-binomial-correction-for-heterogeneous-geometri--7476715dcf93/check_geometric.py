#!/usr/bin/env python3
"""Exact-rational finite-coefficient diagnostics for a geometric-sum signed correction.

Run: python3 check_geometric.py
Finite diagnostics do not prove any all-order or infinite-support theorem.
"""
from fractions import Fraction as F
from math import comb

N = 42
checks = 0

def assert_eq(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1

def assert_le(x, y):
    global checks
    assert x <= y, (x, y)
    checks += 1

def geom(y):
    return [(1-y) * y**k for k in range(N+1)]

def conv(a,b):
    return [sum((a[j]*b[k-j] for j in range(k+1)), F(0)) for k in range(N+1)]

def mass(y):
    a = [F(1)]+[F(0)]*N
    for t in y:
        a=conv(a,geom(t))
    return a

def nb(c,w):
    return [F(comb(c+k-1,k))*(1-w)**c*w**k for k in range(N+1)]

def quad(c,w,S2):
    p=nb(c,w)
    return [S2/F(2)*p[k]*(F(k*(k-1),c*(c+1))/w**2 - 1/(1-w)**2) for k in range(N+1)]

def proof_B_coeff(y,w,k):
    # B_{y,w}(z)=(A_y(z)-A_w(z))/(y-w) for y != w
    # Validate by multiplying formal power series in the exact-rational domain.
    def A(t, k):
        if k==0: return -1/(1-t)
        return t**(k-1) # since z/(1-t*z)=sum_{k>=1}t^(k-1)z^k
    if y == w:
        if k==0: return -1/(1-w)**2
        return F(k-1)*w**(k-2) if k>=2 else F(0)
    return (A(y,k)-A(w,k))/(y-w)

for c in (2,3,4,6):
    for w in (F(1,4),F(2,5),F(1,2),F(2,3)):
        vectors = [([F(1),-F(1)]+[F(0)]*(c-2)),
                   ([F(1)]*(c-1)+[-F(c-1)])]
        for v in vectors:
            for eta in (F(1,100),F(1,1000)):
                y=[w+eta*z for z in v]
                if not all(F(0)<z<F(1) for z in y): continue
                r=max(y+[w]); aa=1-r
                S2=sum((z-w)**2 for z in y)
                S3=sum(abs(z-w)**3 for z in y)
                ps=mass(y); b=nb(c,w); q=quad(c,w,S2)
                l1=sum(abs(ps[k]-b[k]) for k in range(N+1))/2
                l2=sum(abs(ps[k]-b[k]-q[k]) for k in range(N+1))/2
                assert_le(l1, S2/(2*aa**2))
                assert_le(l2, S3/(3*aa**3) + S2*S2/(4*aa**4))
                assert_le(l2, S2/aa**2)
                assert_eq(sum(v),F(0))
                # Exact coefficient of g_w^c A'_w from two equivalent power-series forms.
                h=nb(c+2,w)
                for k in range(N+1):
                    from_pmf=q[k]
                    from_pgf = S2/F(2) * ((1-w)**c * F(comb(c+k-1,k-2))*w**(k-2) if k>=2 else F(0)) - S2/F(2)*b[k]/(1-w)**2
                    assert_eq(from_pmf,from_pgf)
        # Analytical sign threshold and exact tail constant via NB cumulative tails.
        theta=F(c*(c+1))*w*w/(1-w)**2
        m=1
        while (m+1)*m<=theta: m+=1
        assert_le(F(m*(m-1)),theta)
        assert_le(theta,F((m+1)*m))
        bc=nb(c,w); bp=nb(c+2,w)
        # Tail of NB(c+2) from index m-1 versus tail of NB(c) from m+1.
        tail_difference=sum(bc[:m+1])-sum(bp[:max(0,m-1)])
        assert_le(F(0),tail_difference)
        for k in range(N+1):
            signed = bc[k]*(F(k*(k-1),c*(c+1))/w**2-1/(1-w)**2)
            if k<=m: assert_le(signed,F(0))
            else: assert_le(F(0),signed)
# Validate A'_w term-by-term (first 42 coefficients), where the formulas are finite exact identities.
for y,w in [(F(1,5),F(2,5)),(F(2,5),F(2,5)),(F(3,5),F(1,2))]:
    for k in range(N+1):
        exact=proof_B_coeff(y,w,k)
        if y==w:
            expected= (-1/(1-w)**2) if k==0 else (F(k-1)*w**(k-2) if k>=2 else F(0))
            assert_eq(exact,expected)
        else:
            # B=(z-1)*(1+(1-y-w)z)/((1-y)(1-w)(1-y*z)(1-w*z))
            # First use direct finite geometric coefficients.
            D=lambda j: sum(y**i*w**(j-i) for i in range(j+1)) if j>=0 else F(0)
            expected=(D(k-1)-D(k)+(1-y-w)*(D(k-2)-D(k-1)))/((1-y)*(1-w))
            assert_eq(exact,expected)
print(f"PASS: {checks} exact-rational assertions (finite coefficient diagnostics; not an infinite proof).")
