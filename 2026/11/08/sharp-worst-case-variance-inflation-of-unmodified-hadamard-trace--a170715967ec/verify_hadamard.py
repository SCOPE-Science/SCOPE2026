#!/usr/bin/env python3
"""Exact finite-population verification of structured trace-probe variance identities.

All matrix data and variance checks use integer or Fraction arithmetic.
"""
from fractions import Fraction
from itertools import combinations, product
from random import Random

checks = 0

def confirm(test, desc):
    global checks
    checks += 1
    if not test:
        raise AssertionError(desc)


def dot_quad(z, A):
    return sum(z[i]*A[i][j]*z[j] for i in range(len(z)) for j in range(len(z)))


def hadamard(n):
    return [[(-1 if ((r & j).bit_count() % 2) else 1) for j in range(n)] for r in range(n)]


def finite_pop_var(q, k):
    n=len(q)
    mean=Fraction(sum(q),n)
    popv=sum((Fraction(x)-mean)**2 for x in q)/n
    return Fraction(n-k,k*(n-1))*popv


def direct_row_var(q,k):
    values=[Fraction(sum(q[r] for r in ind),k) for ind in combinations(range(len(q)),k)]
    mu=Fraction(sum(values),len(values))
    return sum((x-mu)**2 for x in values)/len(values)


def test_matrix(A):
    n=len(A)
    H=hadamard(n)
    tr=sum(A[i][i] for i in range(n))
    q=[dot_quad(h,A) for h in H]
    confirm(sum(q)==n*tr, f'unbiased {n}')
    C=[sum(A[i][i^s] for i in range(n)) for s in range(1,n)]
    popv=sum(x*x for x in C)
    confirm(Fraction(sum((x-tr)**2 for x in q),n)==popv, f'Walsh Parseval {n}')
    sum_pairs=sum(A[i][j]**2 for i in range(n) for j in range(i+1,n))
    iid_var=lambda k:Fraction(4*sum_pairs,k)
    for k in range(1,n+1):
        v=finite_pop_var(q,k)
        exact=Fraction(n-k,k*(n-1))*popv
        confirm(v==exact, f'row variance formula {n} {k}')
        confirm(v<=Fraction(n*(n-k),2*(n-1))*iid_var(k),f'worst-case bound {n} {k}')
        if n==4 or k in (1,2,n-1,n):
            confirm(direct_row_var(q,k)==v,f'exhaustive subsampling {n} {k}')
    # Exhaust all diagonal signings: sample each independent sign bit shared among rows.
    total_popv=Fraction(0)
    for signs in product((-1,1),repeat=n):
        signed_q=[dot_quad([H[r][i]*signs[i] for i in range(n)],A) for r in range(n)]
        confirm(sum(signed_q)==n*tr, f'sign-unbiased {n}')
        total_popv+=Fraction(sum((x-tr)**2 for x in signed_q),n)
    mean_popv=total_popv/(2**n)
    confirm(mean_popv==4*sum_pairs,f'sign-averaged Walsh energy {n}')
    for k in range(1,n+1):
        signed_variance=Fraction(n-k,k*(n-1))*mean_popv
        confirm(signed_variance==Fraction(n-k,n-1)*iid_var(k),f'signed variance {n} {k}')

rng=Random(1019)
for n in (2,4,8):
    for sample in range(2 if n<8 else 3):
        R=[[rng.randrange(-3,4) for _ in range(n)] for _ in range(n)]
        A=[[sum(R[t][i]*R[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        test_matrix(A)
    for s in range(1,n):
        # I + (1/2) P_s is strictly positive definite. Avoid floating point by using 2I + P_s.
        A=[[2 if i==j else (1 if (i^j)==s else 0) for j in range(n)] for i in range(n)]
        test_matrix(A)
        sum_pairs=n//2
        q=[dot_quad(h,A) for h in hadamard(n)]
        for k in range(1,n):
            v=finite_pop_var(q,k)
            iid=Fraction(4*sum_pairs,k)
            confirm(v==Fraction(n*(n-k),2*(n-1))*iid,f'extremal matching n={n} s={s} k={k}')

# Independently enumerate signed-and-row-sampled variance for n=4, k=2 on asymmetric PSD Gram matrix.
n=4;k=2
R=[[1,2,0,-1],[3,-1,2,0],[0,1,1,2],[2,0,-1,3]]
A=[[sum(R[t][i]*R[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
H=hadamard(n)
vals=[]
for signs in product((-1,1),repeat=n):
    q=[dot_quad([H[r][i]*signs[i] for i in range(n)],A) for r in range(n)]
    for rows in combinations(range(n),k):
        vals.append(Fraction(sum(q[r] for r in rows),k))
mu=sum(vals)/len(vals)
var=sum((x-mu)**2 for x in vals)/len(vals)
iid_var=Fraction(4*sum(A[i][j]**2 for i in range(n) for j in range(i+1,n)),k)
confirm(mu==sum(A[i][i] for i in range(n)),'independently sampled mean')
confirm(var==Fraction(n-k,n-1)*iid_var,'full enumeration signed variance')
print(f'PASS {checks} exact variance and equality assertions')
print('n=8,k=3,matching worst-case inflation:',Fraction(8*(8-3),2*(8-1)))
print('n=8,k=7 universal upper ratio:',Fraction(8,2*7))
print('signed-Hadamard improvement for n=8,k=3:',Fraction(8-3,8-1))
