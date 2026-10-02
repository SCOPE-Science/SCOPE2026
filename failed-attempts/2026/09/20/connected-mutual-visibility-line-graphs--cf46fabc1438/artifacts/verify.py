#!/usr/bin/env python3
from itertools import combinations
from collections import deque
from math import floor


def line_adj(e, f):
    return bool(set(e) & set(f))


def connected_selected(selected):
    if not selected:
        return False
    seen = {0}
    q = deque([0])
    while q:
        i = q.popleft()
        for j in range(len(selected)):
            if j not in seen and line_adj(selected[i], selected[j]):
                seen.add(j); q.append(j)
    return len(seen) == len(selected)


def mv_complete(selected):
    S = set(selected)
    for e, f in combinations(selected, 2):
        if line_adj(e, f):
            continue
        a,b = e; c,d = f
        connectors = {(min(x,y), max(x,y)) for x in (a,b) for y in (c,d)}
        if connectors <= S:
            return False
    return True


def mv_bipartite(selected):
    S = set(selected)
    for e, f in combinations(selected, 2):
        if line_adj(e, f):
            continue
        a,b = e; c,d = f
        # edges encoded (left,right)
        if (a,d) in S and (c,b) in S:
            return False
    return True


def analyze_complete(n):
    host = list(combinations(range(n),2))
    mv_masks=[]
    best=best_conn=0
    for mask in range(1 << len(host)):
        selected=[host[i] for i in range(len(host)) if mask>>i & 1]
        if not mv_complete(selected):
            continue
        mv_masks.append(mask)
        best=max(best,len(selected))
        if selected and connected_selected(selected):
            best_conn=max(best_conn,len(selected))
    maximal=[]
    for mask in mv_masks:
        if all(((mask>>i)&1) or not mv_complete([host[j] for j in range(len(host)) if ((mask | (1<<i))>>j)&1]) for i in range(len(host))):
            maximal.append(mask)
    disconnected=[]
    for mask in maximal:
        selected=[host[i] for i in range(len(host)) if mask>>i & 1]
        if not connected_selected(selected): disconnected.append(mask)
    return best,best_conn,len(maximal),len(disconnected)


def analyze_bipartite(m,n):
    host=[(i,j) for i in range(m) for j in range(n)]
    mv_masks=[]
    best=best_conn=0
    for mask in range(1 << len(host)):
        selected=[host[i] for i in range(len(host)) if mask>>i & 1]
        if not mv_bipartite(selected):
            continue
        mv_masks.append(mask)
        best=max(best,len(selected))
        if selected and connected_selected(selected):
            best_conn=max(best_conn,len(selected))
    maximal=[]
    for mask in mv_masks:
        ok=True
        for i in range(len(host)):
            if not (mask>>i)&1:
                sel=[host[j] for j in range(len(host)) if ((mask | (1<<i))>>j)&1]
                if mv_bipartite(sel):
                    ok=False; break
        if ok: maximal.append(mask)
    disconnected=[]
    for mask in maximal:
        selected=[host[i] for i in range(len(host)) if mask>>i & 1]
        if not connected_selected(selected): disconnected.append(mask)
    return best,best_conn,len(maximal),len(disconnected)

print('Complete hosts K_n / line graphs L(K_n)')
for n in range(3,7):
    a=analyze_complete(n)
    print(f'n={n}: mu={a[0]}, mu_c={a[1]}, maximal={a[2]}, disconnected_maximal={a[3]}, floor(n^2/3)={floor(n*n/3)}')
    assert a[0]==a[1]==floor(n*n/3) and a[3]==0

print('\nComplete bipartite hosts K_{m,n} / rook graphs')
for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
    a=analyze_bipartite(m,n)
    print(f'({m},{n}): mu={a[0]}, mu_c={a[1]}, maximal={a[2]}, disconnected_maximal={a[3]}')
    assert a[0]==a[1] and a[3]==0

print('\nAll checks passed.')
