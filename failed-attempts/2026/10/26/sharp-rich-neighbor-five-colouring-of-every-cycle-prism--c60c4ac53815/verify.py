#!/usr/bin/env python3
"""Independent, standalone verification of edge-colour certificates for cycle prisms.

Colour values 0..4. Each column lists (top horizontal, bottom horizontal, rung).
For a cyclic prism, horizontal edges extend from column i to i+1.
"""
from itertools import product

BASE = {
 3: [(1,4,3),(3,1,2),(4,2,0)],
 4: [(0,3,4),(4,2,1),(2,4,0),(1,0,3)],
 5: [(2,0,4),(4,3,1),(3,4,2),(2,0,1),(0,2,4)],
 6: [(2,0,4),(4,3,1),(3,4,2),(2,0,1),(3,1,4),(1,2,0)],
 7: [(2,0,4),(4,3,1),(3,4,2),(2,0,1),(0,4,1),(1,2,3),(3,1,0)],
 8: [(2,0,4),(4,3,1),(3,4,2),(2,0,1),(4,2,3),(0,4,1),(3,1,2),(1,3,2)],
 9: [(2,0,4),(4,3,1),(3,4,2),(2,0,1),(0,4,1),(1,3,2),(2,0,4),(0,4,3),(3,2,1)]
}

def verify(cols, verbose=False):
    n=len(cols)
    assert n>=3 and all(len(t)==3 and all(isinstance(c,int) and 0<=c<=4 for c in t) for t in cols)
    E=[]; colors=[]
    for i,(a,b,r) in enumerate(cols):
        j=(i+1)%n
        E.extend([frozenset(((i,0),(j,0))),frozenset(((i,1),(j,1))),frozenset(((i,0),(i,1)))])
        colors.extend([a,b,r])
    assert len(set(E))==3*n
    inc={}
    for j,e in enumerate(E):
        for v in e: inc.setdefault(v,[]).append(j)
    adj=[sorted(set(inc[u]+inc[v])-{i}) for i,(u,v) in enumerate(map(tuple,E))]
    assert all(len(a)==4 for a in adj)
    assert all(colors[i]!=colors[j] for i in range(3*n) for j in adj[i])
    rich=[len({colors[j] for j in adj[i]})==4 for i in range(3*n)]
    assert all(any(rich[j] for j in adj[i]) for i in range(3*n))
    if verbose:
        return (n,sum(rich),tuple(sorted(set(colors))))
    return True

def compose(n):
    assert n>=10
    # The five residue classes mod five have basis 10..14.
    q,r=divmod(n-10,5)
    basis={0:[5,5],1:[5,6],2:[5,7],3:[6,7],4:[7,7]}[r]
    pieces=basis+[5]*q
    assert sum(pieces)==n
    return [tri for size in pieces for tri in BASE[size]]

def main():
    assert BASE[5][:4]==BASE[6][:4]==BASE[7][:4]
    for n,cols in BASE.items():
        print('basis',verify(cols,True))
    for n in range(10,501):
        verify(compose(n))
    # Check every concatenation of the three sockets with up to six blocks.
    for k in range(1,7):
        for pieces in product((5,6,7),repeat=k):
            verify([tr for p in pieces for tr in BASE[p]])
    print('VERIFY_OK; seven base certificates; all n=10..500; 1092 socket concatenations')
if __name__=='__main__':main()
