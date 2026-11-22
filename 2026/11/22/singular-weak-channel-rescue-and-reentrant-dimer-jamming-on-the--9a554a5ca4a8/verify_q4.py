"""Exact finite-state certificates for dimer adsorption on the four-cube.

Vertices are binary words 0..15. Edge clocks are independent exponential
clocks. Direction zero has rate r; directions 1,2,3 have rate one.
No third-party modules are needed.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache


def edges(d):
    return [((1 << u) | (1 << (u ^ (1 << j))), j)
            for u in range(1 << d) for j in range(d)
            if u < (u ^ (1 << j))]


def terminal_backward(d, rate=Q(1)):
    es = edges(d)
    @lru_cache(None)
    def f(mask):
        choices = [(e, rate if j == 0 else Q(1))
                   for e, j in es if not (mask & e)]
        if not choices:
            return {mask.bit_count() // 2: Q(1)}
        den = sum((w for _, w in choices), Q())
        out = defaultdict(Q)
        for e, w in choices:
            for k, p in f(mask | e).items():
                out[k] += w * p / den
        return dict(out)
    return f(0)


def terminal_forward(d, rate=Q(1)):
    es = edges(d)
    states = {0: Q(1)}
    result = defaultdict(Q)
    for _ in range((1 << d) // 2 + 1):
        nxt = defaultdict(Q)
        for mask, p in states.items():
            choices = [(e, rate if j == 0 else Q(1))
                       for e, j in es if not (mask & e)]
            if not choices:
                result[mask.bit_count() // 2] += p
                continue
            den = sum((w for _, w in choices), Q())
            for e, w in choices:
                nxt[mask | e] += p * w / den
        states = dict(nxt)
    assert not states
    return dict(result)


def series_backward(mode, order=2):
    """Taylor coefficients at r=0+ (low) or eps=1/r=0+ (high)."""
    es = edges(4)
    @lru_cache(None)
    def f(mask):
        fast = [e for e, j in es if not mask & e and
                (j != 0 if mode == 'low' else j == 0)]
        slow = [e for e, j in es if not mask & e and
                (j == 0 if mode == 'low' else j != 0)]
        a, b = len(fast), len(slow)
        if not a and not b:
            return (Q(mask.bit_count() == 16),) + (Q(),) * order
        if not a:
            z = [f(mask | e) for e in slow]
            return tuple(sum((v[k] for v in z), Q()) / b
                         for k in range(order + 1))
        fastv, slowv = [f(mask | e) for e in fast], [f(mask | e) for e in slow]
        result = []
        for k in range(order + 1):
            num = sum((v[k] for v in fastv), Q())
            if k:
                num += sum((v[k - 1] for v in slowv), Q()) - b * result[k - 1]
            result.append(num / a)
        return tuple(result)
    return f(0)


def series_forward(mode, order=2):
    """Independent propagation of formal edge-race probabilities."""
    es = edges(4)
    states = {0: (Q(1),) + (Q(),) * order}
    full = [Q() for _ in range(order + 1)]
    for _ in range(9):
        nxt = defaultdict(lambda: [Q() for _ in range(order + 1)])
        for mask, p in states.items():
            fast = [e for e, j in es if not mask & e and
                    (j != 0 if mode == 'low' else j == 0)]
            slow = [e for e, j in es if not mask & e and
                    (j == 0 if mode == 'low' else j != 0)]
            a, b = len(fast), len(slow)
            if not a and not b:
                if mask.bit_count() == 16:
                    for k in range(order + 1):
                        full[k] += p[k]
                continue
            if a == 0:
                for e in slow:
                    for k in range(order + 1):
                        nxt[mask | e][k] += p[k] / b
                continue
            inverse = [Q((-b)**k, a**(k+1)) for k in range(order + 1)]
            for e in fast:
                for k in range(order + 1):
                    nxt[mask | e][k] += sum(p[j] * inverse[k-j] for j in range(k+1))
            for e in slow:
                for k in range(1, order + 1):
                    nxt[mask | e][k] += sum(p[j] * inverse[k-1-j] for j in range(k))
        states = {k:tuple(v) for k,v in nxt.items()}
    assert not states
    return tuple(full)


def q3_uncovered_pairs():
    es = edges(3)
    @lru_cache(None)
    def f(mask):
        choices = [e for e,j in es if not mask & e]
        if not choices:
            return {mask:Q(1)}
        out = defaultdict(Q)
        for e in choices:
            for ending, p in f(mask | e).items():
                out[ending] += p / len(choices)
        return dict(out)
    states = f(0)
    bad = {s:p for s,p in states.items() if s.bit_count()==6}
    for mask, p in bad.items():
        vacant = [v for v in range(8) if not ((mask>>v)&1)]
        assert vacant[0] ^ vacant[1] == 7  # opposite binary corners
        assert p == Q(1,21)
    assert len(bad)==4
    return sum(bad.values(),Q())


def main():
    expect = {6:Q(1416949,56019600),
              7:Q(389239200251,735257250000),
              8:Q(6296549887,14139562500)}
    assert terminal_backward(4)==expect
    assert terminal_forward(4)==expect
    assert terminal_backward(4,Q(1,2))[8] == Q(570855820090139614856593,1201811705012081012850000)
    assert terminal_forward(4,Q(2))[8] == Q(12973948988785984681,26501736736290816000)
    assert q3_uncovered_pairs()==Q(4,21)
    assert terminal_forward(3)=={3:Q(4,21),4:Q(17,21)}
    low=(Q(293,441),-Q(225653011,290332350),Q(17759824852187387,13252394315160000))
    high=(Q(1),Q(0),Q(-36))
    assert series_backward('low')==low
    assert series_forward('low')==low
    assert series_backward('high')==high
    assert series_forward('high')==high
    assert Q(17,21)**2 == Q(289,441)
    assert low[0]-Q(289,441)==Q(4,441)
    assert terminal_forward(4,Q(1,2))[8]>expect[8]
    assert terminal_forward(4,Q(2))[8]>expect[8]
    print('PASS: independent forward and backward full distributions at r=1')
    print('PASS: exact r=1/2 and r=2 comparisons; interior minimum follows')
    print('PASS: Q3 antipodal-vacancy classification')
    print('PASS: both independent weak- and strong-rate Taylor certificates')
    print('All calculations use rational arithmetic.')

if __name__=='__main__':
    main()
