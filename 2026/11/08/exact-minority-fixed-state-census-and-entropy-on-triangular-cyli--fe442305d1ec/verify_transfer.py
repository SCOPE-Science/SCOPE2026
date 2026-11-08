#!/usr/bin/env python3
"""Exact symbolic certificate for local fixed configurations of a triangular tube."""
import sympy as sp

X = sp.Symbol('X')


def allowed(a, b, c):
    """Three bits per column, each central bit sees >=2 opposite neighbors."""
    for j in range(3):
        bit = (b >> j) & 1
        ones = ((a >> j) & 1) + ((c >> j) & 1) + b.bit_count() - bit
        if (bit == 1 and ones > 2) or (bit == 0 and ones < 2):
            return False
    return True


def matrix():
    M = sp.zeros(64)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                if allowed(a, b, c):
                    M[8*a+b, 8*b+c] = 1
    return M


def powersums(poly, end):
    roots = sp.Poly(poly, X)
    degree = roots.degree()
    coeffs = [int(v) for v in roots.all_coeffs()]
    vals = [degree]
    for n in range(1, end+1):
        if n <= degree:
            value = -sum(coeffs[j]*vals[n-j] for j in range(1,n)) - n*coeffs[n]
        else:
            value = -sum(coeffs[j]*vals[n-j] for j in range(1, degree+1))
        vals.append(value)
    return vals

M = matrix()
C = X**3 - 3*X**2 - 3*X + 2
Q = X**4 + X**3 + 4*X**2 - 3*X + 3
expected = X**40*(X-2)*(X-1)**3*(X+1)**3*(X**2+X+1)**3*C*Q**2
cp = M.charpoly(X).as_expr()
assert sp.expand(cp-expected) == 0
print('64-by-64 symbolic characteristic polynomial: PASS')
print('matrix nonzero entries:', sum(int(M[i,j]) for i in range(64) for j in range(64)))
print('factor:',sp.factor(cp))
Sc = powersums(C, 20)
Sq = powersums(Q, 20)
N = sp.eye(64)
for n in range(1,15):
    N = N*M
    predicted = 2**n + 3*((-1)**n) + (9 if n%3==0 else 0) + Sc[n]+2*Sq[n]
    assert int(sp.trace(N)) == predicted, (n, sp.trace(N), predicted)
    if n>=3:
        print('length=%d fixed=%d'%(n,predicted))
print('trace formula through length 14: PASS')
print('root-bound certificate: at radius 3, 3^4=81 > 3^3+4*3^2+3*3+3=75.')
print('cubic: C(3)=-7, C(4)=6; other roots are in (-2,-1) and (0,1).')
