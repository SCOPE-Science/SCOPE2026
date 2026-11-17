from itertools import combinations, product
from math import comb, sqrt
import numpy as np
from scipy.spatial import ConvexHull

def area_formula(p,q,k,t):
    u=k+t;v=p-k+q-t
    def tau(a,b):return (a+b)**(a-1)*a**(b-1) if a>=1 else 0
    return sqrt(u*v)*tau(k,t)*tau(p-k,q-t)

def formula(p,q):
    n=p+q
    singleton=2*q*(n-1)**(p-.5)*p**(q-2)
    split=sum(comb(p,k)*comb(q,t)*area_formula(p,q,k,t) for k in range(1,p) for t in range(q+1))
    return singleton,split

def vertex_positions(e,s,n):
    edges=[(u,v) for u,v in e if u in s and v in s]
    arr=[]
    for bits in product((0,1),repeat=len(edges)):
        vec=np.zeros(n)
        for (u,v),a in zip(edges,bits):vec[(v if a else u)]+=1
        arr.append(vec)
    return np.array(arr)

def facet_vertices(edges,S,n):
    S=set(S); base=np.zeros(n)
    for u,v in edges:
        if (u in S)!=(v in S): base[u if u in S else v]+=1
    internal=[(u,v) for u,v in edges if (u in S)==(v in S)]
    return vertex_positions(internal,set(range(n)),n)+base

def hull_volume(verts,rank):
    unique=np.unique(verts,axis=0)
    mean=unique.mean(axis=0)
    _,s,VT=np.linalg.svd(unique-mean, full_matrices=False)
    assert sum(s>1e-7)==rank,(s,rank)
    proj=(unique-mean)@VT[:rank,:].T
    if rank==1:return np.max(proj)-np.min(proj)
    return ConvexHull(proj).volume

def test(p,q):
    n=p+q;eds=list(combinations(range(p),2))+[(u,v) for u in range(p) for v in range(p,n)]
    errs=[];ct=0; ssum=0;bsum=0
    for k in range(1,1<<n-1):
        S={i for i in range(n) if (k>>i)&1}; T=set(range(n))-S
        def connected(SS):
            root=next(iter(SS)); seen={root}
            while True:
                nxt=seen|{v for u,v in eds if u in seen and v in SS}|{u for u,v in eds if v in seen and u in SS}
                if nxt==seen:break
                seen=nxt
            return SS==seen
        if connected(S) and connected(T):
            for W in (S,T):
                x=hull_volume(facet_vertices(eds,W,n),n-2)
                if len(W.intersection(range(p)))==0 or len(W.intersection(range(p)))==p:
                    y=(n-1)**(p-.5)*p**(q-2); ssum+=x
                else:
                    kx=len(W.intersection(range(p)));t=len(W.intersection(range(p,n)))
                    y=area_formula(p,q,kx,t);bsum+=x
                errs.append(abs(x-y));ct+=1
    f=formula(p,q)
    print('p,q',p,q,'facets',ct,'max_abs_err',max(errs),'actual',ssum,bsum,'formula',f)
    assert max(errs)<1e-7 and abs(ssum-f[0])<1e-7 and abs(bsum-f[1])<1e-7
for p,q in [(2,2),(2,3),(2,4),(3,2),(3,3)]:test(p,q)

# Independent finite matrix-tree verification by testing graph edge sets.
def spanning_tree_count_brute(a,b):
    n=a+b
    eds=list(combinations(range(a),2))+[(u,v) for u in range(a) for v in range(a,n)]
    count=0
    for chosen in combinations(eds,n-1):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        for u,v in chosen:
            ru,rv=root(u),root(v)
            if ru!=rv:parent[ru]=rv
        if len({root(i) for i in range(n)})==1:count+=1
    return count
for p,q in [(2,2),(3,2),(3,3),(4,2)]:
    got=spanning_tree_count_brute(p,q)
    want=(p+q)**(p-1)*p**(q-1)
    assert got==want,(p,q,got,want)
    print('tree_count',p,q,got)

# Check the exact finite surface ratio in a numerically stable binomial form.
from math import lgamma, log, exp

def asymptotic_coefficient(p):
    return (p*p/2)*sum(comb(p,k)/(k*(p-k))*(k/p)**(k-.5)*((p-k)/p)**(p-k-.5) for k in range(1,p))

def normalized_split_to_singleton(p,q):
    weighted=0.0
    for k in range(1,p):
        prob=k/p
        ex=0.0
        for t in range(q+1):
            logpmf=(lgamma(q+1)-lgamma(t+1)-lgamma(q-t+1)
                    +t*log(prob)+(q-t)*log(1-prob))
            ex+=exp(logpmf)*(k+t)**(k-.5)*(p-k+q-t)**(p-k-.5)
        weighted+=comb(p,k)/(k*(p-k))*ex
    return p*p*weighted/(2*q*(p+q-1)**(p-.5))
assert abs(asymptotic_coefficient(3)-3*sqrt(2))<1e-12
assert abs(asymptotic_coefficient(4)-(3*sqrt(3)+1.5))<1e-12
for p in (3,4,6):
    for q in (40,100):
        scaled=normalized_split_to_singleton(p,q)*q**1.5
        coeff=asymptotic_coefficient(p)
        print('asymptotic',p,q,'scaled=',round(scaled,8),'coefficient=',round(coeff,8))
        assert abs(scaled/coeff-1)<0.13
print('SPLIT_SURFACE_PASS direct_facets=156')
