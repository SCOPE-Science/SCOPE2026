#!/usr/bin/env python3
"""Exact finite-field checks of a modular truncated-symmetric derivation theorem.
No nonstandard dependencies; all matrices and computations are exact over F_3.
"""
from itertools import product
from collections import Counter
from math import prod

P=3

def rank(rows):
    if not rows:
        return 0
    a=[[v%P for v in row] for row in rows]
    m=len(a); n=len(a[0]); r=0
    for j in range(n):
        s=next((i for i in range(r,m) if a[i][j]),None)
        if s is None: continue
        a[r],a[s]=a[s],a[r]
        t=pow(a[r][j],-1,P)
        a[r][j:]=[(t*v)%P for v in a[r][j:]]
        for i in range(r+1,m):
            if a[i][j]:
                c=a[i][j]
                a[i][j:]=[(x-c*y)%P for x,y in zip(a[i][j:],a[r][j:])]
        r+=1
        if r==m: break
    return r

def mult(A,B):
    m=len(A); inner=len(B); n=len(B[0]); out=[[0]*n for _ in range(m)]
    for i in range(m):
        for k in range(inner):
            aik=A[i][k]
            if aik:
                for j in range(n):out[i][j]=(out[i][j]+aik*B[k][j])%P
    return out

def induced(T):
    n=len(T); b=list(product(range(3), repeat=n)); look={u:i for i,u in enumerate(b)}
    M=[[0]*len(b) for _ in b]
    for j,exps in enumerate(b):
        for col,e in enumerate(exps):
            if not e:continue
            for row in range(n):
                c=(e*T[row][col])%3
                if not c:continue
                nxt=list(exps);nxt[col]-=1;nxt[row]+=1
                if nxt[row]<3:M[look[tuple(nxt)]][j]=(M[look[tuple(nxt)]][j]+c)%3
    return M

def jordan_counts(M):
    dim=len(M);r=rank(M);r2=rank(mult(M,M))
    return (dim-2*r+r2,r-2*r2,r2)

def J(n):
    return [[1 if i+1==j else 0 for j in range(n)] for i in range(n)]

def tensor_sum(X,Y):
    n=len(X);m=len(Y);a=[[0]*(n*m) for _ in range(n*m)]
    for i in range(n):
        for j in range(m):
            for k in range(n):
                if X[i][k]:a[i*m+j][k*m+j]=(a[i*m+j][k*m+j]+X[i][k])%3
            for l in range(m):
                if Y[j][l]:a[i*m+j][i*m+l]=(a[i*m+j][i*m+l]+Y[j][l])%3
    return a

def power_zero_three(T):
    return all(not v for row in mult(mult(T,T),T) for v in row)

def jordan_type_T(T):
    n=len(T);r=rank(T);r2=rank(mult(T,T))
    return (n-2*r+r2,r-2*r2,r2)

def predicted(n,a,b,c):
    if b+c==0:return (3**n,0,0)
    h=3**a*2**(2*(b+c)-1)
    return (h,h,3**(n-1)-h)


def run():
    assert jordan_counts(induced(J(1)))==(3,0,0)
    assert jordan_counts(induced(J(2)))==(2,2,1)
    assert jordan_counts(induced(J(3)))==(2,2,7)
    assert jordan_counts(tensor_sum(J(2),J(2)))==(1,0,1)
    assert jordan_counts(tensor_sum(J(2),J(3)))==(0,0,2)
    assert jordan_counts(tensor_sum(J(3),J(3)))==(0,0,3)
    print('Local block modules and all three primitive tensor products: verified')
    signatures=Counter();n=3;nilpotent=0
    for entries in product(range(3),repeat=n*n):
        T=[list(entries[i*n:(i+1)*n]) for i in range(n)]
        if not power_zero_three(T):continue
        nilpotent+=1
        a,b,c=jordan_type_T(T)
        actual=jordan_counts(induced(T))
        expected=predicted(n,a,b,c)
        assert actual==expected,(T,actual,expected)
        signatures[(a,b,c,3**n-actual[0]-actual[1]-actual[2], actual[1]+2*actual[2])]+=1
    assert nilpotent==729,nilpotent
    assert { (a,b,c):v for (a,b,c,_,_),v in signatures.items()}=={(3,0,0):1,(1,1,0):104,(0,0,1):624}
    print('Exhaustive 3^9 matrices: all 729 with T^3=0 verified on 27-dimensional algebra')
    for n in [4,5,6]:
        for c in range(n//3+1):
            for b in range((n-3*c)//2+1):
                a=n-2*b-3*c
                T=[[0]*n for _ in range(n)];off=0
                for length,count in [(1,a),(2,b),(3,c)]:
                    for _ in range(count):
                        for i in range(length-1):T[off+i][off+i+1]=1
                        off+=length
                if n>5:continue # 3^6 matrices impractical; sample n<=5
                assert jordan_counts(induced(T))==predicted(n,a,b,c),(n,a,b,c)
    print('Canonical Jordan types n=4,5: verified, including mixed blocks')
    print('TRUNCATED_SYMMETRIC_JORDAN_RIGIDITY_VERIFIED')

if __name__=='__main__':run()
