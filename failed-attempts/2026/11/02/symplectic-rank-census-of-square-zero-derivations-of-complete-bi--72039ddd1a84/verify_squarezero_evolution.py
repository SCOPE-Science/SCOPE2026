"""Exhaustive tests for square-zero derivations of complete-bipartite evolution algebras.

Uses direct finite-field matrix multiplication and Gaussian elimination.
No mathematical proof is delegated to this script.
"""
from itertools import product
from fractions import Fraction


def mul(a, b, q):
    if q == 2:
        return a & b
    poly = {4: 0b111, 8: 0b1011}[q]
    deg = q.bit_length() - 1
    t = 0
    while b:
        if b & 1:
            t ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= poly
    return t


def inverse(a, q):
    assert a
    for b in range(1, q):
        if mul(a, b, q) == 1:
            return b
    raise AssertionError('noninvertible nonzero field element')


def rank(A, q):
    B = [row[:] for row in A]
    n = len(B)
    width = len(B[0]) if B else 0
    pivot = 0
    for j in range(width):
        k = next((i for i in range(pivot, n) if B[i][j]), None)
        if k is None:
            continue
        B[pivot], B[k] = B[k], B[pivot]
        u = inverse(B[pivot][j], q)
        for c in range(j, width):
            B[pivot][c] = mul(B[pivot][c], u, q)
        for i in range(pivot+1, n):
            t = B[i][j]
            if t:
                for c in range(j, width):
                    B[i][c] ^= mul(t, B[pivot][c], q)
        pivot += 1
        if pivot == n:
            break
    return pivot


def symmetric_form_count(r, q):
    if r == 0:
        return 1
    p, c = 1, q-1
    for j in range(2, r+1):
        p, c = c, (q-1)*q**(j-1)*c + (q**(j-1)-1)*q**(j-1)*p
    return c


def symplectic_isotropic_count(h, r, q):
    z = Fraction(1)
    for i in range(r):
        z *= Fraction(q**(2*h-i)-q**i, q**r-q**i)
    assert z.denominator == 1
    return z.numerator


def predicted(m, q):
    if m % 2:
        h = m//2
        return [symplectic_isotropic_count(h,r,q)*symmetric_form_count(r,q)
                for r in range(h+1)]
    h = m//2
    out = [0]*(h+1)
    for r in range(h):
        t = symplectic_isotropic_count(h-1,r,q)*symmetric_form_count(r,q)
        out[r] += t*q**r
        out[r+1] += t*(q-1)*q**r
        if r+2 <= h:
            out[r+2] += t*q*(q**(2*h-2-r)-q**r)
    return out


def matrix_from_edges(m, coeff):
    M = [[0]*m for _ in range(m)]
    j=0
    for a in range(m):
        for b in range(a+1,m):
            c=coeff[j]
            j+=1
            M[a][b] = c
            M[b][a] = c
            M[a][a] ^= c
            M[b][b] ^= c
    return M


def is_square_zero(A, q):
    m = len(A)
    for i in range(m):
        for j in range(m):
            s = 0
            for k in range(m):
                s ^= mul(A[i][k], A[k][j], q)
            if s:
                return False
    return True


def direct_spectrum(m,q):
    spec=[0]*(m//2+1)
    for a in product(range(q),repeat=m*(m-1)//2):
        M=matrix_from_edges(m,a)
        if is_square_zero(M,q):
            spec[rank(M,q)]+=1
    return spec


def is_derivation(D,r,s,q):
    n=r+s
    sq=[]
    for i in range(n):
        vec=[0]*n
        if i<r:
            for j in range(r,n):vec[j]=1
        else:
            for j in range(r):vec[j]=1
        sq.append(vec)
    # D(e_i^2)=2e_i D(e_i)=0, and D(e_i)e_j+e_iD(e_j)=0 for distinct i,j.
    for i in range(n):
        for c in range(n):
            z=0
            for j in range(n):
                z ^= mul(sq[i][j],D[c][j],q)
            if z:return False
    for i in range(n):
        for j in range(i+1,n):
            for c in range(n):
                if mul(D[j][i],sq[j][c],q)^mul(D[i][j],sq[i][c],q):
                    return False
    return True


def direct_all_derivations(r,s,q):
    n=r+s
    total=0
    squared=0
    for a in product(range(q),repeat=n*n):
        D=[list(a[i*n:(i+1)*n]) for i in range(n)]
        if is_derivation(D,r,s,q):
            total+=1
            if is_square_zero(D,q):squared+=1
    return total,squared


def main():
    cases = [(2,m) for m in range(1,7)] + [(4,m) for m in range(1,5)] + [(8,2),(8,3),(8,4)]
    for q,m in cases:
        actual=direct_spectrum(m,q)
        want=predicted(m,q)
        assert actual==want,(q,m,actual,want)
        print('PASS',f'GF({q})','m',m,'ranks',actual)
    for r,s,q in [(1,2,2),(2,2,2)]:
        nder,nsquare=direct_all_derivations(r,s,q)
        exp_der=q**(r*(r-1)//2+s*(s-1)//2)
        exp_sq=sum(predicted(r,q))*sum(predicted(s,q))
        assert (nder,nsquare)==(exp_der,exp_sq),(r,s,q,nder,nsquare,exp_der,exp_sq)
        print('LEIBNIZ',r,s,q,nder,nsquare)
    print('EVOLUTION_SQUARE_ZERO_RANK_OK',len(cases),'spectra; 2 full Leibniz enumerations')


if __name__=='__main__':
    main()
