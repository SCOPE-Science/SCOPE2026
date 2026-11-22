"""Standalone exact checks for terminal-diameter-two semi-cutting factorization.
Python 3, standard library only. No external data or dependencies.
"""
from itertools import combinations
from collections import Counter, deque

def product(a,b):
    out=Counter()
    for j,x in a.items():
        for k,y in b.items():out[j+k]+=x*y
    return dict(out)

def local_formula(n, edges, terminals):
    E={tuple(sorted(e)) for e in edges}
    T=set(terminals); U=set(range(n))-T
    eTT=sum(u in T and v in T for u,v in E)
    eUU=sum(u in U and v in U for u,v in E)
    poly={eTT:1}
    for _ in range(eUU):poly=product(poly,{0:1,1:1})
    for v in sorted(U):
        nbr=[u for u in sorted(T) if tuple(sorted((u,v))) in E]
        d=len(nbr); f=Counter()
        for bits in range(1<<d):
            clique=[nbr[k] for k in range(d) if (bits>>k)&1]
            if all(tuple(sorted((a,b))) in E for a,b in combinations(clique,2)):
                f[d-len(clique)]+=1
        poly=product(poly,f)
    return poly

def distance(n,edges,s):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    ds=[n+1]*n;ds[s]=0;queue=deque([s])
    while queue:
        v=queue.popleft()
        for u in adj[v]:
            if ds[u]==n+1:ds[u]=ds[v]+1;queue.append(u)
    return ds

def direct_count(n,edges,terminals):
    T=tuple(terminals);base={t:distance(n,edges,t) for t in T}
    if any(base[a][b]>2 for a,b in combinations(T,2)):return None
    out=Counter()
    for mask in range(1<<len(edges)):
        remain=[e for j,e in enumerate(edges) if not(mask>>j&1)]
        ds={t:distance(n,remain,t) for t in T}
        if all(ds[a][b]>base[a][b] for a,b in combinations(T,2)):
            out[mask.bit_count()]+=1
    return dict(out)

def main():
    checked=0;graphs=0
    for n in range(2,6):
        universe=list(combinations(range(n),2))
        for mask in range(1<<len(universe)):
            E=[e for j,e in enumerate(universe) if (mask>>j)&1]
            graphs+=1
            for tmask in range(1<<n):
                T=[u for u in range(n) if (tmask>>u)&1]
                if len(T)<2:continue
                direct=direct_count(n,E,T)
                if direct is None:continue
                assert direct==local_formula(n,E,T),(n,E,T,direct,local_formula(n,E,T))
                checked+=1
    print('ALL_GRAPHS_TERMINAL_DIAMETER_TWO_DISTANCE_CENSUS_PASS', 'graphs=',graphs,'cases=',checked)
    # Two disjoint 3-cliques with a universal apex; all six clique vertices are terminals.
    E=list(combinations(range(3),2))+list(combinations(range(3,6),2))+[(i,6) for i in range(6)]
    assert local_formula(7,E,range(6))=={9:2,10:6,11:6,12:1}
    # Discriminant of z^3+6z^2+6z+2.
    a,b,c,d=1,6,6,2
    assert b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d==-108
    print('NONREAL_CLIQUE_POLYNOMIAL_WITNESS_PASS')
    # Complete multipartite sample K_(2,3,4), terminal counts (1,2,2).
    parts=(2,3,4); E=[]; groups=[]; pos=0
    for size in parts:groups.append(list(range(pos,pos+size)));pos+=size
    for i,g in enumerate(groups):
        for h in groups[i+1:]:E.extend((u,v) for u in g for v in h)
    T=[0,2,3,5,6]
    P=local_formula(9,E,T)
    expected={13:1}
    for _ in range(8):expected=product(expected,{0:1,1:1})
    for _ in range(5):expected=product(expected,{0:2,1:1})
    assert P==expected,(P,expected)
    print('MULTIPARTITE_COROLLARY_EXACT_SAMPLE_PASS')
    print('VERIFY_OK')
if __name__=='__main__':main()
