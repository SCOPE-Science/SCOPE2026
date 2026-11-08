"""Exact finite-field verification of graph-period diagonal Rota--Baxter count."""
from itertools import product
from math import gcd

FIELDS=[(2,0),(3,0),(4,0b111),(5,0),(7,0),(8,0b1011)]

def add(a,b,q):
    return a^b if q in (2,4,8) else (a+b)%q

def mul(a,b,q,poly):
    if poly == 0:
        return a*b%q
    acc=0
    while b:
        if b&1: acc^=a
        b>>=1
        a<<=1
        if a&q: a^=poly
    return acc

def strong(n,edges):
    for a in range(n):
        visited={a}
        for _ in range(n):
            visited|={j for i,j in edges if i in visited}
        if len(visited)!=n: return False
    return True

def period(n,edges):
    d=[-1]*n;d[0]=0
    for _ in range(n):
        for i,j in edges:
            if d[i]>=0 and d[j]<0: d[j]=d[i]+1
    g=0
    for i,j in edges: g=gcd(g,d[i]+1-d[j])
    return abs(g)

def independent_cycle_period(n, edges):
    by_vertex = {v: [w for a,w in edges if a==v] for v in range(n)}
    g = 0
    def visit(start, pos, visited, length):
        nonlocal g
        for nxt in by_vertex[pos]:
            if nxt == start:
                g = gcd(g, length + 1)
            elif nxt not in visited:
                visit(start, nxt, visited | {nxt}, length + 1)
    for start in range(n): visit(start, start, {start}, 0)
    return g

def checker():
    for q,poly in FIELDS:
        for a in range(1,q):
            assert set(mul(a,b,q,poly) for b in range(q)) == set(range(q))
    configurations=0
    matrices=0
    candidate_maps=0
    witnesses=[]
    for n in range(1,4):
        for mask in range(1,2**(n*n)):
            edges=[(i,j) for i in range(n) for j in range(n) if mask&(1<<(n*i+j))]
            if not strong(n,edges):continue
            d=period(n,edges)
            assert d>=1 and d==independent_cycle_period(n,edges)
            for q,poly in FIELDS:
                count=0
                for r in product(range(q),repeat=n):
                    candidate_maps+=1
                    if all(mul(r[i],r[i],q,poly)==mul(add(add(r[i],r[i],q),1,q),r[j],q,poly) for i,j in edges):count+=1
                expected=1+gcd(2**d-1,q-1)
                assert count==expected, (n,mask,q,d,count,expected)
                configurations+=1
                matrices+=len(edges)
                if n==d and all((i,(i+1)%n) in edges for i in range(n)) and len(edges)==n and q in (4,8):
                    witnesses.append((n,q,d,count))
    # Complete bipartite 2+2: a non-monomial invertible structure matrix over GF(4).
    q,poly=4,0b111
    a=[[0,0,1,1],[0,0,1,2],[1,1,0,0],[1,2,0,0]]
    assert add(mul(1,2,q,poly),mul(1,1,q,poly),q)!=0
    count=0;nonconstant=[]
    for r in product(range(q),repeat=4):
        candidate_maps+=1
        if all(mul(a[i][j],mul(r[i],r[i],q,poly),q,poly)==mul(a[i][j],mul(add(add(r[i],r[i],q),1,q),r[j],q,poly),q,poly) for i in range(4) for j in range(4)):
            count+=1
            if len(set(r))>1: nonconstant.append(r)
    assert count==4 and len(nonconstant)==2
    print(f'VERIFY_OK configurations={configurations} tested_directed_edges={matrices} maps={candidate_maps} dense_perfect_example={count}')
    print('SIMPLE_CYCLE_CASES',witnesses)
    e0={(0,1),(1,2),(2,0)}
    e1=e0|{(1,0)}
    totals=[]
    for edges in (e0,e1):
        assert strong(3,edges)
        d=period(3,edges)
        count=sum(all(mul(r[i],r[i],8,0b1011)==mul(add(add(r[i],r[i],8),1,8),r[j],8,0b1011) for i,j in edges) for r in product(range(8),repeat=3))
        assert count==1+gcd(2**d-1,7)
        totals.append((d,count))
    assert totals==[(3,8),(1,2)]
    print('EDGE_COLLAPSE_GF8',totals)


if __name__=='__main__': checker()
