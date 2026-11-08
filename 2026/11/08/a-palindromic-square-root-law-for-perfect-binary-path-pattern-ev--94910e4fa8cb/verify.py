"""Exact enumeration for perfect path-pattern evolution algebras over F_2."""
from itertools import product,permutations

def det_bit(diag):
    pprev,p=0,1
    for x in diag:
        pprev,p=p,(x*p+pprev)&1
    return p

def formula(n):
    return (2**(n+1)+(-1)**n)//3

def data(n):
    rows=[]
    for d in product(range(2),repeat=n):
        if det_bit(d):rows.append(d)
    pal=sum(d==d[::-1] for d in rows)
    assert len(rows)==formula(n),(n,len(rows),formula(n))
    assert pal==formula(n//2),(n,pal,formula(n//2))
    return rows,pal

def matrix_of(d):
    n=len(d)
    return [[int(i==j)*d[i] ^ int(abs(i-j)==1) for j in range(n)] for i in range(n)]

def monomial_fixes(M,p):
    n=len(M)
    return all(M[i][j]==M[p[i]][p[j]] for i in range(n) for j in range(n))

for n in range(2,13):
    rows,pal=data(n)
    if n<=6:
        for d in rows:
            M=matrix_of(d)
            perms=[p for p in permutations(range(n)) if monomial_fixes(M,p)]
            assert len(perms)==(2 if d==d[::-1] else 1),(n,d,perms)
    print(n,len(rows),pal,(len(rows)+pal)//2)
print('VERIFY_OK')
