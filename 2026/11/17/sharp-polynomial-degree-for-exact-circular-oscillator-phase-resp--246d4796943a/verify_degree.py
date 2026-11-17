#!/usr/bin/env python3
"""Exact checks for the polynomial circular-oscillator synthesis theorem.

The theorem's lower bound is analytical: the script checks the constructive
identities and one motivating fourth-harmonic example, not a numerical search
or a certificate for all polynomial vector fields.
"""
import sympy as sp
x,y=sp.symbols('x y', real=True)
R=x*x+y*y
circle=R-1
J=lambda u:sp.Matrix([-u[1],u[0]])
p=sp.Matrix([x,y])

def modes(m):
    C=[sp.Integer(1),x]; S=[sp.Integer(0),y]
    for k in range(1,m):
        C.append(sp.expand(x*C[k]-y*S[k]))
        S.append(sp.expand(y*C[k]+x*S[k]))
    return C[:m+1],S[:m+1]

def poly_remainder(expr):
    return sp.rem(sp.expand(expr),circle,y)

def check(coeffs_cos,coeffs_sin, omega, kappa):
    m=max(k for k in set(coeffs_cos)|set(coeffs_sin) if coeffs_cos.get(k,0)!=0 or coeffs_sin.get(k,0)!=0)
    C,S=modes(max(m,1))
    h=sp.expand(sum(coeffs_cos.get(j,0)*C[j]+coeffs_sin.get(j,0)*S[j] for j in range(m+1)))
    hp=sp.expand(sum(j*(-coeffs_cos.get(j,0)*S[j]+coeffs_sin.get(j,0)*C[j]) for j in range(1,m+1)))
    H=sp.expand((kappa*h-omega*hp)/2)
    F=sp.expand(omega*J(p)+(R-1)*(-kappa*p/2+H*J(p)))
    assert max(sp.Poly(z,x,y).total_degree() for z in F)==m+3
    # Exact radial and angular identities at ALL planar points.
    assert sp.expand(p.dot(F)-kappa*R*(1-R)/2)==0
    assert sp.expand(J(p).dot(F)-R*(omega+(R-1)*H))==0
    # On the circle, prescribed radial phase sensitivity and its adjoint.
    Z=sp.expand(J(p)+h*p)
    assert poly_remainder(Z.dot(F)-omega)==0
    Dz=sp.Matrix([sp.diff(z,x)*(-omega*y)+sp.diff(z,y)*(omega*x) for z in Z])
    JF=F.jacobian([x,y])
    for z in Dz+JF.T*Z:
        assert poly_remainder(z)==0
    assert poly_remainder(J(p).dot(Z)-1)==0
    assert poly_remainder(p.dot(Z)-h)==0
    return m, F, h, H

# The exact published high-harmonic target; omega=kappa=1.
m,F,h,H=check({}, {2:sp.Integer(2),4:sp.Integer(-2)},sp.Integer(1),sp.Integer(1))
assert m==4
assert sp.expand(H-(2*x*y-4*x*y*(x*x-y*y)-2*(x*x-y*y)+4*(x**4-6*x*x*y*y+y**4)))==0
# Verify the two target components without floating-point trigonometry.
C,S=modes(5)
Ztarget=sp.Matrix([-S[5],2*C[1]-2*C[3]+C[5]])
Zours=J(p)+h*p
assert all(poly_remainder(z)==0 for z in Ztarget-Zours)
print('published_target: exact iPRC, adjoint, normalization, degree=7, radial law PASS')
for j in range(0,8):
    cc={k:sp.Rational((-1)**k*(k+1),k+3) for k in range(j+1)}
    ss={k:sp.Rational(((-1)**(k+1))*(k+2),k+5) for k in range(1,j+1)}
    degree,_,_,_=check(cc,ss,sp.Rational(3,2),sp.Rational(5,3))
    assert degree==j
print('harmonic degrees 0 through 7: exact construction and adjoint PASS')
print('lower bound: analytical Fourier argument in RESULT.md; no finite exhaustive search claimed')
# Exhaustive coefficient-space obstruction for the paper's m=4 target: if
# deg F<=6 then deg G<=4. Every such polynomial G has these 30 coefficients.
C,S=modes(4)
h4=2*S[2]-2*S[4]
hp4=4*C[2]-8*C[4]
mon=[x**i*y**j for i in range(5) for j in range(5-i)]
a=sp.symbols('a0:'+str(len(mon)));b=sp.symbols('b0:'+str(len(mon)))
g1=sum(z*u for z,u in zip(a,mon));g2=sum(z*u for z,u in zip(b,mon))
k=x*g1+y*g2
s=-y*g1+x*g2
res=sp.Poly(poly_remainder(s+hp4/2+k*h4),x,y)
M,v=sp.linear_eq_to_matrix([c for _,c in res.terms()],(*a,*b))
assert M.shape==(19,30)
assert M.rank()==18 and M.row_join(v).rank()==19
print('source target degree<=6: full 30-variable linear system inconsistent, ranks 18 versus 19 PASS')
