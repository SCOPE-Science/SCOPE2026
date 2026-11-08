#!/usr/bin/env python3
"""Direct exhaustive finite checks for Rota--Baxter operators on a split square-zero algebra.
Usage: python verify.py. Python standard library only.
"""
from itertools import product
from math import prod


def rank_mod(A, q):
    A = [list(row) for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((j for j in range(r,m) if A[j][c]%q),None)
        if pivot is None: continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c] % q, -1, q)
        A[r] = [(a*inv)%q for a in A[r]]
        for j in range(m):
            if j!=r and A[j][c]:
                b=A[j][c]
                A[j] = [(x-b*y)%q for x,y in zip(A[j],A[r])]
        r+=1
        if r==m: break
    return r


def matmul(A,B,q):
    return tuple(tuple(sum(a*b for a,b in zip(row,col))%q for col in zip(*B)) for row in A)


def N(d,r,q):
    gauss=lambda n,k:prod((q**(n-i)-1)//1 for i in range(k))//prod(q**(k-i)-1 for i in range(k)) if k else 1
    # The separate products divide exactly, but integer division is performed once.
    A=gauss(d,r)
    B=gauss(d-r,r)
    GL=prod(q**r-q**i for i in range(r))
    return A*B*GL


def squarezero_profile(d,q):
    return [N(d,r,q) for r in range(d//2+1)]


def all_rows(n,q):
    return product(range(q),repeat=n)


def direct_rb_counts(d,q):
    n=d+1
    # q prime: exhaustive independent multiplication, rather than using the block normal form.
    vectors=list(product(range(q),repeat=n))
    pairs=[(x,y) for x in vectors for y in vectors]
    mul=lambda x,y:tuple(([x[0]*y[0]%q]+[(x[0]*y[i]+y[0]*x[i])%q for i in range(1,n)]))
    ops={}
    zero=(0,)*n
    good=0; rank2=0; rank3=0; jordan_counts={}
    for flat in product(range(q),repeat=n*n):
        P=tuple(tuple(flat[i*n+j] for j in range(n)) for i in range(n))
        def act(v):return tuple(sum(a*b for a,b in zip(row,v))%q for row in P)
        applied={v:act(v) for v in vectors}
        valid=True
        for x,y in pairs:
            a,b=applied[x],applied[y]
            z=tuple((u+v)%q for u,v in zip(mul(x,b),mul(a,y)))
            if mul(a,b)!=applied[z]:
                valid=False;break
        if valid:
            good+=1
            P2=matmul(P,P,q)
            key=(rank_mod(P,q),rank_mod(P2,q))
            jordan_counts[key]=jordan_counts.get(key,0)+1
            if P2!=tuple((0,)*n for _ in range(n)):
                rank3+=1
                assert matmul(P2,P,q)==tuple((0,)*n for _ in range(n))
            else:rank2+=1
    print('DIRECT_RB', 'q',q,'d',d, 'count',good,'P2zero',rank2,'P2nonzero',rank3)
    expected_jordan={}
    for r,num in enumerate(squarezero_profile(d,q)):
        if q%2==0:
            cases=[((r,0),q**r),((r+1,0),q**(d-r)-q**r),((r+1,1),q**d-q**(d-r))]
        else:cases=[((r,0),q**r),((r+1,0),q**(d-r)-q**r)]
        for key,k in cases:
            if k:
                expected_jordan[key]=expected_jordan.get(key,0)+num*k
    assert jordan_counts == expected_jordan,(q,d,jordan_counts,expected_jordan)
    print('JORDAN_RANK_PROFILE_OK',q,d,sorted(jordan_counts.items()))
    return good,rank2,rank3


def verify():
    for q,d in [(2,1),(2,2),(3,1),(3,2),(5,1)]:
        profile=squarezero_profile(d,q)
        even=(q%2==0)
        total=sum(profile)*(q**d) if even else sum(z*q**(d-r) for r,z in enumerate(profile))
        p2zero=sum(z*q**(d-r) for r,z in enumerate(profile))
        expected=(total,p2zero if even else total,total-p2zero if even else 0)
        actual=direct_rb_counts(d,q)
        assert actual==expected,(q,d,actual,expected)
        print('PROFILE_OK',q,d,profile,expected)
    for d in range(1,7):
        q=2
        profile=squarezero_profile(d,q)
        total=q**d*sum(profile)
        p3=sum(profile[r]*(q**d-q**(d-r)) for r in range(len(profile)))
        assert p3 == total-sum(profile[r]*q**(d-r) for r in range(len(profile)))
        print('LARGE_RANK_FORMULA',q,d,'total',total,'index3',p3,'fraction',round(p3/total,8))
    print('VERIFY_OK')

if __name__=='__main__':verify()
