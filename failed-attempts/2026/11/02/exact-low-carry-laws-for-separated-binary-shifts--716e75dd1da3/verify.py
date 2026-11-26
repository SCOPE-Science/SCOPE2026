"""Exact finite-state check of the low-carry law for sparse shifts.

Finite checks support, but do not replace, the general proof.
"""
from fractions import Fraction
from math import comb
from itertools import combinations


def carry_distribution_bounded(t, cap):
    # Bernoulli(1/2) independent low bits; all state values exact rationals.
    states = {(0, 0): Fraction(1)}
    for pos in range(t.bit_length()):
        delta = (t >> pos) & 1
        nxt = {}
        for (carry, count), mass in states.items():
            for bit in (0, 1):
                newcarry = (bit + delta + carry) // 2
                nc = count + newcarry
                if nc <= cap:
                    key = (newcarry, nc)
                    nxt[key] = nxt.get(key, Fraction(0)) + mass / 2
        states = nxt
    probs = [Fraction(0) for _ in range(cap + 1)]
    for (carry, count), mass in states.items():
        if carry == 0:
            probs[count] += mass
        else:
            # Beyond the top bit of t, additional carries are geometric:
            # P(number of further carries equals k) = 2^(-k-1).
            for extra in range(cap - count + 1):
                probs[count + extra] += mass * Fraction(1, 2 ** (extra + 1))
    return probs


def check():
    checked = 0
    for h in range(1, 8):
        reference = [Fraction(comb(h+j-1, j), 2 ** (h+j)) for j in range(h+1)]
        # Gaps at the threshold and beyond, including nonuniform positions.
        gap_patterns = [[h+1]*(h-1), [h+2]*(h-1), [h+1+j%3 for j in range(h-1)], [2*h+3]*(h-1)]
        for gaps in gap_patterns:
            places = [0]
            for g in gaps: places.append(places[-1]+g)
            t = sum(1 << p for p in places)
            probs = carry_distribution_bounded(t, h)
            assert probs == reference, (h, gaps, probs, reference)
            total = sum(probs)
            claimed = Fraction(1,2)+Fraction(comb(2*h,h),2*4**h)
            assert total == claimed
            checked += 1
    # Sharpness in the first nontrivial case: a gap of only h is inadequate.
    assert sum(carry_distribution_bounded(5,2)) == Fraction(5,8)
    assert sum(carry_distribution_bounded(9,2)) == Fraction(11,16)
    # Direct exact dyadic-frequency calculation, not stochastic sampling.
    for t in (1,3,5,9,17,73,273):
        h=t.bit_count()
        precision=t.bit_length()+h+2
        if precision>18: continue
        size=1<<precision
        counts=[0]*(h+1)
        for n in range(size):
            carry_count=h+n.bit_count()-(n+t).bit_count()
            if carry_count<=h: counts[carry_count]+=1
        # For <=h events the first precision bits decide all outcomes:
        # a carry after precision would itself push total above h.
        values=[Fraction(x,size) for x in counts]
        assert values==carry_distribution_bounded(t,h),(t,values)
    print('VERIFY_OK', 'families',checked, 'low-carry profiles',sum(4*(h+1) for h in range(1,8)))

if __name__=='__main__': check()
