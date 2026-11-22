#!/usr/bin/env python3
"""Independent finite-state algebra and numerical semigroup checks for the stated theorem.
Finite checks corroborate, but do not replace, the all-size spectral proof.
"""
from fractions import Fraction as Q
from math import comb, exp, log


def kj(n, j, k):
    return sum((-1)**i * comb(k, i) * comb(n-k, j-i)
               for i in range(max(0, j-(n-k)), min(j,k)+1))


def conv(a, b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

# Exact generator, spectrum, and orthogonality checks for distinct n values.
for n in range(1, 12):
    pi=[Q(comb(n,k),2**n) for k in range(n+1)]
    assert sum(pi)==1
    for j in range(n+1):
        for k in range(n+1):
            val=-(2*j)*kj(n,j,k)
            lhs=Q(0)
            if k<n: lhs+=(n-k)*(kj(n,j,k+1)-kj(n,j,k))
            if k>0: lhs+=k*(kj(n,j,k-1)-kj(n,j,k))
            assert lhs==val, (n,j,k)
        for ell in range(n+1):
            inner=sum(pi[k]*kj(n,j,k)*kj(n,ell,k) for k in range(n+1))
            assert inner==(comb(n,j) if j==ell else 0), (n,j,ell)
    # Each assigned crossing time is exactly prescribed by an integer-root polynomial.
    roots=[Q(i,n) for i in range(1,n)]
    coeff=[Q(1)]
    for r in roots: coeff=conv(coeff,[-r,Q(1)])
    assert len(coeff)==n
    for r in roots:
        assert sum(c*r**i for i,c in enumerate(coeff))==0
    for j in range(n):
        # The coefficient of z^(j) can be assigned as difference of squares.
        c=coeff[j]
        assert (max(c, Q(0))-max(-c,Q(0)))==c

# Physical four-state model, with two independent spins flipping at rates 1 and 2.
states=[(1,1),(1,-1),(-1,1),(-1,-1)]
pi={s:Q(1,4) for s in states}
p={s:Q(1,4)*(1+Q(1,4)*(Q(12,25)*s[0]+s[0]*s[1])) for s in states}
q={s:Q(1,4)*(1+Q(1,4)*s[1]) for s in states}
assert sum(p.values())==sum(q.values())==1
assert min(p.values())==Q(63,400)
assert min(q.values())==Q(3,16)

def eval_mode(s, mode):
    return {'a':s[0],'b':s[1],'ab':s[0]*s[1]}[mode]

def Lphi(s, mode):
    a,b=s
    return (eval_mode((-a,b),mode)-eval_mode(s,mode)) +2*(eval_mode((a,-b),mode)-eval_mode(s,mode))
for mode,rate in [('a',2),('b',4),('ab',6)]:
    for s in states: assert Lphi(s,mode)==-rate*eval_mode(s,mode)

# Verify the two fixed crossing times and exact polynomial coefficients.
A=Q(12,25)**2
assert A==Q(9,25)*Q(16,25)
assert Q(9,25)+Q(16,25)==1

def d2(law):
    return sum((law[s]-pi[s])**2/pi[s] for s in states)
assert d2(p)-d2(q)==Q(1,16)*Q(144,625)

def flow(law,t):
    result={}
    for aa,bb in states:
        total=0.0
        for a,b in states:
            pa=(1+a*aa*exp(-2*t))/2
            pb=(1+b*bb*exp(-4*t))/2
            total+=float(law[(a,b)])*pa*pb
        result[(aa,bb)]=total
    return result

def d2f(law):
    return sum(4*(law[s]-0.25)**2 for s in states)

for t in [0.0,0.04,0.08,0.13,0.18,0.25,0.31,0.9,2.0]:
    z=exp(-4*t)
    exact=(1/16)*exp(-4*t)*(z-9/25)*(z-16/25)
    derived=d2f(flow(p,t))-d2f(flow(q,t))
    assert abs(exact-derived)<1e-13,(t,exact,derived)
assert 0 < log(Q(25,16))/4 < log(Q(25,9))/4
assert (1-Q(9,25))*(1-Q(16,25))>0
assert (Q(1,2)-Q(9,25))*(Q(1,2)-Q(16,25))<0
assert (Q(1,8)-Q(9,25))*(Q(1,8)-Q(16,25))>0
print('PASS: exact Krawtchouk eigen/orthogonality identities for N=1,...,11')
print('PASS: exact arbitrary rational crossing-factor construction for N=1,...,11')
print('PASS: normalized strictly positive physical four-state preparations and Walsh eigenmodes')
print('PASS: exact two-crossing polynomial and 9 independent time-semigroup comparisons')
print('t_early=',log(25/16)/4,'t_late=',log(25/9)/4)
