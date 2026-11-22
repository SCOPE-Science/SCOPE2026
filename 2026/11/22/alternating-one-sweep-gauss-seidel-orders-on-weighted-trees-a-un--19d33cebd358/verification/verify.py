"""Exact finite cross-checks of a weighted-tree one-sweep ordering theorem.

The all-tree proof is analytic; this file tests concrete rational instances.
No external dependencies. Run: python verify.py
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial


def matmul(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def transpose(a): return [list(t) for t in zip(*a)]


def risk(n, edges, eps, order):
    # For F(x)=1/2*x^T(I-eps W)x and Cov(x0)=I, returns 2 E F(x_after).
    w=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i,j,t in edges:
        w[i][j]=w[j][i]=eps*t
    m=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for i in order:
        m[i]=[sum(w[i][k]*m[k][j] for k in range(n)) for j in range(n)]
    h=[[Q(int(i==j))-w[i][j] for j in range(n)] for i in range(n)]
    b=matmul(h,m)
    return sum(m[k][i]*b[k][i] for k in range(n) for i in range(n))


def wedge_loss(edges,order):
    rank={v:i for i,v in enumerate(order)}
    t=Q(0)
    for a,(u,v,w1) in enumerate(edges):
        for (s,r,w2) in edges[a+1:]:
            common={u,v}&{s,r}
            if not common: continue
            c=next(iter(common))
            a1=v if c==u else u
            a2=r if c==s else s
            if min(rank[a1],rank[a2])<rank[c]<max(rank[a1],rank[a2]):
                t+=w1*w1*w2*w2
    return t


def is_bipartite_orientation(edges,order):
    return wedge_loss(edges,order)==0


def exact_rb(n,edges,eps):
    ss=sum(t*t for _,_,t in edges)
    v4=sum(t**4 for _,_,t in edges)
    wedges=Q(0)
    for a,(i,j,s) in enumerate(edges):
        for u,v,t in edges[a+1:]:
            if len({i,j,u,v})==3:wedges+=s*s*t*t
    return eps*eps*ss-eps**4*(v4+2*wedges)


def test_tree(n, edges, eps):
    opts=[]; vals=[]; q=exact_rb(n,edges,eps)
    for order in permutations(range(n)):
        a=risk(n,edges,eps,order)
        if a<q: raise AssertionError(('negative gap',n,edges,order,a-q))
        if is_bipartite_orientation(edges,order):
            assert a==q, ('red-black exact risk',n,order,a,q)
            opts.append(order)
        else:
            assert a>q, ('non-RB ties',n,order,a,q)
        vals.append(a)
    assert min(vals)==q
    return len(vals),len(opts)


def go():
    # Strict diagonal dominance guarantees SPD for all instances.
    trees=[
      (3,[(0,1,Q(2,5)),(1,2,Q(1,3))]),
      (4,[(0,1,Q(1,4)),(1,2,Q(1,5)),(2,3,Q(1,6))]),
      (5,[(0,i,Q(i+2,19)) for i in range(1,5)]),
      (6,[(i,i+1,Q(1+i,20)) for i in range(5)]),
      (6,[(0,1,Q(1,8)),(1,2,Q(1,7)),(1,3,Q(1,9)),(3,4,Q(1,6)),(3,5,Q(1,10))]),
    ]
    checked=0
    for n,edges in trees:
        total,opts=test_tree(n,edges,Q(1,2))
        checked+=total
        print('tree n=',n,'orders=',total,'optimal=',opts,'eps=1/2')
    # Rational coefficient recovery at weak coupling; remainder is O(eps^6).
    for n,edges in trees:
        base=exact_rb(n,edges,Q(1,100))
        for order in list(permutations(range(n)))[:min(40,factorial(n))]:
            e=Q(1,100)
            d=risk(n,edges,e,order)-base
            w=wedge_loss(edges,order)
            assert d>=0
            # n<=6, e tiny: difference tends to exactly 2*w*eps^4
            if w:
                assert abs(d/e**4-2*w)<Q(1,10000), (n,order,d/e**4,2*w)
    print('PASS',checked,'exact-rational full permutations; weak-coupling fourth-order spot checks')

if __name__=='__main__':go()
