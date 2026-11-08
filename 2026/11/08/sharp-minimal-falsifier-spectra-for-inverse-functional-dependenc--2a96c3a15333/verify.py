"""Independent finite checks for obstruction spectra of inverse dependence.
Run: python verify.py   (standard library only)
"""
from collections import Counter
from itertools import combinations


def team_semantics(edges, p, q):
    """Brute-force disjoint witnesses, no pseudoforest characterization used."""
    E = list(edges)
    for choices in range(1 << len(E)):
        left_seen, right_seen = {}, {}
        good = True
        for k, (a,b) in enumerate(E):
            if choices & (1 << k):
                if b in right_seen and right_seen[b] != a: good=False; break
                right_seen[b]=a
            else:
                if a in left_seen and left_seen[a] != b: good=False; break
                left_seen[a]=b
        if good: return True
    return False


def pseudoforest(mask,p,q):
    parent=list(range(p+q)); sizes=[1]*(p+q); e=[0]*(p+q)
    def find(a):
        while a!=parent[a]:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    for a in range(p):
        for b in range(q):
            if (mask>>(a*q+b))&1:
                x,y=find(a),find(p+b)
                if x==y:e[x]+=1
                else:
                    if sizes[x]<sizes[y]:x,y=y,x
                    parent[y]=x;sizes[x]+=sizes[y];e[x]+=e[y]+1
    return all(e[i]<=sizes[i] for i in range(p+q) if parent[i]==i)


def predicted(p,q):
    if min(p,q)<=1 or p==q==2:return set()
    m=min(p,q)
    top=2*m+1 if p==q else 2*m+2
    return set(range(6,top+1))


def enumerate_minimal(p,q):
    n=p*q
    good=[pseudoforest(x,p,q) for x in range(1<<n)]
    mult=Counter()
    for mask in range(1<<n):
        if not good[mask] and all(good[mask^(1<<i)] for i in range(n) if mask & (1<<i)):
            mult[mask.bit_count()]+=1
    return mult


def run():
    semantic_teams=0
    for p,q in [(1,3),(2,2),(2,3),(2,4),(3,3),(3,4)]:
        for mask in range(1<<(p*q)):
            edges=[(i,j) for i in range(p) for j in range(q) if mask>>(i*q+j)&1]
            assert team_semantics(edges,p,q)==pseudoforest(mask,p,q),(p,q,mask)
            semantic_teams+=1
    print('direct team-semantics comparisons',semantic_teams)
    from math import comb
    for p,q in [(1,5),(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)]:
        c=enumerate_minimal(p,q)
        assert set(c)==predicted(p,q), (p,q,c,predicted(p,q))
        assert c.get(6,0)==comb(p,2)*comb(q,3)+comb(p,3)*comb(q,2) if p>=2 and q>=2 else not c
        assert c.get(7,0)==18*comb(p,3)*comb(q,3) if p>=3 and q>=3 else c.get(7,0)==0
        print(f'{p}x{q}:',dict(sorted(c.items())))
    print('all checks passed')

if __name__=='__main__':run()
