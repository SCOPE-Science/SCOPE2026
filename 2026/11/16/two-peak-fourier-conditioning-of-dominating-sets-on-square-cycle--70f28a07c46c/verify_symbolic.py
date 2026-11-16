"""Exact symbolic polynomial certificate for the five-gap structure factor.
Requires sympy. Run: python verify_symbolic.py
"""
import sympy as s
x,t=s.symbols('x t')
h=sum(t**j for j in range(1,6))-1
cheb=[s.Integer(1),x]
for k in range(2,6):cheb.append(s.expand(2*x*cheb[-1]-cheb[-2]))
ab=s.expand(sum(t**(i+j)*cheb[abs(i-j)] for i in range(1,6) for j in range(1,6)))
re=s.expand(sum(t**j*cheb[j] for j in range(1,6)))
P=4*t**3*(t+1)-4*(t**2-t+1)*(t**2+t-1)*x-8*(t-1)*(t**3+2*t**2+t-1)*x**2+16*(2*t-1)*x**3
Q=-2*(3*t**4+2*t**3-t**2-1)+4*(3*t**4+4*t**3+2*t**2+4*t-3)*x+8*t*(4*t**3+3*t**2-1)*x**2-16*(t**4+2*t**3+2*t**2+4*t-3)*x**3-32*(t**4+t**3+t**2+t-1)*x**4
R=(8*(7*t**4+4*t**3-11*t**2-14*t+9)
 +64*t*(t+1)*(2*t-1)**2*x
 -32*(15*t**4+13*t**3+7*t**2+9*t-9)*x**2
 -128*(3*t**4+6*t**3+4*t**2+2*t-3)*x**3
 +128*(9*t**4-2*t**3-13*t**2+3)*x**4
 +512*(t**4-4*t**2-4*t+3)*x**5
 -512*(t**4+t**3+t**2+5*t-3)*x**6)
for label,expr in [('numerator',1-ab-(1-x)*P),('denominator',1+ab-2*re-(1-x)*Q),('derivative',s.diff(P,x)*Q-P*s.diff(Q,x)-R)]:
    rr=s.rem(s.expand(expr),h,t)
    assert s.expand(rr)==0, label
print('Three exact algebraic polynomial identities: PASS')
