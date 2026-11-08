#!/usr/bin/env python3
"""Exact reproducible checks for fourth-order Sylvester character minors.
No external dependencies. All ranks and determinants use integer arithmetic.
"""
from collections import Counter
from itertools import product, combinations
from math import comb


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def rank3(a):
    if det3(a): return 3
    for i,j in combinations(range(3),2):
        for k,l in combinations(range(3),2):
            if a[i][k]*a[j][l]-a[i][l]*a[j][k]:return 2
    return int(any(v for row in a for v in row))


def projection_matrix(case, cols):
    if case == 'plane':
        return [[(v >> 0)&1 for v in cols],
                [(v >> 1)&1 for v in cols],
                [((v >> 0)&1)^((v >> 1)&1) for v in cols]]
    return [[(v >> i)&1 for v in cols] for i in range(3)]


def raw_weight(cols, h):
    c=Counter(cols); z=1
    for v,k in c.items():
        size=h-(v==0)
        for i in range(k):z*=size-i
    return z


def predicted_polys(case,h):
    ans={(1,0):(h-1)*(h-2)*(h-3)}
    if case=='plane':
        ans.update({(2,0):3*h*(h-1)*(7*h-11),
                    (3,0):36*h*h*(h-1),
                    (4,16):6*h**3})
    else:
        ans.update({(2,0):7*h*(h-1)*(7*h-11),
                    (3,0):36*h*h*(8*h-7),
                    (4,8):168*h**3,
                    (4,16):6*h**3})
    return ans


def enumerate_projection(case,h):
    r=2 if case=='plane' else 3
    counts=Counter()
    unweighted=Counter()
    for cols in product(range(1<<r),repeat=3):
        mat=projection_matrix(case,cols)
        rk=1+rank3(mat)
        dt=abs(det3(mat))
        minor=8*dt if rk==4 else 0
        unweighted[rk,minor]+=1
        counts[rk,minor]+=raw_weight(cols,h)
    return counts,unweighted


def per_row_formula(case,N):
    # All exact integers; entry is a count of four-element column sets.
    if case=='plane':
        out={(1,0):N*(N-12)*(N-8)*(N-4)//1536,
             (2,0):N*N*(N-4)*(7*N-44)//512,
             (3,0):3*N**3*(N-4)//128,
             (4,16):N**4//256}
    else:
        out={(1,0):N*(N-24)*(N-16)*(N-8)//12288,
             (2,0):7*N*N*(N-8)*(7*N-88)//12288,
             (3,0):3*N**3*(N-7)//128,
             (4,8):7*N**4//512,
             (4,16):N**4//2048}
    return {key:val for key,val in out.items() if val}


def det4(a):
    return sum(((-1)**j)*a[0][j]*det3(
        [[a[i][k] for k in range(4) if k!=j] for i in range(1,4)])
        for j in range(4))


def rank4_direct(a):
    if det4(a):return 4
    for rows in combinations(range(4),3):
        for cols in combinations(range(4),3):
            if det3([[a[i][j] for j in cols] for i in rows]):return 3
    for i,j in combinations(range(4),2):
        for k,l in combinations(range(4),2):
            if a[i][k]*a[j][l]-a[i][l]*a[j][k]:return 2
    return int(any(v for row in a for v in row))


def dim_components(case,N):
    # Fixed A: 0 and three chosen difference rows.
    a=[0,1,2,3] if case=='plane' else [0,1,2,4]
    result=Counter()
    for b in combinations(range(N),4):
        # The original 4 by 4 real matrix is equivalent by signs to
        # first row/col all ones; its rank is 1 + rank3 below.
        z=[b[j]^b[0] for j in range(1,4)]
        mat=[[( (ai&bj).bit_count() & 1) for bj in z]
             for ai in a[1:]]
        rk=1+rank3(mat)
        minor=8*abs(det3(mat)) if rk==4 else 0
        if N<=16:
            orig=[[(-1)**((ai&bj).bit_count()&1) for bj in b] for ai in a]
            assert rank4_direct(orig)==rk
            assert abs(det4(orig))==minor
        result[rk,minor]+=1
    return result


def main():
    for case in ('plane','tetra'):
        r=2 if case=='plane' else 3
        for h in range(1,7):
            weights,unweighted=enumerate_projection(case,h)
            expected=Counter(predicted_polys(case,h))
            assert weights==expected,(case,h,weights,expected)
            assert sum(weights.values())==(2**r*h-1)*(2**r*h-2)*(2**r*h-3)
        _,base=enumerate_projection(case,1)
        assert sum(base.values())==2**(3*r)
        print(case,'rank / determinant classes',sorted(base.items()))
    for d in (3,4,5):
        N=1<<d
        for case in ('plane','tetra'):
            got=dim_components(case,N)
            want=Counter(per_row_formula(case,N))
            assert got==want,(d,case,got,want)
            assert sum(got.values())==comb(N,4)
            print('d=',d,case,dict(sorted(got.items())))
    for d in (3,4,5):
        N=1<<d; pc=N*(N-1)*(N-2)//24;tc=comb(N,4)-pc
        allr=Counter()
        for case,multiplicity in [('plane',pc),('tetra',tc)]:
            for sig,amount in per_row_formula(case,N).items():
                allr[sig]+=multiplicity*amount
        assert sum(allr.values())==comb(N,4)**2
        # Cauchy--Binet, independently known for Hadamard matrices:
        assert sum(det**2*amount for (rk,det),amount in allr.items())==N**4*comb(N,4)
    N=16
    plane=N*(N-1)*(N-2)//24
    tetra=comb(N,4)-plane
    zero=(plane*(comb(N,4)-per_row_formula('plane',N)[4,16])+
          tetra*(comb(N,4)-sum(v for (rank,det),v in per_row_formula('tetra',N).items() if rank==4)))
    assert zero==1717520
    print('ORDER16_SINGULAR_COUNT_MATCHES_BRENT_OSBORN',zero)
    print('ALL_FOURTH_WALSH_MINOR_CHECKS_OK')

if __name__=='__main__':main()
