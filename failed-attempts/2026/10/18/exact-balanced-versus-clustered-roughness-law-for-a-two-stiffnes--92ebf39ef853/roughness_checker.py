"""Exact checks for harmonic-chain width on a cycle, independent of an analytic proof.
Run: python roughness_checker.py (requires sympy only for the matrix cross-check).
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd

def width_arc(bits, base=1, increment=1):
    n=len(bits); r=[F(base)+F(increment)*a for a in bits]; R=sum(r)
    out=F(0)
    for i in range(n):
        s=F(0)
        for ell in range(1,n):
            s+=r[(i+ell-1)%n]
            out+=s*(R-s)
    return out/(2*n*n*R)

def width_pair(bits, base=1, increment=1):
    n=len(bits); m=sum(bits); R=F(n*base+m*increment)
    ix=[i for i,a in enumerate(bits) if a]
    phi=sum((j-i)*(n-(j-i)) for i,j in combinations(ix,2))
    return (R*(n*n-1)/(12*n*n)
        -F(increment*increment*m*m*(n*n-1),12*n*n)/R
        +F(increment*increment*phi,n*n)/R)

def ex_bounds(n,m,base=1,increment=1):
    R=F(n*base+m*increment); g=gcd(n,m)
    main=R*F(n*n-1,12*n*n)
    factor=F(increment*increment,12*n*n)/R
    return (main-factor*m*(n-m)*(m*(n-m)+2),
            main-factor*(n*n-g*g))

def mechanical(n,m):
    return [((j+1)*m)//n-(j*m)//n for j in range(n)]

def rotations(bits):
    n=len(bits)
    return {tuple(bits[i:]+bits[:i]) for i in range(n)}

def exact_matrix(bits,base=1,increment=1):
    from sympy import Matrix, Rational, eye, ones, trace
    n=len(bits); L=Matrix.zeros(n)
    for i,v in enumerate(bits):
        c=Rational(1,base+increment*v); j=(i+1)%n
        L[i,i]+=c; L[j,j]+=c; L[i,j]-=c; L[j,i]-=c
    J=ones(n,n)/n
    cov=(L+J).inv()-J
    return F(str(trace(cov)/n))

def check():
    formula=extrema=matrix=0
    for n in range(3,11):
        for m in range(1,n):
            cluster=rotations([1]*m+[0]*(n-m))
            balance=rotations(mechanical(n,m))
            for base,inc in [(1,1),(2,3)]:
                lo,hi=ex_bounds(n,m,base,inc)
                for comb in combinations(range(n),m):
                    bits=[int(i in comb) for i in range(n)]
                    w=width_arc(bits,base,inc)
                    assert w==width_pair(bits,base,inc),('pair formula',n,m,comb)
                    assert lo<=w<=hi,('bounds',n,m,comb,w,lo,hi)
                    assert (w==lo)==(tuple(bits) in cluster),('cluster uniqueness',n,m,comb)
                    assert (w==hi)==(tuple(bits) in balance),('balanced uniqueness',n,m,comb)
                    formula+=1;extrema+=1
    for n in range(3,8):
        for m in range(1,n):
            for comb in combinations(range(n),m):
                bits=[int(i in comb) for i in range(n)]
                assert width_arc(bits,1,2)==exact_matrix(bits,1,2),('matrix check',n,m,comb)
                matrix+=1
    print('PASS exact-rational arc/pair identity:',formula)
    print('PASS exact-rational global extrema and uniqueness:',extrema)
    print('PASS independent Laplacian covariance checks:',matrix)
if __name__=='__main__':check()
