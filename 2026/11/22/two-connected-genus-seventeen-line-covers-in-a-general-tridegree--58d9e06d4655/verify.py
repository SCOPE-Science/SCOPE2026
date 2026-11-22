"""Exact finite-field witness for generality of the line-cover theorem.

This verifies existence of an integral tridegree-(2,2,2) model with smooth
branch surface, two smooth (4,4) discriminants, reduced eight-point
coefficient bases, and a common squarefree degree-24 critical-value
polynomial modulo 101. The universal double-cover and genus arguments are
mathematical, not exhaustive computations.
"""
import random
import sympy as sp

p = 101
t, u, v = sp.symbols('t u v')
rng = random.Random(130052)
coeff = {(i,j,k):rng.randrange(p) for i in range(3) for j in range(3) for k in range(3)}
F = sp.Poly(sum(c*t**i*u**j*v**k for (i,j,k),c in coeff.items()),t,u,v,modulus=p).as_expr()

def canonical(f,*xs):
    return sp.Poly(sp.expand(f),*xs,modulus=p).as_expr()

def reverse(f,variable,d):
    return sp.expand(variable**d*f.subs(variable,1/variable))

def unit(eqs,vars):
    G = sp.groebner(eqs,*vars,modulus=p)
    return len(G.polys)==1 and G.polys[0].is_one

# Smooth total branch K3: all eight affine charts.
for a in (0,1):
    for b in (0,1):
        for c in (0,1):
            f=F
            for x,sw in ((t,a),(u,b),(v,c)):
                if sw:f=reverse(f,x,2)
            f=canonical(f,t,u,v)
            assert unit([f,sp.diff(f,t),sp.diff(f,u),sp.diff(f,v)],(t,u,v)),(a,b,c)
print('smooth tridegree-(2,2,2) branch: 8/8 charts')

critical=[]
for other,removed in ((u,v),(v,u)):
    A=[]
    for k in range(3):
        if removed==v:
            expr=sum(coeff[i,j,k]*t**i*other**j for i in range(3) for j in range(3))
        else:
            expr=sum(coeff[i,k,j]*t**i*other**j for i in range(3) for j in range(3))
        A.append(canonical(expr,t,other))
    aa,bb,cc=A
    D=canonical(bb**2-4*aa*cc,t,other)
    for a in (0,1):
        for b in (0,1):
            d=D; a0=aa; b0=bb
            if a:
                d=reverse(d,t,4);a0=reverse(a0,t,2);b0=reverse(b0,t,2)
            if b:
                d=reverse(d,other,4);a0=reverse(a0,other,2);b0=reverse(b0,other,2)
            d=canonical(d,t,other);a0=canonical(a0,t,other);b0=canonical(b0,t,other)
            assert unit([d,sp.diff(d,t),sp.diff(d,other)],(t,other)),(removed,a,b)
            jac=canonical(sp.diff(a0,t)*sp.diff(b0,other)-sp.diff(a0,other)*sp.diff(b0,t),t,other)
            assert unit([a0,b0,jac],(t,other)),(removed,a,b)
    polynomial=sp.Poly(sp.discriminant(D,other),t,modulus=p).monic()
    assert polynomial.degree()==24
    assert polynomial.gcd(polynomial.diff()).degree()==0
    critical.append(polynomial)
    print('smooth discriminant; reduced eight-point base; degree-24 simple critical values:',removed)
assert critical[0]==critical[1]
print('the two rulings have identical critical-value sets')
print('PASS')
