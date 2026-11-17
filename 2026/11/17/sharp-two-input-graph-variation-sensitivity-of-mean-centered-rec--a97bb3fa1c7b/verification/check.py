"""Exact finite verification of centered-rectifier graph-variation formulas.

Requires only Python 3 standard library. This is corroboration, not an
infinite-family certificate: the proof is analytical.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random

def make_tree(n,rng):
    return [(v,rng.randrange(v)) for v in range(1,n)]

def component(n,edges,e):
    graph=[[] for _ in range(n)]
    for f,(u,v) in enumerate(edges):
        if f!=e:
            graph[u].append(v);graph[v].append(u)
    seen={edges[e][0]};todo=list(seen)
    while todo:
        for k in graph[todo.pop()]:
            if k not in seen:seen.add(k);todo.append(k)
    return seen,set(range(n))-seen

def norm(e,n,edges,mu,w):
    U,W=component(n,edges,e); total=sum(mu)
    muU=sum(mu[v] for v in U);muW=sum(mu[v] for v in W)
    internalU=sum(w[i] for i,(u,v) in enumerate(edges) if u in U and v in U)
    internalW=sum(w[i] for i,(u,v) in enumerate(edges) if u in W and v in W)
    return (w[e]+muW/total*internalU+muU/total*internalW)/w[e]

def jacobian_column(n,edges,mu,w,A,e):
    U,W=component(n,edges,e)
    s=sum(mu[v] for v in W)/sum(mu)
    h=[Q(int(v in W),1)-s for v in range(n)]
    f=[h[v] if v in A else Q(0) for v in range(n)]
    return sum(w[i]*abs(f[u]-f[v]) for i,(u,v) in enumerate(edges))/w[e]

def tv(x,edges,w):
    return sum(w[i]*abs(x[u]-x[v]) for i,(u,v) in enumerate(edges))

def F(x,mu):
    mean=sum(a*b for a,b in zip(x,mu))/sum(mu)
    return [max(Q(0),xi-mean) for xi in x]

def verify():
    rng=Random(20261113); cases=0; columns=0; pairtests=0; witnesses=0
    for n in range(2,9):
        for rep in range(30):
            edges=make_tree(n,rng)
            mu=[Q(rng.randrange(1,11),1) for _ in range(n)]
            w=[Q(rng.randrange(1,11),1) for _ in edges]
            expected=max(norm(e,n,edges,mu,w) for e in range(n-1)) if n>2 else max(mu)/sum(mu)
            actual=Q(0)
            for mask in range(1,(1<<n)-1):
                A={j for j in range(n) if (mask>>j)&1}
                for e in range(n-1):
                    val=jacobian_column(n,edges,mu,w,A,e)
                    if val>actual: actual=val
                    columns+=1
            assert expected==actual,(n,edges,mu,w,expected,actual)
            for rep2 in range(12):
                x=[Q(rng.randrange(-20,21),1) for _ in range(n)]
                y=[Q(rng.randrange(-20,21),1) for _ in range(n)]
                inp=tv([a-b for a,b in zip(x,y)],edges,w)
                if inp:
                    out=tv([a-b for a,b in zip(F(x,mu),F(y,mu))],edges,w)
                    assert out<=expected*inp,(n,out,expected,inp)
                    pairtests+=1
            e=max(range(n-1),key=lambda e:norm(e,n,edges,mu,w))
            U,W=component(n,edges,e)
            A=set()
            for S in (U,W):
                root=next(v for v in (edges[e][0],edges[e][1]) if v in S)
                adj={v:[] for v in S}
                for u,v in edges:
                    if u in S and v in S:adj[u].append(v);adj[v].append(u)
                stack=[(root,None,0)]
                while stack:
                    v,p,d=stack.pop()
                    if d%2==0:A.add(v)
                    for z in adj[v]:
                        if z!=p:stack.append((z,v,d+1))
            if n>=3:
                assert jacobian_column(n,edges,mu,w,A,e)==norm(e,n,edges,mu,w)
                x=[Q(int(v in A),1) for v in range(n)]
                h=[Q(int(v in W),1) for v in range(n)]
                eps=Q(1,1000)
                y=[a+eps*b for a,b in zip(x,h)]
                inp=tv([a-b for a,b in zip(x,y)],edges,w)
                out=tv([a-b for a,b in zip(F(x,mu),F(y,mu))],edges,w)
                assert out==expected*inp,(n,expected,out,inp)
                witnesses+=1
            cases+=1
    for n in range(3,31):
        path=[(i,i+1) for i in range(n-1)]
        star=[(0,i) for i in range(1,n)]
        ones=[Q(1)]*n
        p=max(norm(e,n,path,ones,[Q(1)]*(n-1)) for e in range(n-1))
        s=max(norm(e,n,star,ones,[Q(1)]*(n-1)) for e in range(n-1))
        assert p==Q(2*(n//2)*(n-n//2),n),(n,p)
        assert s==Q(2*(n-1),n),(n,s)
    print('EXACT_ALL_ACTIVATION_SETS_AND_WEIGHTED_TREE_CUTS_PASS',cases,columns)
    print('EXACT_TWO_INPUT_RATIONAL_TESTS_PASS',pairtests)
    print('EXACT_ATTAINED_BIPARTITE_ACTIVATION_WITNESSES_PASS',witnesses)
    print('ALL_PATH_AND_STAR_EXTREMA_PASS',28)
    print('ALL_CENTERED_RECTIFICATION_VARIATION_CHECKS_PASS')

if __name__=='__main__':verify()
