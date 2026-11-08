#!/usr/bin/env python3
"""Direct finite-field checks for linear local/2-local Heisenberg derivations.

Run: python3 verify.py  (standard-library only).
"""
from itertools import product
from collections import Counter


def rank_mod(a,q):
    if not a: return 0
    a=[list(row) for row in a]
    r=0
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][j]%q),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k]
        d=pow(a[r][j],-1,q)
        a[r]=[(v*d)%q for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                t=a[i][j]%q
                a[i]=[(x-t*y)%q for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def maps(q,m):
    for vals in product(range(q),repeat=(m+1)**2):
        yield [list(vals[i*(m+1):(i+1)*(m+1)]) for i in range(m+1)]


def loc_type(M,q,m):
    return all(M[i][m]==0 for i in range(m))


def csp_type(M,q,m):
    # standard hyperbolic pairing e_1...e_n,f_1...f_n
    n=m//2
    def pairing(u,v):
        return sum(u[i]*v[i+n]-u[i+n]*v[i] for i in range(n))%q
    basis=[[int(j==i) for j in range(m)] for i in range(m)]
    def col(j):return [M[i][j] for i in range(m)]
    c=pairing(col(0),basis[n])+pairing(basis[0],col(n))
    for i in range(m):
        for j in range(m):
            beta=(pairing(col(i),basis[j])+pairing(basis[i],col(j)))%q
            if beta!=(c*pairing(basis[i],basis[j]))%q:
                return False
    return True


def counts_formula(q,m):
    ans=Counter()
    # Count matrix B by exact finite-field enumeration; independently count bottom row by rank.
    for data in product(range(q),repeat=m*m):
        B=[data[i*m:(i+1)*m] for i in range(m)]
        r=rank_mod(B,q)
        ans[r]+=q**r
        ans[r+1]+=q**(m+1)-q**r
    return ans


def direct_counts(q,m):
    out=Counter()
    for M in maps(q,m):
        if loc_type(M,q,m):
            out[rank_mod(M,q)]+=1
    return out


def matvec(M,v,q):
    return tuple(sum(x*y for x,y in zip(row,v))%q for row in M)


def exhaustive_heisenberg3(q):
    vectors=list(product(range(q),repeat=3))
    # In dimension 3, each 2x2 matrix A has conformal multiplier trace(A).
    deriv=[]
    for a,b,c,d,fx,fy in product(range(q),repeat=6):
        deriv.append([[a,b,0],[c,d,0],[fx,fy,(a+d)%q]])
    images={x:set() for x in vectors}
    pairs={(x,y):set() for x in vectors for y in vectors}
    for D in deriv:
        d={x:matvec(D,x,q) for x in vectors}
        for x in vectors:images[x].add(d[x])
        for x in vectors:
            for y in vectors:pairs[(x,y)].add((d[x],d[y]))
    # Characterize every linear map (GF2); sampling is used at q=3.
    if q==2: candidates=list(maps(q,2))
    else:
        import random
        rng=random.Random(1004)
        candidates=[[[rng.randrange(q) for _ in range(3)] for _ in range(3)] for _ in range(350)]
    count=Counter()
    for M in candidates:
        loc=all(matvec(M,x,q) in images[x] for x in vectors)
        tl=all((matvec(M,x,q),matvec(M,y,q)) in pairs[(x,y)] for x in vectors for y in vectors)
        der=any(M==D for D in deriv)
        assert loc==loc_type(M,q,2)
        assert tl==(loc_type(M,q,2) and csp_type(M,q,2))
        assert der==(loc_type(M,q,2) and csp_type(M,q,2) and M[2][2]%q==(M[0][0]+M[1][1])%q)
        count[(loc,tl,der)]+=1
    return count


def main():
    for q,m in [(2,2),(3,2)]:
        direct=direct_counts(q,m)
        formula=counts_formula(q,m)
        assert direct==formula,(q,m,direct,formula)
        print('RANK_DISTRIBUTION',q,m,sorted(direct.items()))
    print('EXHAUSTIVE_F2_H3',sorted(exhaustive_heisenberg3(2).items()))
    print('F3_H3_350_SAMPLES',sorted(exhaustive_heisenberg3(3).items()))
    q=2;m=4
    total=Counter(); csp=0
    # Explicit enumeration of all quotient matrices; cross-check csp dimension and
    # mixed alternating-form matrix tests (no purported full 5x5 enumeration).
    for data in product(range(q),repeat=m*m):
        B=[list(data[i*m:(i+1)*m])+[0] for i in range(m)]
        M=B+[[0]*(m+1)]
        csp+=csp_type(M,q,m)
        total[rank_mod([r[:m] for r in B],q)]+=1
    assert csp==q**(2*2*2+2+1) # csp(4) dimension 2*(2*2+1)+1=11
    assert sum(total.values())==q**(m*m)
    # Rank counts have an unrelated Gaussian-binomial product derivation.
    def gaussian(n,r,q):
        num=den=1
        for i in range(r):num*=q**(n-i)-1;den*=q**(r-i)-1
        return num//den
    for r in range(m+1):
        p=1
        for i in range(r): p*=q**m-q**i
        assert total[r]==gaussian(m,r,q)*p
    # Independently test an isotropic-pair condition on 600 sampled 4x4 maps.
    # This is a direct vector-level test, rather than the matrix identity.
    from random import Random
    rng=Random(1104)
    V=list(product(range(q),repeat=m))
    def omega(x,y):
        return sum(x[i]*y[i+m//2]-x[i+m//2]*y[i] for i in range(m//2))%q
    for _ in range(600):
        data=[rng.randrange(q) for j in range(m*m)]
        B=[data[i*m:(i+1)*m] for i in range(m)]
        M=[row+[0] for row in B]+[[0]*(m+1)]
        condition=True
        for x in V:
            for y in V:
                if omega(x,y)==0:
                    bx=tuple(sum(B[i][j]*x[j] for j in range(m))%q for i in range(m))
                    by=tuple(sum(B[i][j]*y[j] for j in range(m))%q for i in range(m))
                    if (omega(bx,y)+omega(x,by))%q!=0:
                        condition=False
        assert condition==csp_type(M,q,m)
    print('F2_H5_ISOTROPIC_PAIR_SAMPLES',600)
    print('F2_H5_CSP_QUOTIENT_COUNT',csp)
    print('F2_H5_QUOTIENT_MATRIX_RANKS',sorted(total.items()))
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
