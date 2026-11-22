#!/usr/bin/env python3
"""Exact finite checks of gradient Hessian and inertia at representative closed polygons."""
import sympy as sp

def jac_and_inertia(w, a, c=sp.Integer(1), k=sp.Integer(1)):
    m=len(w)
    x=sp.symbols('x0:'+str(m))
    y=sp.symbols('y0:'+str(m))
    beta=[a[j]+m*c for j in range(m)]
    vec=[]
    for j in range(m):
        r2=x[j]**2+y[j]**2
        vec.append((beta[j]-k*r2-m*c)*x[j]+c*sum(x))
    for j in range(m):
        r2=x[j]**2+y[j]**2
        vec.append((beta[j]-k*r2-m*c)*y[j]+c*sum(y))
    var=list(x)+list(y)
    J=sp.Matrix(vec).jacobian(var).subs({x[j]:sp.re(w[j]) for j in range(m)} | {y[j]:sp.im(w[j]) for j in range(m)})
    J=sp.simplify(J)
    assert J==J.T
    assert all(sp.simplify(z)==0 for z in sp.Matrix(vec).subs({x[j]:sp.re(w[j]) for j in range(m)} | {y[j]:sp.im(w[j]) for j in range(m)}))
    ev=J.eigenvals()
    result={"positive":0,"negative":0,"zero":0}
    for e,mult in ev.items():
        e=sp.simplify(e)
        if e.is_zero is True: result['zero']+=mult
        elif e.is_positive is True: result['positive']+=mult
        elif e.is_negative is True: result['negative']+=mult
        else: raise AssertionError('symbolic eigenvalue sign not determined: '+str(e))
    return result, [(str(e),int(n)) for e,n in ev.items()]

w=[sp.Integer(1),sp.I,sp.Integer(-1),-sp.I]
out,ev=jac_and_inertia(w,[sp.Integer(1)]*4)
assert out=={'positive':2,'negative':4,'zero':2},(out,ev)
print('square: ',out,ev)

w=[sp.Integer(1),sp.Integer(1),sp.Integer(-1),sp.Integer(-1)]
for c,expected in [(sp.Rational(1,4),{'positive':1,'negative':4,'zero':3}), (sp.Rational(1,2),{'positive':1,'negative':3,'zero':4}), (sp.Integer(1),{'positive':2,'negative':3,'zero':3})]:
    out,ev=jac_and_inertia(w,[sp.Integer(1)]*4,c)
    assert out==expected,(c,out,ev)
    print('collinear c=',c, out,ev)

w=[sp.Integer(1),(-1+sp.sqrt(3)*sp.I)/2,(-1-sp.sqrt(3)*sp.I)/2]
out,ev=jac_and_inertia(w,[sp.Integer(1)]*3)
assert out=={'positive':2,'negative':3,'zero':1},(out,ev)
print('triangle: ',out,ev)
print('All exact fixed-point, symmetry, and inertia checks passed.')
