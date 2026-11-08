#!/usr/bin/env python3
"""Independent exact enumeration of source / two-step-path covariance.
Python 3 standard library only; run: python3 check.py.
"""
from fractions import Fraction as Q
from itertools import product


def F(b, q):
    return q**(b-1)*(1-(b+1)*q)+(1-q)*((2*b-1)*q-b)


def prediction(b, q):
    return 2*b*q*(1-q)*F(b,q)


def exact_enumeration(b, q):
    # K_{2,b}: each coordinate is the pair (A0->Bj, A1->Bj).
    num, den = q.numerator, q.denominator
    z = den**(2*b)
    s1 = p1 = sp = mass = 0
    for state in product(range(4), repeat=b):
        x = y = s_b = p_b = 0
        for r in state:
            e0, e1 = r & 1, (r >> 1) & 1
            x += e0
            y += e1
            t = e0+e1
            s_b += (t==0)
            p_b += (t==1)
        s = (x==b) + (y==b) + s_b
        path2 = x*(b-x)+y*(b-y)+p_b
        weight = num**(x+y) * (den-num)**(2*b-x-y)
        s1 += weight*s
        p1 += weight*path2
        sp += weight*s*path2
        mass += weight
    assert mass == z, (b,q,mass,z)
    return Q(sp*z-s1*p1,z*z)


def derivative(b,q):
    return (b-1)*q**(b-2)-b*(b+1)*q**(b-1)+(3*b-1)-2*(2*b-1)*q


def check():
    tests=0
    for b in range(2,8):
        for q in [Q(1,5),Q(1,4),Q(2,5),Q(1,2),Q(3,5),Q(5,8),Q(13,20),Q(3,4),Q(4,5)]:
            got=exact_enumeration(b,q)
            want=prediction(b,q)
            assert got==want,(b,q,got,want)
            tests+=1
    # Polynomial negativity certificates: strict concavity plus tangent lines.
    # The maximum of each affine tangent on [0,1] occurs at an endpoint.
    for b,t in [(3,Q(11,20)),(4,Q(7,12)),(5,Q(3,5))]:
        v,m=F(b,t),derivative(b,t)
        assert max(v-m*t, v+m*(1-t))<0,(b,t)
        tests+=1
    for b in range(6,101):
        assert F(b,Q(5,8))>0,b
        assert F(b,Q(1,2))<0,b
        tests+=2
    for b in range(2,6):
        for i in range(1,100):
            assert F(b,Q(i,100))<0,(b,i)
            tests+=1
    assert F(6,Q(5,8))==Q(1641,262144)
    assert prediction(6,Q(5,8))==Q(73845,4194304)
    tests+=2
    print(f'PASS: {tests} exact enumerations and rational-sign checks.')
    print('K_{2,6} at bias 5/8: covariance = 73845/4194304 > 0.')
    print('Computational checks supplement the analytic proof; they do not establish its infinite statements.')

if __name__=='__main__':
    check()
