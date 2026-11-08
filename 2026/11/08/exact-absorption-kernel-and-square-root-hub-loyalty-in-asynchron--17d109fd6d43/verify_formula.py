"""Independent multinomial evaluation of the full-family majority flip law.

Run: python verify_formula.py
"""
from fractions import Fraction
from math import comb, pi, sqrt


def weighted_hub_flip_probability(k):
    total = Fraction(0)
    for num_opposing in range(k+1):
        for num_supporting in range(k+1-num_opposing):
            j = k-num_opposing-num_supporting
            d = num_opposing-num_supporting
            if d > 0:
                multiplicity = comb(k,num_opposing)*comb(k-num_opposing,num_supporting)*2**j
                total += multiplicity*Fraction(min(d,j+1),j+1)
    return total /4**k


def independent_consensus_formula(k):
    p = Fraction(3**k,4**k)
    p += sum((Fraction(comb(k,j)*2**j, 4**k*(j+1)) for j in range(k)),Fraction(0))
    return p

for k in (1, 2, 3, 4, 5, 6, 8, 12, 20, 40, 80, 160):
    p = weighted_hub_flip_probability(k)
    consensus = independent_consensus_formula(k)
    consensus_closed = Fraction(3**k,4**k) + Fraction(3**(k+1)-1-2**(k+1),2*(k+1)*4**k)
    assert consensus == consensus_closed
    assert 0 < p < 1 and 0 < consensus <= 1
    print(f'k={k}: hub-flip={p}; consensus={consensus}; sqrt(pi*k)*hub-flip={sqrt(pi*k)*float(p):.8f}')
print('PASS: independent multinomial and consensus identity calculations')
