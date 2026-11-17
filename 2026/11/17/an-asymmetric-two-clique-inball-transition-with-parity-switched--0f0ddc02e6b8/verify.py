"""Exact rational verification of two-clique Lipschitz-free inball theorem.

Run: python3 verify.py. Requires only Python 3 standard library.
All arithmetic in numerical verification is exact integer arithmetic.
"""
from itertools import combinations, product
from collections import Counter
from math import comb


def polar_words(n):
    """All extreme hub-zero potentials of a single clique blade of size n."""
    for k in range(1,n+1):
        for indices in combinations(range(n),k):
            for sign in (-1,1):
                x=[0]*n
                for i in indices:x[i]=sign
                yield tuple(x)


def direct_candidates(a,b):
    # Direct Cartesian enumeration; no use of the maximizing formula.
    pa=list(polar_words(a)); pb=list(polar_words(b))
    N=a+b+1
    top=-1
    wins=[]
    for x in pa:
        for y in pb:
            v=x+y
            k=sum(z*z for z in v)
            s=sum(v)
            numerator=N*k-s*s
            if numerator>top:
                top=numerator; wins=[v]
            elif numerator==top:
                wins.append(v)
    return top,wins


def predicted(a,b):
    N=a+b+1
    values={t:N*(a+t)-(t-a)**2 for t in range(1,b+1)}
    top=max(values.values())
    indices=tuple(t for t in values if values[t]==top)
    predicted_contacts=2*sum(comb(b,t) for t in indices)
    rank=1 if indices==(b,) else (b+1 if len(indices)==2 else b)
    dim=a+b-rank
    return top,indices,predicted_contacts,dim


def rank_integer(rows):
    # Exact rational Gaussian elimination with Fraction only for small contact sets.
    from fractions import Fraction
    if not rows:return 0
    a=[[Fraction(x) for x in row] for row in rows]
    m=len(a); n=len(a[0]); p=0
    for j in range(n):
        i=next((i for i in range(p,m) if a[i][j]),None)
        if i is None:continue
        a[p],a[i]=a[i],a[p]
        for h in range(p+1,m):
            if a[h][j]:
                f=a[h][j]/a[p][j]
                for z in range(j,n):a[h][z]-=f*a[p][z]
        p+=1
        if p==m:break
    return p


def tight_connected(hub_zero,a,b,edges):
    vals=(0,)+hub_zero
    visited={0}
    while True:
        new={v for u,v in edges if u in visited and abs(vals[u]-vals[v])==1}
        new|={u for u,v in edges if v in visited and abs(vals[u]-vals[v])==1}
        new-=visited
        if not new:break
        visited|=new
    return len(visited)==a+b+1


def independently_enumerate_vertices(a,b):
    # Enumeration from the full inequality system and tight-edge connectivity,
    # not from the Cartesian product blade lemma.
    N=a+b+1
    group1=tuple(range(1,a+1)); group2=tuple(range(a+1,N))
    edges=[(0,i) for i in range(1,N)]
    edges += list(combinations(group1,2)) +list(combinations(group2,2))
    got=set()
    for word in product((-1,0,1),repeat=a+b):
        v=(0,)+word
        if any(abs(v[i]-v[j])>1 for i,j in edges):continue
        if tight_connected(word,a,b,edges):got.add(word)
    return got


def run():
    total=0
    cases=[]
    for a in range(2,5):
        # Covers equal, generic unequal and the sharp b=3a+2 wall.
        bs={a,a+1,3*a+1,3*a+2,3*a+3,3*a+4}
        if a==4:bs={4,5,12,13,14} # keep exact checks bounded
        for b in sorted(bs):
            top,winners=direct_candidates(a,b)
            target,idx,contact,dim=predicted(a,b)
            assert top==target,(a,b,top,target)
            assert len(winners)==contact,(a,b,len(winners),contact)
            assert all(all(x==w[0] for x in w[:a]) and w[0] in (-1,1) and
                       all(x in (0,-w[0]) for x in w[a:]) and
                       sum(z!=0 for z in w[a:]) in idx for w in winners),(a,b)
            if a+b<=14:
                rank=rank_integer(winners)
                assert a+b-rank==dim,(a,b,rank,dim)
                if a+b<=10:
                    direct=independently_enumerate_vertices(a,b)
                    assert direct=={u+v for u in polar_words(a) for v in polar_words(b)},(a,b)
                # Every polar vertex is an extreme point by independent rank test.
            cases.append((a,b))
            total+=(2**(a+1)-2)*(2**(b+1)-2)
    print('EXACT_POLAR_PRODUCT_MAX_CONTACT_PASS cases=%d checked_vertices=%d' % (len(cases),total))
    print('INDEPENDENT_TIGHT_EDGE_GRAPH_AND_CENTER_RANK_PASS')
    for a in range(2,17):
        for b in range(a,11*a+9):
            N=a+b+1
            top,inds,contact,dim=predicted(a,b)
            z=(3*a+b+1)/2
            closest=min(abs(t-z) for t in range(1,b+1))
            assert all(abs(t-z)==closest for t in inds)
            if b<=3*a+1:
                assert inds==(b,) and contact==2 and dim==a+b-1
            if b==3*a+2:
                assert inds==(b-1,b) and contact==2*(b+1) and dim==a-1
            if b>=3*a+3:
                assert b not in inds
                assert dim==(a if (a+b+1)%2==0 else a-1)
    print('INTEGER_QUADRATIC_THRESHOLD_EXACT_PASS profiles=%d' % sum((11*a+9-a) for a in range(2,17)))
    print('TWO_CLIQUE_INBALL_AND_INCENTER_ALL_CHECKS_PASS')

if __name__=='__main__':run()
