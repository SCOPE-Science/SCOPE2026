#!/usr/bin/env python3
"""Exact characteristic-seven bicanonical Hasse-Wronskian computation.
Needs sympy. All field operations are exact rational functions over GF(7)."""
from sympy.polys.fields import field
from sympy.polys.domains import GF
K, x = field('x', GF(7))
N = 9
zero, one = K.zero, K.one
R = x**4 + 1

def convolution(a, b):
    return [sum((a[j]*b[n-j] for j in range(n+1)),zero) for n in range(N)]

def power(a, k):
    v = [one] + [zero]*(N-1)
    for _ in range(k):
        v = convolution(v, a)
    return v

# In the affine coordinate Z=1, y^4=-(x^4+1).
# For t=x+h, y(t)=y*(sum a_n h^n), and (sum a_n h^n)^4
# equals (1+(x+h)^4)/(1+x^4) in GF(7)(x)[[h]].
target = [one] + [zero]*(N-1)
for n, coeff in enumerate([4*x**3, 6*x**2, 4*x, one],start=1):
    target[n] = coeff/R
Y = [one] + [zero]*(N-1)
for n in range(1,N):
    residue = power(Y,4)[n]
    Y[n] = (target[n] - residue)/4
assert all((a-b).numer == 0 for a,b in zip(power(Y,4),target))
Y2 = convolution(Y,Y)

def determinant3(n):
    # First three columns 1,x,x^2 pivot at Hasse orders 0,1,2.
    # Replace xy column by xy-x*y; the remaining rows are 3,4,n.
    M = [[Y[i], Y[i-1], Y2[i]] for i in (3,4,n)]
    return (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))

assert (Y[3]*Y[3]-Y[2]*Y[4]).numer != 0
assert determinant3(5).numer == 0
assert determinant3(6).numer == 0
# No floating-point computation: exact equality in GF(7)(x).
assert (determinant3(7)*R**14 - x**3*(x**24-1)).numer == 0
assert determinant3(7).numer != 0
# The full 6x6 Wronskian is y^4 times determinant3(7); y^4=-R.
# Thus W_x=-x^3*(x^24-1)/R^13, up to an invertible scalar.
print('FERMAT7_WRONSKIAN_SYMBOLIC_OK')
