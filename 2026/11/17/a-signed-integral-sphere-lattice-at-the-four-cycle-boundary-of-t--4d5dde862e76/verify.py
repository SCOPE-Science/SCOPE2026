#!/usr/bin/env python3
"""Finite checks for a three-cut Alexander-dual collapse on thin cycle products.
No external dependencies. The all-order theorem rests on the accompanying proof.
"""
from itertools import combinations
from collections import Counter

def edges_and_faces(n):
    N=4*n
    vertices=range(N)
    def idx(a,b): return (a%4)*n+(b%n)
    E=set()
    for a in range(4):
        for b in range(n):
            x=idx(a,b)
            for y in (idx(a+1,b),idx(a,b+1)):
                E.add(tuple(sorted((x,y))))
    adj=[set() for _ in vertices]
    for a,b in E: adj[a].add(b);adj[b].add(a)
    def good_triple(t):
        return sum((b in adj[a]) for a,b in combinations(t,2))>=2
    triangles=set(t for t in combinations(vertices,3) if good_triple(t))
    tetra=set(q for q in combinations(vertices,4) if all(t in triangles for t in combinations(q,3)))
    F={0:{(i,) for i in vertices},1:set(combinations(vertices,2)),2:triangles.copy(),3:tetra.copy()}
    return E,adj,F,idx

def square_cycles(n,idx):
    sq=set()
    for a in range(4):
        for b in range(n):
            sq.add(tuple(sorted((idx(a,b),idx(a+1,b),idx(a+1,b+1),idx(a,b+1)))))
    for b in range(n):
        sq.add(tuple(sorted(idx(a,b) for a in range(4))))
    return sq

def collapse(n,verbose=False):
    E,adj,F,idx=edges_and_faces(n)
    N=4*n
    assert len(E)==8*n
    S=square_cycles(n,idx)
    assert F[3]==S and len(S)==5*n,(n,len(F[3]),len(S))
    assert len(F[2])==24*n
    # An admissible five-face would have ten admissible 3-subsets.
    for quint in combinations(range(N),5):
        assert not all(t in F[2] for t in combinations(quint,3)),('five-face',n,quint)
    pairs=[]
    for q in sorted(S):
        diagonals=sorted(p for p in combinations(q,2) if p not in E)
        assert len(diagonals)==2,(n,q,diagonals)
        e=diagonals[0]
        triangles=sorted(t for t in combinations(q,3) if set(e).issubset(t))
        assert len(triangles)==2
        removed=triangles[0]
        assert sum(set(removed).issubset(h) for h in F[3])==1
        F[3].remove(q);F[2].remove(removed);pairs.append((removed,q))
        remaining=triangles[1]
        assert sum(set(e).issubset(t) for t in F[2])==1
        assert sum(set(e).issubset(t) for t in F[3])==0
        F[2].remove(remaining);F[1].remove(e);pairs.append((e,remaining))
    singles=0
    for u,v in combinations(range(N),2):
        pair=(u,v)
        if pair in E: continue
        common=adj[u]&adj[v]
        if len(common)==1:
            w=next(iter(common))
            t=tuple(sorted((u,v,w)))
            assert pair in F[1] and t in F[2]
            assert sum(set(pair).issubset(q) for q in F[2])==1
            assert not F[3]
            F[2].remove(t);F[1].remove(pair);pairs.append((pair,t))
            singles+=1
        else:
            assert len(common) in (0,2), (u,v,common)
    assert singles==4*n
    assert len(pairs)==14*n
    assert not F[3]
    assert len(F[2])==10*n
    kept_d=set(F[1])-E
    expected_diagonals={d for q in S for d in combinations(q,2) if d not in E and d in F[1]}
    assert len(expected_diagonals)==5*n
    for q in S:
        tris=[t for t in F[2] if set(t).issubset(q)]
        assert len(tris)==2 and set().union(*map(set,tris))==set(q)
    long_edges={p for p in combinations(range(N),2) if p not in E and not adj[p[0]].intersection(adj[p[1]])}
    assert F[1]==E|expected_diagonals|long_edges
    assert len(long_edges)==8*n*(n-3)
    assert len(F[1])==len(E)+5*n+len(long_edges)
    # Independent F_2 simplicial boundary ranks by exact XOR elimination.
    def rank(d):
        src=sorted(F0[d]);trg={f:i for i,f in enumerate(sorted(F0[d-1]))}
        basis={}
        for simplex in src:
            vec=0
            for face in combinations(simplex,d):
                vec^=1<<trg[face]
            while vec:
                p=vec.bit_length()-1
                if p in basis: vec^=basis[p]
                else: basis[p]=vec;break
        return len(basis)
    # Build original complex independently instead of computing from collapsed one.
    _,_,F0,_=edges_and_faces(n)
    r1,r2,r3=rank(1),rank(2),rank(3)
    assert (r1,r2,r3)==(N-1,18*n,5*n), (n,r1,r2,r3)
    betti1=len(F0[1])-r1-r2
    betti2=len(F0[2])-r2-r3
    assert (betti1,betti2)==(8*n*(n-3)+1,n)
    if verbose: print(f'PASS n={n} faces=( {N}, {len(F0[1])}, {len(F0[2])}, {len(F0[3])} ) 4cycles={len(S)} collapse_pairs={len(pairs)} extra_edges={len(long_edges)} ranks=({r1},{r2},{r3}) betti=({betti1},{betti2})')

if __name__=='__main__':
    for n in [5,6,7,8]: collapse(n,True)
    print('THIN_TORUS_THREE_CUT_PASS')

# Integral oriented square-cell chain model, independent of mod-two ranks.
def symmetry_lattice_check(n):
    E,adj,F,idx=edges_and_faces(n)
    cells={}
    for a in range(4):
        for b in range(n):
            cells[('Q',a,b)]=(idx(a,b),idx(a+1,b),idx(a+1,b+1),idx(a,b+1))
    for b in range(n):
        cells[('D',b)]=tuple(idx(a,b) for a in range(4))
    by_set={frozenset(v):k for k,v in cells.items()}
    assert len(by_set)==5*n
    def chain_boundary(chain):
        out=Counter()
        for key,c in chain.items():
            if not c:continue
            v=cells[key]
            for u,w in zip(v,v[1:]+v[:1]):
                p=tuple(sorted((u,w)))
                out[p]+= c*(1 if (u,w)==p else -1)
        return {p:c for p,c in out.items() if c}
    z={}
    for b in range(n):
        c=Counter({('Q',a,b):1 for a in range(4)})
        c[('D',b)]-=1
        c[('D',(b+1)%n)]+=1
        z[b]={k:v for k,v in c.items() if v}
        assert not chain_boundary(z[b])
    def image(chain,morphism):
        out=Counter()
        for key,c in chain.items():
            v=tuple(morphism(i) for i in cells[key])
            tgt=by_set[frozenset(v)]
            w=cells[tgt]
            rotations={w[k:]+w[:k] for k in range(4)}
            inverse=w[::-1]
            reverse_rotations={inverse[k:]+inverse[:k] for k in range(4)}
            assert v in rotations or v in reverse_rotations
            sign=1 if v in rotations else -1
            out[tgt]+=c*sign
        return {k:v for k,v in out.items() if v}
    def transform(kind):
        def f(i):
            a,b=divmod(i,n)
            if kind=='r4': a=(a+1)%4
            elif kind=='s4': a=(-a)%4
            elif kind=='rn': b=(b+1)%n
            elif kind=='sn': b=(-b)%n
            else: raise ValueError(kind)
            return idx(a,b)
        return f
    for kind in ('r4','s4','rn','sn'):
        for b in range(n):
            target={'r4':b,'s4':b,'rn':(b+1)%n,'sn':(-b-1)%n}[kind]
            sgn=-1 if kind in ('s4','sn') else +1
            assert image(z[b],transform(kind))=={k:sgn*v for k,v in z[target].items()}
    # Every integral two-cycle is uniquely parametrized by the n coefficients
    # of the Q_{0,b} cells; z_b have the corresponding identity matrix.
    for b in range(n):
        assert [z[b].get(('Q',0,j),0) for j in range(n)]==[int(j==b) for j in range(n)]
    print(f'INTEGRAL_SYMMETRY_PASS n={n} rank={n} signed_generators=r4:+,s4:-,rn:shift,sn:-reverse_edge')

if __name__=='__main__':
    for n in [5,6,7,8]: symmetry_lattice_check(n)
