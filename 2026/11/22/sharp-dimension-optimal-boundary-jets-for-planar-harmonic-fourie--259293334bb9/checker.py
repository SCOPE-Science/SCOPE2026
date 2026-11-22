"""Independent finite checks for planar harmonic boundary-jet Fourier aliasing.

Run with Python >=3.9; standard library only. Finite checks support but do not
replace the all-degree polynomial-Vandermonde proof.
"""
from fractions import Fraction
from math import ceil, factorial, pi
import cmath


def falling(n, j):
    if j > n:
        return 0
    out = 1
    for u in range(j):
        out *= n-u
    return out


def fraction_rank(rows):
    if not rows:
        return 0
    a = [[Fraction(v) for v in row] for row in rows]
    nr, nc = len(a), len(a[0]); pivot = 0
    for c in range(nc):
        nxt = next((r for r in range(pivot, nr) if a[r][c]), None)
        if nxt is None: continue
        a[pivot], a[nxt] = a[nxt], a[pivot]
        d = a[pivot][c]
        for col in range(c, nc): a[pivot][col] /= d
        for r in range(pivot+1, nr):
            if not a[r][c]: continue
            q = a[r][c]
            for col in range(c, nc): a[r][col] -= q*a[pivot][col]
        pivot += 1
        if pivot == nr: break
    return pivot


def complex_rank(mat, atol=1e-7):
    if not mat: return 0
    a = [list(map(complex, row)) for row in mat]
    nr, nc = len(a), len(a[0]); rank = 0
    for col in range(nc):
        r = max(range(rank, nr), key=lambda u: abs(a[u][col]), default=None)
        if r is None or abs(a[r][col]) < atol: continue
        a[rank], a[r] = a[r], a[rank]
        val=a[rank][col]
        for j in range(col,nc): a[rank][j]/=val
        for u in range(rank+1,nr):
            mult=a[u][col]
            for j in range(col,nc): a[u][j]-=mult*a[rank][j]
        rank+=1
        if rank==nr:break
    return rank


def block(L,k,M,r):
    freq = [n for n in range(-L,L+1) if n%M==r]
    a = [[1 for n in freq]]
    a += [[falling(n,j) if n>0 else 0 for n in freq] for j in range(1,k+1)]
    a += [[falling(-n,j) if n<0 else 0 for n in freq] for j in range(1,k+1)]
    p=sum(n>0 for n in freq);q=sum(n<0 for n in freq)
    c=int(0 in freq)
    predicted=min(p,k)+min(q,k)+int(bool(c or p>k or q>k))
    return a, predicted


def full(L,k,M,R=1.0):
    freq=list(range(-L,L+1))
    rows=[]
    for t in range(M):
        z=cmath.exp(2j*pi*t/M)
        rows.append([R**abs(n)*z**n for n in freq])
        for j in range(1,k+1):
            rows.append([falling(n,j)*R**(n-j)*z**(n-j) if n>0 else 0 for n in freq])
            rows.append([falling(-n,j)*R**(-n-j)*z**(n+j) if n<0 else 0 for n in freq])
    return rows


def run():
    assertions=0
    for k in range(0,5):
        for L in range(0,17):
            for M in range(1,15):
                total=0
                for r in range(M):
                    a, predicted=block(L,k,M,r)
                    got=fraction_rank(a)
                    assert got==predicted,(k,L,M,r,got,predicted)
                    total+=got;assertions+=1
                target=ceil((2*L+1)/(2*k+1))
                assert (total==2*L+1)==(M>=target),(k,L,M,total,target)
                assertions+=1
    for k in range(0,4):
        for L in range(0,9):
            for M in range(1,12):
                predicted=sum(block(L,k,M,r)[1] for r in range(M))
                actual=complex_rank(full(L,k,M,R=1.0))
                assert actual==predicted,(k,L,M,actual,predicted)
                assertions+=1
    assert fraction_rank(block(4,1,3,0)[0])==3;assertions+=1
    assert fraction_rank(block(4,1,3,1)[0])==3;assertions+=1
    assert fraction_rank(block(4,1,3,2)[0])==3;assertions+=1
    print(f'PASS {assertions} exact-block/complex-matrix assertions')

if __name__=='__main__': run()
