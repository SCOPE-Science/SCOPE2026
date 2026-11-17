"""Exact finite diagnostics for rectangular checkerboard averaging in edge variation.
Run: python3 verify.py. Standard library only.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def vertices(m, n):
    return [(i,j) for i in range(m) for j in range(n)]


def edges(m,n):
    return [tuple(sorted(((i,j),(k,l)))) for i in range(m) for j in range(n)
            for k,l in ((i+1,j),(i,j+1)) if k<m and l<n]


def snake(m,n,axis,reverse_order,reverse_first):
    out=[]
    if axis=='h':
        order=list(range(m))
        if reverse_order: order.reverse()
        for a,i in enumerate(order):
            js=list(range(n))
            if (a%2)^reverse_first: js.reverse()
            out += [(i,j) for j in js]
    else:
        order=list(range(n))
        if reverse_order: order.reverse()
        for a,j in enumerate(order):
            ii=list(range(m))
            if (a%2)^reverse_first: ii.reverse()
            out += [(i,j) for i in ii]
    return out


def snake_flux(m,n,path):
    B=(m*n+1)//2;W=(m*n-1)//2
    assert len(set(path))==m*n and all(abs(x[0]-y[0])+abs(x[1]-y[1])==1 for x,y in zip(path,path[1:]))
    p={};acc=F(0)
    for u,v in zip(path,path[1:]):
        acc += F(1,B) if (sum(u)%2==0) else -F(1,W)
        e=tuple(sorted((u,v)))
        p[e] = acc * (1 if sum(u)%2==0 else -1)
    assert acc == -F(1,B)  # the final black vertex supplies the remaining 1/B
    return p


def odd_flux(m,n):
    assert m%2==n%2==1
    weights={'h':F(m-1,m+n-2),'v':F(n-1,m+n-2)}
    flow={e:F(0) for e in edges(m,n)}
    for axis,ro,rf in product(('h','v'),(0,1),(0,1)):
        P=snake_flux(m,n,snake(m,n,axis,ro,rf))
        for e,q in P.items():
            flow[e]+=weights[axis]*q/4
    return flow


def check_flow(m,n,flow):
    B=(m*n+1)//2;W=(m*n-1)//2
    cap=F(1,2*B)
    assert set(flow)==set(edges(m,n))
    assert all(F(0)<=v<=cap for v in flow.values())
    for v in vertices(m,n):
        incident=sum((q for e,q in flow.items() if v in e),F(0))
        assert incident == (F(1,B) if sum(v)%2==0 else F(1,W))
    return cap


def check_closed_edge_formula(m,n,flow):
    b=(m*n+1)//2;w=(m*n-1)//2;alpha=F(m-1,m+n-2);beta=1-alpha
    for i in range(m):
      for j in range(n-1):
        e=tuple(sorted(((i,j),(i,j+1))))
        sigma=(-1)**(i+j)
        r=F(m*n+sigma*(n-2*j-2),4*b*w)
        s=(n-1-j) if j%2==0 else (j+1)
        c=F(m*s,4*b*w) if i in (0,m-1) else F(0)
        assert flow[e]==alpha*r+beta*c,(m,n,i,j,flow[e],alpha*r+beta*c)


def check_cut(m,n):
    es=edges(m,n)
    vs=vertices(m,n)
    b=(m*n+1)//2;w=(m*n)//2
    N=m*n
    best=F(0);bestS=None
    for bits in range(1,(1<<N)-1):
        B=sum((bits>>k)&1 for k,v in enumerate(vs) if sum(v)%2==0)
        W=sum((bits>>k)&1 for k,v in enumerate(vs) if sum(v)%2==1)
        dd=abs(F(B,b)-F(W,w))
        if not dd:continue
        cut=sum(bool((bits>>vs.index(u))&1)!=bool((bits>>vs.index(v))&1) for u,v in es)
        g=F(len(es))*dd/cut
        if g>best:best=g;bestS=bits
    expected=F(len(es),2*b)
    assert best==expected,(m,n,best,expected,bestS)


def check_even_cycle(m,n):
    assert m*n%2==0
    if m%2==1:m,n=n,m
    # m even. Reserve first column for return path, snake all other columns.
    path=[]
    for i in range(m):
        js=list(range(1,n))
        if i%2:js.reverse()
        path += [(i,j) for j in js]
    path += [(i,0) for i in range(m-1,-1,-1)]
    assert len(path)==m*n and len(set(path))==m*n
    assert all(abs(x[0]-y[0])+abs(x[1]-y[1])==1 for x,y in zip(path,path[1:]+path[:1]))
    return len(path)


if __name__=='__main__':
    cnt=0
    for m in range(2,14):
      for n in range(2,14):
        if m*n%2:
            f=odd_flux(m,n)
            check_flow(m,n,f)
            check_closed_edge_formula(m,n,f)
        else:
            check_even_cycle(m,n)
        cnt+=1
    print('RECTANGULAR_ALL_PARITY_FLOW_CERTIFICATES_PASS',cnt)
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4)]:
        check_cut(m,n)
    print('EXHAUSTIVE_ALL_NONTRIVIAL_CUTS_SMALL_GRIDS_PASS',7)
    for m,n in [(3,25),(5,31),(17,19),(35,37)]:
        f=odd_flux(m,n)
        check_flow(m,n,f)
        check_closed_edge_formula(m,n,f)
    print('LARGE_ODD_GRID_EXACT_RATIONAL_FLUX_CERTIFICATES_PASS',4)
    print('ALL_CHECKERBOARD_VARIATION_CHECKS_PASS')
