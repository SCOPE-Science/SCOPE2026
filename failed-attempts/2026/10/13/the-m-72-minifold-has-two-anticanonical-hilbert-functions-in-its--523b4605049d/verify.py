#!/usr/bin/env python3
from fractions import Fraction
from math import comb

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def eye(n):
    return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(x) for x in zip(*A)]

def inv(A):
    n=len(A)
    M=[[Fraction(A[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv=next(r for r in range(c,n) if M[r][c])
        M[c],M[piv]=M[piv],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                q=M[r][c]
                M[r]=[M[r][j]-q*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def add(A,B,scale=1):
    return [[A[i][j]+scale*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def power(A,k):
    R=eye(len(A))
    for _ in range(k):
        R=matmul(R,A)
    return R

def T_of(A):
    Ai=inv(A)
    return [[-x for x in row] for row in matmul(transpose(Ai),A)]

def coeffs(A):
    A=[[Fraction(x) for x in row] for row in A]
    T=T_of(A)
    N=add(T,eye(4),scale=-1)
    assert power(N,4)==[[Fraction(0)]*4 for _ in range(4)]
    out=[]
    for i in range(4):
        row=[]
        for k in range(4):
            M=matmul(A,power(N,k))
            row.append(M[i][i])
        out.append(row)
    return out

Apr=[[1,3,11,18],[0,1,6,11],[0,0,1,3],[0,0,0,1]]
Adu=[[1,3,7,6],[0,1,6,7],[0,0,1,3],[0,0,0,1]]

cpr=coeffs(Apr)
cdu=coeffs(Adu)
outer=[Fraction(1),Fraction(38),Fraction(108),Fraction(72)]
middle=[Fraction(1),Fraction(146),Fraction(432),Fraction(288)]
assert cpr==[outer,outer,outer,outer]
assert cdu==[outer,middle,middle,outer]

def eval_bin(c,p):
    return sum(c[k]*comb(p,k) for k in range(4))

def outer_poly(p):
    return 12*p**3+18*p**2+8*p+1

def middle_poly(p):
    return 48*p**3+72*p**2+26*p+1

# Polynomial identity is fixed by the binomial-basis coefficients;
# these four evaluations also check the expanded coefficient arithmetic.
for p in range(4):
    assert eval_bin(outer,p)==outer_poly(p)
    assert eval_bin(middle,p)==middle_poly(p)

def hilbert_numerator(vals):
    # coefficients of (1-t)^4 * sum h(p)t^p through degree 3;
    # a cubic polynomial gives no higher numerator terms.
    h=[vals(i) for i in range(4)]
    return [
        h[0],
        h[1]-4*h[0],
        h[2]-4*h[1]+6*h[0],
        h[3]-4*h[2]+6*h[1]-4*h[0],
    ]

assert hilbert_numerator(outer_poly)==[1,35,35,1]
assert hilbert_numerator(middle_poly)==[1,143,143,1]
assert Fraction(48,12)==4

print("standard_binomial_coefficients=1,38,108,72 x4")
print("right_dual_outer=1,38,108,72")
print("right_dual_middle=1,146,432,288")
print("outer_polynomial=12p^3+18p^2+8p+1")
print("middle_polynomial=48p^3+72p^2+26p+1")
print("outer_series_numerator=1,35,35,1")
print("middle_series_numerator=1,143,143,1")
print("leading_coefficient_ratio=4")
print("VERIFY_OK")
