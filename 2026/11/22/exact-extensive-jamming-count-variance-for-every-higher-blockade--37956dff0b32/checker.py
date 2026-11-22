#!/usr/bin/env python3
"""Reproduce the finite first-split laws and the blockade-two variance slope."""
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache


def convolution(u, v):
    out = defaultdict(Fraction)
    for a, p in u.items():
        for b, q in v.items():
            out[a + b + 1] += p * q
    return dict(out)


def split_laws(b, nmax):
    a = [{0: Fraction(1)}]
    c = [{1: Fraction(1)}]
    empty = {0: Fraction(1)}
    def get(shape, k):
        return empty if k < 0 else (a if shape == 'A' else c)[k]
    for k in range(1, nmax + 1):
        outcomes_a = []
        outcomes_b = []
        for j in range(k):
            outcomes_a.append(convolution(get('A', j-b), get('B', k-j-b)))
        for j in range(1, k+1):
            outcomes_a.append(convolution(get('B', j-b), get('A', k-j-b)))
        for j in range(k+1):
            outcomes_b.append(convolution(get('A', j-b), get('A', k-j-b)))
        for j in range(1, k):
            outcomes_b.append(convolution(get('B', j-b), get('B', k-j-b)))
        for dest, outcomes in [(a, outcomes_a), (c, outcomes_b)]:
            total = defaultdict(Fraction)
            assert len(outcomes) == 2*k
            for law in outcomes:
                for count, probability in law.items():
                    total[count] += probability / (2*k)
            assert sum(total.values()) == 1
            dest.append(dict(total))
    return a, c


def direct_law(shape, b, k):
    if shape == 'A':
        pos = [(0, x) for x in range(k)] + [(1, x) for x in range(1, k + 1)]
    else:
        pos = [(0, x) for x in range(1, k)] + [(1, x) for x in range(k + 1)]
    masks = []
    for r, x in pos:
        masks.append(sum(1 << j for j, (s, y) in enumerate(pos)
                         if abs(x-y) + (r != s) <= b))
    @lru_cache(None)
    def recurse(occupied):
        admissible = [j for j in range(len(pos)) if not (occupied & masks[j])]
        if not admissible:
            return {occupied.bit_count(): Fraction(1)}
        total = defaultdict(Fraction)
        for j in admissible:
            for count, probability in recurse(occupied | (1 << j)).items():
                total[count] += probability / len(admissible)
        return dict(total)
    return recurse(0)


def expectation(law, power=1):
    return sum(Fraction(n**power)*p for n,p in law.items())


def high_precision_slope(b=2, length=130):
    with localcontext() as dc:
        dc.prec = 48
        a = [Decimal(0)]*(length+1)
        c = [Decimal(0)]*(length+1)
        va = [Decimal(0)]*(length+1)
        vc = [Decimal(0)]*(length+1)
        c[0] = Decimal(1)
        for k in range(1, length+1):
            moments = []
            for shape in ['A', 'B']:
                pairs = ([('A', j-b, 'B', k-j-b) for j in range(k)] +
                         [('B', j-b, 'A', k-j-b) for j in range(1,k+1)]) if shape=='A' else (
                         [('A', j-b, 'A', k-j-b) for j in range(k+1)] +
                         [('B', j-b, 'B', k-j-b) for j in range(1,k)])
                s=Decimal(0);q=Decimal(0);h=Decimal(0)
                for sh1,i,sh2,j in pairs:
                    x=(a if sh1=='A' else c)[i] if i>=0 else Decimal(0)
                    y=(a if sh2=='A' else c)[j] if j>=0 else Decimal(0)
                    vx=(va if sh1=='A' else vc)[i] if i>=0 else Decimal(0)
                    vy=(va if sh2=='A' else vc)[j] if j>=0 else Decimal(0)
                    s += x+y; q += (x+y)*(x+y); h += vx+vy
                mean = Decimal(1)+s/(2*k)
                var = (h+q)/(2*k)-(s/(2*k))**2
                moments.append((mean,var))
            a[k], va[k] = moments[0]
            c[k], vc[k] = moments[1]
        v=lambda k:(va[k]+vc[k])/2
        return v(length)-v(length-1), v(length)//1


def main():
    tests = 0
    for b in [1,2,3]:
        a,c=split_laws(b,9)
        for k in range(1,6):
            assert a[k]==direct_law('A',b,k)
            assert c[k]==direct_law('B',b,k)
            tests += 2
        if b>=2:
            meanA=expectation(a[b]); secondA=expectation(a[b],2)
            varA=secondA-meanA**2
            assert varA == Fraction(b-1,b*b)
            assert expectation(c[b],2)-expectation(c[b])**2==0
            tests += 2
    val,_=high_precision_slope()
    reference=Decimal('0.0267945787085631864907625185535')
    assert abs(val-reference)<Decimal('0.000000000000000000000001')
    tests+=1
    print('PASS',tests,'exact-law / positivity / high-precision assertions')
    print('b=2 variance coefficient estimate:',val)

if __name__=='__main__':
    main()
