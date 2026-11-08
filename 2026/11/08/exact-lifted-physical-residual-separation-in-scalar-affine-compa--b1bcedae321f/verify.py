#!/usr/bin/env python3
"""Exact arithmetic checks for the scalar affine-parameter infinite-GMRES formulas.

Run: python verify.py
Requires SymPy. The accompanying proof, not these finite checks, covers all m.
"""
import sympy as sp


def check(c, s, m):
    assert s > 0 and c >= 0 and m >= 1
    T = sp.zeros(m + 1, m + 1)
    T[1, 0] = 1
    if m >= 2:
        T[1, 1] = -c
        for j in range(1, m):
            T[j + 1, j] = 1
    E = sp.zeros(m + 1, m)
    for j in range(m):
        E[j, j] = 1
    B = (sp.eye(m + 1) - s*T)*E
    rhs = sp.zeros(m + 1, 1)
    rhs[0] = 1
    v = (B.T*B).inv()*(B.T*rhs)
    r = rhs - B*v
    lifted_squared = sp.factor((r.T*r)[0])
    S = sum(s**(2*j) for j in range(m-1))
    predicted = sp.factor(s**(2*m)/(s**(2*m) + s**(2*m-2) + (1+s*c)**2*S))
    assert sp.simplify(lifted_squared - predicted) == 0
    assert sp.simplify(r[0] - predicted) == 0
    vv2 = v[1] if m >= 2 else sp.Integer(0)
    recovered = v[0] - c*vv2
    physical = sp.factor(1 - (1+c*s)*recovered)
    assert sp.simplify(physical - (1-c/s)*predicted) == 0
    return 1


def main():
    count = 0
    for c in map(sp.Rational,['0','1/4','1','2','5']):
        for s in map(sp.Rational,['1/3','1','3/2','2','5']):
            for m in range(1,8):
                count += check(c, s, m)
    x=sp.symbols('x',positive=True)
    limit_squared = 1/(1+x**(-2)+(1+x**2)**2/(x*x*(x*x-1)))
    assert sp.factor(limit_squared-(x*x-1)/(2*(x*x+1))) == 0
    print(f'PASS: {count} exact rational companion least-squares comparisons; one symbolic limiting identity.')


if __name__ == '__main__':
    main()
