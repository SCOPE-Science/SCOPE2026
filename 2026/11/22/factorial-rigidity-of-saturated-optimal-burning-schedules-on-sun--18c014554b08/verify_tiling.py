"""Check the explicit saturated sunlet burning classification using cyclic blocks.
No external dependencies; Python >=3.9.
"""
from itertools import permutations
from math import factorial

def distance(a, b, n):
    if a == b:
        return 0
    cyclic = min((a % n - b % n) % n, (b % n - a % n) % n)
    return cyclic + int(a >= n) + int(b >= n)

def sequence_fires_all(seq, n):
    k = len(seq)
    valid_order = all(distance(seq[j], seq[t], n) > t-j
                      for t in range(k) for j in range(t))
    coverage = all(any(distance(seq[t], v, n) <= k-t-1
                       for t in range(k)) for v in range(2*n))
    return valid_order and coverage

def tilings(k):
    n = (k-1)**2+1
    sizes = [2*(k-t-1)-1 if t<k-1 else 1 for t in range(k)]
    assert sum(sizes)==n
    for order in permutations(range(1,k)):
        starts={0:0}
        cur=sizes[0]
        for t in order:
            starts[t]=cur
            cur+=sizes[t]
        for shift in range(n):
            base=[(shift+starts[t]+sizes[t]//2)%n for t in range(k)]
            for penultimate_leaf in (False,True):
                seq=base[:]
                if penultimate_leaf: seq[-2]+=n
                seq[-1]+=n
                yield tuple(seq)

for k in range(3,8):
    n=(k-1)**2+1
    histories=set(tilings(k))
    target=2*n*factorial(k-1)
    assert len(histories)==target,(k,len(histories),target)
    assert all(sequence_fires_all(seq,n) for seq in histories)
    print('n=',n,'k=',k,'histories=',len(histories),'exact=',target)
print('tiling construction and strict-burning checks passed')
for k in range(3,6):
    n=(k-1)**2+1
    histories=set(tilings(k))
    edge_pairs=set()
    for seq in histories:
        neighbors=[]
        for t in range(k):
            for candidate in range(2*n):
                if candidate==seq[t]:continue
                seq2=seq[:t]+(candidate,)+seq[t+1:]
                if seq2 in histories:
                    neighbors.append(seq2)
        assert len(neighbors)==1,(k,seq,neighbors)
        other=neighbors[0]
        assert other[k-2]==(seq[k-2]+n)%(2*n)
        edge_pairs.add(frozenset((seq,other)))
    assert len(edge_pairs)==n*factorial(k-1)
    print('n=',n,'single-ignition-exchange-edges=',len(edge_pairs),'isolated-K2-components=',len(edge_pairs))
