#!/usr/bin/env python3
"""Reproduce the minimum-isolation-set census of uniform loose hypercycles.
Standard library only. Run: python verify_hypercycle.py
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def predicted(m, r):
    k = (m + 3) // 4
    delta = 4*k - m
    a = [0] * (delta+1)
    a[0] = 1
    for _ in range(k):
        b = [0] * (delta+1)
        for i, val in enumerate(a):
            for d in range(4):
                if i+d <= delta:
                    b[i+d] += val * (r-1 if d else 1)
        a = b
    return k, m*a[delta]//k


def predicted_types(m, r):
    k=(m+3)//4; delta=4*k-m
    # polynomial 1+(1+(r-2)y)(u+u^2+u^3), modulo u^(delta+1)
    table={(0,0):1}
    for _ in range(k):
        nxt={}
        for (deficit, private), count in table.items():
            for du,dy,weight in [(0,0,1)]+[(d,0,1) for d in range(1,4)]+[(d,1,r-2) for d in range(1,4)]:
                if deficit+du<=delta:
                    idx=(deficit+du,private+dy)
                    nxt[idx]=nxt.get(idx,0)+count*weight
        table=nxt
    out={j:(m*table.get((delta,j),0))//k for j in range(k+1)}
    assert all(m*table.get((delta,j),0)%k==0 for j in range(k+1))
    return {j:v for j,v in out.items() if v}


def exhaustive(m, r, connectivity=True):
    # Junction j_i lies in E_i and E_(i+1); private u_i,a lies in E_i.
    edges=[]
    for i in range(m):
        edges.append({i,(i-1)%m} | {m+i*(r-2)+j for j in range(r-2)})
    n=m*(r-1)
    neighborhoods=[{v} for v in range(n)]
    for e in edges:
        for v in e:
            neighborhoods[v].update(e)
    edge_hit_masks=[]
    for v in range(n):
        edge_hit_masks.append(sum((1<<i) for i,e in enumerate(edges) if neighborhoods[v].intersection(e)))
    target=(1<<m)-1
    k=(m+3)//4
    minima=set()
    got=Counter()
    for sel in combinations(range(n),k):
        bits=0
        for v in sel:bits |= edge_hit_masks[v]
        if bits == target:
            minima.add(frozenset(sel))
            got[sum(v>=m for v in sel)]+=1
    assert dict(got)==predicted_types(m,r),(m,r,got,predicted_types(m,r))
    assert len(minima)==predicted(m,r)[1]
    if connectivity:
        unseen=set(minima)
        ncomponents=0
        for _ in range(len(minima)):
            if not unseen:break
            ncomponents+=1
            s=unseen.pop(); stack=[s]
            while stack:
                cur=stack.pop()
                for v in cur:
                    smaller=cur-{v}
                    for w in range(n):
                        if w in cur:continue
                        other=frozenset(smaller|{w})
                        if other in unseen:
                            unseen.remove(other);stack.append(other)
        assert (ncomponents==4 if (m%4==0 and m>=8) else ncomponents==1),(m,r,ncomponents)
    return len(minima),dict(got)


def main():
    cases=0
    scanned=0
    for r in range(3,7):
        for m in range(3,17):
            n=m*(r-1);k=(m+3)//4
            if comb(n,k)>70000:continue
            total, types=exhaustive(m,r,connectivity=True)
            cases+=1;scanned+=comb(n,k)
    # verify all residue-polynomial identities through many orders and ranks
    for r in range(3,40):
        for m in range(3,700):
            k, total=predicted(m,r)
            types=predicted_types(m,r)
            assert sum(types.values())==total
            if m%4==0:assert total==4 and types=={0:4}
            if m%4==3:assert total==m*(r-1)
    print('DIRECT_HYPERGRAPH_NEIGHBORHOOD_CENSUS_PASS', 'cases=', cases, 'candidate_subsets=', scanned)
    print('DIRECT_ONE_VERTEX_EXCHANGE_CONNECTIVITY_PASS')
    print('EXACT_TYPE_ENUMERATOR_IDENTITIES_PASS ranks=3..39 orders=3..699')
    print('VERIFY_OK')

if __name__=='__main__':main()
