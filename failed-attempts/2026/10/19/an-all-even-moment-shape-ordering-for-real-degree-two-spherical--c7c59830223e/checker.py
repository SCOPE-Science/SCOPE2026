#!/usr/bin/env python3
"""Exact checks for even moments of real quadratic spherical harmonics."""
from fractions import Fraction as F
from math import factorial, comb
from itertools import product


def odd_double_fact(n):
    out = 1
    for k in range(1, n + 1, 2):
        out *= k
    return out


def poch_half(n):
    y = F(1)
    for k in range(n):
        y *= F(2*k+1,2)
    return y


def invariant_moment(m, a, b, c):
    # A is the diagonal traceless matrix diag(a,b,c).
    assert a+b+c==0
    s2=a*a+b*b+c*c
    det=a*b*c
    u=F(det*det, s2**3)
    poly = F(0)
    for j in range(m//3+1):
        poly+=poch_half(m-j)*F((2*s2)**(m-3*j)*(64*det*det)**j, factorial(m-3*j)*factorial(2*j))
    return F(factorial(2*m),odd_double_fact(4*m+1))*poly


def direct_sphere_moment(m,a,b,c):
    n=2*m
    terms=F(0)
    for i in range(n+1):
        for j in range(n-i+1):
            k=n-i-j
            multi=F(factorial(n),factorial(i)*factorial(j)*factorial(k))
            num=odd_double_fact(2*i-1)*odd_double_fact(2*j-1)*odd_double_fact(2*k-1)
            terms+=multi*a**i*b**j*c**k*num
    return terms/F(odd_double_fact(4*m+1))


def normalized_polynomial(m):
    cs=[]
    for j in range(m//3+1):
        coefficient=F(factorial(2*m),odd_double_fact(4*m+1))*F(15,2)**m
        coefficient*=poch_half(m-j)*F((2**(m-3*j))*(64**j),factorial(m-3*j)*factorial(2*j))
        cs.append(coefficient)
    return cs


def at(cs,x):
    return sum(c*x**i for i,c in enumerate(cs))


def main():
    cnt=0
    for m in range(1,11):
        cs=normalized_polynomial(m)
        assert all(c>0 for c in cs)
        if m<=2: assert len(cs)==1
        if m>=3: assert len(cs)>=2 and cs[1]>0
        cnt+=1
    assert normalized_polynomial(1)==[F(1)]
    assert normalized_polynomial(2)==[F(15,7)]
    assert normalized_polynomial(3)==[F(5625,1001),F(54000,1001)]
    assert at(normalized_polynomial(3),F(1,54))==F(6625,1001)
    assert at(normalized_polynomial(3),F(0))==F(5625,1001)
    cnt+=5
    # Independently compute spherical integrals by exact monomial moments.
    shapes=[(1,-1,0),(2,-1,-1),(5,-2,-3),(1,2,-3),(9,-4,-5),
        (F(1,2),F(2,3),F(-7,6)),(F(4,7),F(-1,7),F(-3,7))]
    for m in range(1,10):
        for shape in shapes:
            aa,bb,cc=map(F,shape)
            independent=direct_sphere_moment(m,aa,bb,cc)
            via_mgf=invariant_moment(m,aa,bb,cc)
            assert independent==via_mgf,(m,shape,independent,via_mgf)
            cnt+=1
    # Independently obtain upper/lower L6 levels from exact sphere integration.
    for shape,want in [((1,-1,0),F(5625,1001)),((2,-1,-1),F(6625,1001))]:
        a,b,c=map(F,shape)
        q2=direct_sphere_moment(1,a,b,c)
        q6=direct_sphere_moment(3,a,b,c)
        assert q6/q2**3==want
        cnt+=1
    # Matrix characteristic discriminant: nonnegative for symmetric eigenvalues.
    for a in range(-8,9):
        for b in range(-8,9):
            c=-a-b
            if a==b==c==0: continue
            s2=a*a+b*b+c*c
            d=a*b*c
            assert s2**3-54*d*d>=0
            assert (s2**3-54*d*d)==2*(a-b)**2*(b-c)**2*(c-a)**2
            cnt+=1
    print('PASS: exact moment identity, all positive coefficients, sharp L6 endpoint values')
    print('Assertions evaluated:',cnt)
    print('Degree six normalized moment: 5625/1001 + (54000/1001) u')
    print('Admissible u: [0,1/54]; lower=5625/1001 upper=6625/1001')
    print('The general theorem rests on the formal series and discriminant proof;')
    print('the bounded exact checks do not certify an infinite quantifier by enumeration.')


if __name__=='__main__':
    main()
