#!/usr/bin/env python3
"""Reproduce exact and high-precision checks for the bounded Haldane illumination theorem.
All tests use Python's standard library and deterministic seeds.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import math
import random

getcontext().prec = 70
D = Decimal
checks = 0

def chk(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)

def growth(u,c):
    return u/(1+u+c*u*u)

def tangent_level(L,c):
    return (1+(1+L+c*L*L).sqrt())/(c*L)

def curvature_numerator(u,c):
    return c*c*u*u*u-3*c*u-1

def upper_value(m,L,c):
    q=tangent_level(L,c)
    if m<=q: return growth(m,c)
    w=(m-q)/(L-q)
    return (1-w)*growth(q,c)+w*growth(L,c)

def check_analytic():
    # Rational pointwise identity, after clearing denominators and using
    # the quadratic defining q, can be checked without approximate q.
    # P(q) = c^2 L q^2 -2cq -cL-1.
    for c in [Fraction(1,4),Fraction(1),Fraction(5,3),Fraction(8)]:
        for L in [Fraction(2),Fraction(3),Fraction(8),Fraction(11,2)]:
            # Check exact coefficient identity for all rational q,u even off root:
            # L(1+q+cq²)^2(1+u+cu²) * (tangent-f(u))
            # - (2cq+1)(u-q)^2(L-u) = -u(u-q)^2 P(q).
            for q in [Fraction(1,3),Fraction(3,2),Fraction(4,5)]:
                for u in [Fraction(0),Fraction(1,7),Fraction(2), L]:
                    f=lambda z:growth(z,c)
                    fp=(1-c*q*q)/(1+q+c*q*q)**2
                    tangent=f(q)+fp*(u-q)
                    lhs=L*(1+q+c*q*q)**2*(1+u+c*u*u)*(tangent-f(u))-(2*c*q+1)*(u-q)**2*(L-u)
                    P=c*c*L*q*q-2*c*q-c*L-1
                    rhs=-u*(u-q)**2*P
                    chk(lhs==rhs,('cleared polynomial identity',c,L,q,u))

def check_curvature_and_threshold():
    for ic in [D('0.02'),D('0.125'),D('0.5'),D('1'),D('7'),D('20')]:
        lo=D(0); hi=max(D(3),(D(1)/ic.sqrt())*D(5))
        while curvature_numerator(hi,ic)<0: hi*=2
        for _ in range(240):
            mid=(lo+hi)/2
            if curvature_numerator(mid,ic)>0: hi=mid
            else:lo=mid
        r=(lo+hi)/2
        chk(abs(curvature_numerator(r,ic))<D('1e-58'),'inflection residual')
        for factor in [D('0.15'),D('0.9'),D('0.999'),D('1.001'),D('1.1'),D('4')]:
            L=r*factor
            q=tangent_level(L,ic)
            eq=ic*ic*L*q*q-2*ic*q-ic*L-1
            chk(abs(eq)<D('1e-58'),'tangency residual')
            if L>r: chk(0<q<r<L,'q below inflection')
            else: chk(q>=L,'cap below inflection')

def check_pointwise_and_global():
    rnd=random.Random(2026111502)
    for c_s,L_s in [('1','10'),('0.01','40'),('2','3'),('0.5','10')]:
        c=D(c_s);L=D(L_s);q=tangent_level(L,c)
        # Only these choices with L>inflection are used here.
        chk(q<L,'test cap beyond inflection')
        fp=(1-c*q*q)/(1+q+c*q*q)**2
        f=lambda u:growth(u,c)
        for j in range(1000):
            u=L*D(j)/D(999)
            tangent=f(q)+fp*(u-q)
            K=(2*c*q+1)/(L*(1+q+c*q*q)**2)
            slack=K*(u-q)**2*(L-u)/(1+u+c*u*u)
            chk(abs(tangent-f(u)-slack)<D('1e-55'),'slack identity')
            chk(tangent+ D('1e-55')>=f(u),'supporting upper line')
        for j in range(300):
            m=L*D(j)/D(299)
            opt=upper_value(m,L,c)
            # Random 3-atomic mean-constrained distributions; test Jensen envelope.
            u1=L*D(str(rnd.random())); u2=L*D(str(rnd.random()))
            u3=L*D(str(rnd.random()))
            # Construct mixture from three atoms, then use its OWN mean.
            w1=D(str(rnd.random())); w2=D(str(rnd.random())); w3=D(str(rnd.random()))
            W=w1+w2+w3
            w1/=W;w2/=W;w3/=W
            mu=w1*u1+w2*u2+w3*u3
            avg=w1*f(u1)+w2*f(u2)+w3*f(u3)
            chk(avg <= upper_value(mu,L,c)+D('1e-55'),'global upper bound')
            # Exact two-point mean and supporting line equality
            if m>q:
                w=(m-q)/(L-q)
                chk(abs((1-w)*q+w*L-m)<D('1e-55'),'fixed mean achieved')
                chk(abs((1-w)*f(q)+w*f(L)-opt)<D('1e-55'),'optimizer rate')

def main():
    check_analytic()
    check_curvature_and_threshold()
    check_pointwise_and_global()
    c=D(1);L=D(10);m=D(4)
    q=tangent_level(L,c)
    w=(m-q)/(L-q)
    print('checks:', checks)
    print('example q:',format(q,'.18f'))
    print('example high duty:',format(w,'.18f'))
    print('example optimal:',format(upper_value(m,L,c),'.18f'))
    print('example constant:',format(growth(m,c),'.18f'))
    print('relative increase (%):', format((upper_value(m,L,c)/growth(m,c)-1)*100,'.12f'))
    print('PASS')

if __name__=='__main__':main()
