#!/usr/bin/env python3
"""Exact 5-point isometry-extension and orbit census for the regular 24-cell.

Uses Python standard library only. All arithmetic is integer arithmetic.
The 24 vertices here are the twice-unit-short-root realization.
"""
from itertools import combinations, permutations, product
from collections import Counter, deque
from pathlib import Path

V = []
for j in range(4):
    for s in (-2, 2):
        x = [0] * 4
        x[j] = s
        V.append(tuple(x))
V += list(product((-1, 1), repeat=4))
assert len(V) == len(set(V)) == 24
INDEX = {v: i for i, v in enumerate(V)}
H = ((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))

def squared_dist(i,j):
    return sum((V[i][t]-V[j][t])**2 for t in range(4))

SQDIST = tuple(tuple(squared_dist(i,j) for j in range(24)) for i in range(24))
assert {SQDIST[i][j] for i in range(24) for j in range(i+1,24)} == {4,8,12,16}

def determinant4(rows):
    a,b,c,d=rows
    def det3(x,y,z):
        return x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0])
    return sum((-1)**j*a[j]*det3([b[k] for k in range(4) if k!=j],
                                  [c[k] for k in range(4) if k!=j],
                                  [d[k] for k in range(4) if k!=j]) for j in range(4))

def absdet(ids):
    base=V[ids[0]]
    return abs(determinant4([[V[j][k]-base[k] for k in range(4)] for j in ids[1:]]))

def generate_group():
    acts=[]
    for k in range(3):
        def adjacent_swap(v,k=k):
            w=list(v)
            w[k],w[k+1]=w[k+1],w[k]
            return tuple(w)
        acts.append(adjacent_swap)
    acts.append(lambda v: (-v[0],v[1],v[2],v[3]))
    def triality(v):
        n=tuple(sum(h[i]*v[i] for i in range(4)) for h in H)
        assert all(t%2==0 for t in n)
        return tuple(t//2 for t in n)
    acts.append(triality)
    gens=[tuple(INDEX[act(v)] for v in V) for act in acts]
    identity=tuple(range(24))
    group={identity}
    queue=deque([identity])
    while queue:
        cur=queue.popleft()
        for gen in gens:
            g=tuple(gen[cur[i]] for i in range(24))
            if g not in group:
                group.add(g)
                queue.append(g)
    assert len(group)==1152
    for g in group:
        assert all(SQDIST[i][j]==SQDIST[g[i]][g[j]] for i in range(24) for j in range(i+1,24))
    return sorted(group)

def signature(ids):
    return min(tuple(SQDIST[p[i]][p[j]] for i in range(5) for j in range(i+1,5))
               for p in permutations(ids))

def isometries_of_five(ids):
    return {tuple(p) for p in permutations(range(5))
            if all(SQDIST[ids[i]][ids[j]]==SQDIST[ids[p[i]]][ids[p[j]]]
                   for i in range(5) for j in range(i+1,5))}

def burnside(G):
    coeff_sum=0
    fixed=Counter()
    for g in G:
        seen=set()
        lengths=[]
        for i in range(24):
            if i in seen: continue
            t=i
            n=0
            while t not in seen:
                seen.add(t)
                n+=1
                t=g[t]
            lengths.append(n)
        assert sum(lengths)==24
        coeff=[1]+[0]*5
        for n in lengths:
            for i in range(5,n-1,-1):
                coeff[i]+=coeff[i-n]
        coeff_sum+=coeff[5]
        fixed[coeff[5]]+=1
    assert coeff_sum == 93312
    assert coeff_sum//len(G)==81
    return fixed

def run():
    G=generate_group()
    bs=burnside(G)
    assert bs==Counter({0:693,2:96,6:96,10:72,20:36,96:32,110:84,220:18,402:12,2292:12,42504:1})
    seen=set()
    rows=[]
    coverage=Counter()
    sigs=set()
    orbit_types=Counter()
    det_orbits=Counter()
    d_counts=Counter()
    for ids in combinations(range(24),5):
        if ids in seen: continue
        orbit={tuple(sorted(g[j] for j in ids)) for g in G}
        assert ids in orbit and not orbit.intersection(seen)
        seen.update(orbit)
        det=absdet(ids)
        s=signature(ids)
        assert s not in sigs
        sigs.add(s)
        size=len(orbit)
        autos=isometries_of_five(ids)
        index={k:j for j,k in enumerate(ids)}
        restrictions={tuple(index[g[j]] for j in ids) for g in G
                      if set(g[j] for j in ids)==set(ids)}
        assert autos==restrictions
        fixpointwise=sum(1 for g in G if all(g[j]==j for j in ids))
        assert fixpointwise*size*len(autos)==len(G), (ids,size,len(autos),fixpointwise)
        if det>0: assert fixpointwise==1
        coverage[det]+=size
        det_orbits[det]+=1
        orbit_types[size]+=1
        rows.append((det,size,ids,s,len(autos)))
    assert len(seen)==42504
    assert len(sigs)==len(rows)==81
    assert det_orbits==Counter({0:32,8:15,16:21,24:7,32:4,40:1,48:1})
    assert coverage==Counter({0:12168,8:11328,16:13776,24:3936,32:1152,40:96,48:48})
    assert orbit_types==Counter({576:39,288:15,1152:12,96:4,192:4,144:4,48:2,72:1})
    assert sum(size for _,size,_,_,_ in rows)==42504
    assert sum(det_orbits[d] for d in det_orbits if d>0)==49
    rows.sort(key=lambda row:(-row[0],row[3],row[2]))
    output=Path(__file__).resolve().parent/'orbit_catalogue.tsv'
    header='orbit_id\tabs_determinant\torbit_size\tpoint_indices_0based\tcanonical_squared_distances\tlocal_metric_automorphisms\n'
    lines=[header]
    for n,(det,size,ids,s,autom) in enumerate(rows,1):
        lines.append(f'{n:02d}\t{det}\t{size}\t{",".join(map(str,ids))}\t{",".join(map(str,s))}\t{autom}\n')
    expected=''.join(lines).encode('utf-8')
    if output.exists():
        assert output.read_bytes()==expected, 'catalogue mismatch'
    else:
        output.write_bytes(expected)
    print('24_CELL_FIVE_POINT_METRIC_RIGIDITY_PASSED group=1152 sets=42504 orbits=81 spanning=49 degenerate=32 distinct_signatures=81 burnside_sum=93312 strong_extension=81')
    return rows

if __name__=='__main__':run()
