#!/usr/bin/env python3
"""Exact finite cross-checks for odd-square numerical semigroup identities."""
from heapq import heappush, heappop

def formula(n):
    assert n >= 7 and n % 2 == 1
    a, b, c = n*n, (n+2)**2, (n+4)**2
    assert (n+2)*b == ((n+1)//2)*c + ((n+3)//2)*a
    assert (n+2)*c == 8*b + (n+2)*a
    assert (n-6)*b + ((n+3)//2)*c == ((3*n+7)//2)*a
    T=[(x,y) for x in range(n+2) for y in range(n+2)
        if not(x>=n-6 and y>=(n+3)//2)]
    assert len(T)==a
    Ws={ (x*b+y*c)%a: x*b+y*c for x,y in T}
    assert len(Ws)==a
    PF={ (n-7)*b+(n+1)*c-a,
        (n+1)*b+((n+1)//2)*c-a }
    Fs=max(PF)
    G=(n+1)*(2*n*n+5*n+7)//2
    assert (sum(Ws.values())//a)-(a-1)//2==G
    return a,b,c,Ws,PF,Fs,G

def independent_shortest_path(a,b,c):
    dist=[None]*a
    dist[0]=0
    Q=[(0,0)]
    while Q:
        value,r=heappop(Q)
        if value != dist[r]:
            continue
        for v in (b,c):
            newr=(r+v)%a
            newv=value+v
            if dist[newr] is None or dist[newr]>newv:
                dist[newr]=newv
                heappush(Q,(newv,newr))
    assert all(v is not None for v in dist)
    return dist

def verify(n):
    a,b,c,Ws,PF,F,G=formula(n)
    dist=independent_shortest_path(a,b,c)
    assert dist == [Ws[r] for r in range(a)], ('Apery',n)
    actual_pf={v-a for v in dist if all((v+d)>dist[(v+d)%a] for d in (b,c))}
    assert PF==actual_pf, ('PF',n,actual_pf,PF)
    assert max(dist)-a==F
    assert sum(dist)//a-(a-1)//2 ==G
    return F,G,PF

if __name__=='__main__':
    cases=list(range(7,100,2)) + [101,127,151,201,251]
    for n in cases:
        verify(n)
    print('APERY_PF_FROBENIUS_GENUS_EXACT_OK',len(cases),'n_min',min(cases),'n_max',max(cases))
    for n in [7,9,11,13,15,101]:
        F,G,PF=verify(n)
        print('SAMPLE',n,'F',F,'genus',G,'pseudo_frobenius',sorted(PF))
    print('INFINITE_PROOF_SEPARATE=True INDEPENDENT_AUDIT=False')
