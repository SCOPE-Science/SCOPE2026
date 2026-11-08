#!/usr/bin/env python3
"""Independent finite instances of the parabolic Kakeya Fourier-energy theorem.

Uses ordinary integer arithmetic for additive energy, and numerical checks only
for the independently derived pointwise Fourier formula. The general-field
statement follows from the written Gauss-sum proof, not this finite test.
"""
import cmath
import math
from collections import Counter
from fractions import Fraction


class Field:
    def __init__(self, p, d=None):
        self.p = p
        self.d = d
        self.q = p if d is None else p * p

    def add(self, a, b):
        p = self.p
        if self.d is None:
            return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)

    def neg(self, a):
        return self.mul(a,self.p-1)

    def mul(self, a, b):
        p = self.p
        if self.d is None:
            return (a*b)%p
        aa,ab = a%p,a//p
        ba,bb = b%p,b//p
        return ((aa*ba-self.d*ab*bb)%p)+p*((aa*bb+ab*ba)%p)

    def inv(self, a):
        assert a
        for b in range(1,self.q):
            if self.mul(a,b)==1:
                return b
        raise AssertionError('field inverse missing')

    def char(self,a):
        p = self.p
        trace = a if self.d is None else (2*(a%p))%p
        return cmath.exp(2j*math.pi*trace/p)


def cases():
    for p in (3,5,7,11,13,17,19,23,29,31):
        yield Field(p)
    yield Field(3,1) # adjoining a root of t^2+1
    yield Field(5,2) # adjoining a root of t^2+2


def energy_formula(q,eta2):
    m=(q*q+2*q-1)//2
    if q%4==3:
        fourth_nonzero_v=Fraction((q-1)*q*(q*q-3)*(q+1)**2,16)
    else:
        fourth_nonzero_v=Fraction((q-1)*q*((q*q-3)*(q*q+6*q+1)+8*eta2*q*(q+1)),16)
    fourth_total=Fraction(m**4,1)+Fraction((q-1)**5,16)+fourth_nonzero_v
    return fourth_total/q**2


def check_field(F):
    q=F.q
    sq={F.mul(t,t) for t in range(q)}
    K={(x,F.add(F.mul(x,x),F.neg(s))) for x in range(q) for s in sq}
    K.update((0,y) for y in range(q))
    assert len(K)==(q*q+2*q-1)//2
    assert len(sq)==(q+1)//2
    # Tangent lines give every nonvertical direction.
    for t in range(q):
        for x in range(q):
            y=F.add(F.mul(F.add(t,t),x),F.neg(F.mul(t,t)))
            assert (x,y) in K
    for y in range(q):
        assert (0,y) in K
    count=Counter((F.add(x,a),F.add(y,b)) for x,y in K for a,b in K)
    E=sum(v*v for v in count.values())
    assert E==energy_formula(q,1 if 2 in sq else -1),(q,E)
    if q<=25:
        G=sum(F.char(F.mul(t,t)) for t in range(q))
        psi=F.char
        for u in range(q):
            for v in range(q):
                direct=sum(psi(F.neg(F.add(F.mul(u,x),F.mul(v,y)))) for x,y in K)
                if u==0 and v==0:
                    predicted=len(K)
                elif v==0:
                    predicted=(q-1)/2
                else:
                    eta_v=1 if v in sq else -1
                    negv=F.neg(v)
                    eta_negv=1 if negv in sq else -1
                    b=(1+eta_v*G)/2
                    inv4v=F.inv(F.mul(4%F.p,v))
                    phase=F.mul(F.mul(u,u),inv4v)
                    predicted=b*(eta_negv*G*psi(phase)-1)
                assert abs(predicted-direct)<2e-8,(q,u,v,direct,predicted)
    return len(K),E


def main():
    out=[]
    for f in cases():
        size,energy=check_field(f)
        out.append((f.q,size,energy))
    print('CHECK_OK independent_integer_energy_cases=12 independent_fourier_cases=5')
    print('q,cardinality,additive_energy:',out)


if __name__=='__main__':
    main()
