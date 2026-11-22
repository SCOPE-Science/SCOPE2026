#!/usr/bin/env python3
"""Independently enumerate normalized enriched-nerve chains at length two.
Run: python3 verify_quadfree.py
"""
import itertools

def rank_mod2(vectors):
    piv={}
    for z in vectors:
        while z:
            p=z.bit_length()-1
            if p not in piv:
                piv[p]=z; break
            z^=piv[p]
    return len(piv)

def graph_stats(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    seen={0}; stack=[0]
    while stack:
        for u in adj[stack.pop()]:
            if u not in seen: seen.add(u); stack.append(u)
    if len(seen)<n: return None
    quad=any(len(adj[a]&adj[b])>=2 for a in range(n) for b in range(a+1,n))
    if quad: return None
    tri=sum(len(adj[a]&adj[b]) for a,b in edges)//3
    pairs=set(edges)
    for a in range(n):
        for b in adj[a]:
            for c in adj[b]:
                if a!=c: pairs.add(tuple(sorted((a,c))))
    cells1=sorted((a,b) for a,b in itertools.permutations(range(n),2) if tuple(sorted((a,b))) in pairs)
    index={x:i for i,x in enumerate(cells1)}
    columns=[]
    for a in range(n):
        for b in adj[a]:
            for c in adj[b]:
                bits=(1<<index[(a,b)])^(1<<index[(b,c)])
                if a!=c:bits ^=1<<index[(a,c)]
                columns.append(bits)
    r=rank_mod2(columns)
    b1=len(cells1)-(n-1)-r
    b2=len(columns)-r
    return (b1,b2,tri,len(edges),len(cells1),len(columns),r)

def main():
    total=0;counts=[]
    for n in range(2,7):
        ee=list(itertools.combinations(range(n),2))
        accepted=0
        for mask in range(1<<len(ee)):
            E=[e for j,e in enumerate(ee) if mask>>j&1]
            s=graph_stats(n,E)
            if s is None:continue
            b1,b2,t,e,c1,c2,r=s
            assert b1==e-n+1-t and b2==e+5*t, (n,E,s)
            accepted+=1
        total+=accepted
        counts.append((n,accepted))
    print('All connected four-cycle-free labeled graphs on 2..6 vertices:',counts)
    print('Total independently checked:', total)
    for n,E in [(3,[(0,1),(1,2),(0,2)]),(5,[(0,1),(1,2),(2,3),(3,4),(0,4)]),(6,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,5)])]:
        print('Example',n,E,graph_stats(n,E))

if __name__=='__main__':main()
