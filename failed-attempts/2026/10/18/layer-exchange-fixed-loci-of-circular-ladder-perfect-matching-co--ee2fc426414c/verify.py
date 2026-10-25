#!/usr/bin/env python3
"""Standalone finite checks for symmetry-fixed perfect-matching complexes.
The infinite-family proof is in RESULT.md; this is independent finite corroboration.
"""
from collections import defaultdict, deque


def cycle_whiskered_faces(n):
    # Core cycle edges h_i have indices 0..n-1; whiskers r_i indices n..2n-1.
    edges = [(i, (i + 1) % n) for i in range(n)] + [(i, n + i) for i in range(n)]
    incidence = [0] * (2 * n)
    for k, (a,b) in enumerate(edges):
        incidence[k] = (1 << a) | (1 << b)
    faces = [0]
    for mask in range(1, 1 << (2*n)):
        used = 0
        valid = True
        for j in range(2*n):
            if mask >> j & 1:
                if used & incidence[j]:
                    valid = False
                    break
                used |= incidence[j]
        if valid:
            faces.append(mask)
    return set(faces)


def fixed_orbit_faces_from_actual_ladder(n):
    # Construct the graph C_n x K_2, enumerate its actual perfect matchings,
    # then enumerate invariant subsets of their edge sets.
    edges = []
    for a in range(2):
        for i in range(n):
            edges.append((a*n+i, a*n+(i+1)%n))
    for i in range(n):
        edges.append((i,n+i))
    v_to_edges=[[] for _ in range(2*n)]
    for e,(u,v) in enumerate(edges):
        v_to_edges[u].append(e);v_to_edges[v].append(e)
    perfect=[]
    def rec(unmatched, chosen):
        if not unmatched:
            perfect.append(tuple(chosen));return
        i=min(unmatched)
        for e in v_to_edges[i]:
            u,v=edges[e]
            other = v if u==i else u
            if other in unmatched:
                rec(unmatched-{i,other},chosen+[e])
    rec(set(range(2*n)),[])
    orb={}
    for i in range(n):
        orb[i]=orb[n+i]=i
        orb[2*n+i]=n+i
    invariant=set()
    for matching in perfect:
        for subset in range(1<<n):
            chosen=[matching[k] for k in range(n) if subset>>k&1]
            orbits={orb[e] for e in chosen}
            if all(sum(orb[e]==j for e in chosen)==(2 if j<n else 1)
                   for j in orbits):
                invariant.add(sum(1<<j for j in orbits))
    return invariant


def audit(n):
    faces = cycle_whiskered_faces(n)
    direct = fixed_orbit_faces_from_actual_ladder(n)
    assert direct == faces, (n, len(direct), len(faces))
    sorted_faces=sorted(faces, key=lambda s:(s.bit_count(),s))
    pairing={}
    # Match within the fiber of core-edge selections; no cross-fiber matches.
    for s in sorted_faces:
        core = s & ((1 << n)-1)
        covered = 0
        for i in range(n):
            if core >> i & 1:
                covered |= (1 << i) | (1 << ((i+1)%n))
        free = [i for i in range(n) if not (covered >> i & 1)]
        if free:
            j = n + free[0]
            if not (s >> j & 1) and s != 0:
                partner = s | (1 << j)
                assert partner in faces
                pairing[s] = partner
    upper = set(pairing.values())
    assert not (set(pairing) & upper)
    critical = faces - set(pairing) - upper - {0}
    # For the empty-core fiber, the critical vertex is r_0.
    expected={1 << n}
    if n % 2 == 0:
        expected |= {sum(1 << i for i in range(parity,n,2)) for parity in (0,1)}
    assert critical == expected, (n, critical, expected)
    # Directed Hasse graph with matching edges directed up and all other edges down.
    nonempty=faces-{0}
    incoming={s:0 for s in nonempty}
    out=defaultdict(list)
    for s in nonempty:
        for j in range(2*n):
            if not(s >> j & 1):continue
            t=s^(1<<j)
            if t==0:continue
            if pairing.get(t)==s:
                a,b=t,s
            else:
                a,b=s,t
            out[a].append(b)
            incoming[b]+=1
    dq=deque([s for s in nonempty if incoming[s]==0]); visited=0
    while dq:
        x=dq.popleft(); visited+=1
        for y in out[x]:
            incoming[y]-=1
            if incoming[y]==0:dq.append(y)
    assert visited==len(nonempty), ('acyclicity failed',n,visited,len(nonempty))
    # Independent mod-two chain homology, without using the Morse matching.
    levels=defaultdict(list)
    for s in faces:levels[s.bit_count()].append(s)
    ranks={}
    for k in range(1,n+1):
        index={s:i for i,s in enumerate(levels[k-1])}
        piv={}
        for s in levels[k]:
            column=0
            for j in range(2*n):
                if s>>j&1:column ^= 1<<index[s^(1<<j)]
            while column:
                high=column.bit_length()-1
                if high in piv:column ^= piv[high]
                else:piv[high]=column;break
        ranks[k]=len(piv)
    betti = {k-1:len(levels[k])-ranks.get(k,0)-ranks.get(k+1,0)
             for k in range(n+1)}
    betti = {d:v for d,v in betti.items() if v}
    target=({n//2-1:2} if n%2==0 else {})
    assert betti == target, (n,betti,target)
    return {'n':n,'augmented_faces':len(faces),'pairs':len(pairing),
            'critical_dimensions':dict(sorted((d,sum(s.bit_count()-1==d for s in critical))
                 for d in set(s.bit_count()-1 for s in critical))),
            'mod2_betti':betti, 'acyclic':'yes'}

if __name__=='__main__':
    for n in range(3,10): print(audit(n),flush=True)
    print('ALL CHECKS PASSED')
