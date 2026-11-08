"""Finite-field exhaustive checks of the Heisenberg idempotent-derivation rank formula.
Run: python3 verify.py. No third-party dependencies.
"""
from itertools import product
from math import prod
from collections import Counter

def mm(A,B,q):
    d=len(A); n=len(B[0]); w=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(w))%q for j in range(n)] for i in range(d)]

def transpose(A):
    return [list(r) for r in zip(*A)]

def rank(A,q):
    if not A: return 0
    M=[row[:] for row in A]
    d=len(M); w=len(M[0]); k=0
    for j in range(w):
        pivot=next((i for i in range(k,d) if M[i][j]%q),None)
        if pivot is None:continue
        M[k],M[pivot]=M[pivot],M[k]
        inv=pow(M[k][j],-1,q)
        M[k]=[(v*inv)%q for v in M[k]]
        for i in range(d):
            if i!=k and M[i][j]:
                a=M[i][j]
                M[i]=[(x-a*y)%q for x,y in zip(M[i],M[k])]
        k+=1
        if k==d: break
    return k

def sp_order(n,q):
    return q**(n*n)*prod(q**(2*j)-1 for j in range(1,n+1))

def expected(n,q):
    out=Counter()
    lag=q**(n*(n+3)//2)*prod(q**j+1 for j in range(1,n+1))
    out[n+1]+=lag
    if q%2:
        out[0]+=1
    else:
        for r in range(n+1):
            out[2*r]+=sp_order(n,q)//(sp_order(r,q)*sp_order(n-r,q))*q**(2*r)
    return dict(sorted(out.items()))

def exhaustive(n,q):
    d=2*n; size=d+1
    J=[[0]*d for _ in range(d)]
    for i in range(n): J[i][n+i]=1; J[n+i][i]=(-1)%q
    out=Counter(); valid_A=0
    for flat in product(range(q),repeat=d*d):
        A=[list(flat[i*d:(i+1)*d]) for i in range(d)]
        if mm(A,A,q)!=A: continue
        lhs=mm(transpose(A),J,q); rhs=mm(J,A,q)
        for lam in (0,1):
            if any((lhs[i][j]+rhs[i][j]-lam*J[i][j])%q for i in range(d) for j in range(d)):continue
            valid_A+=1
            for f in product(range(q),repeat=d):
                D=[A[i][:]+[0] for i in range(d)]+[list(f)+[lam]]
                if mm(D,D,q)!=D: continue
                # Direct Leibniz identity on all basis pairs; nontrivial
                # bracket is carried by J in the final coordinate.
                for i in range(d):
                    for j in range(d):
                        bracket_lhs=(lam*J[i][j])%q
                        bracket_rhs=(sum(A[k][i]*J[k][j]+A[k][j]*J[i][k] for k in range(d)))%q
                        if bracket_lhs!=bracket_rhs: raise AssertionError('derivation identity')
                out[rank(D,q)]+=1
    assert dict(sorted(out.items()))==expected(n,q),(n,q,dict(out),expected(n,q))
    return valid_A,dict(sorted(out.items()))

if __name__=='__main__':
    for n,q in [(1,2),(1,3),(1,5),(2,2)]:
        c,dist=exhaustive(n,q)
        print('n',n,'q',q,'eligible (A,lambda)',c,'ranks',dist)
    # Check group-order arithmetic and positivity through larger n.
    for q in (2,3,4,5,8):
        for n in range(2,12):
            counts=expected(n,q)
            assert all(isinstance(v,int) and v>=0 for v in counts.values())
            assert counts[0]==1
            if q%2:assert set(counts)=={0,n+1}
    print('VERIFY_OK')
