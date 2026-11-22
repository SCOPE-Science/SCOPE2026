#!/usr/bin/env python3
"""Standalone arithmetic diagnostics for a two-channel Poisson loading model.

All finite checks supplement the closed-form proof in RESULT.md.
Requires only Python 3 standard library.
"""
from fractions import Fraction
from itertools import product
from math import exp, log, sqrt, isclose
from random import Random

checks = 0

def test(condition, msg):
    global checks
    assert condition, msg
    checks += 1

# Sparse bivariate integer polynomials, a^i b^j.
def add(P, Q):
    R = P.copy()
    for k, v in Q.items(): R[k] = R.get(k, 0) + v
    return {k: v for k, v in R.items() if v}

def neg(P): return {k: -v for k,v in P.items()}
def mul(P,Q):
    R = {}
    for (i,j), v in P.items():
        for (k,l), w in Q.items():
            t = (i+k,j+l)
            R[t] = R.get(t,0)+v*w
    return {k:v for k,v in R.items() if v}

one={(0,0):1}; a={(1,0):1}; b={(0,1):1}
s=add(a,b); z=mul(a,b)
f_a=add(add(one,neg(a)),mul(a,a))
f_b=add(add(one,neg(b)),mul(b,b))
lhs=mul(f_a,f_b)
rhs=add(add(mul(s,s),neg(mul(add(one,z),s))),add(add(one,neg(z)),mul(z,z)))
test(lhs == rhs, 'exact symmetric-polynomial identity')

critical = 2*log(2+sqrt(3))
zc = exp(-critical)
test(isclose(zc, 7-4*sqrt(3),rel_tol=1e-13), 'critical z')
test(isclose(4*sqrt(zc),1+zc,rel_tol=1e-13), 'transition discriminant')

def one_failure(v):
    e=exp(-v)
    return 1-e+e*e

def prob(vs):
    F=1.0
    for v in vs: F *= one_failure(v)
    return 1-F

def optimum_two(V):
    z=exp(-V)
    if V<=critical:
        return (V/2, V/2), prob((V/2,V/2))
    s=(1+z)/2
    delta=sqrt(max(0,s*s-4*z))
    a=(s+delta)/2
    b=z/a # avoid cancellation for large V
    return (-log(a),-log(b)), 1-0.75*(1-z)**2

for V in [0.01,0.1,0.6,1,2,critical,critical+1e-7,3,4,5,7,10,13]:
    vs, p=optimum_two(V)
    test(isclose(sum(vs),V,rel_tol=1e-10,abs_tol=1e-10), f'conservation V={V}')
    test(isclose(prob(vs),p,rel_tol=1e-10,abs_tol=1e-10), f'formula V={V}')
    for i in range(401):
        x=V*i/400
        test(prob((x,V-x)) <= p + 4e-14, f'optimality grid V={V} x={x}')

rng=Random(20261120)
for _ in range(5000):
    V=rng.uniform(.0001,18)
    x=rng.uniform(0,V)
    _, p=optimum_two(V)
    test(prob((x,V-x)) <= p+1e-13, 'random allocation')

for eps in [1e-2,1e-3,1e-4,1e-5]:
    (u,v),_=optimum_two(critical+eps)
    test(abs((v-u)/sqrt(eps) - sqrt(2*sqrt(3))) < 0.02, 'square root onset')

# Many-chamber structural and asymptotic diagnostics. Candidate general
# optimum reduces to either equal loading or a single exceptional chamber.
h=log(2+sqrt(3))

def candidate_m(m,V):
    equal=[V/m]*m
    best=equal
    bestP=prob(equal)
    if V <= h: return best,bestP
    hi=min(h, V/(m-1))
    # fine scan for supplementary checks; not used to prove uniqueness.
    for i in range(1601):
        small=hi*i/1600
        large=V-(m-1)*small
        if large < h: continue
        layout=[small]*(m-1)+[large]
        p=prob(layout)
        if p>bestP:
            bestP=p; best=layout
    return best,bestP

for m in range(3,8):
    for V in [2,4,8,12,20]:
        best,bp=candidate_m(m,V)
        for _ in range(1000):
            weights=[-log(rng.random()) for j in range(m)]
            zsum=sum(weights)
            layout=[V*w/zsum for w in weights]
            test(prob(layout)<=bp+2e-5,f'many-channel probe n={m} V={V}')

for m in range(2,7):
    for V in [16,20,24]:
        if m==2: layout,p=candidate_m(2,V)
        else: layout,p=candidate_m(m,V)
        s=sorted(layout)[0]
        pred=1-(.75)**(m-1)+(1.5)**(m-1)*exp(-V)
        test(abs(s-log(2))<0.01, f'm={m} small asymptotic')
        test(abs(p-pred)<4e-6, f'm={m} detection asymptotic')

# Unequal target/inhibitor intensities: curvature switching and the
# general one-exceptional-channel variational reduction.
def failure_general(x, lam, mu):
    return 1-exp(-mu*x)+exp(-(lam+mu)*x)

def H(a,p):
    return -1+p*p*a**(p-1)-(p-1)**2*a**p

def inflection(lam,mu):
    p=1+lam/mu
    lo,hi=0.,1.
    for _ in range(85):
        mid=(lo+hi)/2
        if H(mid,p)>0: hi=mid
        else: lo=mid
    return -log((lo+hi)/2)/mu

def log_second(x,lam,mu):
    a=exp(-mu*x)
    p=1+lam/mu
    return mu*mu*a*H(a,p)/failure_general(x,lam,mu)**2

def probability_general(xs,lam,mu):
    v=1.
    for x in xs: v*=failure_general(x,lam,mu)
    return 1-v

def candidate_general(m,W,lam,mu):
    h=inflection(lam,mu)
    equal=[W/m]*m
    best=equal
    bp=probability_general(equal,lam,mu)
    upper=min(h,W/(m-1))
    for j in range(1501):
        small=upper*j/1500
        large=W-(m-1)*small
        if large<h: continue
        v=probability_general([small]*(m-1)+[large],lam,mu)
        if v>bp: bp=v; best=[small]*(m-1)+[large]
    return best,bp

for lam,mu in [(1.,1.),(.1,2.),(3.,.5),(6.,4.),(1.,6.)]:
    h=inflection(lam,mu)
    test(log_second(h*.5,lam,mu)>0, 'convex small loads')
    test(log_second(h*1.5,lam,mu)<0, 'concave large loads')
    for i in range(1,81):
        x=h*i/40
        test((x<h)==(log_second(x,lam,mu)>0) if i!=40 else abs(log_second(x,lam,mu))<1e-12,'single inflection')
    single=log(1+lam/mu)/lam
    for m in [2,3,5]:
        for W in [0.3,1.2,3.5,8.,18.]:
            best,bp=candidate_general(m,W,lam,mu)
            for _ in range(60):
                weights=[rng.expovariate(1.) for _ in range(m)]
                tot=sum(weights)
                alloc=[W*v/tot for v in weights]
                test(probability_general(alloc,lam,mu)<=bp+5e-5,'arbitrary rate global comparison')
            if W > (m-1)*single + 10*h:
                test(abs(sorted(best)[0]-single)<0.1,'general large-volume concentration')

print('PASS',checks,'finite and symbolic assertions')
print('Vc =',format(critical,'.15f'))
for V in [3,5]:
    vs,p=optimum_two(V)
    print('V=',V,'volumes=',vs,'optimum=',p,'equal=',prob((V/2,V/2)))
