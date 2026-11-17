"""Exact checks for the Euclidean outer-radius theorem of two-dimensional acyclohedra.
Run: python3 acyclohedron_verify.py (Python 3.10+, standard library only).
Finite checks are corroboration; the accompanying written argument proves arbitrary n.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial

def data(n):
    edges=list(combinations(range(n),2))
    triangles=list(combinations(range(n),3))
    tetrahedra=list(combinations(range(n),4))
    row={e:i for i,e in enumerate(edges)}
    col={t:j for j,t in enumerate(triangles)}
    B=[[0]*len(triangles) for _ in edges]
    for j,(a,b,c) in enumerate(triangles):
        B[row[(b,c)]][j]=1
        B[row[(a,c)]][j]=-1
        B[row[(a,b)]][j]=1
    D=[[0]*len(tetrahedra) for _ in triangles]
    for j,(a,b,c,d) in enumerate(tetrahedra):
        for sign,tri in ((1,(b,c,d)),(-1,(a,c,d)),(1,(a,b,d)),(-1,(a,b,c))):
            D[col[tri]][j]=sign
    return edges,triangles,tetrahedra,B,D

def test_hodge(n,B,D):
    t=len(B[0]);e=len(B);q=len(D[0]) if D else 0
    assertions=0
    for i in range(t):
        for j in range(t):
            v=sum(B[k][i]*B[k][j] for k in range(e))+sum(D[i][k]*D[j][k] for k in range(q))
            assert v==(n if i==j else 0)
            assertions+=1
    return assertions

def boundary(B,sigma):
    return [sum(c*v for c,v in zip(row,sigma)) for row in B]

def cyclic_sigma(n,triangles,order):
    ranks={v:i for i,v in enumerate(order)}
    def x(i,j):return 1 if ranks[i]<ranks[j] else -1
    out=[]
    for t in triangles:
        if 0 in t:
            _,i,j=t
            out.append(x(i,j))
        else:
            i,j,k=t
            out.append(x(j,k)-x(i,k)+x(i,j))
    return out

def full_gray(n,B,triangles):
    m=len(triangles)
    cols=[[(i,B[i][j]) for i in range(len(B)) if B[i][j]] for j in range(m)]
    sigma=[1]*m
    coords=boundary(B,sigma)
    norm=sum(x*x for x in coords)
    hist=Counter({norm:1})
    gray=0
    for step in range(1,1<<m):
        new=step^(step>>1)
        j=(gray^new).bit_length()-1
        diff=-2*sigma[j]
        sigma[j]=-sigma[j]
        for i,b in cols[j]:
            old=coords[i]
            fresh=old+diff*b
            coords[i]=fresh
            norm+=fresh*fresh-old*old
        hist[norm]+=1
        gray=new
    expected=n*comb(n,3)
    assert max(hist)==expected,(n,max(hist),expected)
    assert hist[expected]==factorial(n-1),(n,hist[expected])
    if n>=4:
        assert sorted(hist,reverse=True)[1]==expected-4*(n-3)
    assert sum(hist.values())==1<<m
    return len(hist),hist[expected], (sorted(hist,reverse=True)[1] if n>=4 else None)

def main():
    checks=0
    for n in range(3,9):
        edges,triangles,tetrahedra,B,D=data(n)
        checks+=test_hodge(n,B,D)
        cyclic_count=0;seen=set()
        for order in permutations(range(1,n)):
            sigma=cyclic_sigma(n,triangles,order)
            assert all(abs(v)==1 for v in sigma)
            assert sum(x*x for x in boundary(B,sigma))==n*comb(n,3)
            seen.add(tuple(sigma))
            cyclic_count+=1;checks+=2
            # One-coordinate flip provides the sharp second shell.
            if n>=4:
                j=cyclic_count%len(sigma)
                sigma[j]*=-1
                assert sum(x*x for x in boundary(B,sigma))==n*comb(n,3)-4*(n-3)
                checks+=1
        assert len(seen)==factorial(n-1)
        checks+=1
        if n<=6:
            nsh,far,second=full_gray(n,B,triangles)
            print(f'n={n}: exhaustive {1<<len(triangles)} endpoint signs, norm-shells={nsh}, outer-signs={far}, second-norm2={second}')
        else:
            print(f'n={n}: {cyclic_count} distinct cyclic-order maximizers, Hodge identity checked; not exhaustive')
    print(f'PASS: {checks} exact analytical-identity/order checks plus 1,049,618 exhaustive endpoint signs (n=3..6)')

if __name__=='__main__':main()
