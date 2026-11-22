#!/usr/bin/env python3
"""Numerical diagnostics for a two-wave dose-timing theorem; proof is analytic."""
import math

checks = 0

def verify(condition, message):
    global checks
    assert condition, message
    checks += 1

def U(t):
    return math.exp(-20*t)*(t/21+1/441)

def V(t):
    return math.exp(-t/4)*(4*t/5+16/25)

def J(A,t):
    return A*U(t)+V(t)

def F(A,t):
    return A*math.exp(-20*t)*(1/441-20*t/21)+math.exp(-t/4)*(16/25-t/5)

def root(A,lo,hi):
    x, y = F(A,lo), F(A,hi)
    verify(x*y < 0, 'root bracket does not change sign')
    for _ in range(85):
        mid = (lo+hi)/2
        if (F(A,mid)>0) == (x>0):
            lo, x = mid, F(A,mid)
        else:
            hi, y = mid, F(A,mid)
    result = (lo+hi)/2
    verify(abs(F(A,result)) < 1e-10, 'root residual')
    return result

def all_roots(A):
    return [root(A,0,1/20),root(A,1/20,1),root(A,1,4)]

def difference(A):
    x,y,z=all_roots(A)
    return J(A,x)-J(A,z)

verify(abs(U(0)-1/441)<1e-15,'zero value')
verify(abs(V(0)-16/25)<1e-15,'zero value')
verify(abs(U(1/420)-math.exp(-1/21)/420)<1e-15,'fast maximum')
verify(abs(V(16/5)-16/5*math.exp(-4/5))<1e-15,'slow maximum')

for k in range(401):
    A=100+k
    verify(F(A,0)>0 and F(A,1/20)<0 and F(A,1)>0 and F(A,4)<0,'four fixed signs')
    r=all_roots(A)
    verify(0<r[0]<1/20<r[1]<1<r[2]<4,'root ordering')
    verify(J(A,r[0])>J(A,0),'early increase')
    verify(J(A,r[2])>J(A,4),'late maximum')
    verify(J(A,r[0])>J(A,r[1]) and J(A,r[2])>J(A,r[1]),'two maxima')
    verify(U(r[0])>U(r[2]),'strict envelope derivative')

verify(difference(100)<0,'later optimum at lower amplitude')
verify(difference(500)>0,'earlier optimum at upper amplitude')
lo,hi=100.,500.
for i in range(53):
    mid=(lo+hi)/2
    if difference(mid)>0: hi=mid
    else: lo=mid
Ac=(lo+hi)/2
r=all_roots(Ac)
verify(350.47<Ac<350.49,'crossing interval')
verify(abs(difference(Ac))<1e-10,'equal height')
verify(0.0044<r[0]<0.0046 and 3.199<r[2]<3.201,'two date estimates')

# Direct interpretation of survival probabilities at one nontrivial hazard scale.
for A in (100.,Ac,500.):
    r=all_roots(A)
    for scale in (.001,.02,.1):
        base=scale*(A/400+16)
        p=[math.exp(-base+scale*J(A,t)) for t in r]
        verify(all(0<item<1 for item in p),'valid infection-free probabilities')
        verify(p[0]>p[1] and p[2]>p[1],'probability shares the local extrema')
print('PASS',checks,'assertions; crossover',format(Ac,'.12f'), 'stationary dates', [format(t,'.12f') for t in r])
