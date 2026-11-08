#!/usr/bin/env python3
"""Exact finite certificate for Boolean degree-two multiplicities and four-cube energies."""
from itertools import combinations, product
from math import comb
from fractions import Fraction


def walsh(values):
    a = list(values)
    step = 1
    while step < len(a):
        for p in range(0, len(a), 2 * step):
            for j in range(p, p + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return a


def table_class(m):
    """Truth-table enumeration of ALL 2^(2^m) sign functions, no sampling."""
    n = 1 << m
    result = {'balanced_deg2': {}, 'pure_deg2': {}}
    explicit = {'balanced_deg2': {}, 'pure_deg2': {}}
    for bits in range(1 << n):
        a = walsh([1 if (bits >> u) & 1 else -1 for u in range(n)])
        if any(a[S] for S in range(n) if S.bit_count() > 2):
            continue
        used = 0
        for S in range(1, n):
            if a[S]: used |= S
        if a[0] != 0: continue
        count = used.bit_count()
        result['balanced_deg2'][count] = result['balanced_deg2'].get(count, 0) + 1
        explicit['balanced_deg2'].setdefault(count, set()).add(bits)
        if not any(a[S] for S in range(n) if S.bit_count() == 1):
            result['pure_deg2'][count] = result['pure_deg2'].get(count, 0) + 1
            explicit['pure_deg2'].setdefault(count, set()).add(bits)
    return result, explicit


def encode(m, f):
    return sum((1 << u) for u in range(1 << m) if f(tuple(1 if (u >> i) & 1 else -1 for i in range(m))) == 1)


def construction_test():
    for m in (1, 2, 3, 4):
        counts, classes = table_class(m)
        expected = ({'balanced_deg2': {1: 2}, 'pure_deg2': {}} if m == 1 else
                    {'balanced_deg2': {1: 4, 2: 2}, 'pure_deg2': {2: 2}} if m == 2 else
                    {'balanced_deg2': {1: 6, 2: 6, 3: 24}, 'pure_deg2': {2: 6}} if m == 3 else
                    {'balanced_deg2': {1: 8, 2: 12, 3: 96, 4: 24},
                     'pure_deg2': {2: 12, 4: 24}})
        assert counts == expected, (m, counts, expected)
        print('local', m, counts)
    # All 24 essential-three-variable zero-mean degree-two functions are multiplexers.
    mux = set()
    for sel in range(3):
        j, k = [i for i in range(3) if i != sel]
        for a, b in ((j, k), (k, j)):
            for sa, sb in product((-1, 1), repeat=2):
                mux.add(encode(3, lambda x, sel=sel, a=a, b=b, sa=sa, sb=sb:
                               sa * x[a] if x[sel] == 1 else sb * x[b]))
    assert mux == table_class(3)[1]['balanced_deg2'][3]
    # All 24 essential-four-variable level-two functions use a signed K_{2,2}.
    quad = set()
    for first in combinations(range(4), 2):
        if 0 not in first: continue
        other = [i for i in range(4) if i not in first]
        a, b = first
        c, d = other
        for signs in product((-1, 1), repeat=4):
            if signs[0] * signs[1] * signs[2] * signs[3] != -1: continue
            quad.add(encode(4, lambda x, a=a, b=b, c=c, d=d, s=signs:
                            (s[0]*x[a]*x[c]+s[1]*x[a]*x[d]
                             +s[2]*x[b]*x[c]+s[3]*x[b]*x[d])//2))
    assert quad == table_class(4)[1]['pure_deg2'][4]
    print('constructive classifications: 24 three-variable muxes, 24 four-variable signed squares')


def spectral_min(d, j1, j2):
    vals = [j1 * (d - 2*k) + j2 * ((d - 2*k)**2 - d)//2
            for k in range(d + 1)]
    # Integer couplings above; exact division gives integers for Krawtchouk terms.
    m = min(vals)
    return (1 << (d-1)) * m, [k for k, v in enumerate(vals) if v == m]


def enumerate_q4():
    d, n = 4, 16
    adj = {1: [[] for _ in range(n)], 2: [[] for _ in range(n)]}
    for u in range(n):
        for v in range(u+1, n):
            dist=(u^v).bit_count()
            if dist in (1,2):
                adj[dist][u].append(v)
                adj[dist][v].append(u)
    tests = [((1,0), (-32,2)), ((3,1),(-48,10)),
             ((2,1),(-32,8)), ((1,1),(-16,140)), ((1,2),(-32,36))]
    for (a,b), target in tests:
        s=[1]*n
        energy=32*a+48*b
        low=energy
        ways=1
        prev=0
        for t in range(1,1<<n):
            gray=t^(t>>1)
            flip=gray^prev
            u=flip.bit_length()-1
            delta=-2*s[u]*(a*sum(s[v] for v in adj[1][u])+
                           b*sum(s[v] for v in adj[2][u]))
            energy+=delta
            s[u]=-s[u]
            if energy<low: low=energy; ways=1
            elif energy==low: ways+=1
            prev=gray
        assert (low,ways)==target, ((a,b),(low,ways),target)
        print('Q4', a, b, 'energy', low, 'degeneracy', ways)


def phase_tests():
    for d in range(4, 21):
        g1=Fraction(1,d-1);g2=Fraction(1,d-3)
        g3=Fraction(1,d-5) if d>5 else None
        for r, levels in [(g1/2,[d]),(g1,[d-1,d]),
                          ((g1+g2)/2,[d-1]),(g2,[d-2,d-1]),
                          ((g2+g3)/2 if g3 is not None else g2+1,[d-2])]:
            mult=__import__('math').lcm(r.denominator,1)
            value, ks=spectral_min(d,mult,r.numerator*(mult//r.denominator))
            assert ks==levels, (d, r, ks, levels)
    for d in range(4,20):
        a=2*d+2*comb(d,2)+24*comb(d,3)+24*comb(d,4)
        b=2*comb(d,2)+24*comb(d,4)
        assert a>b>=2
    print('all-dimensional spectral-phase samples: d=4..20 PASS')

if __name__=='__main__':
    construction_test()
    enumerate_q4()
    phase_tests()
    print('ALL CHECKS PASS')
