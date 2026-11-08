#!/usr/bin/env python3
"""Independent finite arithmetic and numerical tests for Fourier high-p asymptotics.
Only standard Python library; finite tests do not establish p->infinity theorems.
"""
import cmath
import math
import random


def power_coefficients(lam, a, q):
    coeff = {0: 1+0j}
    for _ in range(q):
        new = {}
        for k, x in coeff.items():
            for l, y in zip(lam, a):
                new[k+l] = new.get(k+l, 0j) + x*y
        coeff = new
    return coeff


def moment(lam, a, q):
    return sum(abs(v)**2 for v in power_coefficients(lam, a, q).values())


def normalized(v):
    s = math.sqrt(sum(x*x for x in v))
    return [x/s for x in v]


def optimizer(lam, q):
    # Positive-coefficient gradient ascent on the sphere using exact convolution
    # and central finite-difference derivative. Pure numerical corroboration.
    m=len(lam)
    a=[m**(-.5)]*m
    for step in range(2000):
        base=math.log(moment(lam,a,q))
        eps=2e-6
        grad=[]
        for j in range(m):
            ap=a.copy(); am=a.copy()
            ap[j]+=eps; am[j]-=eps
            ap=normalized(ap); am=normalized(am)
            grad.append((math.log(moment(lam,ap,q))-math.log(moment(lam,am,q)))/(2*eps))
        tangent=[v-sum(grad[k]*a[k] for k in range(m))*a[j] for j,v in enumerate(grad)]
        n=math.sqrt(sum(x*x for x in tangent))
        if n < 2e-7: break
        lr=min(0.015, 0.10/max(1,q))
        while lr>1e-11:
            nxt=normalized([a[j]+lr*tangent[j] for j in range(m)])
            if min(nxt)>0 and math.log(moment(lam,nxt,q))>=base-1e-12:
                a=nxt;break
            lr*=.5
        else: break
    return a


def run():
    checks=0
    rnd=random.Random(2608)
    for lam in [(0,1,3),(0,1,2),(0,2,5),(0,1,3,7)]:
        m=len(lam)
        mu=sum(lam)/m
        v=sum((l-mu)**2 for l in lam)/m
        g=0
        for l in lam[1:]:g=math.gcd(g,abs(l-lam[0]))
        for q in [2,3,4,5]:
            for _ in range(6):
                a=[complex(rnd.uniform(-1,1),rnd.uniform(-1,1)) for _ in lam]
                exact=moment(lam,a,q)
                N=1024
                # degree q*max(lam) <1024, trapezoid is exact to roundoff.
                quad=sum(abs(sum(a[j]*cmath.exp(2j*math.pi*lam[j]*k/N) for j in range(m)))**(2*q) for k in range(N))/N
                assert abs(exact-quad)<2e-7*max(1,exact),(lam,q,exact,quad)
                checks+=1
                maj=moment(lam,[abs(z) for z in a],q)
                assert exact <= maj+1e-7*max(1,maj)
                checks+=1
        for q in [20,40,80]:
            p=2*q
            a=optimizer(lam,q)
            target=[1/math.sqrt(m)-((l-mu)**2-v)/(2*p*math.sqrt(m)*v) for l in lam]
            assert max(abs(a[j]-target[j]) for j in range(m)) < 0.0007,(lam,p,a,target)
            checks+=1
            norm=moment(lam,a,q)**(1/p)
            pred=math.sqrt(m)*math.exp(math.log(g/math.sqrt(2*math.pi*p*v))/p)
            assert abs(norm-pred)<0.00025,(lam,p,norm,pred)
            checks+=1
    print('FINITE_FOURIER_HIGH_P_CHECKS_PASS',checks)

if __name__=='__main__':run()
