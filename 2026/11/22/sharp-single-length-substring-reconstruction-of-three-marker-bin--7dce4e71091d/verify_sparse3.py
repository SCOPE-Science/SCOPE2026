"""Independent finite checks of sharp single-length substring read reconstruction.

The symbolic argument in RESULT.md, not these finite checks, proves the general theorem.
"""
from collections import defaultdict, Counter
from itertools import combinations
from math import comb, ceil


def deck(bits, k):
    n = len(bits)
    return tuple(sorted(bits[i:i+k] for i in range(n-k+1)))


def marginals(bits, k):
    r = len(bits)-k+1
    return tuple(sum(bits[t:t+r]) for t in range(k))


def source(n, positions):
    bits = [0]*n
    for j in positions:
        bits[j] = 1
    return tuple(bits)


def threshold(n):
    r = (n+5)//4  # ceil((n+2)/4)
    return n-r+1, r


def witnesses(n):
    k, r = threshold(n)
    full, b = divmod(n, r)
    assert full in (2, 3)
    phases = list(range(b)) if full==2 else list(range(b, r))
    assert len(phases) >= 2
    ws = [tuple(int((j-a)%r == 0) for j in range(n)) for a in phases]
    assert all(sum(w) == 3 for w in ws)
    assert len(set(ws))==len(ws)
    assert len({deck(w, k) for w in ws})==1
    return len(ws)


def main():
    counts = Counter()
    for n in range(8, 27):
        kstar, rstar = threshold(n)
        by_k = {k: defaultdict(list) for k in range(kstar+1,n+1)}
        by_r = defaultdict(list)
        for pos in combinations(range(n), 3):
            w=source(n,pos)
            for k in by_k:
                by_k[k][deck(w,k)].append(pos)
            by_r[deck(w,kstar)].append(pos)
        for k,d in by_k.items():
            bad=[v for v in d.values() if len(v)>1]
            assert not bad,(n,k,bad[0])
            counts['fully_enumerated_unique_decks']+=1
        assert any(len(v)>1 for v in by_r.values()),n
        # stronger result: position marginals alone separate all three-one words
        for k in by_k:
            margin={}
            for pos in combinations(range(n),3):
                w=source(n,pos)
                m=marginals(w,k)
                assert m not in margin or margin[m]==pos,(n,k,pos,margin[m])
                margin[m]=pos
                counts['checked_marginal_instances']+=1
        counts['checked_sources']+=comb(n,3)
        counts['witness_phases']+=witnesses(n)
    for n in range(8,501):
        counts['witness_phases_large']+=witnesses(n)
    print('PASS: for every n=8..26, all larger-k complete decks and even their offset marginals are injective')
    print('PASS: for every n=8..500, explicit periodic witnesses attain the claimed largest ambiguous k')
    for k,v in sorted(counts.items()):
        print(f'{k}: {v}')

if __name__=='__main__':
    main()
