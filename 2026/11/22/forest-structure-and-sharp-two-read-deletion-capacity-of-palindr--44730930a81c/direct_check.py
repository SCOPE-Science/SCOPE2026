"""Independent exhaustive deletion-deck graph, component and optimum verification."""
from itertools import product, combinations
from collections import Counter, defaultdict

def experiment(q,m):
    n=2*m+1
    halves=list(product(range(q),repeat=m+1))
    def palindrome(h):return h + h[-2::-1]
    words={h:palindrome(h) for h in halves}
    def deck(w):return {w[:i]+w[i+1:] for i in range(len(w))}
    decks={h:deck(w) for h,w in words.items()}
    edges={frozenset((x,y)) for x,y in combinations(halves,2) if len(decks[x]&decks[y])>=2}
    predicted=set()
    for h in halves:
        for k in range(1,m+1):
            block=h[-k-1:]
            if all(block[i]!=block[i+1] for i in range(k)) and all(block[i]==block[i+2] for i in range(k-1)):
                a,b=block[-2:]
                other=h[:-k-1]+tuple(b if x==a else a for x in block)
                predicted.add(frozenset((h,other)))
    assert edges==predicted,(q,m,len(edges),len(predicted),list(edges^predicted)[:2])
    parent={x:x for x in halves}
    def root(x):
        while x!=parent[x]:x=parent[x]
        return x
    for pair in edges:
        x,y=tuple(pair); a,b=root(x),root(y)
        assert a!=b,(q,m,'cycle')
        parent[a]=b
    comps=defaultdict(set)
    for x in halves:comps[root(x)].add(x)
    counts=Counter(len(v) for v in comps.values())
    expected=Counter({1:q**m})
    for r in range(1,m):expected[2**r]+=(q*(q-1)//2)*(q-2)*q**(m-r-1)
    expected[2**m]+=q*(q-1)//2
    assert counts==expected,(q,m,counts,expected)
    assert len(edges)==q*(q**m-1)//2,(q,m,len(edges))
    # All nontrivial components have perfect matchings via the central triple flip.
    middle_pairs=set()
    for x in halves:
        if x[-2]!=x[-1]:
            y=x[:-2]+(x[-1],x[-2])
            middle_pairs.add(frozenset((x,y)))
    assert middle_pairs<=edges
    assert len(middle_pairs)==q**m*(q-1)//2
    for component in comps.values():
        if len(component)>1:
            assert sum(pair<=component for pair in middle_pairs)==len(component)//2
    return q,m,len(halves),len(edges),dict(sorted(counts.items())),q**m*(q+1)//2

if __name__=='__main__':
    cases=[(2,m) for m in range(1,8)]+[(3,m) for m in range(1,5)]+[(4,m) for m in range(1,4)]+[(5,m) for m in range(1,3)]
    for c in cases:print(experiment(*c))
    for q in (2,3,4):
        for m in range(1,5):
            n=2*m
            halves=list(product(range(q),repeat=m))
            words=[h+h[::-1] for h in halves]
            decks=[{w[:i]+w[i+1:] for i in range(n)} for w in words]
            assert all(len(a&b)<2 for a,b in combinations(decks,2))
    print('PASS: direct deck comparisons, all cases')
