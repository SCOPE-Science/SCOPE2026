#!/usr/bin/env python3
"""Finite-field checks for the harmonic-quartic middle-rank theorem."""
from math import comb


def rank_mod(matrix, p):
    a = [row[:] for row in matrix]
    nrows = len(a)
    ncols = len(a[0]) if nrows else 0
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, nrows) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        for r in range(rank + 1, nrows):
            mult = (a[r][col] * inv) % p
            if mult:
                for c in range(col, ncols):
                    a[r][c] = (a[r][c] - mult * a[rank][c]) % p
        rank += 1
        if rank == nrows:
            break
    return rank


def determinant_mod(matrix, p):
    a = [row[:] for row in matrix]
    n = len(a)
    ans = 1
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col] % p), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            ans = -ans
        z = a[col][col] % p
        ans = ans * z % p
        iz = pow(z, -1, p)
        for row in range(col+1, n):
            w = a[row][col] * iz % p
            if w:
                for c in range(col, n):
                    a[row][c] = (a[row][c] - w*a[col][c]) % p
    return ans % p


def quartic_cube(p, lam):
    # f=x*y*(x-y)*(x-lam*y); f^3 has degree 12.
    # Its term x^(3+s+t)y^(9-s-t) has coefficient
    # (-1)^(6-s-t)*binom(3,s)*binom(3,t)*lam^(3-t).
    terms = [0] * 13
    for s in range(4):
        for t in range(4):
            coef = (-1)**(6-s-t)*comb(3,s)*comb(3,t)*pow(lam,3-t,p)
            terms[3+s+t] = (terms[3+s+t]+coef)%p
    return terms


def middle_matrix(p, lam):
    coeffs = quartic_cube(p,lam)
    n = p-6
    return [[coeffs[6+j-i] if 0 <= 6+j-i <= 12 else 0
             for i in range(n)] for j in range(n)]


def graded_rank(p, lam, t):
    coeffs = quartic_cube(p, lam)
    src = [(i,t-i) for i in range(max(0,t-p+1),min(t,p-1)+1)]
    u = t+12
    dst = [(i,u-i) for i in range(max(0,u-p+1),min(u,p-1)+1)] if u<=2*p-2 else []
    if not src or not dst:
        return 0, min(len(src),len(dst))
    row = {pair:j for j,pair in enumerate(dst)}
    mat = [[0]*len(src) for _ in dst]
    for i,(a,b) in enumerate(src):
        for e,coef in enumerate(coeffs):
            if not coef:
                continue
            j=row.get((a+e,b+12-e))
            if j is not None:
                mat[j][i] = coef
    return rank_mod(mat,p),min(len(src),len(dst))


def minor_harmonic(p):
    m=(p-7)//2
    c=[-1,3,-3,1]
    B=[[c[s] if 0<= (s:=m+1-a-b)<=3 else 0 for b in reversed(range(m))] for a in range(m)]
    return determinant_mod(B,p), ((-1)**m * comb(m+2,2))%p


def run():
    for p in [7,11,13,17,19,23,29,31]:
        n=p-6
        vals={}
        for name,lam in [('degenerate',0),('harmonic_-1',p-1),('harmonic_2',2),('harmonic_half',pow(2,-1,p)),('trial_3',3)]:
            vals[name]=rank_mod(middle_matrix(p,lam),p)
        assert vals['degenerate']==n
        assert all(vals[z]==n-1 for z in ('harmonic_-1','harmonic_2','harmonic_half'))
        det, expected=minor_harmonic(p)
        assert det==expected and det!=0
        assert determinant_mod(middle_matrix(p,0),p)==(-1)**n%p
        # The full degenerate cubic multiplication has maximal graded rank.
        for t in range(2*p-1):
            actual,bound=graded_rank(p,0,t)
            assert actual==bound, (p,t,actual,bound)
        print(f'p={p} n={n} middle={vals} harmonic_minor={det} generic_total_bound={n*n} PASS')
    print('ALL_HARMONIC_QUARTIC_MIDDLE_RANK_CHECKS_PASS')

if __name__=='__main__':
    run()
