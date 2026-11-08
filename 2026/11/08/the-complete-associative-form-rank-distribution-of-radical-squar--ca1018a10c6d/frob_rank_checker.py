"""Direct rank calculations for associative multiplication forms on small quiver algebras."""
from itertools import product
from collections import Counter


def rank_mod(A,q):
    a=[row[:] for row in A]
    m=len(a);n=len(a[0]);h=0
    for j in range(n):
        pivot=next((i for i in range(h,m) if a[i][j]%q),None)
        if pivot is None:continue
        a[h],a[pivot]=a[pivot],a[h]
        inv=pow(a[h][j],-1,q)
        a[h]=[x*inv%q for x in a[h]]
        for i in range(m):
            if i!=h and a[i][j]%q:
                z=a[i][j]
                a[i]=[(x-z*y)%q for x,y in zip(a[i],a[h])]
        h+=1
        if h==m:break
    return h


def direct(n,edges,q):
    m=len(edges);ans=Counter()
    for vals in product(range(q),repeat=n+m):
        d=vals[:n]; c=vals[n:];A=[[0]*(n+m) for _ in range(n+m)]
        for i in range(n):A[i][i]=d[i]
        for ai,(s,t) in enumerate(edges):
            A[s][n+ai]=c[ai]
            A[n+ai][t]=c[ai]
        ans[rank_mod(A,q)]+=1
    return ans


def expected(n,edges,q):
    m=len(edges);r=Counter()
    for support in product((0,1),repeat=m):
        S={edges[i][0] for i in range(m) if support[i]}
        T={edges[i][1] for i in range(m) if support[i]}
        covered=S|T
        wt=(q-1)**sum(support)*q**len(covered)
        un=n-len(covered)
        for dmask in product((0,1),repeat=un):
            r[len(S)+len(T)+sum(dmask)]+=wt*(q-1)**sum(dmask)
    return r

cases=[
(1,[]), (1,[(0,0)]), (1,[(0,0),(0,0)]),
(2,[(0,1)]),(2,[(0,1),(1,0)]),(2,[(0,1),(0,1)]),
(2,[(0,0),(0,1)]),(2,[(0,0),(1,1)]),
(3,[(0,1),(1,2)]),(3,[(0,1),(1,2),(2,0)]),
(3,[(0,1),(0,2)]),(3,[(0,1),(1,2),(1,0)]),
(3,[(0,0),(0,1),(2,1)]),
]
checks=0
for n,E in cases:
    for q in [2,3]:
        if q**(n+len(E))>200000:continue
        obs=direct(n,E,q);exp=expected(n,E,q)
        assert obs==exp, (n,E,q,obs,exp)
        assert sum(obs.values())==q**(n+len(E))
        print(f'PASS n={n} edges={E} q={q} ranks={dict(sorted(obs.items()))}')
        checks+=1
assert checks>=20
print('ALL_FROBENIUS_RANK_CHECKS_PASS',checks)
