#!/usr/bin/env python3
"""Independent checks for the next-factor frequency formula (stdlib only)."""
from collections import Counter
from fractions import Fraction


def probability(n, s):
    assert n >= 2 and 0 <= s < (1 << (n+1))
    m = n-1
    e, f = s >> 1, s & ((1 << n)-1)
    if e == f:
        return Fraction(0)
    mask = (1 << m)-1
    u = s >> 2
    v = (s >> 1) & mask
    w = s & mask
    total = Fraction(1)
    for t in range(m):
        length = m-t
        low_mask = (1 << length)-1
        match = lambda x,y: (x & low_mask) == (y >> t)
        delta = int(match(v,u))-int(match(v,v))-int(match(w,u))+int(match(w,v))
        total += Fraction(delta,1 << (t+1))
    return total


def euler_wirings(n):
    m = n-1
    states = 1 << m
    arcs = 1 << n
    incoming = [[] for _ in range(states)]
    outgoing = [[] for _ in range(states)]
    for arc in range(arcs):
        outgoing[arc >> 1].append(arc)
        incoming[arc & (states-1)].append(arc)
    assert all(len(x)==2 for x in incoming + outgoing)
    motif_counts = [0] * (1 << (n+1))
    cycles = 0
    for wiring_mask in range(1 << states):
        successor = [0]*arcs
        for v in range(states):
            for j in (0,1):
                successor[incoming[v][j]] = outgoing[v][j^((wiring_mask>>v)&1)]
        seen = {0}
        x = successor[0]
        while x not in seen:
            seen.add(x)
            x = successor[x]
        if len(seen)!=arcs or x!=0:
            continue
        cycles += 1
        for e in range(arcs):
            f = successor[e]
            s = (e<<1) | (f&1)
            motif_counts[s] += 1
    return cycles,motif_counts


def run():
    print('Check A: independent Euler successor enumeration and exact formula')
    for n in range(2,6):
        cycles, counts = euler_wirings(n)
        expected_cycles = 1 << ((1 << (n-1))-n)
        assert cycles == expected_cycles, (n,cycles,expected_cycles)
        for s,count in enumerate(counts):
            assert Fraction(count,cycles) == probability(n,s), (n,s,count,cycles,probability(n,s))
        hist = Counter(Fraction(c,cycles) for c in counts)
        print('n',n,'cycles',cycles,'hist',dict(sorted(hist.items())))
    print('Check B: all motifs have valid rational probabilities, fixed total expectation and exact zero support')
    for n in range(2,12):
        probs = [probability(n,s) for s in range(1 << (n+1))]
        assert all(Fraction(0)<=p<=Fraction(1) and (1 << (n-1)) % p.denominator == 0 for p in probs)
        assert sum(probs) == 1 << n, (n,sum(probs))
        zeros = {s for s,p in enumerate(probs) if p==0}
        expected_zeros = {0, (1 << (n+1))-1, (1<<n)-2, (1 << n)+1} # 0 1^(n-1) 0 and 1 0^(n-1) 1
        assert zeros == expected_zeros,(n,zeros,expected_zeros)
        print('n',n,'motifs',len(probs),'sum',sum(probs),'zero_count',len(zeros))
    print('PASS all checks')


if __name__ == '__main__':
    run()
