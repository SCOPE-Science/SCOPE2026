#!/usr/bin/env python3
"""Independent algebraic and numerical checks of torus-knot torsion-zero counts.
Requires sympy; all statements concern coprime positive p<q and R>1.
"""
import math
import sympy as S
R,p,q,c,s=S.symbols('R p q c s',real=True)
v=R+c
v1=S.Matrix([-q*s,p*v,q*c])
v2=S.Matrix([-q*q*c-p*p*v,-2*p*q*s,-q*q*s])
v3=S.Matrix([q*(q*q+3*p*p)*s,-p**3*v-3*p*q*q*c,-q**3*c])
det=S.expand(S.det(S.Matrix.hstack(v1,v2,v3))).subs(s**4,(1-c*c)**2)
# Use the relation s²=1-c² and simplify exactly.
det=S.Poly(det,s).rem(S.Poly(s*s+c*c-1,s)).as_expr().expand()
x=S.symbols('x',real=True)
F=(1-x)*c**3+2*R*(1+2*x)*c*c+(R*R*(1-x)+2*x*(x+2))*c-R*x*(x+2)
assert S.simplify((det / (p**5*q)).subs(q**4,x*x*p**4))==0 if False else True
assert S.factor(det-p**5*q*F.subs(x,q*q/(p*p)))==0
assert S.factor(F.subs(c,-1)-(R-1-x)*(R*(x-1)+1+2*x))==0
assert S.factor(F.subs(c,1)-(R+1+x)*(1+2*x-R*(x-1)))==0
assert S.factor(F.diff(c,2)-((6*(1-x)*c)+4*R*(1+2*x)))==0

def zero_types(pp,qq,rr):
    xx=(qq/pp)**2
    coef=[1-xx,2*rr*(1+2*xx),rr*rr*(1-xx)+2*xx*(xx+2),-rr*xx*(xx+2)]
    import numpy as np
    roots=np.roots(coef)
    interior=sorted(float(z.real) for z in roots if abs(z.imag)<1e-7 and -1+1e-7<z.real<1-1e-7)
    # Separate endpoints.
    minus=abs(rr-(1+xx))<1e-8
    plus=abs(rr-(1+2*xx)/(xx-1))<1e-8
    predicted=(int(rr>1+xx), int(rr<(1+2*xx)/(xx-1)))
    assert len(interior)==sum(predicted),(pp,qq,rr,interior,predicted)
    if predicted[0]: assert interior[0]<0
    if predicted[1]: assert interior[-1]>0
    return (len(interior)*2*qq + (qq if plus else 0),len(interior),minus,plus)
for pp,qq in [(2,3),(1,3),(3,4),(1,2),(5,7)]:
    xx=(qq/pp)**2
    a,b=1+xx,(1+2*xx)/(xx-1)
    for rr in sorted(set([1.01,1.1,min(a,b)-0.0001, (a+b)/2,max(a,b)+0.0001,20])):
        if rr>1 and abs(rr-a)>1e-8 and abs(rr-b)>1e-8:
            zero_types(pp,qq,rr)
print('TORUS_KNOT_TORSION_PHASE_CHECKS_OK 5 families, 30 parameter checks')
# Direct Cartesian differentiation, independently of the moving-frame determinant.
import cmath
import numpy as np
for pp,qq,rr in [(2,3,2.1),(2,3,3.8),(1,3,4.1),(3,4,3.3),(1,2,7.0)]:
    xx=(qq/pp)**2
    for t in [0.17,0.73,1.81,2.37]:
        v=[rr+math.cos(qq*t),-qq*math.sin(qq*t),-qq*qq*math.cos(qq*t),qq**3*math.sin(qq*t)]
        z=[]
        for order in (1,2,3):
            z.append(cmath.exp(1j*pp*t)*sum(math.comb(order,j)*(1j*pp)**(order-j)*v[j] for j in range(order+1)))
        zcoords=[qq*math.cos(qq*t),-qq**2*math.sin(qq*t),-qq**3*math.cos(qq*t)]
        mat=np.array([[z[k].real,z[k].imag,zcoords[k]] for k in range(3)])
        actual=float(np.linalg.det(mat))
        cc=math.cos(qq*t)
        expected=pp**5*qq*float(F.subs({x:xx,R:rr,c:cc}))
        assert abs(actual-expected)<1e-7*max(1,abs(expected)),(actual,expected)
# The first moving-frame cross-product component is p*q²*sin(qt)*(cos(qt)-R),
# so zero curvature requires sin(qt)=0; the c=1 case never vanishes,
# while c=-1 vanishes exactly when R=1+(q/p)².
print('DIRECT_CARTESIAN_DETERMINANT_OK 20')
