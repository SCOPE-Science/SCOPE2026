#!/usr/bin/env python3
"""Self-contained finite verification for a theorem about high-degree matching complexes.
Usage: python3 check_rectangular.py
No downloads, no external modules, no randomness.
"""
from itertools import combinations


def complex_of_faults(n, faults):
    edges = [(i,j) for i in range(n) for j in range(n) if (i,j) not in faults]
    rows = {i for i in range(n) if all((i,j) not in faults for j in range(n))}
    cols = {j for j in range(n) if all((i,j) not in faults for i in range(n))}
    constraints = []
    for i in sorted(rows):
        constraints.append(sum(1 << k for k,(a,b) in enumerate(edges) if a==i))
    for j in sorted(cols):
        constraints.append(sum(1 << k for k,(a,b) in enumerate(edges) if b==j))
    N=len(edges)
    faces_by_size=[[] for _ in range(N+1)]
    for S in range(1<<N):
        if all(S&c != c for c in constraints):
            faces_by_size[S.bit_count()].append(S)
    return edges, rows, cols, constraints, faces_by_size

def rank_two(columns):
    pivot={}
    for v in columns:
        while v:
            k=v.bit_length()-1
            if k not in pivot:
                pivot[k]=v
                break
            v ^= pivot[k]
    return len(pivot)

def homology_mod2(faces_by_size):
    ranks=[]
    for s in range(1,len(faces_by_size)):
        if not faces_by_size[s]:
            ranks.append(0); continue
        lower={S:i for i,S in enumerate(faces_by_size[s-1])}
        cols=[]
        for S in faces_by_size[s]:
            bits=0; u=S
            while u:
                lsb=u&-u
                bits ^= 1<<lower[S^lsb]
                u^=lsb
            cols.append(bits)
        ranks.append(rank_two(cols))
    betti={}
    for s in range(len(faces_by_size)):
        left=ranks[s-1] if s>0 else 0
        right=ranks[s] if s<len(ranks) else 0
        betti[s-1]=len(faces_by_size[s])-left-right
    return {k:v for k,v in betti.items() if v}

def prediction(n,faults):
    R={i for i,j in faults}; C={j for i,j in faults}
    if not faults: return ('intact', (n-1)**2-1)
    if len(faults)==n*n: return ('empty-edge-set',-1)
    if faults=={(i,j) for i in R for j in C}:
        N=n*n-len(faults); r=2*n-len(R)-len(C)
        return ('sphere',N-r-1)
    return ('cone',None)

def check_one(n,faults, homology=True):
    E, rows, cols, C, faces=complex_of_faults(n,faults)
    case, degree=prediction(n,faults)
    # Validate the exact cone/constraint covering or private-edge hypotheses.
    if case=='cone':
        R={i for i,j in faults}; S={j for i,j in faults}
        witnesses=[(i,j) for i in R for j in S if (i,j) not in faults]
        assert witnesses and all(i not in rows and j not in cols for i,j in witnesses)
        assert witnesses[0] in E
        w=E.index(witnesses[0]); assert all(((f & (1<<w)) or (f | (1<<w)) in faces[f.bit_count()+1]) for layer in faces for f in layer if f.bit_count()<len(E))
        expected={}
    elif case=='sphere':
        R={i for i,j in faults}; S={j for i,j in faults}
        private=[]
        for i in rows: private.append(E.index((i,min(S))))
        for j in cols: private.append(E.index((min(R),j)))
        assert len(set(private))==len(C)
        for ii,p in enumerate(private):
            assert C[ii] & (1<<p)
            assert sum(bool(c & (1<<p)) for c in C)==1
        assert all(any(c & (1<<k) for c in C) for k in range(len(E)))
        expected={degree:1}
    elif case=='intact': expected={degree:1}
    else: expected={-1:1}
    if homology:
        actual=homology_mod2(faces)
        assert actual==expected,(n,sorted(faults),case,degree,actual,expected)
    return case,len(E),sum(map(len,faces))

def run():
    summary={}
    for n in (2,3):
        counts={}
        for mask in range(1<<(n*n)):
            F={(i,j) for i in range(n) for j in range(n) if mask & (1<<(n*i+j))}
            if not F or len(F)==n*n: continue
            case,N,nfaces=check_one(n,F,True)
            counts[case]=counts.get(case,0)+1
        summary[f'n={n}']=counts
    # For n=4 check one representative of each rectangular size pair.
    n=4; counts={}
    for a in range(1,n+1):
        for b in range(1,n+1):
            F={(i,j) for i in range(a) for j in range(b)}
            if len(F)==n*n:continue
            case,N,nfaces=check_one(n,F,True)
            counts[(a,b)]=(case,N,nfaces)
    print('n=2,3 exhaustive mod-two homology:',summary)
    print('n=4 rectangular representative mod-two homology:',counts)
    print('PASS: exhaustive fault patterns n=2,3; 15 rectangle types n=4')
if __name__=='__main__':run()
