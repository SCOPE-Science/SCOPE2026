"""Exact checks for motif--isolation covariances in fixed-edge random graphs.

Run: python3 verify.py
All calculations use the Python standard library and exact rational arithmetic.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def fall(x,r):
    z=1
    for j in range(r):z*=x-j
    return z


def copies(n,kind):
    edges=list(combinations(range(n),2)); idx={e:i for i,e in enumerate(edges)}
    cp=set()
    if kind=='wedge':
        for c in range(n):
            for a,b in combinations([u for u in range(n) if u!=c],2):
                cp.add(frozenset([idx[tuple(sorted((a,c)))],idx[tuple(sorted((b,c)))]]))
    elif kind=='matching2':
        for v in combinations(range(n),4):
            for a,b in combinations(v,2):
                remain=tuple(x for x in v if x!=a and x!=b)
                cp.add(frozenset([idx[(a,b)],idx[remain]]))
    elif kind=='wedge_plus_edge':
        for v in combinations(range(n),5):
            for c in v:
                for a,b in combinations([x for x in v if x!=c],2):
                    remain=tuple(sorted(set(v)-{a,b,c}))
                    cp.add(frozenset([idx[tuple(sorted((a,c)))],idx[tuple(sorted((b,c)))],idx[remain]]))
    else:raise ValueError(kind)
    return edges,cp


def theoretical(n,m,k,e,number_copies):
    N=comb(n,2);B=comb(n-1,2)
    mean_i=Fraction(n*comb(B,m),comb(N,m))
    mean_h=Fraction(number_copies*fall(m,e),fall(N,e))
    ratio=Fraction(n-k,n)*Fraction(fall(N,e),fall(B,e))
    return mean_i*mean_h*(ratio-1)


def exhaustive(n,kind,k,e):
    edges,cp=copies(n,kind)
    total=0;checks=0
    for m in range(e,comb(n-1,2)+1):
        count=comb(len(edges),m);si=sh=sih=0
        for draw in combinations(range(len(edges)),m):
            deg=[0]*n
            for z in draw:
                a,b=edges[z];deg[a]+=1;deg[b]+=1
            num_iso=deg.count(0);present=set(draw)
            num_motif=sum(1 for q in cp if q.issubset(present))
            si+=num_iso;sh+=num_motif;sih+=num_iso*num_motif
        mean_i=Fraction(si,count);mean_h=Fraction(sh,count)
        cov=Fraction(sih,count)-mean_i*mean_h
        assert cov==theoretical(n,m,k,e,len(cp)),(n,m,kind,cov)
        assert mean_i==Fraction(n*comb(comb(n-1,2),m),comb(comb(n,2),m))
        assert mean_h==Fraction(len(cp)*fall(m,e),fall(comb(n,2),e))
        total+=count;checks+=3
    return total,checks


def check():
    cases=[(5,'wedge',3,2),(5,'matching2',4,2),(6,'wedge_plus_edge',5,3)]
    graph_total=checks=0
    for n,kind,k,e in cases:
        g,c=exhaustive(n,kind,k,e)
        graph_total+=g;checks+=c
    for n in range(5,101):
        N=comb(n,2);B=comb(n-1,2)
        for k,e in [(3,2),(4,2),(5,3)]:
            if n<=k or e>B:continue
            delta=(n-k)*fall(N,e)-n*fall(B,e)
            assert (delta>0 if (k,e)==(3,2) else delta<0 if (k,e)==(4,2) else delta>0 if n>=11 else delta<0)
            checks+=1
            if (k,e)==(5,3):
                cubic=n**3-12*n*n+15*n+20
                assert 8*delta==n*(n-1)*(n-2)*cubic
                checks+=1
    print('VERIFY_OK',graph_total,'exhaustively enumerated fixed-edge graphs;',checks,'exact checks')

if __name__=='__main__':check()
