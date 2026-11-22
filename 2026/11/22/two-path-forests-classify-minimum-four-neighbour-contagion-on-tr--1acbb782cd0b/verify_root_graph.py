"""Independent root-graph threshold check, optimum families, and exchange graph.
Run: python3 verify_root_graph.py
"""
from itertools import combinations, permutations
from collections import Counter, deque
from math import comb

def steps(n, chosen, edges):
    have=set(chosen)
    time=0
    while True:
        deg=[0]*n
        for i in have:
            a,b=edges[i];deg[a]+=1;deg[b]+=1
        add={i for i,(a,b) in enumerate(edges) if i not in have and deg[a]+deg[b]>=4}
        if not add:break
        have.update(add);time+=1
    return len(have)==len(edges),time

def make_expected(n, edges):
    labels={e:i for i,e in enumerate(edges)}
    families={}
    for v5 in combinations(range(n),5):
        for path in permutations(v5):
            x=frozenset(labels[tuple(sorted((a,b)))] for a,b in zip(path,path[1:]))
            families[x]='P5'
    for v6 in combinations(range(n),6):
        for centers in combinations(v6,2):
            rem=sorted(set(v6)-set(centers))
            for left in combinations(rem,2):
                right=sorted(set(rem)-set(left))
                chosen=[(centers[0],a) for a in left]+[(centers[1],b) for b in right]
                x=frozenset(labels[tuple(sorted(e))] for e in chosen)
                families[x]='2P3'
    return families

def neighbors(s, universe, m):
    for removed in s:
        rest=s-{removed}
        for new in range(m):
            if new not in s:
                candidate=rest|{new}
                if candidate in universe:yield candidate

for n in range(5,9):
    edges=list(combinations(range(n),2))
    predicted=make_expected(n,edges)
    observed={}
    for indices in combinations(range(len(edges)),4):
        works, t=steps(n,indices,edges)
        if works: observed[frozenset(indices)]=t
    assert set(predicted)==set(observed)
    expected_path=60*comb(n,5)
    expected_pair=90*comb(n,6) if n>=6 else 0
    assert Counter(predicted.values())=={'P5':expected_path,**({'2P3':expected_pair} if n>=6 else {})}
    assert Counter(observed.values())==({3:60} if n==5 else ({3:90,4:360} if n==6 else {4:len(observed)}))
    deg_by_shape=Counter();visited=set();sizes=[];edges_twice=0
    for v in predicted:
        nbs=set(neighbors(v,predicted,len(edges)))
        deg=len(nbs);edges_twice+=deg
        deg_by_shape[(predicted[v],deg)]+=1
        if predicted[v]=='P5':assert deg==8*(n-4)
        else:assert deg==8*n-28
        if v not in visited:
            queue=deque([v]);visited.add(v);size=0
            while queue:
                w=queue.popleft();size+=1
                for nxt in neighbors(w,predicted,len(edges)):
                    if nxt not in visited:
                        visited.add(nxt);queue.append(nxt)
            sizes.append(size)
    assert sizes==[len(predicted)]
    edge_formula=4*(n-4)*expected_path+(4*n-14)*expected_pair
    assert edges_twice//2==edge_formula
    print(f'n={n} count={len(predicted)} path={expected_path} two_paths={expected_pair} time={dict(Counter(observed.values()))} edges={edge_formula} degree={dict(deg_by_shape)} connected=PASS')
