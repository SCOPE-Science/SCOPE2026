"""Exact finite orbit-bisimulation for Boolean affine parallelogram structures.
Scientific reproducibility utility; no dependencies.
"""
from collections import deque, defaultdict
from itertools import combinations


def canon(t):
    """Affine canonical form using greedy independent difference vectors."""
    basis=[]
    out=[0]
    for v in t[1:]:
        v ^= t[0]
        # Proper representation via all 2^rank linear combos (rank <= 6)
        orig = v
        rep = None
        for c in range(1<<len(basis)):
            y=0
            for j,b in enumerate(basis):
                if c>>j &1: y ^= b
            if y==orig:
                rep=c;break
        if rep is None:
            rep=1<<len(basis)
            basis.append(orig)
        out.append(rep)
    return tuple(out)


def atom_type(t):
    z=tuple(i for i,j in combinations(range(len(t)),2) if t[i] == t[j])
    q=tuple(inds for inds in combinations(range(len(t)),4) if not (t[inds[0]]^t[inds[1]]^t[inds[2]]^t[inds[3]]))
    return z,q


def graph(k,d):
    init=(0,)*k
    trans={}
    q=deque([init]); visited={init}
    while q:
        t=q.popleft()
        ttrans=[]
        for i in range(k):
            a=set()
            for x in range(1<<d):
                arr=list(t);arr[i]=x
                s=canon(arr)
                a.add(s)
                if s not in visited:
                    visited.add(s);q.append(s)
            ttrans.append(tuple(sorted(a)))
        trans[t]=tuple(ttrans)
    return trans


def refine(graphs):
    # all disjoint states are (graph_idx, tuple)
    states=[(j,t) for j,g in enumerate(graphs) for t in g]
    color={s:atom_type(s[1]) for s in states}
    colors={c:i for i,c in enumerate(sorted(set(color.values())))}
    color={s:colors[color[s]] for s in states}
    rounds=0
    while True:
        groups={}
        signatures={}
        for s in states:
            j,t=s
            sig=(color[s], tuple(tuple(sorted({color[(j,z)] for z in out})) for out in graphs[j][t]))
            signatures[s]=sig
        order={v:i for i,v in enumerate(sorted(set(signatures.values())))}
        new={s:order[signatures[s]] for s in states}
        rounds+=1
        if len(set(new.values()))==len(set(color.values())):
            # sig includes old color so no merged classes, no splits => stable
            return new,rounds,len(set(new.values())),len(states)
        color=new


def run(k,ds):
    gs=[graph(k,d) for d in ds]
    cl,nr,nc,ns=refine(gs)
    zeros=[cl[(i,(0,)*k)] for i in range(len(ds))]
    return dict(k=k,dimensions=ds,orbits=[len(g) for g in gs],rounds=nr,stable_types=nc,total_states=ns,zero_state_colors=zeros,zero_equivalent=len(set(zeros))==1)

if __name__=='__main__':
    for k, ds in [(2,(0,1)),(3,(1,2)),(3,(2,3)),(4,(2,3)),(4,(3,4)),(5,(3,4)),(5,(4,5)),(6,(3,4)),(6,(4,5)),(7,(4,5))]:
        r=run(k,ds)
        print(r,flush=True)
