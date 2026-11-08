"""Exact algebra checks for the fourth-order Jacobi disk kernel.

Requires SymPy and NumPy. The universal root-count proof is analytic;
numerical roots here are only supplementary tests.
"""
import numpy as np
import sympy as sp

s, t, n, w = sp.symbols('s t n w')

rising = sp.prod(n+t+j for j in range(5))
moment_poly = sp.Poly(sp.expand(rising),n)
S = [1/(1-s)]
for k in range(1,6):
    S.append(sp.factor(s*sp.diff(S[-1],s)))
Q = sp.cancel((1-s)**6 * sum(moment_poly.nth(k)*S[k] for k in range(6)))
expected = sum([
 t*(t+1)*(t+2)*(t+3)*(t+4),
 -5*(t-1)*(t+1)*(t+2)*(t+3)*(t+4)*s,
 10*t*(t-1)*(t+2)*(t+3)*(t+4)*s**2,
 -10*t*(t-1)*(t+1)*(t+3)*(t+4)*s**3,
 5*t*(t-1)*(t+1)*(t+2)*(t+4)*s**4,
 -t*(t-1)*(t+1)*(t+2)*(t+3)*s**5])
assert sp.factor(Q-expected)==0
T = sp.factor(sp.cancel((w+1)**5*Q.subs(s,(w-1)/(w+1))))
assert sp.Poly(T,w).degree()==5
A = [sp.factor(sp.Poly(T,w).nth(j)) for j in range(5,-1,-1)]
a5,a4,a3,a2,a1,a0=A
b1=sp.factor((a4*a3-a5*a2)/a4)
b2=sp.factor((a4*a1-a5*a0)/a4)
c1=sp.factor((b1*a2-a4*b2)/b1)
d1=sp.factor((c1*b2-b1*a0)/c1)
assert a5==120
assert sp.simplify(a4-120*(2*t+3))==0
assert sp.simplify(b1-160*(t+1)*(t+2))==0
assert sp.simplify(c1-8*(2*t+1)*(2*t+3)*(2*t+5))==0
assert sp.simplify(d1+64*t*(t-2)*(t+1)*(t+2)*(t+3)*(t+5)/((2*t+1)*(2*t+5)))==0
p=2*t**4+12*t**3+12*t**2-18*t-5
assert sp.factor(a0-8*(2*t+3)*p)==0
assert sp.factor(T.subs(t,2)-120*(w+3)*(w*w+3)*(w*w+4*w+7))==0
assert sp.factor(Q.subs(t,2)+120*(s-2)*(s*s-3*s+3)*(s*s-s+1))==0
r0=(sp.sqrt(15+2*sp.sqrt(19))-3)/2
assert sp.simplify(p.subs(t,r0))==0
assert .93<float(r0)<.94
assert sp.factor(Q.subs(t,1)-120)==0
for sample, expected_count in [(sp.Rational(1,4),1),(sp.Rational(1,2),1),(sp.Rational(9,10),1),(sp.Rational(1),0),(sp.Rational(3,2),0),(sp.Rational(3),2),(sp.Rational(5),2),(sp.Rational(10),2)]:
    v=np.roots([float(c) for c in sp.Poly(Q.subs(t,sample),s).all_coeffs()])
    count=sum(abs(z)<1-1e-7 for z in v)
    assert count==expected_count,(sample,count,v)
print('JACOBI_REENTRANCE_CHECK_PASS exact_identities=9 numerical_root_cases=8')
