#!/usr/bin/env python3
"""Exact facet-normal and asymptotic checks for edge simplices of odd cycles."""
from fractions import Fraction as F
from math import acos, cos, pi, sqrt

def matmul(A, B):
    return [[sum(A[i][t]*B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def cycle_matrices(n):
    # Vertex i is e_i+e_(i+1), with indices taken modulo n.
    A = [[int(j == i or (j+1)%n == i) for j in range(n)] for i in range(n)]
    # Solve y_j = (x_j - y_(j-1)) cyclically for odd n.
    B = [[F((-1)**((i-j)%n), 2) for j in range(n)] for i in range(n)]
    assert matmul(B,A)==[[int(i==j) for j in range(n)] for i in range(n)], n
    return A,B

def formula(n,d):
    return F(1-(-1)**d*n*(n-2*d), n*n-1)

assert formula(3,1)==F(1,2)
check_count=0
for n in range(3,40,2):
    A,B=cycle_matrices(n)
    H=[[sum((B[i][q]-F(1,2*n))*(B[j][q]-F(1,2*n)) for q in range(n)) for j in range(n)] for i in range(n)]
    for i in range(n):
        assert H[i][i]==F(n*n-1,4*n)
        for j in range(i+1,n):
            d=min(j-i,n-(j-i))
            assert -H[i][j]/H[i][i] == formula(n,d), (n,i,j,d)
            check_count+=1
    assert sum(formula(n,d)>0 for d in range(1,(n-1)//2+1))==((n-1)//2+1)//2
    assert sum(formula(n,d)<0 for d in range(1,(n-1)//2+1))==((n-1)//2)//2

def kolmogorov_uniform_cos(n):
    k=(n-1)//2
    x=sorted(float(formula(n,d)) for d in range(1,k+1))
    return max(max(abs((j+1)/k-(v+1)/2), abs(j/k-(v+1)/2)) for j,v in enumerate(x))
for n in (101,501,2001,10001):
    delta=kolmogorov_uniform_cos(n)
    assert delta<8/n,(n,delta)
print(f'ODD_CYCLE_EDGE_SIMPLEX_PASS odd_orders=3..39 direct_normal_pairs={check_count} distribution_orders=101,501,2001,10001')
for n in (101,501,2001,10001):
    print('KOLMOGOROV',n,'%.8f'%kolmogorov_uniform_cos(n))
