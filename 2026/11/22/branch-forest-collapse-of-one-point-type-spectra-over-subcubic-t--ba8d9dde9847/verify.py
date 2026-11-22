"""Exact checks for graded Henson one-types over subcubic tree line graphs.
Requires only Python 3 standard library. No sample is used as an infinite proof.
"""
from itertools import product,combinations
from collections import Counter,defaultdict
from random import Random
from math import comb

def tree_prufer(seq):
    n=len(seq)+2
    deg=[1]*n
    for x in seq: deg[x]+=1
    edges=[]
    for x in seq:
        leaf=next(i for i,d in enumerate(deg) if d==1)
        edges.append((leaf,x));deg[leaf]-=1;deg[x]-=1
    x,y=[i for i,d in enumerate(deg) if d==1]
    edges.append((x,y))
    return n, tuple(edges)

def canonical(n,edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    def rooted(v,p):
        return '('+''.join(sorted(rooted(w,v) for w in adj[v] if w!=p))+')'
    centers=set(range(n))
    while len(centers)>2:
        leaves=[x for x in centers if sum(y in centers for y in adj[x])<=1]
        centers.difference_update(leaves)
    return min(rooted(v,-1) for v in centers) if len(centers)==1 else 'E'+min(rooted(v,w)+rooted(w,v), rooted(w,v)+rooted(v,w)) if (v:=min(centers))>=0 and (w:=max(centers))>=0 else ''

def direct(n,edges):
    m=len(edges)
    tris=[]
    for a,b,c in combinations(range(m),3):
        e=[set(edges[i]) for i in (a,b,c)]
        if all(e[i]&e[j] for i,j in ((0,1),(1,2),(0,2))):
            tris.append((a,b,c))
    counts=[0]*(m+1)
    for mask in range(1<<m):
        if not any(all(mask>>i&1 for i in tri) for tri in tris):
            counts[mask.bit_count()]+=1
    return tuple(counts)

def prediction(n,edges):
    m=len(edges)
    deg=Counter(v for e in edges for v in e)
    B=sorted(v for v in range(n) if deg[v]==3)
    assert max(deg.values(),default=0)<=3
    out=[0]*(m+1)
    for mask in range(1<<len(B)):
        W={B[i] for i in range(len(B)) if mask>>i&1}
        e=sum(a in W and b in W for a,b in edges)
        u=3*len(W)-e
        assert 0<=u<=m
        sg=-1 if len(W)&1 else 1
        for k in range(u,m+1):out[k]+=sg*comb(m-u,k-u)
    return tuple(out)

def spider(arms):
    edge=[];cur=1
    for length in arms:
        previous=0
        for j in range(length):
            edge.append((previous,cur));previous=cur;cur+=1
    return cur,tuple(edge)

classes=defaultdict(dict)
count_lab=0
for n in range(2,7):
    for pr in product(range(n),repeat=n-2):
        N,E=tree_prufer(pr)
        D=Counter(v for e in E for v in e)
        if max(D.values())>3: continue
        count_lab+=1
        a=direct(n,E);b=prediction(n,E)
        assert a==b,(n,pr,a,b)
        key=canonical(n,E)
        if key in classes[n]: assert classes[n][key]==a
        classes[n][key]=a
    print('n',n,'subcubic_classes',len(classes[n]),'distinct_polynomials',len(set(classes[n].values())))
assert [len(classes[n]) for n in range(2,7)]==[1,1,2,2,4]
assert [len(set(classes[n].values())) for n in range(2,7)]==[1,1,2,2,3]
S1=spider((1,1,3));S2=spider((1,2,2))
assert canonical(*S1)!=canonical(*S2)
assert direct(*S1)==direct(*S2)==(1,5,10,9,3,0)
assert prediction(*S1)==prediction(*S2)
print('first_collision',len(classes[6]),'types',sum(direct(*S1)),'witness_polynomial',direct(*S1))
for n in range(6,31):
    a=spider((1,1,n-3));b=spider((1,2,n-4))
    assert a[0]==b[0]==n
    assert canonical(*a)!=canonical(*b)
    assert prediction(*a)==prediction(*b)
print('all_order_spider_pairs',25)
# All-input coefficient recovery tests using more complex branch forests.
rng=Random(1201)
checked=0
for n in range(7,15):
    for z in range(200):
        N,E=tree_prufer(tuple(rng.randrange(n) for _ in range(n-2)))
        D=Counter(v for e in E for v in e)
        if max(D.values())>3:continue
        pred=prediction(n,E)
        assert pred==direct(n,E)
        b=sum(x==3 for x in D.values())
        h=sum(D[a]==3 and D[c]==3 for a,c in E)
        m=n-1
        assert b==comb(m,3)-pred[3] if m>=3 else b==0
        if m>=5:
            assert h==pred[5]-comb(m,5)+b*comb(m-3,2)
        checked+=1
print('deterministic_random_checks',checked)
print('VERIFY_OK')
