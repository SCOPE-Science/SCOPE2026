#!/usr/bin/env python3
"""Direct finite-field checks of a modular matrix commutator census.
Runs using the Python standard library only.
"""
from itertools import product
from fractions import Fraction
from math import prod


def matmul(A, B, q, n):
    return [sum(A[i*n+k]*B[k*n+j] for k in range(n))%q
            for i in range(n) for j in range(n)]

def rank_augmented(cols, rhs, p):
    d=len(rhs)
    mat=[[cols[c][r] for c in range(d)]+[rhs[r]] for r in range(d)]
    rank=0
    for c in range(d):
        pivot=next((r for r in range(rank,d) if mat[r][c]%p),None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv=pow(mat[rank][c]%p,-1,p)
        mat[rank]=[(x*inv)%p for x in mat[rank]]
        for r in range(rank+1,d):
            coef=mat[r][c]%p
            if coef:
                mat[r]=[(a-coef*b)%p for a,b in zip(mat[r],mat[rank])]
        rank+=1
    return rank, all(any(x%p for x in row[:-1]) or row[-1]%p==0 for row in mat[rank:])

def exact_pred(n,q,p):
    vec=[Fraction(0) for _ in range(n+1)]
    vec[0]=Fraction(1)
    for j in range(1,n+1):
        if j%p:
            step=j; scalar=1
        else:
            step=j; scalar=q
        coeff=[Fraction(1)]
        for m in range(1,n//step+1):
            coeff.append(coeff[-1]*scalar/(1-Fraction(1,q**m)))
        out=[Fraction(0) for _ in range(n+1)]
        for i,a in enumerate(vec):
            for m,b in enumerate(coeff):
                if i+m*step<=n:
                    out[i+m*step]+=a*b
        vec=out
    gl=prod(q**n-q**i for i in range(n))
    ans=vec[n]*gl
    assert ans.denominator==1, (n,q,ans)
    return int(ans)

def check(n,p):
    q=p; d=n*n
    count=0
    feasible_y=0
    rank_fibers={}
    for yy in product(range(p),repeat=d):
        Y=list(yy)
        Y2=matmul(Y,Y,p,n)
        cols=[]
        for a in range(n):
            for b in range(n):
                col=[0]*d
                for i in range(n):
                    for j in range(n):
                        col[i*n+j]=((Y[b*n+j] if i==a else 0)-(Y[i*n+a] if j==b else 0))%p
                cols.append(col)
        rk,ok=rank_augmented(cols,Y2,p)
        if ok:
            feasible_y+=1
            count+=p**(d-rk)
            rank_fibers[rk]=rank_fibers.get(rk,0)+1
    predicted=exact_pred(n,q,p)
    assert count==predicted,(n,p,count,predicted)
    print(f'PASS p={p} n={n}: admissible Y={feasible_y}, solution pairs={count}, predicted={predicted}, commutator-rank histogram={rank_fibers}')

if __name__=='__main__':
    for n,p in [(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(1,5),(2,5)]:
        check(n,p)
    print('MODULAR_JORDAN_PLANE_DIRECT_MATRIX_CENSUS_PASS')

def check_gf4_n2():
    def mult(a,b):
        z=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:
                    z ^= 1<<(i+j)
        if z&8:
            z^=(8|4|2)
        if z&4:
            z^=(4|2|1)
        return z
    def mm(A,B):
        return [mult(A[i*2],B[j])^mult(A[i*2+1],B[2+j]) for i in range(2) for j in range(2)]
    els=list(product(range(4),repeat=4))
    total=0
    admiss=0
    for YY in els:
        y=list(YY)
        y2=mm(y,y)
        num=0
        for XX in els:
            x=list(XX)
            xy=mm(x,y); yx=mm(y,x)
            if all((xy[i]^yx[i])==y2[i] for i in range(4)):
                num+=1
        admiss+=(num>0)
        total+=num
    expected=exact_pred(2,4,2)
    assert total==expected
    print(f'PASS q=4 p=2 n=2: admissible Y={admiss}, solution pairs={total}, predicted={expected}')

if __name__=='__main__':
    check_gf4_n2()
