#!/usr/bin/env python3
"""Exact rational certificates and independent small-order matrix enumeration.
This program checks finite instances of the analytical one-defect projection theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial


def canonical(n):
    A=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j in ((0,1),(1,0),(1,2),(2,1)):
        A[i][j]=F(1)
    A[1][1]=F(-1)
    for i in range(3,n):
        A[i][i]=F(1)
    return A


def full_certificate(n):
    A=canonical(n)
    s=n+5
    h=[-F(1,s), F(1,2)+F(1,s), -F(1,s)]+[F(1,2*s)]*(n-3)
    X=[[max(F(0),A[i][j]-h[i]-h[j]) for j in range(n)] for i in range(n)]
    assert all(sum(row)==1 for row in X)
    assert all(sum(X[i][j] for i in range(n))==1 for j in range(n))
    assert all(X[i][j]>=0 for i in range(n) for j in range(n))
    assert sum((A[i][j]-X[i][j])**2 for i in range(n) for j in range(n))==2+F(2,s)
    assert all(X[i][j]==max(F(0), A[i][j]-h[i]-h[j]) for i in range(n) for j in range(n))
    assert all(X[i][j]==F(1,2) for i,j in ((0,1),(1,0),(1,2),(2,1)))
    assert all(X[i][j]==F(2,s) for i,j in product((0,2),repeat=2))
    for i in range(3,n):
        assert X[i][i]==1-F(1,s)
        for j in (0,2):
            assert X[i][j]==X[j][i]==F(1,2*s)
    return A,X


def partial_certificate(m,n):
    assert m>=3 and n>=3
    A=[[F(0) for j in range(n)] for i in range(m)]
    for i,j in ((0,1),(1,0),(1,2),(2,1)):
        A[i][j]=F(1)
    A[1][1]=F(-1)
    for i in range(3,min(m,n)):
        A[i][i]=F(1)
    Y=[[max(F(0),A[i][j]) for j in range(n)] for i in range(m)]
    for i,j in ((0,1),(1,0),(1,2),(2,1)):
        Y[i][j]=F(1,2)
    assert all(sum(row)<=1 for row in Y)
    assert all(sum(Y[i][j] for i in range(m))<=1 for j in range(n))
    assert all(z>=0 for row in Y for z in row)
    assert sum((A[i][j]-Y[i][j])**2 for i,j in product(range(m),range(n)))==2



def partial_asm_enum(m,n):
    # Enumerate all row-prefix-admissible patterns and enforce column prefixes.
    patterns=[]
    for row in product((-1,0,1),repeat=n):
        pre=0
        for z in row:
            pre+=z
            if pre not in (0,1):break
        else:
            patterns.append(row)
    def rec(rows,sums):
        if len(rows)==m:
            yield tuple(rows)
            return
        for row in patterns:
            new=tuple(a+b for a,b in zip(sums,row))
            if all(z in (0,1) for z in new):
                yield from rec(rows+[row],new)
    yield from rec([],tuple([0]*n))


def partial_one_defect_certificate(A):
    m=len(A);n=len(A[0]);neg=[(i,j) for i,j in product(range(m),range(n)) if A[i][j]==-1]
    assert len(neg)==1
    i,j=neg[0]
    arms_row=[k for k in range(n) if A[i][k]==1]
    arms_col=[k for k in range(m) if A[k][j]==1]
    a=len(arms_row);b=len(arms_col)
    assert a in (1,2) and b in (1,2)
    Y=[[F(z) for z in row] for row in A]
    Y[i][j]=F(0)
    if a==2:
        for k in arms_row:Y[i][k]=F(1,2)
    if b==2:
        for k in arms_col:Y[k][j]=F(1,2)
    assert all(z>=0 for row in Y for z in row)
    assert all(sum(row)<=1 for row in Y)
    assert all(sum(Y[k][l] for k in range(m))<=1 for l in range(n))
    assert sum((F(A[k][l])-Y[k][l])**2 for k in range(m) for l in range(n))==F(a+b,2)
    return (a,b)

def asm_enum(n):
    # Independent transfer enumeration using row patterns and prefix-column validity.
    patterns=[]
    for row in product((-1,0,1),repeat=n):
        if sum(row)!=1: continue
        nz=[v for v in row if v]
        if nz and all(v==((-1)**i) for i,v in enumerate(nz)):
            patterns.append(row)
    def rec(rows, sums):
        if len(rows)==n:
            if all(s==1 for s in sums):
                yield tuple(rows)
            return
        for row in patterns:
            new=tuple(s+v for s,v in zip(sums,row))
            if all(0<=s<=1 for s in new):
                yield from rec(rows+[row],new)
    yield from rec([],tuple([0]*n))


def main():
    count=0
    for n in range(3,51):
        full_certificate(n)
        count+=1
    for m in range(3,9):
        for n in range(3,9):
            partial_certificate(m,n)
    rectangular=0
    shells={}
    for m,n in ((2,3),(3,2),(3,3),(3,4),(4,3),(4,4),(4,5)):
        for A in partial_asm_enum(m,n):
            if sum(z==-1 for row in A for z in row)!=1:continue
            a,b=partial_one_defect_certificate(A)
            rectangular+=1
            shells[(a,b)]=shells.get((a,b),0)+1
    assert all((a,b) in shells for a,b in product((1,2),repeat=2))
    enum_count=0
    defect_count=0
    for n in (3,4,5):
        found=0
        for A in asm_enum(n):
            enum_count+=1
            if sum(z==-1 for row in A for z in row)!=1:
                continue
            found+=1
            defect_count+=1
            rs=sorted({i for i in range(n) if any(v==-1 for v in A[i]) or sum(v==1 for v in A[i])==2})
            # Reorder arbitrary one-defect ASM to canonical D3 plus identity by location,
            # independent row/column permutations using the support sets.
            ci=next(i for i in range(n) for j in range(n) if A[i][j]==-1)
            cj=next(j for i in range(n) for j in range(n) if A[i][j]==-1)
            arm_rs=[i for i in range(n) if A[i][cj]==1]
            arm_cs=[j for j in range(n) if A[ci][j]==1]
            row_order=[arm_rs[0],ci,arm_rs[1]]
            col_order=[arm_cs[0],cj,arm_cs[1]]
            remaining_r=[i for i in range(n) if i not in row_order]
            remaining_c=[]
            for i in remaining_r:
                cs=[j for j in range(n) if A[i][j]==1]
                assert len(cs)==1
                remaining_c.append(cs[0])
            row_order+=remaining_r
            col_order+=remaining_c
            cA,_=full_certificate(n)
            assert tuple(tuple(A[i][j] for j in col_order) for i in row_order)==tuple(tuple(row) for row in cA)
        assert found==comb(n,3)**2*factorial(n-3),(n,found)
    print(f'ONE_DEFECT_CERTIFICATES_PASS full_orders={count} partial_rectangles=36 partial_one_defect={rectangular} partial_shells={sorted(shells.items())} enumerated_ASM={enum_count} full_one_defect={defect_count}')

if __name__=='__main__': main()
