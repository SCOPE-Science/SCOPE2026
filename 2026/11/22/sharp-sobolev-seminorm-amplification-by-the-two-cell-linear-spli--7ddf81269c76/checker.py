"""Exact symbolic checks for sharp two-interval spline projection Sobolev norms.
Run: python checker.py (requires SymPy). The proof in RESULT.md is independent.
"""
import sympy as S
h,t=S.symbols('h t',positive=True)
b=1-h
M=S.Matrix([[2*h,h,0],[h,2,h*0+b],[0,b,2*b]])/6
Minv=S.Matrix([[1+3/h,-2,1],[-2,4,-2],[1,-2,1+3/b]])
assert S.simplify(M*Minv-S.eye(3))==S.zeros(3)
L0=3*t*(2*h*(h+1)-(3*h+1)*t)/(2*h**3)
L1=3*(1-t)*(1+2*h-3*t)/(2*h*b)
R0=3*t*(3*t-2*h)/(2*h*b)
R1=3*(1-t)*(2*b*(1+b)-(3*b+1)*(1-t))/(2*b**3)
# Kernel for projected slopes (in y=t), directly from the inverse Gram matrix.
phi0=S.Matrix([1-t/h,t/h,0]);phi1=S.Matrix([0,(1-t)/b,(t-h)/b])
qL0=S.simplify(((Minv.row(1)-Minv.row(0))*phi0)[0]/h)
qL1=S.simplify(((Minv.row(1)-Minv.row(0))*phi1)[0]/h)
qR0=S.simplify(((Minv.row(2)-Minv.row(1))*phi0)[0]/b)
qR1=S.simplify(((Minv.row(2)-Minv.row(1))*phi1)[0]/b)
for x,y in [(qL0,-S.diff(L0,t)),(qL1,-S.diff(L1,t)),(qR0,-S.diff(R0,t)),(qR1,-S.diff(R1,t))]:
    assert S.simplify(x-y)==0
for X0,X1 in [(L0,L1),(R0,R1)]:
    assert S.simplify(X0.subs(t,0))==0
    assert S.simplify(X1.subs(t,1))==0
    assert S.simplify(X0.subs(t,h)-X1.subs(t,h))==0
    assert S.simplify(S.integrate(X0,(t,0,h))+S.integrate(X1,(t,h,1))-1)==0
r=(1+2*h)/3
nrL=S.simplify(S.integrate(L0,(t,0,h))+S.integrate(L1,(t,h,r))-S.integrate(L1,(t,r,1)))
assert S.simplify(nrL-(1+4*b*b/(9*h)))==0
rr=2*h/3
nrR=S.simplify(-S.integrate(R0,(t,0,rr))+S.integrate(R0,(t,rr,h))+S.integrate(R1,(t,h,1)))
assert S.simplify(nrR-(1+4*h*h/(9*b)))==0
# Exact continuous tent extremizer, slope on the first element.
fx0=t
fxm=t
fx1=2*r-t
lf=S.integrate(fx0*qL0,(t,0,h))+S.integrate(fxm*qL1,(t,h,r))+S.integrate(fx1*qL1,(t,r,1))
assert S.simplify(lf-nrL)==0
A=S.factor(S.integrate(L0**2,(t,0,h))+S.integrate(L1**2,(t,h,1)))
B=S.factor(S.integrate(R0**2,(t,0,h))+S.integrate(R1**2,(t,h,1)))
C=S.factor(S.integrate(L0*R0,(t,0,h))+S.integrate(L1*R1,(t,h,1)))
assert S.simplify(A-3*(2*h*h+h+1)/(10*h*h))==0
assert S.simplify(B-3*(2*b*b+b+1)/(10*b*b))==0
assert S.simplify(C+3*(2*h-1)**2/(20*h*b))==0
tr=S.factor(h*A+b*B)
det=S.factor(h*b*(A*B-C*C))
assert S.simplify(tr-3*(1+4*h*b)/(10*h*b))==0
assert S.simplify(det-9*(15+4*h*b)/(400*h*b))==0
assert S.simplify(tr*tr-4*det-9*(2*h-1)**2*(1-3*h*b)/(100*h*h*b*b))==0
# Check H1 maximum eigenvalue and W1,infty at representative exact rational knots.
for ratio in [S.Rational(1,10),S.Rational(1,3),S.Rational(1,2),S.Rational(3,4),S.Rational(9,10)]:
    hv=S.Rational(ratio);bv=1-hv
    import math
    AA=float(A.subs(h,hv)); BB=float(B.subs(h,hv)); CC=float(C.subs(h,hv))
    trace=float((h*A+b*B).subs(h,hv)); determinant=float(det.subs(h,hv))
    numerical=(trace+math.sqrt(trace**2-4*determinant))/2
    formula=3*(1+4*float(hv*bv)+abs(1-2*float(hv))*math.sqrt(1-3*float(hv*bv)))/(20*float(hv*bv))
    assert abs(numerical-formula)<1e-10
    lhs=float(max(nrL.subs(h,hv),nrR.subs(h,hv)))
    mu=min(float(hv),float(bv))
    assert abs(lhs-(1+4*(1-mu)**2/(9*mu)))<1e-12
print('PASS: inverse Gram, slope kernels, tent extremizer, both exact Sobolev norms, and five rational mesh cases')
