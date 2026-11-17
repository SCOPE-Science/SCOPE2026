#!/usr/bin/env python3
"""Check algebra and a physical triple preimage for a risk-memory learning map.
Only sympy/mpmath dependencies; the numerical example is not proof of universal claims.
"""
import sympy as sp
import mpmath as mp
x, a, c, k, p1 = sp.symbols('x a c k p1', positive=True)
s=sp.symbols('s',positive=True)
chi=1-k*(1+c*p1)
# Direct derivative in (x,q): dF1/dx = U(1-U)(1/[x(1-x)]-a), etc.
det_over_output_var=sp.factor((1-k)*(1/(x*(1-x))-a)+a*c*k*p1)
assert sp.simplify(det_over_output_var-((1-k)-a*chi*x*(1-x))/(x*(1-x))) == 0
# Independently differentiate the actual two-coordinate nonlinear map.
q, b, p0 = sp.symbols('q b p0', real=True)
U=x/(x+(1-x)*sp.exp(a*(x-b+c*q)))
V=(1-k)*q+k*(p0+p1*x)
raw_det=sp.diff(U,x)*sp.diff(V,q)-sp.diff(U,q)*sp.diff(V,x)
assert sp.simplify(sp.together(raw_det - U*(1-U)*((1-k)-a*chi*x*(1-x))/(x*(1-x))))==0
assert sp.simplify(det_over_output_var.subs({k:sp.Rational(1,2),c:500,p1:sp.Rational(1,1000),a:8})-(1/(2*x*(1-x))-2))==0
# Critical equality: logit(1/2+t)-logit(1/2) -4t = 16 t^3 /3+ O(t^5)
t=sp.symbols('t')
y=sp.log((sp.Rational(1,2)+t)/(sp.Rational(1,2)-t))
assert sp.simplify(sp.diff(y-4*t,t,3).subs(t,0)) == 32
assert sp.simplify(sp.diff(y-4*t,t).subs(t,0)) == 0
mp.mp.dps=75
p0=mp.mpf('0.00001');P1=mp.mpf('0.001');C=mp.mpf('500');K=mp.mpf('.5');B=mp.mpf('.3');aa=mp.mpf('8.1')
ac=4*(1-K)/(1-K*(1+C*P1));eta=aa/ac-1
f=lambda T: mp.atanh(2*T)/(2*T)-(1+eta)
T=mp.findroot(f, (mp.mpf('.07'),mp.mpf('.13')))
qmid=p0+P1/2
xs=[mp.mpf('.5')-T,mp.mpf('.5'),mp.mpf('.5')+T]
qs=[qmid-K*P1/(1-K)*(X-mp.mpf('.5')) for X in xs]
assert all(p0<Q<p0+P1 for Q in qs)
def F(X,Q):
 y0=mp.log(X/(1-X))
 out=1/(1+mp.exp(-(y0-aa*(X-B+C*Q))))
 belief=(1-K)*Q+K*(p0+P1*X)
 return out,belief
outs=[F(X,Q) for X,Q in zip(xs,qs)]
assert max(abs(outs[0][i]-zz[i]) for zz in outs for i in (0,1))<mp.mpf('1e-65')
print('VERIFY_OK determinant_identity=1 cubic_contact=1 three_physical_preimages=1')
print('threshold_a',mp.nstr(ac,20),'learning_a',mp.nstr(aa,20),'offset',mp.nstr(T,30))
for X,Q in zip(xs,qs): print('preimage',mp.nstr(X,22),mp.nstr(Q,22))
print('common_image',*[mp.nstr(z,30) for z in outs[0]])
