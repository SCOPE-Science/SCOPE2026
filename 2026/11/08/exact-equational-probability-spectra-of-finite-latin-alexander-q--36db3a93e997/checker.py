#!/usr/bin/env python3
"""Exact finite-field checks for equational probability spectra of latin affine groupoids."""
from itertools import product


def eye(d):
    return tuple(tuple(int(i==j) for j in range(d)) for i in range(d))


def add(A,B,p):
    return tuple(tuple((a+b)%p for a,b in zip(ar,br)) for ar,br in zip(A,B))


def sub(A,B,p):
    return tuple(tuple((a-b)%p for a,b in zip(ar,br)) for ar,br in zip(A,B))


def mul(A,B,p):
    d=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(d))%p for j in range(d)) for i in range(d))


def matvec(A,x,p):
    return tuple(sum(a*b for a,b in zip(row,x))%p for row in A)


def rank(A,p):
    B=[list(row) for row in A]
    d=len(B); r=0
    for col in range(d):
        pivot=next((i for i in range(r,d) if B[i][col]%p),None)
        if pivot is None:continue
        B[r],B[pivot]=B[pivot],B[r]
        k=pow(B[r][col],-1,p)
        B[r]=[(a*k)%p for a in B[r]]
        for i in range(d):
            if i!=r and B[i][col]:
                c=B[i][col]
                B[i]=[(a-c*b)%p for a,b in zip(B[i],B[r])]
        r+=1
    return r


def polynomial_ring(T,p):
    d=len(T)
    I=eye(d); Z=tuple(tuple(0 for _ in range(d)) for _ in range(d))
    powers=[]; P=I
    for _ in range(d):
        powers.append(P);P=mul(P,T,p)
    R=set()
    for coeff in product(range(p),repeat=d):
        A=Z
        for c,P in zip(coeff,powers):
            for _ in range(c):A=add(A,P,p)
        R.add(A)
    return R


def run_case(p,T,name,expected):
    d=len(T); I=eye(d); U=sub(I,T,p); Z=sub(I,I,p)
    assert rank(T,p)==d and rank(U,p)==d, 'Latin hypothesis failed'
    R=polynomial_ring(T,p)
    C={Z:'y',I:'x'}
    changed=True
    while changed:
        changed=False
        entries=list(C.items())
        for a,expr_a in entries:
            for b,expr_b in entries:
                c=add(mul(T,a,p),mul(U,b,p),p)
                if c not in C:
                    C[c]='('+expr_a+'*'+expr_b+')'
                    changed=True
    assert set(C)==R,(name,len(C),len(R))
    vecs=list(product(range(p),repeat=d))
    observed=set()
    total_eq=0
    for A,expr in C.items():
        ra=rank(A,p)
        predicted=p**(2*d-ra)
        hits=0
        for x in vecs:
            for y in vecs:
                # Every term expression has coefficient A: t_A(x,y)=A x+(I-A)y.
                value=tuple((a+b)%p for a,b in zip(matvec(A,x,p),matvec(sub(I,A,p),y,p)))
                hits+=int(value==y)
                total_eq+=1
        assert hits==predicted, (name,expr,hits,predicted)
        observed.add(ra)
    assert observed==set(expected), (name,sorted(observed),sorted(expected))
    print(f'CASE {name}: p={p} d={d} ring={len(R)} term_coefficients={len(C)} probability_denominators={[p**r for r in sorted(observed)]} direct_binary_evaluations={len(R)*len(vecs)**2}')
    return total_eq


def companion(coeff,p):
    # Monic polynomial coeff=(c0,...,c_(d-1)); companion has columns e2,..,ed,-coeff.
    d=len(coeff)
    return tuple(tuple((1 if j==i-1 else 0) if j<d-1 else (-coeff[i])%p for j in range(d)) for i in range(d))


def main():
    cases=[
      (3,((2,0),(0,2)), 'scalar_F3^2', [0,2]),
      (3,((2,1),(0,2)), 'Jordan_2_F3', [0,1,2]),
      (5,((2,0),(0,3)), 'split_distinct_F5', [0,1,2]),
      (2,companion((1,1),2), 'irreducible_F4', [0,2]),
      (2,companion((1,0,1,0),2), 'primary_square_F16', [0,2,4]),
      (3,((2,1,0),(0,2,0),(0,0,2)), 'mixed_Jordan_F3', [0,1,3]),
    ]
    tot=0
    for p,T,name,expected in cases:
        tot+=run_case(p,T,name,expected)
    print('VERIFY_OK cases=6 evaluated='+str(tot))

if __name__=='__main__':main()
