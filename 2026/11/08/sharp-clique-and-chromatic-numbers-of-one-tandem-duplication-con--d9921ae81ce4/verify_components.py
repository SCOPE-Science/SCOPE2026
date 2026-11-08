#!/usr/bin/env python3
"""Finite checks of zero-run composition graphs, distinct from output-ball enumeration."""
from itertools import product

def compositions(total, d):
    if d == 1:
        yield (total,)
        return
    for a in range(total+1):
        for r in compositions(total-a,d-1):
            yield (a,)+r

def edge(a,b):
    v=[x-y for x,y in zip(a,b)]
    return v.count(1)==1 and v.count(-1)==1 and v.count(0)==len(v)-2

def verify_components():
    cases=0
    for d in range(1,9):
        for B in range(0,9):
            vs=list(compositions(B,d))
            K=d if B else 1
            colors={v:sum(i*a for i,a in enumerate(v))%d for v in vs}
            for j,a in enumerate(vs):
                for b in vs[j+1:]:
                    if edge(a,b):assert colors[a]!=colors[b]
            if B>0:
                clique=[tuple(B if i==j else 0 for i in range(d)) for j in range(d)]
                if B==1:assert all(edge(a,b) for i,a in enumerate(clique) for b in clique[i+1:])
                # For B>1, a size-d clique holds around a fixed B-1 base vector.
                clique=[tuple((B-1 if i==0 else 0)+(1 if i==j else 0) for i in range(d)) for j in range(d)]
                assert all(edge(a,b) for i,a in enumerate(clique) for b in clique[i+1:])
            assert len(set(colors.values()))==K
            cases+=1
    print('VERIFY_COMPOSITION_OK',cases)

if __name__=='__main__': verify_components()
