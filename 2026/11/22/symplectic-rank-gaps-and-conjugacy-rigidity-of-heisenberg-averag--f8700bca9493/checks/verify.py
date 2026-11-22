#!/usr/bin/env python3
"""Direct finite tests for idempotent averaging on Heisenberg Lie algebras.
Run: python3 verify.py. Requires only the Python standard library.
"""
from itertools import product
from collections import Counter
from fractions import Fraction


def gaussian(n, r, q):
    ans = Fraction(1)
    for i in range(r):
        ans *= Fraction(q**(n-i)-1, q**(r-i)-1)
    assert ans.denominator == 1
    return int(ans)


def sp_order(m, q):
    result = q ** (m*m)
    for i in range(1, m+1):
        result *= q**(2*i)-1
    return result


def isotropic(m, r, q):
    return gaussian(m, r, q) * __import__('math').prod(q**(m-i)+1 for i in range(r))


def nondegenerate(m, r, q):
    return sp_order(m,q) // (sp_order(r,q)*sp_order(m-r,q))


def predicted(m,q):
    out=Counter()
    for r in range(m+1):
        out[r] += isotropic(m,r,q)*q**(r*(2*m-r+1))
        out[2*r+1] += nondegenerate(m,r,q)*q**(2*(m-r))
    return out


def rank_cols(columns, q):
    n = len(columns)
    mat = [[columns[j][i] % q for j in range(n)] for i in range(n)]
    row = 0
    for col in range(n):
        pivot = next((i for i in range(row,n) if mat[i][col] % q), None)
        if pivot is None: continue
        mat[row],mat[pivot] = mat[pivot],mat[row]
        t = pow(mat[row][col],-1,q)
        mat[row] = [(x*t)%q for x in mat[row]]
        for i in range(n):
            if i!=row and mat[i][col]:
                t=mat[i][col]
                mat[i] = [(x-t*y)%q for x,y in zip(mat[i],mat[row])]
        row+=1
    return row


def omega(a,b,m,q):
    return sum(a[i]*b[m+i]-a[m+i]*b[i] for i in range(m)) % q


def actual_identity(columns,m,q):
    n = 2*m+1
    ez=tuple(1 if i==n-1 else 0 for i in range(n))
    def act(colvec):
        return tuple(sum(colvec[j]*columns[j][i] for j in range(n))%q for i in range(n))
    if any(act(columns[i])!=columns[i] for i in range(n)):
        return False
    for i in range(n):
        for j in range(n):
            l = omega(columns[i],columns[j],m,q)
            b1 = omega(columns[i],tuple(int(k==j) for k in range(n)),m,q)
            b2 = omega(tuple(int(k==i) for k in range(n)),columns[j],m,q)
            if tuple((l*e)%q for e in ez)!=tuple((b1*t)%q for t in columns[-1]):return False
            if tuple((l*e)%q for e in ez)!=tuple((b2*t)%q for t in columns[-1]):return False
    return True


def exhaustive_3d(q):
    count=Counter()
    accepted=0
    for vals in product(range(q), repeat=9):
        cols=[tuple(vals[3*j+i] for i in range(3)) for j in range(3)]
        if actual_identity(cols,1,q):
            count[rank_cols(cols,q)]+=1
            accepted+=1
    assert count == predicted(1,q), (q,count,predicted(1,q))
    print('EXHAUSTIVE_ORIGINAL_IDENTITY',q, 'dim=3', dict(sorted(count.items())))


def omega_bin(a,b,m):
    return sum(((a>>i)&1)*((b>>(m+i))&1) + ((a>>(m+i))&1)*((b>>i)&1) for i in range(m))%2


def bin_rank(colbits,n):
    basis={}
    for v in colbits:
        t=v
        while t:
            p=t.bit_length()-1
            if p not in basis:
                basis[p]=t; break
            t ^=basis[p]
    return len(basis)


def exhaustive_5d_binary():
    # Enumeration over every 4x4 matrix A, both central scalars, and every
    # central row f, imposing idempotence and checking the ORIGINAL averaging
    # identities independently on the five basis pairs.
    m=2; n=4; ct=Counter()
    e=[1<<i for i in range(n)]
    for A in product(range(16),repeat=4):
        def apply(v):
            w=0
            for i in range(n):
                if v>>i&1:w ^=A[i]
            return w
        if any(apply(A[i]) != A[i] for i in range(n)):
            continue
        for c in (0,1):
            if any(omega_bin(A[i],A[j],m) != c*omega_bin(A[i],e[j],m) or
                   omega_bin(A[i],A[j],m) != c*omega_bin(e[i],A[j],m)
                   for i in range(n) for j in range(n)):
                continue
            for f in range(16):
                if any(((f&A[i]).bit_count()%2)^ (c*((f>>i)&1)) != ((f>>i)&1) for i in range(n)):
                    continue
                colbits=[A[i] | (((f>>i)&1)<<n) for i in range(n)] + [c<<n]
                def apply_full(v):
                    w=0
                    for i in range(n+1):
                        if v>>i&1:w ^=colbits[i]
                    return w
                assert all(apply_full(colbits[i])==colbits[i] for i in range(n+1))
                for i in range(n+1):
                    for j in range(n+1):
                        o=omega_bin(colbits[i]&15,colbits[j]&15,m)
                        l=o<<n
                        rhs1=omega_bin(colbits[i]&15, (1<<j) if j<n else 0,m)*colbits[-1]
                        rhs2=omega_bin((1<<i) if i<n else 0,colbits[j]&15,m)*colbits[-1]
                        assert l==rhs1==rhs2, (A,c,f,i,j)
                ct[bin_rank(colbits,n+1)]+=1
    assert ct==predicted(m,2), (ct,predicted(m,2))
    print('EXHAUSTIVE_REDUCED_AND_ORIGINAL',2,'dim=5',dict(sorted(ct.items())))


if __name__ == '__main__':
    exhaustive_3d(2)
    exhaustive_3d(3)
    exhaustive_5d_binary()
    for m in range(1,5):
        for q in (2,3,5,9):
            a=predicted(m,q)
            assert a[0]==1 and a[2*m+1]==1
            assert set(a)==set(range(m+1))|set(range(1,2*m+2,2))
    print('HEISENBERG_AVERAGING_PROJECTIONS_VERIFIED')
