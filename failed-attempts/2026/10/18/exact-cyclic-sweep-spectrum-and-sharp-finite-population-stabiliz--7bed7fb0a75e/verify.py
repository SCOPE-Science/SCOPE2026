#!/usr/bin/env python3
"""Exact checks for the cyclic complete-mean update theorem."""
import sympy as s
z=s.symbols('z')

def sweep(N,a):
    L=-s.Rational(a)
    M=s.eye(N)
    for i in range(N):
        U=s.eye(N)
        for j in range(N): U[i,j]=L/N
        M=U*M
    return M

def proposed(N,a):
    a=s.Rational(a)
    numerator=s.expand(N**N*z**(N+1)-((N-a)*z+a)**N)
    q,r=s.div(numerator,z-1,z)
    assert r==0
    return s.expand(q/N**N)

for N in range(1,9):
    for a in [s.Rational(1,2),s.Rational(4,3),s.Rational(N),s.Rational(N+2)]:
        M=sweep(N,a)
        observed=M.charpoly(z).as_expr()
        expected=proposed(N,a)
        assert s.simplify(observed-expected)==0,(N,a)
        assert s.det(M)==(-a/s.Integer(N))**N
        if a==N:
            assert s.expand(expected-s.Add(*[z**j for j in range(N+1)]))==0
            assert M**(N+1)==s.eye(N)
            assert sum([M**j for j in range(N+1)],s.zeros(N))==s.zeros(N)
    print('N',N,'verified')
print('VERIFY_OK')
