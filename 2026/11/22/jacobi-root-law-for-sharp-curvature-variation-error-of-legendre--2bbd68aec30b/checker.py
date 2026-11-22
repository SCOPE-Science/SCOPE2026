#!/usr/bin/env python3
"""Reproducible symbolic checks for Legendre hinge-residual formulas.
This finite check supplements, and does not replace, the uniform-in-degree proof.
Requires sympy (tested with version 1.13+).
"""
import sympy as s
x,t=s.symbols('x t',real=True)
q=t*(1-t)
checks=0

def test(expr,tag):
    global checks
    v=s.cancel(s.together(s.expand(expr)))
    assert v==0,(tag,s.factor(v))
    checks+=1

base={}
for n in range(1,11):
    cs=[]
    for k in range(n+1):
        lk=s.legendre(k,2*x-1)
        ck=s.integrate((x-t)*lk,(x,t,1))
        cs.append(s.factor(ck))
        if k>=2:
            test(ck - t**2*(1-t)**2*s.jacobi(k-2,2,2,2*t-1)/(k*(k-1)),f'coeff k={k}')
        if k>=1:
            test(s.diff(ck,t)+t*(1-t)*s.jacobi(k-1,1,1,2*t-1)/k,f'coeff derivative k={k}')
    F=s.factor((1-t)**3/s.Integer(3)-sum((2*k+1)*cs[k]**2 for k in range(n+1)))
    if n<=3:base[n]=F
    test(s.diff(F,t) + t**2*(1-t)**2*s.jacobi(n-1,1,1,2*t-1)*s.jacobi(n,1,1,2*t-1)/(n*(n+1)),f'finite derivative n={n}')
    if n>=2:
        jac=s.jacobi(n-2,1,1,2*t-1)/(n-1)-s.jacobi(n,1,1,2*t-1)/(n+1)
        jac-=2*(2*n+1)*t*(1-t)*s.jacobi(n-2,2,2,2*t-1)/(n*(n-1))
        test(jac,f'contiguous identity n={n}')
test(base[1]-q**3/3,'n=1 exact expression')
test(base[2]-q**3*(4-15*q)/12,'n=2 exact expression')
test(base[3]-q**3*(1-9*q+21*q**2)/3,'n=3 exact expression')
test(base[2].subs(t,(5+s.sqrt(5))/10)-s.Rational(1,1500),'n=2 max value')
test(base[2].subs(t,s.Rational(1,2))-s.Rational(1,3072),'n=2 midpoint value')
test(base[3].subs(t,s.Rational(1,2))-s.Rational(1,3072),'n=3 max value')
assert s.Rational(1,3072)>s.Rational(1,7203)>s.Rational(1,9375)
checks+=1
print(f'PASS: {checks} exact symbolic checks; n=1,...,10; SymPy {s.__version__}.')
print('First three exact profiles:', [s.factor(base[n]) for n in (1,2,3)])
