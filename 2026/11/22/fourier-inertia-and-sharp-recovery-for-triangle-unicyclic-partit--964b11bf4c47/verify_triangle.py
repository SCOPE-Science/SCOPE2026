#!/usr/bin/env python3
"""Exact integer verification of the triangle-unicyclic partition Fourier theorem.

Run: python3 verify_triangle.py . No nonstandard packages required.
"""
from math import comb, factorial

CHECKS = 0

def check(a,b,where):
    global CHECKS
    CHECKS += 1
    if a != b:
        raise AssertionError(f'{where}: {a!r} != {b!r}')


def bells(N):
    B = [1]
    for n in range(1,N+1):
        B.append(sum(comb(n-1,j)*B[j] for j in range(n)))
    return B

B=bells(180)

def U(n,k):
    return sum(comb(k,j)*(-2)**j*B[n-j] for j in range(k+1))

def V(s,r):
    n=s+3
    return U(n,r+3)-8*sum(comb(r,j)*(-2)**j*(B[s-j+1]-B[s-j]) for j in range(r+1))

def rg(n):
    if n==0:
        yield ()
    else:
        def rec(a,highest):
            if len(a)==n:
                yield tuple(a)
            else:
                for k in range(highest+2):
                    a.append(k)
                    yield from rec(a,max(highest,k))
                    a.pop()
        yield from rec([0],0)

def shapes(n):
    assert n>=3
    tri=[(0,1),(1,2),(0,2)]
    return [tri+[(k-1,k) for k in range(3,n)],tri+[(0,k) for k in range(3,n)]]

def signed_spectrum(n,edges):
    f=[0]*(1<<n)
    for a in rg(n):
        mask=sum((a[u]==a[v])<<i for i,(u,v) in enumerate(edges))
        f[mask]+=1
    f=f[:]
    for i in range(n):
        step=1<<i
        for m in range(0,1<<n,step*2):
            for j in range(step):
                a=f[m+j];b=f[m+j+step]
                f[m+j]=a+b;f[m+j+step]=a-b
    return f

def main():
    smallV={
        0:[-3],1:[-7,-1],2:[-18,-4,-2],3:[-49,-13,-5,-1],
        4:[-133,-35,-9,1,3],5:[-310,-44,26,44,42,36],
        6:[-185,435,523,471,383,299,227],
        7:[5653,6023,5153,4107,3165,2399,1801,1347],
    }
    for s,row in smallV.items():
        check([V(s,r) for r in range(s+1)],row,('small V',s))
    for n in range(3,10):
        spectra=[]
        for edges in shapes(n):
            sp=signed_spectrum(n,edges)
            for H,z in enumerate(sp):
                r=(H>>3).bit_count()
                target=V(n-3,r) if (H&7)==7 else U(n,H.bit_count())
                check(z,target,('independent RG enumeration',n,edges,H))
            spectra.append(sp)
        check(spectra[0],spectra[1],('shape independent',n))
        sp=spectra[0]
        check(sum(z>0 for z in sp)+sum(z<0 for z in sp)+sum(z==0 for z in sp),1<<n,('inertia total',n))
    for n in range(3,181):
        s=n-3
        # Basic identities, strict comparisons and all positive/signed cases.
        for k in range(n-1):
            check(U(n,k)-U(n,k+1),2*U(n-1,k),('U recurrence',n,k))
        check(U(n,n-1),sum(comb(n-1,j)*(-1)**j*B[n-1-j] for j in range(n)),('no singleton identity',n))
        for r in range(s):
            check(V(s,r)-V(s,r+1),2*V(s-1,r),('V recurrence',n,r))
        check(U(n,n-1)-V(s,s),2*U(s+2,s),('spectral separation',n))
        if n>=10:
            assert all(V(s,r)>0 for r in range(s+1)),n
            assert n==10 or all(V(s,r)>V(s,r+1) for r in range(s)),n
            assert V(s,s)<U(n,n-1),n
    # Exhaustively classify all frequencies at the finite transitional sizes.
    neg_expected=[1,2,4,8,11,6,1]
    gap_expected=[1,1,2,1,1,26,185]
    for n in range(3,10):
        s=n-3
        vals=[U(n,k) for k in range(n)]+[V(s,r) for r in range(s+1)]
        check(sum(comb(s,r) for r in range(s+1) if V(s,r)<0),neg_expected[n-3],('negative index',n))
        check(min(abs(z) for z in vals if z),gap_expected[n-3],('least abs eigenvalue',n))
        assert all(z!=0 for z in vals)
    for s in range(6,150):
        # Dominant m=6 summand vs absolute negative m=1,3,4,5.
        assert 4**s*4 > 120+300+80*2**s+5*3**s,('domination',s)
    print(f'PASS {CHECKS} exact integer tests, exhaustive set-partition transforms n=3..9 and algebraic recurrence checks through n=180')

if __name__=='__main__': main()
