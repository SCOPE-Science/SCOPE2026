"""Reproduce exact algebra for a two-competitor fear model phase boundary.
Requires Python 3 and SymPy.  Numerical checks are illustrative only.
"""
import sympy as S
v,t,k,b=S.symbols('v t k b',real=True)
u=S.symbols('u',real=True)
F=u*(1-u-v)
G=v*(S.Rational(2)/(1+k*u)-b*v-u)
H=S.factor((G/v).subs(u,1-v))
num=S.factor(H*(1+k*(1-v)))
assert S.simplify(num-((1-k)+( k-(1+k)*(b-1) )*v+k*(b-1)*v**2))==0
K=S.factor(S.solve(num,k)[0]); desired=(1-t*v)/((1-v)*(1+t*v))
assert S.simplify(K.subs(b,1+t)-desired)==0
DK=S.factor(S.diff(desired,v));assert S.simplify(DK+(t*t*v*v-2*t*v+2*t-1)/((v-1)**2*(1+t*v)**2))==0
q=S.sqrt(2*(1-t)); vf=(1-q)/t; kf=2*t/(2-q)**2
assert S.simplify(desired.subs(v,vf)-kf)==0
assert S.simplify(S.together(DK.subs(v,vf)))==0
assert S.simplify(S.limit(kf,t,S.Rational(1,2),dir='+')-1)==0
assert S.simplify(S.limit(kf,t,1,dir='-')-S.Rational(1,2))==0
eta=S.symbols('eta', positive=True)
series=S.series(kf.subs(t,S.Rational(1,2)+eta),eta,0,4).removeO()
assert S.simplify(series-(1-2*eta**2+2*eta**3))==0,series
# stability: trace and determinant on the positive nullcline
J=S.Matrix([F,G]).jacobian((u,v))
Jco=S.simplify(J.subs(u,1-v))
tr=S.simplify(Jco.trace().subs(k,k))
# at equilibrium, only substitute condition (G/v)=0 to simplify lower right
# trace = -u -b*v, det = -u*v*H'(v)
g=S.diff(S.Rational(2)/(1+k*u)-u,u)
assert S.simplify((J[0,0].subs(u,1-v))+(1-v))==0
assert S.simplify((J[1,1] - (G/v) + b*v))==0
D_at=S.factor((1-v)*v*(b+g.subs(u,1-v)))
assert S.simplify(D_at+(1-v)*v*S.diff(H,v))==0
# center manifold at k=1, b=3/2. x = u-1 = -v+O(v^3)
x=S.symbols('x')
B=S.series((G/v).subs({u:1+x,k:1,b:S.Rational(3,2)}).subs(x,-v),v,0,4)
assert S.simplify(B.removeO()-(v**2/(2*(2-v))).series(v,0,4).removeO())==0
assert S.simplify(S.limit(B.removeO()/v**2,v,0)-S.Rational(1,4))==0
# critical generic b>3/2: dv/dt = -(b-3/2)v^2 +O(v^3)
Bgen=S.series((G/v).subs({u:1-v,k:1}),v,0,3).removeO()
assert S.simplify(S.diff(Bgen,v).subs(v,0)-(S.Rational(3,2)-b))==0
# exact resonant nullcline residual and positive cubic sign
assert S.simplify(H.subs({k:1,b:S.Rational(3,2)})-v**2/(2*(2-v)))==0
# rational witness below: t=3/5, k=99/100 should be between fold and transcritical
vals={t:S.Rational(3,5),k:S.Rational(99,100)}
assert bool(vals[k]>kf.subs(t,vals[t])) and bool(vals[k]<1)
roots=S.solve(num.subs({b:S.Rational(8,5),k:S.Rational(99,100)}),v)
assert len(roots)==2 and all(bool(0<r<1) for r in roots)
# roots are stable/saddle by sign of H'
slopes=[S.N(S.diff(H,v).subs({b:S.Rational(8,5),k:S.Rational(99,100),v:r})) for r in roots]
assert slopes[0]<0<slopes[1],slopes
print('VERIFY_OK')
print('phase witness (b,k)=(8/5,99/100), equilibrium v=',roots)
print('fold at b=8/5: ',S.N(kf.subs(t,S.Rational(3,5)),15))
print('fold expansion: ',series)
# General positive-parameter degeneracy at the u-only boundary.
a1,b1,c1,a2,c2=S.symbols('a1 b1 c1 a2 c2',positive=True)
U=a1/b1; c=c1/b1
kc=S.factor((a2/(c2*U)-1)/U)
bstar=S.factor(c*(c2+a2*kc/(1+kc*U)**2))
Hv=S.factor(a2/(1+kc*(U-c*v))-c2*(U-c*v)-bstar*v)
assert S.simplify(Hv.subs(v,0))==0
assert S.simplify(S.diff(Hv,v).subs(v,0))==0
Cexact=S.factor(a2*kc**2*c**2/(1+kc*U)**3)
assert S.simplify(S.diff(Hv,v,2).subs(v,0)/2-Cexact)==0
assert S.simplify(Cexact.subs({a1:1,b1:1,c1:1,a2:2,c2:1})-S.Rational(1,4))==0
print('GENERAL_CUBIC_VERIFY_OK')
