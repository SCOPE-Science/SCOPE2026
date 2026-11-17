"""Scientific checks for the reduced Chialvo map's tangential flip bubble.
Run with: python check_chialvo.py
Dependencies: sympy, scipy, numpy.
"""
import math
import sympy as s
from scipy.optimize import root, brentq

x, k = s.symbols('x k', positive=True, real=True)
x0 = 2 + s.sqrt(2)
kx = x*(x-3)/(x-2)
rx = x-s.log(x*(x-2))
r0 = x0-s.log(x0*(x0-2))
assert s.simplify(kx.subs(x,x0)-1)==0
assert s.simplify(s.diff(rx,x).subs(x,x0))==0
assert s.simplify(s.diff(rx,x,2).subs(x,x0)-s.Integer(2)/x0)==0
assert s.simplify(s.diff(kx,x)-(x*x-4*x+6)/(x-2)**2)==0

r, v = s.symbols('r v',real=True)
f = v**2*s.exp(r-v)+k
ff=s.lambdify((v,r,k),f,'math')
fx=s.diff(f,v)
# At the distinguished point, f(x0)=x0, f'=-1, f''=0, f'''=2/x0
subs={v:x0,r:r0,k:s.Integer(1)}
assert s.simplify(f.subs(subs)-x0)==0
assert s.simplify(fx.subs(subs)+1)==0
assert s.simplify(s.diff(f,v,2).subs(subs))==0
assert s.simplify(s.diff(f,v,3).subs(subs)-2/x0)==0

# Analytic symmetric 2-cycle equations H1 and H2 in mean m and squared half-gap u:
# H1=f(m)+ f''(m)u/2+...-m, H2=f'(m)+f'''(m)u/6+...+1.
# Their Jacobian with respect to (m,u) at the distinguished point is diagonal
# diag(-2,1/(3x0)). The implicit solution has derivatives
# u_r=3x0, u_k=0, u_kk=-3/2 (the last uses m_k=1/2).
assert s.simplify(s.diff(f,r).subs(subs)-(x0-1))==0
assert s.simplify(s.diff(fx,r).subs(subs)+1)==0
assert s.simplify(s.diff(f,v,3).subs(subs)/6 - 1/(3*x0))==0
assert s.simplify(s.diff(f,v,3).subs(subs)*s.Rational(1,4) +s.diff(f,v,3).subs(subs)*(-s.Rational(3,2))/6)==0

# Nonlinear numerical replay; the observed amplitude A equals half-gap.
X=float(x0);R=float(r0)
checks=0
for delta in (0.01,0.002,0.0005):
    for t in (0.,1.,2.):
        K=1+t*math.sqrt(delta)
        target=math.sqrt(delta*(3*X-0.75*t*t))
        def eq(z):
            m,a=z
            return [ff(m+a,R+delta,K)-(m-a), ff(m-a,R+delta,K)-(m+a)]
        sol=root(eq,[X+0.5*t*math.sqrt(delta),target],tol=1e-12)
        m,a=sol.x
        err=max(abs(t0) for t0 in eq((m,a)))
        assert err<2e-12,(delta,t,err)
        assert a>0 and abs(a/target-1)<0.035,(delta,t,a,target)
        d1=(m+a)*math.exp(R+delta-(m+a))*(2-(m+a))
        d2=(m-a)*math.exp(R+delta-(m-a))*(2-(m-a))
        assert -1<d1*d2<1,(delta,t,d1*d2)
        fixed=brentq(lambda w:ff(w,R+delta,K)-w,3,5)
        predicted_center=t*(3*X-.75*t*t)/(4*X)
        observed_center=(m-fixed)/delta**1.5
        if t>0:
            assert abs(observed_center/predicted_center-1)<0.06,(delta,t,observed_center,predicted_center)
        checks+=1

# Critical relaxation: two-step map has cubic coefficient -2/(3X).
# For a moderate close orbit, finite-time weighted squared displacement
# approaches 3X/2, with slow asymptotics.
N=80000
z=0.1
for n in range(1,N+1):
    z=ff(X+z,R,1)-X
assert abs(N*z*z/(1.5*X)-1)<0.02,(N*z*z,1.5*X)
print(f'CHIALVO_TANGENTIAL_FLIP_CHECK_OK exact_identities=12 cycle_cases={checks} relaxation_steps={N}')
