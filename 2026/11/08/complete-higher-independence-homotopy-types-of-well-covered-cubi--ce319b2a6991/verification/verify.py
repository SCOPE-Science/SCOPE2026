#!/usr/bin/env python3
"""Reproduce the integral homotopy classification of well-covered cubic polyhedral graphs.

Only the Python standard library is required. Use: python verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache


def graphs():
    tetra = (4, [(u, v) for u in range(4) for v in range(u+1, 4)])

    def gp(n, k):
        edges = []
        for i in range(n):
            edges += [(i, (i+1)%n), (i, i+n), (i+n, ((i+k)%n)+n)]
        return 2*n, edges
    return [('tetrahedron', tetra), ('triangular_prism', gp(3, 1)),
            ('pentagonal_prism', gp(5, 1)), ('durer', gp(6, 2))]


def admissible_masks(n, edges):
    neighbors = [0]*n
    for a,b in edges:
        assert 0 <= a < n and 0 <= b < n and a != b
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a
    assert all(x.bit_count()==3 for x in neighbors)
    # Two independent enumerations: induced-degree bound and forbidden length-two paths.
    deg = {s for s in range(1 << n)
           if all(not (s & (1<<v)) or (s & neighbors[v]).bit_count() <= 1
                  for v in range(n))}
    forbidden = set()
    for v in range(n):
        ns = [u for u in range(n) if neighbors[v] & (1<<u)]
        for i in range(len(ns)):
            for j in range(i+1,len(ns)):
                forbidden.add((1<<v)|(1<<ns[i])|(1<<ns[j]))
    triples = {s for s in range(1 << n) if all((s & t)!=t for t in forbidden)}
    assert deg == triples
    return deg


def check_wellcovered(n,edges):
    adj=[0]*n
    for a,b in edges:
        adj[a]|=1<<b;adj[b]|=1<<a
    indep={s for s in range(1<<n) if all(not (s>>v&1) or not (s&adj[v]) for v in range(n))}
    facets=[s for s in indep if all((s>>v)&1 or (s|(1<<v)) not in indep for v in range(n))]
    assert len({s.bit_count() for s in facets})==1
    return (len(facets),facets[0].bit_count())


def toggle_match(faces,n):
    remaining=set(faces); pairs=[]
    for v in range(n):
        for s in sorted(remaining,key=lambda x:(x.bit_count(),x)):
            t=s|(1<<v)
            if s in remaining and not (s>>v)&1 and t in remaining:
                remaining.remove(s);remaining.remove(t)
                pairs.append((s,t))
    assert 2*len(pairs)+len(remaining)==len(faces)
    return pairs,remaining


def hasse_acyclic(faces,pairs):
    matched=set(pairs)
    out=defaultdict(list); indeg={s:0 for s in faces};cover=0
    for t in faces:
        for v in range(t.bit_length()):
            if (t>>v)&1:
                s=t^(1<<v)
                assert s in faces
                if (s,t) in matched: a,b=s,t
                else:a,b=t,s
                out[a].append(b);indeg[b]+=1;cover+=1
    q=deque(s for s,d in indeg.items() if d==0)
    visited=0
    while q:
        s=q.popleft(); visited+=1
        for t in out[s]:
            indeg[t]-=1
            if indeg[t]==0:q.append(t)
    assert visited==len(faces),('cycle',len(faces),visited)
    return cover


def incidence(t,s):
    p=t^s
    assert p and p.bit_count()==1 and s==(s&t)
    k=p.bit_length()-1
    return -1 if (t&((1<<k)-1)).bit_count()%2 else 1


def boundary(t):
    return [(t^(1<<i),(-1 if (t&((1<<i)-1)).bit_count()%2 else 1))
            for i in range(t.bit_length()) if (t>>i)&1]


def morse_boundary(pairs,critical,d):
    # Signed gradient-path chain projection from dimension d+1 to d.
    lower=dict(pairs); upper={b for a,b in pairs}
    crit_d={s for s in critical if s.bit_count()==d+1}
    sources=sorted(s for s in critical if s.bit_count()==d+2)
    targets=sorted(crit_d)
    @lru_cache(None)
    def reduce_face(s):
        if s in upper:return ()
        if s in crit_d:return ((s,1),)
        assert s in lower,('unmatched',s)
        t=lower[s];e=incidence(t,s)
        coeff=defaultdict(int)
        for a,c in boundary(t):
            if a==s:continue
            for x,v in reduce_face(a):coeff[x]-=e*c*v
        return tuple(sorted((x,y) for x,y in coeff.items() if y))
    result=[]
    for t in sources:
        coeff=defaultdict(int)
        for s,c in boundary(t):
            for x,v in reduce_face(s):coeff[x]+=c*v
        result.append([coeff[x] for x in targets])
    return targets,sources,result


def eliminate_matched_pairs(faces,pairs,critical):
    """Independent full integer-chain cancellation, without gradient path recursion."""
    differential={t:dict(boundary(t)) for t in faces}
    for a,b in pairs:
        pivot=differential[b].get(a)
        assert pivot in (-1,1)
        for c in list(differential):
            if c in (a,b):continue
            if c.bit_count()==b.bit_count():
                coefficient=differential[c].get(a,0)
                if coefficient:
                    scalar=coefficient//pivot
                    for t,v in differential[b].items():
                        differential[c][t]=differential[c].get(t,0)-scalar*v
                        if not differential[c][t]:del differential[c][t]
            elif c.bit_count()==b.bit_count()+1:
                differential[c].pop(b,None)
        del differential[a]
        del differential[b]
    assert set(differential)==critical
    return differential


def gf2_rank(columns):
    pivots={}
    for x in columns:
        while x:
            j=x.bit_length()-1
            if j in pivots:x ^= pivots[j]
            else:pivots[j]=x;break
    return len(pivots)


def independent_mod2_betti(faces):
    by_n=defaultdict(list)
    for s in faces:
        if s:by_n[s.bit_count()].append(s)
    ranks={0:0}
    for k in sorted(by_n):
        if k==1:continue
        target_index={s:i for i,s in enumerate(by_n[k-1])}
        columns=[]
        for t in by_n[k]:
            v=0
            for a,_ in boundary(t):v ^= 1<<target_index[a]
            columns.append(v)
        ranks[k]=gf2_rank(columns)
    bettis={}
    for k,rows in by_n.items():
        b=len(rows)-ranks.get(k,0)-ranks.get(k+1,0)
        if k==1:b-=1
        if b:bettis[k-1]=b
    return bettis


def run():
    expect={
        'tetrahedron':({1:3}, {-1:1,0:4,1:6}, {1:3}),
        'triangular_prism':({1:4},{-1:1,0:6,1:15,2:6},{1:4}),
        'pentagonal_prism':({3:11},{-1:1,0:10,1:45,2:90,3:75,4:10},{3:11}),
        'durer':({3:3,4:1},{-1:1,0:12,1:66,2:188,3:285,4:204,5:54},{3:4,4:2}),
    }
    for name,(n,edges) in graphs():
        faces=admissible_masks(n,edges)
        pairs,crit=toggle_match(faces,n)
        critical_counts={d:c for d,c in sorted(Counter(s.bit_count()-1 for s in crit).items())}
        full_counts={d:c for d,c in sorted(Counter(s.bit_count()-1 for s in faces).items())}
        exp_hom,exp_f,exp_crit=expect[name]
        assert full_counts==exp_f
        assert critical_counts==exp_crit
        hasse=hasse_acyclic(faces,pairs)
        well=check_wellcovered(n,edges)
        mod2=independent_mod2_betti(faces)
        assert mod2==exp_hom,(name,mod2)
        if name=='durer':
            targets,sources,M=morse_boundary(pairs,crit,3)
            assert len(targets)==4 and len(sources)==2
            assert M==[[-1,0,0,0],[-1,0,0,0]],M
            cancelled=eliminate_matched_pairs(faces,pairs,crit)
            assert [[cancelled[s].get(t,0) for t in targets] for s in sources]==M
            # The integer differential has rank one and a unit minor, so its
            # Smith invariants are (1) and the attaching class is primitive.
            assert any(abs(v)==1 for col in M for v in col)
            # One (3,4)-cell pair cancels; remaining critical CW cells:
            # one 0-cell, three 3-cells, one 4-cell.
        print('%s vertices=%d faces=%d pairs=%d critical=%s hasse=%d maximal_independent_sets=%d size=%d mod2_betti=%s' %
              (name,n,len(faces),len(pairs),critical_counts,hasse,well[0],well[1],mod2))
        if name=='durer':print('durer_signed_Morse_boundary_4_to_3=%s; full_chain_cancellation_agrees=True' % M)
    print('ALL_CHECKS_PASS')

if __name__=='__main__':run()
