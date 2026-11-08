"""Independent coordinate-slot generation and exchange census for saturated rook induced matchings."""
from itertools import permutations,combinations
from collections import deque,Counter
from math import factorial

def configs(n):
    t=n//3
    assert n==3*t
    blocks=set()
    for p in permutations(range(n)):
        singles=tuple(p[:t])
        pairs=tuple(tuple(sorted(p[t+2*i:t+2*i+2])) for i in range(t))
        blocks.add((singles,pairs))
    return sorted(blocks)

def matching(a,b):
    sa,pa=a;sb,pb=b
    hs=[tuple(sorted(((sa[i],pb[i][0]),(sa[i],pb[i][1])))) for i in range(len(sa))]
    vs=[tuple(sorted(((pa[i][0],sb[i]),(pa[i][1],sb[i])))) for i in range(len(sa))]
    return frozenset(hs+vs)

def exchange_neighbours(S,n):
    t=n//3
    H=sorted((e for e in S if e[0][0]==e[1][0]))
    V=sorted((e for e in S if e[0][1]==e[1][1]))
    assert len(H)==len(V)==t
    res=set()
    for x,y in combinations(H,2):
        cols=sorted({v[1] for e in (x,y) for v in e})
        assert len(cols)==4
        for pair in combinations(cols,2):
            r=x[0][0];s=y[0][0]
            X=tuple(sorted(((r,pair[0]),(r,pair[1]))))
            other=sorted(set(cols)-set(pair))
            Y=tuple(sorted(((s,other[0]),(s,other[1]))))
            U=S-{x,y}|{X,Y}
            if U!=S:res.add(U)
    for x,y in combinations(V,2):
        rows=sorted({v[0] for e in (x,y) for v in e})
        assert len(rows)==4
        for pair in combinations(rows,2):
            c=x[0][1];d=y[0][1]
            X=tuple(sorted(((pair[0],c),(pair[1],c))))
            other=sorted(set(rows)-set(pair))
            Y=tuple(sorted(((other[0],d),(other[1],d))))
            U=S-{x,y}|{X,Y}
            if U!=S:res.add(U)
    for x in H:
        for y in V:
            rows=sorted({p[0] for e in (x,y) for p in e})
            cols=sorted({p[1] for e in (x,y) for p in e})
            assert len(rows)==len(cols)==3
            for r in rows:
                for c in cols:
                    rp=sorted(set(rows)-{r});cp=sorted(set(cols)-{c})
                    X=tuple(sorted(((r,cp[0]),(r,cp[1]))))
                    Y=tuple(sorted(((rp[0],c),(rp[1],c))))
                    U=S-{x,y}|{X,Y}
                    if U!=S:res.add(U)
    return res

def validate(S,n):
    E=set()
    for edge in S:
        assert edge[0]!=edge[1]
        u,v=edge
        assert u[0]==v[0] or u[1]==v[1]
        E.update(edge)
    assert len(E)==2*len(S)
    for u,v in combinations(E,2):
        if u[0]==v[0] or u[1]==v[1]:
            assert tuple(sorted((u,v))) in S

def main():
    for t in (1,2):
        n=3*t; blocks=configs(n)
        SS={matching(a,b) for a in blocks for b in blocks}
        pred=(factorial(n)//(2**t*factorial(t)))**2
        assert len(SS)==pred
        degpred=13*t*t-5*t
        for S in SS:
            validate(S,n)
            nei=exchange_neighbours(S,n)
            assert len(nei)==degpred
            assert nei<=SS
            assert all(len(S&N)==2*t-2 for N in nei)
        q=deque([next(iter(SS))]);seen=set(q)
        while q:
            for U in exchange_neighbours(q.popleft(),n):
                if U not in seen:seen.add(U);q.append(U)
        assert seen==SS
        print(f't={t} n={n} coordinate_states={len(SS)} degree={degpred} components=1')
    print('PASS structural verifier')
if __name__=='__main__':main()
