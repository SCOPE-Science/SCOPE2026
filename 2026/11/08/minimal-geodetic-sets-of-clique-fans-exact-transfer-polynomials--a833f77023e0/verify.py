#!/usr/bin/env python3
"""Independent checks of minimal geodetic sets of clique fans.
Uses shortest-path distances directly; no third-party dependencies.
"""
from collections import Counter, deque, defaultdict
from itertools import product


def graph(n, m):
    vertices = [('hub', -1)] + [(i, j) for i in range(n) for j in range(m)]
    adj = [set() for _ in vertices]
    for i in range(len(vertices)):
        for j in range(i):
            a, b = vertices[i], vertices[j]
            if i == 0 or j == 0 or abs(a[0] - b[0]) <= 1:
                adj[i].add(j)
                adj[j].add(i)
    return vertices, adj


def dists(adj):
    dist=[]
    for i in range(len(adj)):
        d=[None]*len(adj)
        d[i]=0
        todo=deque([i])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if d[w] is None:
                    d[w]=d[v]+1;todo.append(w)
        dist.append(d)
    return dist


def bmask(n, m, mask):
    counts=[((mask >> (1+i*m)) & ((1<<m)-1)).bit_count() for i in range(n)]
    return counts


def expected(n, m, mask):
    if mask & 1:
        return False
    s=bmask(n,m,mask)
    if s[0] != m or s[-1] != m:
        return False
    for i in range(1,n-1):
        u,v=s[i-1],s[i+1]
        if s[i]==0 and (u!=m or v!=m):return False
        if s[i]==m and u>0 and v>0:return False
        if 1<s[i]<m:return False
        if s[i]==1 and s[i]<m:
            if not (u>0 and v>0 and (u<m or v<m)):return False
    return True


def predicted_geodetic(n,m,mask):
    s=bmask(n,m,mask)
    return s[0]==m and s[-1]==m and all(s[i]==m or (s[i-1]>0 and s[i+1]>0) for i in range(1,n-1))


def brute(n,m):
    vertices, adj = graph(n,m)
    d = dists(adj)
    full=(1<<len(vertices))-1
    pairs=[(u,v,sum(1<<w for w in range(len(vertices)) if d[u][w]+d[w][v]==d[u][v])) for u in range(len(vertices)) for v in range(u+1,len(vertices))]
    # Independently form each geodesic closure from distances, no state-word shortcuts.
    geos=[]
    for mask in range(1<<len(vertices)):
        cover=mask
        for u,v,between in pairs:
            if ((mask>>u)&1) and ((mask>>v)&1):cover|=between
        geos.append(cover == full)
    assert all(geos[mask] == predicted_geodetic(n,m,mask) for mask in range(len(geos))), ('geodetic',n,m)
    observed=Counter()
    minimal=0
    for mask,yes in enumerate(geos):
        if yes and not any(geos[mask ^ (1<<j)] for j in range(len(vertices)) if (mask>>j)&1):
            minimal+=1
            observed[mask.bit_count()]+=1
            assert expected(n,m,mask),('missing expected',n,m,mask)
        elif expected(n,m,mask):
            raise AssertionError(('false predicted minimal',n,m,mask))
    return len(geos), minimal, observed


def transfer(n,m):
    W={'F':m,'Z':0,'P':1}
    C={'F':1,'Z':1,'P':m}
    states=('F','Z','P')
    # DP over two consecutive statuses; certify each preceding middle vertex.
    dp={('F',b):Counter({m+W[b]:C[b]}) for b in states}
    for _ in range(2,n):
        nxt=defaultdict(Counter)
        for (a,b),poly in dp.items():
            for c in states:
                valid = ((a=='F' and c=='F') if b=='Z' else
                         (a=='Z' or c=='Z') if b=='F' else
                         (a!='Z' and c!='Z' and (a=='P' or c=='P')))
                if not valid:continue
                out=nxt[(b,c)]
                for degree,count in poly.items():out[degree+W[c]]+=count*C[c]
        dp=nxt
    result=Counter()
    for (a,b),poly in dp.items():
        if b=='F':result.update(poly)
    return +result

if __name__ == '__main__':
    profiles=[(n,2) for n in range(3,9)]+[(n,3) for n in range(3,6)]+[(n,4) for n in range(3,5)]
    masks=minsets=0
    for n,m in profiles:
        subsets,count,observed=brute(n,m)
        masks+=subsets;minsets+=count
        assert observed==transfer(n,m),(n,m,observed,transfer(n,m))
    # Polynomial dynamical evaluation, including large orders beyond exhaustive checks.
    for m in range(2,7):
        for n in range(3,36):
            poly=transfer(n,m)
            assert bool(poly)
            pure=(len(poly)==1)
            assert pure == (n==3 or (m==2 and n in (4,6))), ('purity',n,m,poly)
    print('VERIFY_OK graph_profiles=%d full_subsets=%d minimal_sets=%d original_distance_geodesics=PASS exact_three_state_classification=PASS transfer_polynomials=PASS purity_n3to35_m2to6=PASS' %(len(profiles),masks,minsets))
