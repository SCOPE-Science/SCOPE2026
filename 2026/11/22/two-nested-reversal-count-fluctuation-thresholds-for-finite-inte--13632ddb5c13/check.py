"""Standalone symbolic and numerical checks for marked finite-interval telegraph escape."""
import math
import sympy as S
from scipy.optimize import brentq
import numpy as np

q,h,w,d = S.symbols('q h w d', positive=True)

def A(a):
    return 1+a + (a*a/S.Integer(2)+a**3/S.Integer(6))*w + (a**4/S.Integer(24)+a**5/S.Integer(120))*w*w

def B(a):
    return a + a**3*w/6 + a**5*w*w/120

def coeffs(expr, prob):
    series = S.series(expr/prob, w, 0, 3).removeO()
    series = S.series(series.subs(w,-2*d-d**2),d,0,3).removeO().expand()
    mean=S.factor(series.coeff(d,1))
    var=S.factor(2*series.coeff(d,2)+mean-mean**2)
    return mean,var

ell=q+h
right_mean,right_var=coeffs(A(q)/A(ell),(1+q)/(1+ell))
left_mean,left_var=coeffs(S.sqrt(1-w)*B(h)/A(ell),h/(1+ell))
mean_diff = 1+(q*q*(q+3)/(1+q)-h*h)/3
var_diff=S.Rational(2,45)*(q**4*(q*q+6*q+15)/(q+1)**2-h**4+15*(q*q*(q+3)/(q+1)-h*h))
assert S.cancel(left_mean-right_mean-mean_diff)==0
assert S.cancel(left_var-right_var-var_diff)==0
assert S.factor(left_mean-(1+ell**2/S.Integer(3)*((ell+3)/(ell+1)-(h/ell)**2)))==0
assert S.factor(right_mean-ell**2/S.Integer(3)*((ell+3)/(ell+1)-(q/ell)**2*(q+3)/(q+1)))==0
# Monotonicity certificates: all coefficients positive in numerator.
a=q*q*(q+3)/(q+1)
b=q**4*(q*q+6*q+15)/(q+1)**2
for expression in (a,b):
    derivative=S.factor(S.diff(expression,q))
    numerator,_=S.fraction(derivative)
    assert all(c>=0 for c in S.Poly(numerator,q).all_coeffs())
    assert derivative.subs(q,1)>0
# Mean crossing is a strict subset of variance reversal regime.
on_mean=S.factor(var_diff.subs(h**4,(a+3)**2).subs(h**2,a+3))
assert S.simplify(on_mean+4*(4*q**3+12*q**2+18*q+9)/(15*(q+1)**2))==0
# Asymptotic zero positions.
r,c=S.symbols('r c',positive=True)
ell1=1/r; s=S.Rational(1,2)-r/2+c*r**3
me=S.series(mean_diff.subs({q:ell1*s,h:ell1*(1-s)}),r,0,2)
va=S.series(var_diff.subs({q:ell1*s,h:ell1*(1-s)}),r,0,1)
assert S.simplify(me.coeff(r,1)-(2*c+4)/3)==0
assert S.simplify(va.coeff(r,-1)-(2*c/45-S.Rational(4,9)))==0
# Numeric independent transfer-matrix evaluation of generating functions.
def pgf(ell,s,z):
    if z==1:
        return (1+ell*s)/(1+ell), ell*(1-s)/(1+ell)
    w=1-z*z; root=math.sqrt(w)
    def Au(u):
        return math.cosh(ell*root*u)+math.sinh(ell*root*u)/root
    den=Au(1)
    return Au(s)/den, z*math.sinh(ell*root*(1-s))/(root*den)
# Independently solve the constant-coefficient two-state boundary problem.
from scipy.integrate import solve_ivp
checked=0
for ell_float in [0.1,0.5,1.,2.,3.,8.]:
  for start in [0.1,0.31,0.69,0.9]:
    for z in [0.0,0.2,0.7,0.99,1.0]:
      rpg,lpg=pgf(ell_float,start,z)
      from scipy.linalg import expm
      M=ell_float*np.array([[1.,-z],[z,-1.]])
      # Solve transfer boundary data right f_-(0)=0, f_+(1)=1.
      T=expm(M)
      cR=1/T[0,0]
      fR=expm(M*start)@np.array([cR,0.])
      assert abs(fR[0]-rpg)<3e-11
      # Left f_-(0)=1, f_+(1)=0; solve f_+(0).
      cL=-T[0,1]/T[0,0]
      fL=expm(M*start)@np.array([cL,1.])
      assert abs(fL[0]-lpg)<3e-11
      checked+=2

def delta(ell,s):
    qv=ell*s; hv=ell*(1-s)
    dm=1+(qv*qv*(qv+3)/(qv+1)-hv*hv)/3
    dv=(2/45)*(qv**4*(qv*qv+6*qv+15)/(qv+1)**2-hv**4+15*(qv*qv*(qv+3)/(qv+1)-hv*hv))
    return dm,dv
for e in [0.02,0.1,1,math.sqrt(3),2,3,5,10,100,1000]:
    sv=brentq(lambda s:delta(e,s)[1],1e-12,1-1e-12,xtol=1e-14)
    if e>math.sqrt(3)+1e-8:
        sm=brentq(lambda s:delta(e,s)[0],1e-12,1-1e-12,xtol=1e-14)
        assert sm<sv
    else:
        assert delta(e,1e-10)[0]>0
    checked+=1
for e in [2.,3.,5.,10.,100.]:
  sv=brentq(lambda s:delta(e,s)[1],1e-12,1-1e-12)
  sm=brentq(lambda s:delta(e,s)[0],1e-12,1-1e-12)
  print(f'ell={e:6g} mean_threshold={sm:.12f} variance_threshold={sv:.12f}')
print(f'PASS: symbolic PGF moments, strict monotonicity certificates, threshold identity, asymptotics and {checked} transfer/root checks')
