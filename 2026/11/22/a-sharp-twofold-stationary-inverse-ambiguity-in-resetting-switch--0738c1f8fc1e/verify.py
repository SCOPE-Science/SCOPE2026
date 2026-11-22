#!/usr/bin/env python3
"""Exact-rational verification for a two-state resetting-diffusion inverse theorem.

Run with: python3 verify.py
Requires only Python's standard library. This finite test suite complements,
but does not replace, the algebraic proof supplied in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

CHECKS = 0

def eq(x, y, label):
    global CHECKS
    CHECKS += 1
    if x != y:
        raise AssertionError(f'{label}: {x} != {y}')


def inv2(a, b, c, d, y0, y1):
    det = a*d-b*c
    return ((d*y0-b*y1)/det, (-c*y0+a*y1)/det)


def params(d0, d1, r, alpha, beta):
    s = alpha+beta
    theta = alpha/s
    m = (beta*d0+alpha*d1)/s
    n = d0+d1-m
    h = r*(r+s)
    return (n/(r+s), (r*(d0+d1)+s*m)/h, d0*d1/h, m, n, s, theta, h)


def dual(d0, d1, r, alpha, beta):
    _, _, _, m, n, s, theta, h = params(d0,d1,r,alpha,beta)
    rd = r*n/m
    sd = h/rd-rd
    return rd, sd*(1-theta), sd*theta


def moments(d0,d1,r,alpha,beta,degree=3):
    # Solve the joint phase-resolved polynomial moment hierarchy directly.
    s=alpha+beta
    m=(beta/s,alpha/s)
    out=[]
    for j in range(1,degree+1):
        k=F((2*j)*(2*j-1))
        m=inv2(r+alpha,-beta,-alpha,r+beta,k*d0*m[0],k*d1*m[1])
        out.append((m[0]+m[1])/F(__import__('math').factorial(2*j)))
    return out


def recover(d0,d1,u1,u2,u3):
    b=(u3-u1*u2)/(u2-u1*u1)
    c=b*u1-u2
    a=b-u1
    h=d0*d1/c
    # Solve by Vieta from candidate's mean m in a constrained interval.
    disc=(d0+d1)**2-4*u1*a*h
    from math import isqrt
    nd,dd=disc.numerator,disc.denominator
    nds,dds=isqrt(nd),isqrt(dd)
    assert nds*nds==nd and dds*dds==dd
    root=F(nds,dds)
    opts=[]
    for rr in {(d0+d1+root)/(2*u1),(d0+d1-root)/(2*u1)}:
        mm=u1*rr
        ss=h/rr-rr
        if not (d0<mm<d1 and ss>0):
            continue
        th=(mm-d0)/(d1-d0)
        opts.append((rr,ss*th,ss*(1-th)))
    return sorted(opts), (a,b,c), disc


def check_model(d0,d1,r,alpha,beta):
    a,b,c,m,n,s,th,h=params(d0,d1,r,alpha,beta)
    u=moments(d0,d1,r,alpha,beta)
    predicted=[b-a,b*(b-a)-c,b*(b*(b-a)-c)-c*(b-a)]
    for j in range(3):eq(u[j],predicted[j],f'moment {j+1}')
    eq(u[1]-u[0]*u[0],th*(1-th)*(d1-d0)**2/(r*(r+s)),'irreducible')
    candidates,(aa,bb,cc),disc=recover(d0,d1,*u)
    eq((aa,bb,cc),(a,b,c),'coefficient recovery')
    eq((r,alpha,beta) in candidates,True,'original feasible')
    rd,ad,bd=dual(d0,d1,r,alpha,beta)
    if ad>0 and bd>0:
        eq((rd,ad,bd) in candidates,True,'dual feasible')
        for zz in (F(0),F(1,9),F(1),F(13,7)):
            a2,b2,c2,*_=params(d0,d1,rd,ad,bd)
            eq((1+a*zz)/(1+b*zz+c*zz*zz),(1+a2*zz)/(1+b2*zz+c2*zz*zz),'dual phi')
    else:
        eq(len(candidates),1,'no unphysical dual')
    eq(len(candidates),1 if th==F(1,2) or not (ad>0 and bd>0) else 2,'cardinality')
    return len(candidates)


if __name__=='__main__':
    # A concrete exact spatial alias with different reset rates.
    d0,d1=F(1),F(3)
    model=(F(1),F(3,2),F(1,2))
    partner=(F(3,5),F(11,10),F(33,10))
    eq(dual(d0,d1,*model),partner,'example dual')
    eq(params(d0,d1,*model)[:3],(F(1,2),F(3),F(1)),'example transform')
    eq(params(d0,d1,*partner)[:3],(F(1,2),F(3),F(1)),'example partner')
    eq(moments(d0,d1,*model),moments(d0,d1,*partner),'sixth moments alias')
    eq(moments(d0,d1,*model)[0],F(5,2),'example variance/2')

    count={1:0,2:0}
    for d0,d1 in [(F(1),F(2)),(F(1),F(3)),(F(2),F(7))]:
        for r in [F(1,2),F(1),F(4)]:
            for alpha in [F(1,5),F(1),F(7,2)]:
                for beta in [F(1,4),F(1),F(5)]:
                    count[check_model(d0,d1,r,alpha,beta)] += 1
    eq(sum(count.values()),81,'sample count')
    print(f'PASS: {CHECKS} exact-rational assertions across {sum(count.values())} positive parameter tuples;')
    print(f'      physically admissible model cardinalities: {count}')
    print('The analytic proof covers all real positive rates, not only these tuples.')
