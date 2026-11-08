"""Finite-field verification for rank-one, weight-zero Rota--Baxter maps on M_n.

Uses only standard Python.  A rank-one map is encoded as R(X)=tr(BX) A.
For each vector-space image line, A is first-nonzero-coordinate normalized;
then B ranges over all nonzero matrices.  Direct identity checks use matrix units.
"""
from itertools import product
from math import prod


def matrices(n, q):
    return [tuple(x) for x in product(range(q), repeat=n * n)]


def mul(a, b, n, q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def trmul(a,b,n,q):
    return sum(a[i*n+k]*b[k*n+i] for i in range(n) for k in range(n)) % q


def gauss(n,r,q):
    if r < 0 or r > n:
        return 0
    return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))


def gl(r,q):
    return prod(q**r-q**i for i in range(r))


def expected(n,q):
    sq = sum(gauss(n,r,q)*gauss(n-r,r,q)*gl(r,q)*(q**((n-r)**2)-1)//(q-1)
             for r in range(1,n//2+1))
    idem = 2*sum(gauss(n,r,q)*q**(r*(n-r))*(q**(r*(n-r))-1)
                 for r in range(1,n))
    return (sq, idem)


def classify_pair(a,b,n,q):
    zero=(0,)*(n*n)
    a2=mul(a,a,n,q)
    mu=next((u for u in range(q) if a2==tuple(u*x%q for x in a)),None)
    if mu is None:
        return None
    ab=mul(a,b,n,q)
    ba=mul(b,a,n,q)
    if mu == 0:
        return 'nilpotent' if ab==zero and ba==zero else None
    bb=tuple(mu*x%q for x in b)
    return 'idempotent' if ((ab==bb and ba==zero) or (ab==zero and ba==bb)) else None


def original_identity(a,b,n,q,units):
    a2=mul(a,a,n,q)
    for x in units:
        fx=trmul(b,x,n,q)
        xa=mul(x,a,n,q)
        for y in units:
            fy=trmul(b,y,n,q)
            v=(fx*trmul(b,mul(a,y,n,q),n,q)+fy*trmul(b,xa,n,q))%q
            if any((fx*fy*t-v*s)%q for t,s in zip(a2,a)):
                return False
    return True


def test(n,q,original_all=False):
    mm=matrices(n,q)
    u=[]
    for t in range(n*n):
        E=[0]*(n*n);E[t]=1;u.append(tuple(E))
    count={'nilpotent':0,'idempotent':0}
    seen=[]
    for a in mm[1:]:
        if next(v for v in a if v)!=1:
            continue
        for b in mm[1:]:
            kind=classify_pair(a,b,n,q)
            if kind is not None:
                count[kind]+=1
            if original_all:
                assert original_identity(a,b,n,q,u)==(kind is not None)
            elif len(seen)<100 and (kind is not None or ((sum(a)+sum(b))%11==0)):
                assert original_identity(a,b,n,q,u)==(kind is not None)
                seen.append((kind is not None))
    result=(count['nilpotent'], count['idempotent'])
    assert result==expected(n,q),(n,q,result,expected(n,q))
    print(f'M_{n}(F_{q}) full tensor representative count: nil={result[0]}, idempotent={result[1]}, total={sum(result)}; original basis identity checks='+ ('ALL' if original_all else str(len(seen))))


def main():
    test(2,2,True)
    test(2,3,True)
    test(3,2,False)
    for n,q in [(3,3),(4,2)]:
        x,y=expected(n,q)
        print(f'formula evaluation M_{n}(F_{q}): nil={x}, idempotent={y}, total={x+y}; not exhaustive')
    print('RANK_ONE_MATRIX_ROTA_BAXTER_EXACT_COUNTS_OK')

if __name__=='__main__':
    main()
