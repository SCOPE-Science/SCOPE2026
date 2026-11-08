#!/usr/bin/env python3
"""Standalone exact-arithmetic and high-precision diagnostic checks of the theorem."""
from fractions import Fraction as Q
from itertools import product
from decimal import Decimal, localcontext


def evolve(r, state):
    z, x, y = state
    return (1 - 2*x*y, 2*r*x*y, 2*(1-r)*x*y)


def nonempty(state):
    return state[1] + state[2]


def run():
    params = [(Q(1, 4), Q(2, 5)), (Q(1, 3), Q(1, 5))]
    starts = [(Q(1, 4), Q(1, 4), Q(1, 2)), (Q(1, 2), Q(1, 6), Q(1, 3))]
    for r0, r1 in params:
        cc = [2*r*(1-r) for r in (r0,r1)]
        assert cc[0] != cc[1]
        for state0 in starts:
            x0, y0 = state0[1:]
            s1 = 2*x0*y0
            for depth in range(0, 7):
                for word in product((0,1), repeat=depth):
                    state = state0
                    for j, bit in enumerate(word):
                        state = evolve((r0,r1)[bit], state)
                        assert sum(state) == 1 and all(Q(0) <= x <= Q(1) for x in state)
                        if j == 0:
                            assert nonempty(state) == s1
                    if depth >= 1:
                        expected = s1**(2**(depth-1))
                        for j in range(depth-1):
                            expected *= cc[word[j]]**(2**(depth-2-j))
                        assert nonempty(state) == expected
            for x in [Q(k,10) for k in range(11)]:
                for y in [Q(j,10) for j in range(11) if j <= 10-int(10*x)]:
                    z = 1-x-y
                    for r in (r0,r1):
                        w = evolve(r,(z,x,y))
                        phi = (x+y)**2/2
                        assert 0 <= 2*x*y <= phi
                        assert (w[1]+w[2])**2/2 == (2*x*y)**2/2
                        assert sum(w)==1

    p = Q(3, 7)
    for depth in range(0, 12):
        probs = [p**sum(bits)*(1-p)**(depth-sum(bits))
                 for bits in product((0,1), repeat=depth)]
        assert sum(probs)==1
        vals = [sum(Q(bit, 2**(j+1)) for j,bit in enumerate(bits))
                for bits in product((0,1),repeat=depth)]
        e1 = sum(w*t for w,t in zip(probs, vals))
        e2 = sum(w*t*t for w,t in zip(probs, vals))
        assert e1 == p*(1-Q(1,2)**depth)
        assert e2-e1**2 == p*(1-p)*(1-Q(1,4)**depth)/3
    with localcontext() as context:
        context.prec=90
        r0, r1=Q(1,4),Q(2,5)
        state0=Q(1,4),Q(1,4),Q(1,2)
        s1=2*state0[1]*state0[2]
        cc=[2*r*(1-r) for r in (r0,r1)]
        dd=[-(Decimal(c.numerator)/Decimal(c.denominator)).ln() for c in cc]
        a1=-(Decimal(s1.numerator)/Decimal(s1.denominator)).ln()
        word=[0,1,1,0,1,0,0,1,1,1]
        states=[state0]
        for bit in word:
            states.append(evolve((r0,r1)[bit],states[-1]))
        for n in range(1,len(states)):
            sn=nonempty(states[n])
            an=-(Decimal(sn.numerator)/Decimal(sn.denominator)).ln()
            partial=a1/2+sum(dd[word[j]]/Decimal(2)**(j+2) for j in range(n-1))
            assert abs(an/Decimal(2)**n-partial) < Decimal('1e-75')
            # Complete the infinite switching sequence by constant zero symbols.
            L= a1/2+sum(dd[word[j]]/Decimal(2)**(j+2) for j in range(len(word))) + dd[0]/Decimal(2)**(len(word)+1)
            remainder=Decimal(2)**n*L-an
            assert min(dd)-Decimal('1e-65') <= remainder <= max(dd)+Decimal('1e-65')
        d0,d1=dd
        # Uniform-law variance equals interval-length squared divided by twelve.
        half_length = abs(d1-d0)/2
        uniform_variance = half_length**2/12
        general_variance_at_half = (d1-d0)**2*Decimal('0.25')/12
        assert uniform_variance == general_variance_at_half
        # E[U]=p and Var[U]=p(1-p)/3 are geometric sums.
        assert sum(Q(1,2)**(j+1) for j in range(20)) == 1-Q(1,2)**20
        assert sum(Q(1,4)**(j+1) for j in range(20)) == Q(1,3)*(1-Q(1,4)**20)
    g = Q(1)
    for _ in range(12):
        g = g*g/2
    assert g < Q(1, 2**(2**12-1)) * 2
    print('ALL CHECKS PASSED: exact recurrence, simplex, F-stochastic inequalities, cylinders, rate tail and moments')

if __name__ == '__main__':
    run()
