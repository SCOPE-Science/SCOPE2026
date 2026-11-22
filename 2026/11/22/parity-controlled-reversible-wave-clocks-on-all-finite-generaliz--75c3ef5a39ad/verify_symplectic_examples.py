#!/usr/bin/env python3
"""Finite symplectic generalized-quadrangle incidence and characteristic-two reversible dynamics checker."""
from itertools import product, combinations

def inverse_mod(a,p): return pow(a,-1,p)

def norm(v,p):
    lead=next(x for x in v if x%p)
    inv=inverse_mod(lead,p)
    return tuple((x*inv)%p for x in v)

def symp(x,y,p):
    return (x[0]*y[2]-x[2]*y[0]+x[1]*y[3]-x[3]*y[1])%p

def make_gq(p):
    assert p in (2,3,5,7)
    pts=sorted({norm(x,p) for x in product(range(p),repeat=4) if any(x)})
    idx={x:i for i,x in enumerate(pts)}
    lines=set()
    for i,j in combinations(range(len(pts)),2):
        x,y=pts[i],pts[j]
        if symp(x,y,p):continue
        line=tuple(sorted({idx[norm(tuple((a*x[k]+b*y[k])%p for k in range(4)),p)]
                               for a in range(p) for b in range(p) if (a,b)!=(0,0)}))
        assert len(line)==p+1
        lines.add(line)
    lines=sorted(lines)
    v=(p+1)*(p*p+1)
    assert len(pts)==len(lines)==v
    return pts,lines

def adj_from_lines(v,lines):
    n=2*v
    rows=[0]*n
    for j,L in enumerate(lines):
        for i in L:
            rows[i]|=1<<(v+j)
            rows[v+j]|=1<<i
    return rows

def gf2_mul(A,B):
    out=[]
    for ar in A:
        y=0
        while ar:
            bit=ar&-ar
            y^=B[bit.bit_length()-1]
            ar-=bit
        out.append(y)
    return out

def gf2_identity(n): return [1<<i for i in range(n)]
def gf2_rank(rows):
    piv={}
    for x in rows:
        while x:
            k=x.bit_length()
            if k not in piv: piv[k]=x;break
            x^=piv[k]
    return len(piv)

def binary_wave(A):
    n=len(A)
    return [A[i]|(1<<(n+i)) for i in range(n)]+[1<<i for i in range(n)]

def gf2_power(A,k):
    n=len(A); R=gf2_identity(n)
    while k:
        if k&1:R=gf2_mul(R,A)
        A=gf2_mul(A,A)
        k//=2
    return R

def main():
    for p in (2,3,5):
        pts,lines=make_gq(p); v=len(pts); A=adj_from_lines(v,lines);n=2*v
        r1=gf2_rank(A)
        A2=gf2_mul(A,A);r2=gf2_rank(A2)
        A3=gf2_mul(A2,A)
        H=[((1<<v)-1)<<v for _ in range(v)]+[((1<<v)-1) for _ in range(v)]
        assert A3==H,(p,'A3')
        A4=gf2_mul(A3,A)
        P=[((1<<v)-1) for _ in range(v)]+[(((1<<v)-1)<<v) for _ in range(v)]
        assert A4 == (P if p%2==0 else [0]*n)
        T=binary_wave(A)
        expected=24 if p%2==0 else 8
        assert gf2_power(T,expected)==gf2_identity(2*n)
        for d in [1,2,3,4,6,8,12]:
            if expected%d==0 and d<expected:assert gf2_power(T,d)!=gf2_identity(2*n)
        def pred_dim(t):
            nu=(t&(-t)).bit_length()-1
            if p%2:
                a4=2;a3=r2-4;a2=r1-2*r2+2;a1=n-2*r1+r2
                assert min(a1,a2,a3,a4)>=0
                return sum(a*min(2*j,2**nu) for j,a in enumerate([0,a1,a2,a3,a4]) if j)
            b3=r2-2;b2=r1-2*r2+2;b1=n-2*r1+r2
            assert min(b1,b2,b3)>=0
            return sum(a*min(2*j,2**nu) for j,a in enumerate([0,b1,b2,b3]) if j)+(2*min(2,2**nu) if t%3==0 else 0)
        fixed=[]
        for t in (1,2,3,4,6,8,12,24):
            Tt=gf2_power(T,t)
            actual=2*n-gf2_rank([Tt[i]^(1<<i) for i in range(2*n)])
            predicted=pred_dim(t)
            assert actual==predicted,(p,t,actual,predicted)
            fixed.append((t,actual))
        print('q=',p,'points=',v,'N=',n,'r1=',r1,'r2=',r2,'r3=',gf2_rank(A3),'order=',expected,'Fix-exponents=',fixed)
if __name__=='__main__':main()
