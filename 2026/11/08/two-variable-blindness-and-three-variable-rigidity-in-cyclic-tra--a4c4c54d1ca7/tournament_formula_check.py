#!/usr/bin/env python3
"""Direct finite interpretation test of three-variable separating formulas."""
from math import comb, factorial

def canonical(t):
    return min(t,t[1:]+t[:1],t[2:]+t[:2])

def make(t):
    vertex=[(i,r) for i,size in enumerate(t) for r in range(size)]
    N=len(vertex)
    E=[[False]*N for _ in range(N)]
    for u,(i,a) in enumerate(vertex):
        for v,(j,b) in enumerate(vertex):
            E[u][v]=(a<b) if i==j else (j-i)%3==1
    return vertex,E

def cycle(E,u,v,w):
    return E[u][v] and E[v][w] and E[w][u] or E[v][u] and E[u][w] and E[w][v]

def check(t):
    vertices,E=make(t);N=len(E)
    S=[[u==v or not any(cycle(E,u,v,w) for w in range(N)) for v in range(N)] for u in range(N)]
    pair_checks=0;cyclic_checks=0;threshold_checks=0
    for u,(i,r) in enumerate(vertices):
        for v,(j,s) in enumerate(vertices):
            assert S[u][v] == (i==j), (t,u,v,'same_block')
            pair_checks+=1
            for w,(h,z) in enumerate(vertices):
                # A cyclic triangle is exactly one vertex from each of the three blocks.
                expected=(len({i,j,h})==3)
                assert cycle(E,u,v,w)==expected,(t,u,v,w,'three_cycle')
                cyclic_checks+=1
    D=[[E[u][v] and S[u][v] for v in range(N)] for u in range(N)]
    # P_m(v) means a D-directed path of m edges starts at v.
    P=[[True]*N]
    for m in range(1,N+1):
        P.append([any(D[u][v] and P[-1][v] for v in range(N)) for u in range(N)])
    for u,(i,r) in enumerate(vertices):
        for h in range(1,N+2):
            H=(True if h==1 else any(S[u][v] and P[h-1][v] for v in range(N)))
            assert H==(t[i]>=h),(t,u,h,'block_threshold')
            threshold_checks+=1
    # B_s(u) = H_s(u) and not H_{s+1}(u) gives the exact block size.
    return pair_checks,cyclic_checks,threshold_checks

def is_family(E):
    n=len(E)
    S=[[u==v or not any(cycle(E,u,v,w) for w in range(n)) for v in range(n)] for u in range(n)]
    classes=[];used=set()
    for x in range(n):
        if x not in used:
            C=frozenset(v for v in range(n) if S[x][v]);classes.append(C);used.update(C)
    if len(classes)!=3 or sum(map(len,classes))!=n: return False
    if any((S[u][v]!=(any(u in C and v in C for C in classes))) for u in range(n) for v in range(n)):
        return False
    for C in classes:
        if any(cycle(E,x,y,z) for x in C for y in C for z in C):return False
    # Quotient must be a directed triangle, not a transitive tournament.
    a,b,c=[next(iter(C)) for C in classes]
    return cycle(E,a,b,c)

def labelled_tournament_count(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    count=0
    for mask in range(1<<len(edges)):
        E=[[False]*n for _ in range(n)]
        for k,(i,j) in enumerate(edges):
            E[i][j]=bool(mask & (1<<k));E[j][i]=not E[i][j]
        count+=is_family(E)
    expected=factorial(n)*comb(n-1,2)//3
    assert count==expected,(n,count,expected)
    return count

if __name__=='__main__':
    checks=[0,0,0]
    total=0
    for n in range(3,15):
        raw=[(a,b,n-a-b) for a in range(1,n-1) for b in range(1,n-a)]
        distinct={canonical(t) for t in raw}
        expected=(comb(n-1,2)+2*int(n%3==0))//3
        assert len(distinct)==expected,(n,len(distinct),expected)
        for t in raw:
            c=check(t);checks=[a+b for a,b in zip(checks,c)];total+=1
    print('all_positive_compositions',total,'orders',3,14)
    print('same_block_pair_checks',checks[0])
    print('directed_cycle_triple_checks',checks[1])
    print('three_variable_threshold_checks',checks[2])
    print('cyclic_orbit_count_orders',12)
    print('labelled_counts',[(n,labelled_tournament_count(n)) for n in range(3,7)])
    print('DIRECT_FORMULA_OK')
