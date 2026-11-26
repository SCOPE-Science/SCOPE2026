"""Exact labelled extinction histograms by first-step grouping."""
from collections import Counter
from itertools import combinations
from sys import argv


def subsets(mask):
    x = mask
    while True:
        yield x
        if not x:
            break
        x = (x-1) & mask


def run(n):
    if n not in (5, 6):
        raise ValueError('the census covers n=5 and n=6')
    pairs = list(combinations(range(n), 2))
    m = len(pairs)
    full = (1 << m)-1
    stars = [sum(1 << i for i,e in enumerate(pairs) if u in e) for u in range(n)]
    eligible = []
    for x in range(full+1):
        deg = [(x & star).bit_count() for star in stars]
        eligible.append(sum(1 << i for i,(u,v) in enumerate(pairs)
                            if not (x >> i) & 1 and deg[u] + deg[v] >= n-2))

    def step(x,y):
        return eligible[x] & ~y, x

    weights = [0]*(full+1)
    powers = [3**i for i in range(m)]
    for x in range(1,full+1):
        bit = x & -x
        weights[x] = weights[x ^ bit] + powers[bit.bit_length()-1]
    hist, witness, groups = Counter({0: 1, 1: -1}), None, 0
    for x in range(full+1):
        e = eligible[x]
        multiplicity = 1 << (m-x.bit_count()-e.bit_count())
        for z in subsets(e):
            groups += 1
            # For precisely this successor, y includes e\z and excludes z;
            # bits outside x|e are free. Start from the already grouped successor.
            a,b,t = z,x,1
            while a or b:
                if t >= 4:
                    raise RuntimeError(('state did not reach rest within four',n,x,z))
                a,b = step(a,b)
                t += 1
            hist[t] += multiplicity
            if t == 4:
                code = weights[x]+2*weights[e ^ z]
                witness = code if witness is None else min(code,witness)
    result = tuple(hist[t] for t in range(5))
    expected = {5: ((1,1023,24548,29797,3680), 94),
                6: ((1,32767,5733037,8327727,255375), 3199)}
    if sum(result) != 3**m or (result,witness) != expected[n]:
        raise RuntimeError((n,result,witness))
    print(n, sum(result), groups, result, witness)


if __name__ == '__main__':
    for arg in argv[1:] or ('5','6'):
        run(int(arg))
