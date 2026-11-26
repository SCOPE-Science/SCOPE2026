#!/usr/bin/env python3
"""Independent finite checks for reconstruction from directed adjacent-pair counts."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations
from math import comb, factorial


def profile(w):
    return tuple(sorted(Counter(zip(w, w[1:])).items()))


def profile_counter(w):
    return Counter(zip(w, w[1:]))


def decode(P):
    """Decode a valid profile of a noncrossing double-occurrence word."""
    D = Counter(dict(P))
    if not D:
        return ()
    options = [a for a,b in D if a==b and D[a,b]>0]
    if not options:
        raise ValueError('no adjacent repeated symbol')
    a = min(options)
    prev = [x for (x,y), c in D.items() if y==a and x!=a for _ in range(c)]
    nxt = [y for (x,y), c in D.items() if x==a and y!=a for _ in range(c)]
    assert len(prev)<=1 and len(nxt)<=1 and D[a,a]==1
    p = prev[0] if prev else None
    q = nxt[0] if nxt else None
    D[a,a] -= 1
    if p is not None:
        D[p,a] -= 1
    if q is not None:
        D[a,q] -= 1
    if p is not None and q is not None:
        D[p,q] += 1
    D += Counter()
    reduced = decode(tuple(sorted(D.items())))
    if p is None and q is None:
        assert not reduced
        return (a,a)
    if p is None:
        assert reduced[0] == q
        return (a,a) + reduced
    if q is None:
        assert reduced[-1] == p
        return reduced + (a,a)
    matches = [i for i in range(len(reduced)-1) if reduced[i:i+2]==(p,q)]
    assert len(matches)==1, (p,q,reduced)
    i = matches[0]
    return reduced[:i+1] + (a,a) + reduced[i+1:]


@lru_cache(None)
def dyck(n):
    if n==0:
        return ('',)
    return tuple('('+a+')'+b for k in range(n)
                 for a in dyck(k) for b in dyck(n-k-1))


def labeled_noncrossing(shape, labels):
    stack = []
    w = []
    j = 0
    for s in shape:
        if s=='(':
            stack.append(labels[j]);w.append(labels[j]);j+=1
        else:
            w.append(stack.pop())
    return tuple(w)


def noncrossing(w):
    positions = defaultdict(list)
    for i,x in enumerate(w):
        positions[x].append(i)
    for a, ia in positions.items():
        for b, ib in positions.items():
            if a!=b and ia[0]<ib[0]<ia[1]<ib[1]:
                return False
    return True


def catalan(n):
    return comb(2*n,n)//(n+1)


def main():
    for n in range(1,7):
        seen = set()
        count = 0
        for sh in dyck(n):
            for labels in permutations(range(1,n+1)):
                w = labeled_noncrossing(sh,labels)
                assert noncrossing(w)
                p = profile(w)
                assert p not in seen
                seen.add(p)
                assert decode(p)==w
                assert len(set(zip(w,w[1:])))==len(w)-1
                count += 1
        expected = factorial(n)*catalan(n)
        assert count==expected and len(seen)==expected
        print(f'NC n={n}: {count} labeled words, unique profiles, decoder and no repeated bigrams PASS')
    for n in range(1,6):
        perms = set(permutations(tuple(x for x in range(1,n+1) for _ in (0,1))))
        fibers = defaultdict(lambda: [0,0,()])
        for w in perms:
            p = profile(w)
            fibers[p][0] += 1
            if noncrossing(w):
                fibers[p][1] += 1
                fibers[p][2] = w
        for total, nc, w in fibers.values():
            if nc:
                assert nc==1 and total==1, (n,total,nc,w)
        collisions = sum(v[0]>1 for v in fibers.values())
        if n <= 2: assert collisions==0
        if n == 3: assert collisions>0
        print(f'ALL n={n}: {len(perms)} double-occurrence words, {len(fibers)} profiles, {collisions} ambiguous profiles; every noncrossing source globally singleton PASS')
    A=(3,1,1,2,3,2);B=(3,2,3,1,1,2)
    assert profile(A)==profile(B) and A!=B and not noncrossing(A) and not noncrossing(B)
    print('Explicit first crossing collision at n=3 PASS')

if __name__=='__main__':
    main()
