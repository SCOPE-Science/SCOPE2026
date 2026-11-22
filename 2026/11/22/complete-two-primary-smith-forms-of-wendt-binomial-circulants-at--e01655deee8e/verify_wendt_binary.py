"""Finite exact checks for binary Smith invariants of binomial circulants.

All arithmetic is integer or over Z/4Z. The argument for arbitrary exponents
is mathematical; these computations are finite spot checks, not a proof.
"""
from math import comb
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def binomial_circulant(n):
    a = [comb(n, k) for k in range(n)]
    return [[a[(j-i) % n] for j in range(n)] for i in range(n)]


def rank_mod2(a):
    a = [row[:] for row in a]
    h = len(a)
    if not h:
        return 0
    w = len(a[0]); piv = 0
    for j in range(w):
        k = next((i for i in range(piv, h) if a[i][j] & 1), None)
        if k is None:
            continue
        a[piv], a[k] = a[k], a[piv]
        for i in range(piv + 1, h):
            if a[i][j] & 1:
                for c in range(j, w):
                    a[i][c] = (a[i][c] ^ a[piv][c]) & 1
        piv += 1
        if piv == h:
            break
    return piv


def smith_binary_two_levels(mat):
    a = [[v % 4 for v in row] for row in mat]
    n = len(a)
    k = 0
    while k < n:
        pair = next(((i,j) for i in range(k,n) for j in range(k,n)
                     if a[i][j] % 2),None)
        if pair is None:
            break
        i,j = pair
        a[k],a[i]=a[i],a[k]
        for row in a:
            row[k],row[j]=row[j],row[k]
        inv = a[k][k] # 1 and 3 self-inverse mod 4
        for i in range(k+1,n):
            if a[i][k]:
                c=a[i][k]*inv % 4
                for j in range(k+1,n):
                    a[i][j]=(a[i][j]-c*a[k][j])%4
                a[i][k]=0
        k+=1
    assert all(a[i][j]%2==0 for i in range(k,n) for j in range(k,n))
    second = rank_mod2([[a[i][j]//2 for j in range(k,n)] for i in range(k,n)])
    return k,second


def expected(n, family, r):
    if family == 'minus':
        return 1,n-1
    return (n-2,2) if r%2 else (n,0)


def check_family():
    trials = []
    for family in ('minus', 'plus'):
        for r in range(1,8 if family=='minus' else 7):
            n=2**r+(-1 if family=='minus' else 1)
            got=smith_binary_two_levels(binomial_circulant(n))
            target=expected(n,family,r)
            assert got == target, (family,r,n,got,target)
            trials.append((family,r,n,*got))
    return trials


def check_exact_snf():
    trials=[]
    for n in [1,3,5,7,9,15,17]:
        mat=Matrix(binomial_circulant(n))
        S=smith_normal_form(mat,domain=ZZ)
        vals=[]
        for i in range(n):
            x=abs(int(S[i,i])); v=0
            while x>0 and x%2==0:
                x//=2;v+=1
            vals.append(v)
        if n in (1,3,7,15):
            exp=[0]+[1]*(n-1)
        elif n in (5,17):
            exp=[0]*n
        elif n ==9:
            exp=[0]*(n-2)+[1]*2
        assert vals==exp,(n,vals,exp)
        trials.append((n, vals.count(0), vals.count(1)))
    return trials


def check_binomial_identity():
    for r in range(1,12):
        m=2**r
        for k in range(1,m):
            target=2 if k==m//2 else 0
            assert comb(m,k)%4==target,(r,k)
    return 11


def main():
    print('Fermat-neighbor modular Smith trials (family, exponent, size, units, 2-factors):')
    for x in check_family(): print(*x)
    print('Exact integral Smith trials (size, odd factors, valuation-one factors):')
    for x in check_exact_snf(): print(*x)
    print('Binomial coefficient mod-four identity verified for r<=',check_binomial_identity())
    print('PASS: all finite checks')

if __name__=='__main__':
    main()
