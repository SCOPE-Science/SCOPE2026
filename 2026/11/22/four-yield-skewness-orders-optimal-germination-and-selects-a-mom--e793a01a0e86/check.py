"""Exact-rational checks for the four-yield germination moment law.

Uses only Python's standard library. All statements certified by the accompanying
written proof; finite assertions are supplementary tests, not an infinite proof.
Run with: python3 check.py
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random

checks = 0

def assert_true(value):
    global checks
    assert value
    checks += 1

def deriv(xs, ps, s, g):
    return sum((pi*(xi-s)/(s+g*(xi-s)) for pi,xi in zip(ps,xs)),Q(0))

def moments(xs, ps):
    return tuple(sum((p*x**k for p,x in zip(ps,xs)),Q(0)) for k in range(4))

def q_weights(xs):
    return [Q(1,1)/prod([xs[i]-xs[j] for j in range(4) if i != j]) for i in range(4)]

def prod(terms):
    z=Q(1)
    for x in terms: z*=x
    return z

xs = [Q(i,2) for i in range(1,5)]
s = Q(24,25)
minus=[Q(x,24) for x in (7,3,9,5)]
plus=[Q(x,24) for x in (5,9,3,7)]
assert_true(moments(xs,minus)[:3]==moments(xs,plus)[:3])
assert_true(moments(xs,minus)[:3]==(Q(1),Q(5,4),Q(15,8)))
assert_true(moments(xs,minus)[3]==Q(99,32))
assert_true(moments(xs,plus)[3]==Q(101,32))
assert_true(deriv(xs,minus,s,Q(1))==-Q(1,50))
assert_true(deriv(xs,plus,s,Q(1))==Q(1,50))
assert_true(deriv(xs,minus,s,Q(9,10))>0)
assert_true(deriv(xs,minus,s,Q(19,20))<0)
assert_true(deriv(xs,plus,s,Q(1))>0)

# Exact feasible moment-law endpoints, with independent checking of the
# third-moment sensitivity formula for rational g.
lo=[Q(1,3),Q(0),Q(1,2),Q(1,6)]
hi=[Q(1,6),Q(1,2),Q(0),Q(1,3)]
assert_true(moments(xs,lo)[:3]==moments(xs,hi)[:3])
assert_true(moments(xs,lo)[3]==Q(49,16))
assert_true(moments(xs,hi)[3]==Q(51,16))
assert_true(deriv(xs,lo,s,Q(89,100))>0)
assert_true(deriv(xs,lo,s,Q(90,100))<0)
assert_true(deriv(xs,hi,s,Q(1))>0)

rng=Random(271828)
for _ in range(400):
    x=sorted(rng.sample(range(1,80),4))
    x=[Q(z,11) for z in x]
    ss=Q(rng.randint(1,10),11)
    pp=[Q(rng.randint(1,20),1) for _ in range(4)]
    pp=[v/sum(pp) for v in pp]
    mu,nu,m3=moments(x,pp)[1:]
    e1=sum(x)
    e2=sum(x[i]*x[j] for i,j in combinations(range(4),2))
    e3=sum(x[i]*x[j]*x[k] for i,j,k in combinations(range(4),3))
    e4=prod(x)
    harmonic=sum((pp[i]/x[i] for i in range(4)),Q(0))
    assert_true(harmonic==(e3-e2*mu+e1*nu-m3)/e4)
    assert_true(deriv(x,pp,ss,Q(1))==1-ss*harmonic)
    qw=q_weights(x)
    for k in range(3):
        assert_true(sum((qw[i]*x[i]**k for i in range(4)),Q(0))==0)
    assert_true(sum((qw[i]*x[i]**3 for i in range(4)),Q(0))==1)
    for g in (Q(1,9),Q(1,2),Q(7,8),Q(1)):
        diff=sum((qw[i]*(x[i]-ss)/(ss+g*(x[i]-ss)) for i in range(4)),Q(0))
        exact=ss*g*g/prod([ss+g*(xi-ss) for xi in x])
        assert_true(diff==exact)
        assert_true(exact>0)

print('PASS',checks,'exact rational assertions')
