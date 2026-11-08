"""Independent finite checks for generalized-theta uniform-spanning-tree leaf law.
Run: python3 verify.py (Python standard library only). These finite checks
supplement, but do not replace, the theorem's all-parameter proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import prod

checks = 0

def assert_equal(x, y):
    global checks
    assert x == y, (x,y)
    checks += 1

def graph(lengths):
    assert all(d>=2 for d in lengths) and len(lengths)>=3
    nxt=2; edges=[]
    for length in lengths:
        prev=0
        for step in range(length-1):
            edges.append((prev,nxt)); prev=nxt; nxt+=1
        edges.append((prev,1))
    return nxt, edges

def brute(lengths):
    n,edges=graph(lengths)
    counts=Counter()
    for mask in combinations(range(len(edges)),n-1):
        parent=list(range(n)); degree=[0]*n
        def root(a):
            while a!=parent[a]: a=parent[a]
            return a
        acyclic=True
        for idx in mask:
            u,v=edges[idx];ru,rv=root(u),root(v)
            if ru==rv: acyclic=False;break
            parent[ru]=rv;degree[u]+=1;degree[v]+=1
        if acyclic and len({root(u) for u in range(n)})==1:
            counts[sum(d==1 for d in degree)]+=1
    return counts

def analytic(lengths):
    k=len(lengths);out=Counter()
    for omitted in range(k):
        coeff={0:1}
        for j,l in enumerate(lengths):
            if j==omitted:continue
            z=Counter()
            for deg,val in coeff.items():
                z[deg+1]+=val*2
                z[deg+2]+=val*(l-2)
            coeff=z
        out.update()  # retain ordinary counts
        for deg,val in coeff.items():out[deg]+=val
    out[k-1]-=2*k;out[k]+=2*k
    return +out

def law(lengths):
    cs=analytic(lengths);tau=sum(cs.values())
    return {degree:Fraction(count,tau) for degree,count in cs.items()}

def auxiliary_law(lengths, a, b):
    S=[j for j in range(len(lengths)) if j not in (a,b)]
    polynomial=Counter()
    for h in S:
        coeff={4:1}
        for j in S:
            if j==h: continue
            nxt=Counter()
            for deg,n in coeff.items():
                nxt[deg+1]+=2*n
                nxt[deg+2]+=(lengths[j]-2)*n
            coeff=nxt
        for deg,n in coeff.items(): polynomial[deg]+=n
    R=sum(polynomial.values())
    return R,{d:Fraction(n,R) for d,n in polynomial.items()}

def cdf_leq(p,m):
    return sum((v for deg,v in p.items() if deg<=m),Fraction(0))

for k in (3,4,5):
    cases=0
    for arr in product(range(2,6),repeat=k):
        if tuple(sorted(arr))!=arr: continue
        p=law(arr)
        assert_equal(sum(p.values()),1)
        tau=sum(prod(arr[j] for j in range(k) if j!=i) for i in range(k))
        assert_equal(sum(analytic(arr).values()),tau)
        for i in range(k):
            for j in range(i+1,k):
                if arr[j]>=arr[i]+2:
                    nxt=list(arr);nxt[j]-=1;nxt[i]+=1
                    q=law(nxt)
                    delta=arr[j]-arr[i]-1
                    R,aux=auxiliary_law(arr,i,j)
                    tau=sum(analytic(arr).values())
                    for d in range(k-1,2*k):
                        assert_equal(q.get(d,0), (tau*p.get(d,0)+delta*R*aux.get(d,0))/(tau+delta*R))
                    for threshold in range(k-2,2*k):
                        assert cdf_leq(q,threshold)<=cdf_leq(p,threshold),(arr,nxt,threshold)
                        checks+=1
        cases+=1
    print('FOSD sample k=',k,'cases=',cases)

for lengths in [(2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,2,4),(2,3,4),
                (2,2,2,2),(2,2,2,3),(2,2,3,3),(2,3,3,3),
                (2,2,2,2,2)]:
    b=brute(lengths);a=analytic(lengths)
    assert_equal(b,a)
    print('ENUM',lengths, dict(sorted(b.items())))

print('VERIFY_OK',checks,'exact assertions')
