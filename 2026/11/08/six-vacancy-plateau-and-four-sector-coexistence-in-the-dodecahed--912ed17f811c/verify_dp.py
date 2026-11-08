"""Independent exact min-plus variable-elimination verifier for zero-field spin-one dodecahedron.
Uses a graph factorization rather than the ternary Gray-code state enumeration.
"""
from itertools import product

EDGES=[(0, 1), (0, 10), (10, 12), (1, 2), (1, 11), (11, 13), (2, 3), (2, 12), (12, 14), (3, 4), (3, 13), (13, 15), (4, 5), (4, 14), (14, 16), (5, 6), (5, 15), (15, 17), (6, 7), (6, 16), (16, 18), (7, 8), (7, 17), (17, 19), (8, 9), (8, 18), (18, 10), (9, 0), (9, 19), (19, 11)]
ORDER=[0, 2, 4, 6, 8, 11, 15, 10, 14, 17, 3, 18, 9, 1, 5, 7, 12, 13, 16, 19]

# Each factor: tuple of its variables and value table indexed by spin tuples.
# A value is {occupancy: (minimum interaction, count)}.

def initial_factors():
    factors=[]
    for v in range(20):
        factors.append(((v,),{(s,):{s*s:(0,1)} for s in (-1,0,1)}))
    for u,v in EDGES:
        factors.append(((u,v),{(a,b):{0:(a*b,1)} for a in (-1,0,1) for b in (-1,0,1)}))
    return factors

def times(A,B):
    C={}
    for qa,(ea,ca) in A.items():
        for qb,(eb,cb) in B.items():
            q=qa+qb;e=ea+eb
            old=C.get(q)
            if old is None or e<old[0]:C[q]=(e,ca*cb)
            elif e==old[0]:C[q]=(e,old[1]+ca*cb)
    return C

def plus(A,B):
    C=A.copy()
    for q,(e,c) in B.items():
        old=C.get(q)
        if old is None or e<old[0]:C[q]=(e,c)
        elif e==old[0]:C[q]=(e,old[1]+c)
    return C

def solve(verbose=False):
    factors=initial_factors()
    for index,v in enumerate(ORDER):
        hits=[F for F in factors if v in F[0]]
        factors=[F for F in factors if v not in F[0]]
        scope=tuple(sorted(set(w for F,_ in hits for w in F)))
        rest=tuple(w for w in scope if w!=v)
        sindex={w:i for i,w in enumerate(scope)}
        new={}
        locs=[[sindex[w] for w in F] for F,_ in hits]
        for vals in product((-1,0,1),repeat=len(scope)):
            d={0:(0,1)}
            for (F,T),inds in zip(hits,locs):
                d=times(d,T[tuple(vals[i] for i in inds)])
            key=tuple(vals[sindex[w]] for w in rest)
            new[key]=plus(new.get(key,{}),d)
        factors.append((rest,new))
        if verbose:print(index,v,'bag',len(scope),'states',len(new),'max poly',max(map(len,new.values())))
    assert len(factors)==1 and factors[0][0]==()
    return factors[0][1][()]

if __name__=='__main__':
    r=solve(verbose=False)
    for q,(e,c) in sorted(r.items()):print(f'{q},{e},{c}')
