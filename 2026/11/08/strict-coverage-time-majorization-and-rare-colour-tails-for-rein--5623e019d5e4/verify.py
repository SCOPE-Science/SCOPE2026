"""Exact and numerical checks for Dirichlet--Pólya urn full-color coverage.
Run: python3 verify.py (standard library only).
All checks use the same reinforcement convention: replace drawn ball and add one.
"""
from fractions import Fraction
from math import factorial, gamma, prod, lgamma, exp
from itertools import product

assertions=0
def check(ok, note=''):
    global assertions
    assert ok, note
    assertions += 1

def rising(a,n):
    y=1
    for j in range(n):y*=a+j
    return y

def by_inclusion(alpha,t):
    k=len(alpha); A=sum(alpha)
    if t==0:return Fraction(1)
    v=Fraction(0)
    for mask in range(1,1<<k):
        missing=sum(alpha[i] for i in range(k) if mask>>i&1)
        if missing==A:continue
        j=mask.bit_count()
        v += (-1)**(j+1)*Fraction(rising(A-missing,t),rising(A,t))
    return v

def by_compositions(alpha,t):
    k=len(alpha); A=sum(alpha)
    tot=Fraction(0); covered=Fraction(0)
    def rec(index, left, cs):
        nonlocal tot,covered
        if index==k-1:
            xs=cs+(left,)
            pr=Fraction(factorial(t)*prod(rising(a,c) for a,c in zip(alpha,xs)),rising(A,t)*prod(factorial(c) for c in xs))
            tot+=pr
            if all(x>0 for x in xs):covered+=pr
            return
        for j in range(left+1):rec(index+1,left-j,cs+(j,))
    rec(0,t,())
    check(tot==1,'probabilities sum')
    return 1-covered

def by_paths(alpha,t):
    k=len(alpha);A=sum(alpha);s=Fraction(0)
    def go(counts,seen,steps,prob):
        nonlocal s
        if steps==t:
            if seen != (1<<k)-1:s+=prob
            return
        d=A+steps
        for i in range(k):
            c=list(counts)
            go(tuple(c[:i]+[c[i]+1]+c[i+1:]),seen|(1<<i),steps+1,prob*Fraction(alpha[i]+c[i],d))
    go((0,)*k,0,0,Fraction(1))
    return s

# Exact distributions checked by independent probability-mass counting.
for a in [(1,1),(1,2),(2,3),(1,1,1),(2,1,1),(2,2,1),(1,1,1,1),(Fraction(1,2),Fraction(3,2)), (Fraction(2,3),Fraction(4,3),Fraction(5,2))]:
    for t in range(0,11):
        IE=by_inclusion(a,t)
        check(IE==by_compositions(a,t),('mass',a,t))
        if t <= 6:
            check(IE==by_paths(a,t),('paths',a,t))
        check(Fraction(0)<=IE<=Fraction(1),('bounds',a,t))
        if t>0:check(IE<=by_inclusion(a,t-1),('monotone',a,t))

# Balancing a pair in the initial composition strictly speeds full cover for t >= k.
for a,b in [((4,1),(3,2)),((5,1,1),(4,2,1)),((5,1,1),(3,3,1)),((3,3,1),(3,2,2)),((4,1,1,1),(3,2,1,1)),((6,1,2),(4,3,2)),((4,2,2),(3,3,2)),((Fraction(5,2),Fraction(1,2)),(Fraction(3,2),Fraction(3,2))),((Fraction(7,3),Fraction(2,3),Fraction(1,2)),(Fraction(5,3),Fraction(4,3),Fraction(1,2)))]:
    check(sum(a)==sum(b),'total conserved')
    for t in range(0,15):
        pa,pb=by_inclusion(a,t),by_inclusion(b,t)
        check((pa==pb if t<len(a) else pa>pb), ('strict balancing',a,b,t,pa,pb))

# Pair split kernel: for every M >=2, ((x)_M + (h-x)_M)/(h)_M is
# strictly reduced by balancing. Check rational and integer splits.
for h in range(3,18):
    for x in range(1,h):
        for M in range(2,11):
            old=Fraction(rising(x,M)+rising(h-x,M),rising(h,M))
            mid=Fraction(rising(Fraction(h,2),M)*2,rising(h,M))
            check(old>=mid,('convex pair kernel',h,x,M))
            if x!=h-x:check(old>mid,('strict convex pair kernel',h,x,M))

# Leading constants via logarithmic rising factorial evaluation (integer alpha).
# Avoid cancellation in inclusion-exclusion by checking the single-missing and
# double-missing orders independently.
for a in [(1,1),(1,1,1),(1,2,3),(2,2,3),(3,2,2)]:
    A=sum(a); mini=min(a);m=sum(x==mini for x in a)
    K=m*gamma(A)/gamma(A-mini)
    for t in (10000,1000000):
        singles=sum(exp(lgamma(A)-lgamma(A-x)+lgamma(A-x+t)-lgamma(A+t)) for x in a)
        check(abs(singles*t**mini/K-1)<0.01,('tail constant',a,t))
        # At most one unseen color asymptotically: the union bound on double misses
        # is o(t^(-a_min)); inspect the ratio exactly via Gamma identities.
        doubles=sum(exp(lgamma(A)-lgamma(A-a[i]-a[j])+lgamma(A-a[i]-a[j]+t)-lgamma(A+t))
                    for i in range(len(a)) for j in range(i+1,len(a)) if A>a[i]+a[j])
        check(doubles/singles<0.01,('multiple unseen',a,t))

print('VERIFY_OK', assertions)
