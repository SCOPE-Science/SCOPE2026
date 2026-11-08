#!/usr/bin/env python3
"""Exact symbolic check of the four spectral Gram blocks and three capture laws."""
import sympy as s
n=s.symbols('n', integer=True, positive=True)

# Each spectral collision Gram matrix is C(3,r)/n^3 times M_r,
# with diagonal (n-1)^r and off-diagonal (-1)^r.
for r in range(4):
    diag=(n-1)**r
    off=(-1)**r
    standard=s.factor(diag-off)
    uniform=s.factor(diag+(n-1)*off)
    expected=[(0,n),(n,0),(n*(n-2),n*(n-1)),
              (n*(n*n-3*n+3),n*(n-1)*(n-2))][r]
    assert s.simplify(standard-expected[0])==0
    assert s.simplify(uniform-expected[1])==0

p={r:{t:s.expand(sum(s.binomial(t,j)*s.binomial(3-t,r-j)*
    (n-1)**j*(-1)**(r-j) for j in range(r+1)))
    for t in range(4)} for r in range(4)}
patterns={
 'triple':(1,{3:1,0:n-1}),
 'double':(3,{2:1,1:1,0:n-2}),
 'distinct':(6,{1:3,0:n-3}),
}
expected={
 'triple':s.Integer(1),
 'double':(n*n-2*n+2)/((n-1)*(n*n-3*n+3)),
 'distinct':6*(n-2)/((n-1)*(n*n-3*n+3)),
}
for label,(multiplicity,count) in patterns.items():
    total=0
    for r in range(4):
        S=s.expand(sum(z*p[r][t] for t,z in count.items()))
        Q=s.expand(sum(z*p[r][t]**2 for t,z in count.items()))
        if r==0:
            eta=s.Rational(multiplicity,1)/n**3
        elif r==1:
            assert s.simplify(S)==0
            eta=multiplicity*Q/(3*n**4)
        else:
            a=s.expand((n-1)**r-(-1)**r)
            b=(-1)**r
            eta=multiplicity/(n**3*s.binomial(3,r)) * (
                Q/a - b*S*S/(a*(a+n*b)))
        total+=eta
    assert s.simplify(total-expected[label])==0,(label,s.factor(total))
    print(label, s.factor(total))
assert s.simplify(expected['distinct']-expected['double']-
    (-n*n+8*n-14)/((n-1)*(n*n-3*n+3)))==0
print('dimension = binomial(n+2,3)-3*n for n>=3')
print('strict capture-order reversal occurs between n=5 and n=6')
print('SYMBOLIC CHECK PASSED')
