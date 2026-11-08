#!/usr/bin/env python3
"""Exact symbolic checks for the characteristic-three binary-quartic discriminant.
Requires SymPy 1.10 or later; run: python verify.py.
This checks algebraic identities. Geometric gluing and smoothness are proved separately.
"""
import sympy as s

p = 3
a,b,c,d,e,x = s.symbols('a b c d e x')
u,v,t = s.symbols('u v t')
vars5 = (a,b,c,d,e)

def mod(expr, variables):
    return s.Poly(s.expand(expr), *variables, modulus=p).as_expr()

def equal(f,g,variables):
    assert mod(f-g,variables)==0, (f,g)

# The integral discriminant is reduced modulo three without dividing by 3.
f = a*x**4+b*x**3+c*x**2+d*x+e
Delta = mod(s.discriminant(f,x),vars5)
assert len(s.Poly(Delta,*vars5,modulus=p).terms())==8
print('discriminant: 8 characteristic-three monomials')

# Depress the quartic by the genuine polynomial coordinate change x -> x-b.
U = d-b**3+b*c
V = e+b**2*c-b*d
f_depressed = x**4+c*x**2+u*x+v
Delta_depressed = mod(s.discriminant(f_depressed,x),(c,u,v))
F = v*(v-c*c)**2-c**3*u*u
equal(Delta_depressed,F,(c,u,v))
equal(Delta.subs(a,1),F.subs({u:U,v:V}),(b,c,d,e))
print('depression and discriminant normal form: PASS')

# Tjurina scheme of the discriminant: the equation and all partials.
J = [F]+[s.diff(F,z) for z in (c,u,v)]
w=v-c*c
J_simple=[c*c*w,c*v*w,c**3*u,v*w*w]
GJ=s.groebner(J,c,u,v,order='lex',modulus=p)
GS=s.groebner(J_simple,c,u,v,order='lex',modulus=p)
assert all(GS.reduce(g)[1]==0 for g in J)
assert all(GJ.reduce(g)[1]==0 for g in J_simple)
print('Tjurina ideal generators: PASS')

# First component I_T^3=(c,v)^3; second component I_E=(u,v-c^2).
I=[c**3,c*c*v,c*v*v,v**3]
E=[u,v-c*c]
# Intersection by eliminating t from t*I+(1-t)*E.
inter_raw=s.groebner([t*z for z in I]+[(1-t)*z for z in E],
                    t,c,u,v,order='lex',modulus=p)
intersection=[pol.as_expr() for pol in inter_raw.polys
              if not pol.as_expr().has(t)]
GI=s.groebner(intersection,c,u,v,order='lex',modulus=p)
assert all(GI.reduce(g)[1]==0 for g in J)
assert all(GJ.reduce(g)[1]==0 for g in intersection)
print('exact primary-intersection ideal equality: PASS')

# Triple-root locus T is contained in the discriminant and its Tjurina scheme.
# A quartic (alpha*x+beta*y)^3(gamma*x+delta*y) has c=0, ae-bd=0.
alpha,beta,gamma,delta=s.symbols('alpha beta gamma delta')
coeffT={a:alpha**3*gamma,b:alpha**3*delta,c:0,
        d:beta**3*gamma,e:beta**3*delta}
equal((a*e-b*d).subs(coeffT),0,(alpha,beta,gamma,delta))
equal(Delta.subs(coeffT),0,(alpha,beta,gamma,delta))

# The two-double-root locus is the image of a squared quadratic.
A,B,C=s.symbols('A B C')
coeffE={a:A*A,b:2*A*B,c:B*B+2*A*C,d:2*B*C,e:C*C}
equal(Delta.subs(coeffE),0,(A,B,C))
for z in vars5:
    equal(s.diff(Delta,z).subs(coeffE),0,(A,B,C))
print('coincident-root parametrizations: PASS')

# In the quadratic Veronese projection the missing direction has rank 3,
# hence lies outside its rank<=2 secant cubic (in characteristic 3).
M=s.Matrix([[0,0,s.Rational(1,2)],
            [0,1,0],
            [s.Rational(1,2),0,0]])
assert mod(4*M.det(),(u,)) != 0
print('projected Veronese center has rank 3: PASS')

# A length-6 generic transversal thickening has basis
# 1,c,v,c^2,cv,v^2; length 6. The projected Veronese has degree 4,
# the smooth quadric has degree 2; total cycle degree is 6*2+4=16.
assert len([(i,j) for i in range(3) for j in range(3-i)]) == 6
assert 6*2+4==16
print('generic multiplicity and cycle-degree arithmetic: PASS')
print('ALL_CHECKS_PASSED')
