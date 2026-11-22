"""Direct graph-product census for corank-two Motzkin diagrams.
Run: python motzkin_product_checker.py
All calculations are exact integer arithmetic.
"""
from itertools import combinations, product
from collections import Counter
from math import comb


def elements(n):
    pts=set(range(n))
    choices=[]
    for pair in combinations(range(n),2):
        h=[False,True] if pair[1]==pair[0]+1 else [False]
        for hook in h:
            choices.append((tuple(pair),hook))
    for upper,lower in product(choices,repeat=2):
        a,ha=upper; b,hb=lower
        U=sorted(pts-set(a)); V=sorted(pts-set(b))
        edges=[(u,n+v) for u,v in zip(U,V)]
        if ha: edges.append((a[0],a[1]))
        if hb: edges.append((n+b[0],n+b[1]))
        yield tuple(edges)


def product_invariants(n,alpha,beta):
    # Top alpha: 0..n-1; glued middle n..2n-1; bottom beta: 2n..3n-1
    edges=list(alpha)+[(n+a if a<n else 2*n+(a-n), n+b if b<n else 2*n+(b-n)) for a,b in beta]
    parent=list(range(3*n)); degree=[0]*(3*n)
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for x,y in edges:
        degree[x]+=1;degree[y]+=1
        rx,ry=root(x),root(y)
        if rx!=ry: parent[ry]=rx
    c={}
    for x in range(3*n): c.setdefault(root(x),[]).append(x)
    rank=loops=paths=0
    for vertices in c.values():
        top=any(x<n for x in vertices)
        bottom=any(x>=2*n for x in vertices)
        if top and bottom:
            rank+=1
        elif not top and not bottom:
            if all(degree[x]==2 for x in vertices): loops+=1
            else: paths+=1
    return rank,paths,loops


def theory(n):
    W=(n-1)*(n+2)//2
    result=Counter()
    if n>=4:
        result[(n-4,0,0)]=W*W*n*(n+3)*(n-2)*(n-3)//4
    result[(n-3,1,0)]=W*W*n*(n-1)*(n-2)
    result[(n-3,0,0)]=W*W*4*(n-1)*(n-2)
    result[(n-2,2,0)]=W*W*comb(n,2)
    result[(n-2,1,0)]=W*W*2*(n-1)
    result[(n-2,0,1)]=W*W*(n-1)
    result[(n-2,0,0)]=W*W*2*(n-2)
    return +result


def check(n):
    seq=list(elements(n))
    obs=Counter(product_invariants(n,a,b) for a,b in product(seq,repeat=2))
    exp=theory(n)
    assert obs==exp, (n,obs,exp)
    W=(n-1)*(n+2)//2
    assert len(seq)==W*W and sum(obs.values())==W**4
    print(f'n={n}, elements={len(seq)}, products={len(seq)**2}, distribution={sorted(obs.items())}, PASS')

if __name__=='__main__':
    for n in range(3,7):check(n)
