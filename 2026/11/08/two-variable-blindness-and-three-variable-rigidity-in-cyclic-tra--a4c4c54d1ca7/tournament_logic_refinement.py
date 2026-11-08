#!/usr/bin/env python3
"""Finite sanity check for bounded-variable logical equivalence of three-block cyclic tournaments."""
from itertools import product
from math import comb

def canonical(a):
    return min((a[0],a[1],a[2]),(a[1],a[2],a[0]),(a[2],a[0],a[1]))

def triples(max_order):
    return sorted({canonical((a,b,n-a-b)) for n in range(3,max_order+1)
                   for a in range(1,n-1) for b in range(1,n-a)})

def make_graph(t):
    groups=[]
    for i,n in enumerate(t): groups.extend([(i,j) for j in range(n)])
    N=len(groups)
    edges=[[0]*N for _ in range(N)]
    for x,(i,j) in enumerate(groups):
        for y,(ii,jj) in enumerate(groups):
            if x!=y:
                edges[x][y]=int(j<jj if i==ii else (ii-i)%3==1)
    return edges

def types(graphs,k):
    states=[]
    atom_ids={}
    for spec,E in graphs:
        n=len(E)
        tup=list(product(range(n),repeat=k))
        ids=[]
        for v in tup:
            typ=tuple((v[i]==v[j], E[v[i]][v[j]]) for i in range(k) for j in range(k))
            if typ not in atom_ids: atom_ids[typ]=len(atom_ids)
            ids.append(atom_ids[typ])
        states.append((spec,n,tup,ids))
    recolor_rounds=0
    while True:
        signatures={}
        newstates=[]
        for spec,n,tup,ids in states:
            idx={p:i for i,p in enumerate(tup)}
            new=[]
            for p,old in zip(tup,ids):
                replacements=[]
                for i in range(k):
                    seen=set()
                    for u in range(n):
                        q=p[:i]+(u,)+p[i+1:]
                        seen.add(ids[idx[q]])
                    replacements.append(tuple(sorted(seen)))
                sig=(old,tuple(replacements))
                if sig not in signatures: signatures[sig]=len(signatures)
                new.append(signatures[sig])
            newstates.append((spec,n,tup,new))
        recolor_rounds+=1
        same=all(old[3]==new[3] for old,new in zip(states,newstates))
        states=newstates
        if same: break
        assert recolor_rounds<30, 'refinement did not stabilize'
    spectra={spec:frozenset(ids) for spec,n,tup,ids in states}
    for a,sa in spectra.items():
        for b,sb in spectra.items():
            predicted=(k==2) or (a==b)
            actual=(sa==sb)
            assert actual==predicted, (k,a,b,actual,predicted)
    return recolor_rounds,len(spectra),sum(len(t) for _,_,t,_ in states),len({v for v in spectra.values()})

if __name__=='__main__':
    ts=triples(8)
    graphs=[(t,make_graph(t)) for t in ts]
    print('triples',len(ts),'order_range',3,8)
    for k in (2,3):
        rounds,m,tuples,spectra=types(graphs,k)
        print('width',k,'refinement_rounds',rounds,'graphs',m,'ordered_tuples',tuples,'sentence_types',spectra)
    print('FINITE_REFINEMENT_OK')
