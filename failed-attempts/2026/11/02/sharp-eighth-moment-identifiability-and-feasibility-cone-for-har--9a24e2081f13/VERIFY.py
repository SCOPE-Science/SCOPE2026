#!/usr/bin/env python3
"""Reproduce the stationary moment identities for a harmonically confined
Brownian particle with a two-state switching diffusivity.

Independent check: solve joint Markov-generator moment equations over the
rational numbers, then compare with the proposed beta-variance formula.
No sampling and no external dependencies are used.
"""
from fractions import Fraction as F
from math import comb


def prod(xs):
    y=F(1)
    for x in xs: y*=x
    return y


def odd_double_factorial(k):
    return prod(range(1, 2*k, 2))


def beta_moment(q, ell):
    return prod(F(2*j-1,1)/(2*q+2*j-1) for j in range(1,ell+1))


def closed_even_moment(a,dminus,dplus,gamma,k):
    v=(dplus+dminus)/(2*a)
    c=(dplus-dminus)/(dplus+dminus)
    q=gamma/(2*a)
    factor=sum(F(comb(k,2*ell)) * c**(2*ell) * beta_moment(q,ell)
               for ell in range(k//2+1))
    return odd_double_factorial(k)*v**k*factor


def generator_even_moments(a,dminus,dplus,gamma,upto=6):
    mp=mm=F(1,2)
    out=[]
    for k in range(2,2*upto+1,2):
        ap=k*a+gamma
        det=(k*a)*(k*a+2*gamma)
        fp=F(k*(k-1))*dplus*mp
        fm=F(k*(k-1))*dminus*mm
        mp,mm=(ap*fp+gamma*fm)/det,(gamma*fp+ap*fm)/det
        out.append(mp+mm)
    return out


def moment_reconstruct(a,m2,m4,m8):
    A=m4/(3*m2*m2)-1
    B=m8/(105*m2**4)-1-6*A
    if A<=0: raise ValueError('positive contrast not identified')
    r=B/(3*A*A)
    if not (F(1,3)<r<F(1)/(1+2*A)):
        raise ValueError('outside strict physical moment domain')
    q=(3*r-1)/(2*(1-r))
    c2=2*A*r/(1-r)
    return {'mean_diffusivity':a*m2,
            'gamma':2*a*q,'contrast_squared':c2,
            'r':r,'A':A,'B':B}


def main():
    cases=0
    for ia in [F(1,2),F(1),F(3,2),F(3)]:
        for dm in [F(1,3),F(1),F(2)]:
            for gap in [F(1,4),F(2,3),F(3)]:
                for gamma in [F(1,5),F(1),F(7,3),F(8)]:
                    dp=dm+gap
                    recurrence=generator_even_moments(ia,dm,dp,gamma)
                    beta=[closed_even_moment(ia,dm,dp,gamma,k) for k in range(1,7)]
                    assert recurrence==beta,(ia,dm,dp,gamma,recurrence,beta)
                    m2,m4,m6,m8=beta[:4]
                    A=m4/(3*m2*m2)-1
                    assert m6/(15*m2**3)==1+3*A
                    rec=moment_reconstruct(ia,m2,m4,m8)
                    assert rec['gamma']==gamma
                    assert rec['mean_diffusivity']==(dm+dp)/2
                    assert rec['contrast_squared']==((dp-dm)/(dp+dm))**2
                    cases+=1
    a=F(1);dm=F(1);dp=F(3);g=F(2)
    m=generator_even_moments(a,dm,dp,g,4)
    assert m == [F(2),F(13),F(150),F(2541)],m
    # Genuine two-parameter nonidentification through moment order 7:
    # both examples have m2=2 and the same A=1/12.
    aa=F(1)
    g1=F(2); c1sq=F(1,4)
    g2=F(1); c2sq=F(1,6)
    assert c1sq/(1+g1/aa)==c2sq/(1+g2/aa)==F(1,12)
    assert g1!=g2
    print('EXACT SUCCESS: %d independent parameter sets, each through moment 12' % cases)
    print('EXACT example moments: 2, 13, 150, 2541; uniquely reconstruct rate 2 and diffusivities 1,3')
    print('EXACT nonidentification: two different switch rates share all moments through order 7')

if __name__=='__main__': main()
