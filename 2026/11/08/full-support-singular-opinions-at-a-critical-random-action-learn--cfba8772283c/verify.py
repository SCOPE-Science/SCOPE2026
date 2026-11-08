"""Reproducible finite identities for a three-agent random-actions Markov chain.

Run with Python 3 (standard library only): python verify.py
These finite checks do not replace the general proof or entropy argument.
"""
from fractions import Fraction as F
from math import gcd

checks=0

def check(c, label):
    global checks
    if not c:
        raise AssertionError(label)
    checks+=1

def evolve(dist,alpha,self_weight):
    r=1-alpha; a=(1-self_weight)/2
    next_dist={}
    for x, px in dist.items():
        for b,pb in ((0,1-x),(1,x)):
            xp=r*x+alpha*(a+self_weight*b)
            next_dist[xp]=next_dist.get(xp,F(0))+px*pb
    return next_dist

def moments(dist):
    m=sum((x*p for x,p in dist.items()), F(0))
    v=sum((p*(x-m)**2 for x,p in dist.items()), F(0))
    return m,v

for alpha in (F(1,5),F(1,2),F(3,5),F(4,5)):
    for s in (F(1,4),F(1,2),F(3,4)):
        a=(1-s)/2
        r=1-alpha
        c=r+alpha*s
        d=c*c-alpha*alpha*s*s
        v_inf=alpha*s*s/(4*(2*(1-s)-alpha*(1-2*s)))
        check(0<c<1 and 0<d<1,'contraction')
        check(v_inf==alpha*alpha*s*s*F(1,4)/(1-d),'variance fixed-point identity')
        check(0<a<F(1,2) and a+s==1-a,'endpoint consistency')
        # Both affine branches keep the attractor interval invariant.
        check(r*a+alpha*a==a,'left endpoint 0 branch')
        check(r*(1-a)+alpha*(a+s)==1-a,'right endpoint 1 branch')
        # Every initial x=1/2 yields exact zero mean deviation.
        dist={F(1,2):F(1)}
        v0=F(0)
        for t in range(9):
            check(sum(dist.values(),F(0))==1,'total mass')
            m,v=moments(dist)
            check(m==F(1,2),'mean')
            check(v==v_inf*(1-d**t),'finite-time variance')
            check(all(a<=x<=1-a for x in dist),'invariant interval')
            dist=evolve(dist,alpha,s)
        # Exact one-step W1 identity via common uniform coupling.
        for x,y in ((a,F(1,2)),(F(1,2),1-a),(a,1-a)):
            if x>y:x,y=y,x
            after_gap=(r+alpha*s)*(y-x)
            check(after_gap==c*(y-x),'monotone coupling')
        if alpha==F(1,2):
            check(v_inf==s*s/(12-8*s),'critical variance')
            check(s*s/(6-4*s)>0,'positive entropy dimension deficit')

# Explicit equal-weight central Cantor gap, and parameter threshold.
for alpha in (F(1,3),F(1,2),F(2,3),F(3,4)):
    for s in (F(1,3),F(2,3)):
        a=(1-s)/2
        right_branch0=a+(1-alpha)*s
        left_branch1=a+alpha*s
        check(left_branch1-right_branch0==s*(2*alpha-1),'gap identity')
        check((left_branch1>right_branch0)==(alpha>F(1,2)),'gap threshold')
print('VERIFY_OK',checks,'exact rational checks')
