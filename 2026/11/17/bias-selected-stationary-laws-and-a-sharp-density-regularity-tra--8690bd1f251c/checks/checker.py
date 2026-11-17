#!/usr/bin/env python3
"""Finite exact checks for the biased binary forward/inverse-branch map.

These diagnostics test finite cylinder identities, not the infinite proofs.
"""
from fractions import Fraction as F
from itertools import product


def letters(n):
    return list(product((0, 1), repeat=n))


def bernoulli(word, alpha):
    return F(1) if not word else (alpha**sum(word)) * ((1-alpha)**(len(word)-sum(word)))


def geometric_prefix_cylinder(word, rho, alpha):
    # Exactly integrates the full geometric mixture on a length-l cylinder.
    l=len(word)
    out=F(0)
    for k in range(l):
        out += (1-rho)*rho**k * bernoulli(word[:k],alpha) * F(1,2)**(l-k)
    out+=rho**l*bernoulli(word,alpha)
    return out


def shift_push_cylinder(word, law):
    return sum(law((i,)+word) for i in (0,1))


def prepend_push_cylinder(word, alpha, law):
    if not word:
        return F(1)
    return (alpha if word[0] else 1-alpha)*law(word[1:])


def stationary_cylinders(p,alpha,max_length=8):
    rho=(1-p)/p
    m=lambda w:geometric_prefix_cylinder(w,rho,alpha)
    for l in range(max_length+1):
        assert sum(m(w) for w in letters(l))==1, ('norm',l)
        for w in letters(l):
            lhs=m(w)
            rhs=p*shift_push_cylinder(w,m)+(1-p)*prepend_push_cylinder(w,alpha,m)
            assert lhs==rhs, ('stationarity',l,w,lhs,rhs)
    return sum(2**l for l in range(max_length+1))


def moment_phase(p,alpha,s):
    rho=(1-p)/p
    u=2*rho*(1-alpha)
    v=2*rho*alpha
    return (u**s+v**s)/2


def main():
    tests=[(F(3,5),F(4,5)),(F(11,20),F(4,5)),(F(8,13),F(4,5)),(F(7,10),F(4,5)),(F(7,10),F(1,2)),(F(51,100),F(3,5))]
    total=0
    for p,alpha in tests:
        n=stationary_cylinders(p,alpha)
        total+=n
        rho=(1-p)/p
        assert geometric_prefix_cylinder((1,),rho,alpha)==(1-rho)*F(1,2)+rho*alpha
        assert moment_phase(p,alpha,1)==rho
        print('p=',p,'alpha=',alpha,'rho=',rho,'max multiplier=',2*rho*max(alpha,1-alpha),'L2-multiplier=',moment_phase(p,alpha,2),'cylinder checks=',n)
    p=F(8,13); alpha=F(4,5)
    assert 2*(1-p)/p*alpha==1
    assert moment_phase(p,alpha,24)<1
    assert moment_phase(F(11,20),alpha,3)>1
    print('PASS; exact stationary cylinder checks:',total,'+ normalization, first-digit, moment and boundary identities')

if __name__=='__main__':
    main()
