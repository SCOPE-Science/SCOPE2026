"""Exact algebraic and numerical checks of the two-locus selection law.
Run with Python 3, sympy and mpmath installed.
"""
import sympy as S
import mpmath as M

x,y,u,v,a,b,c,z,w,k = S.symbols('x y u v a b c z w k', positive=True)
H = y*u-x*v
X=x+a*H; Y=y-a*H; U=u-b*H; V=v+b*H
assert S.expand(X+Y-x-y)==0
assert S.expand(b*X+a*U-b*x-a*u)==0
# Replacing y=c-x and v=1-c-u, H=c*u-(1-c)*x:
assert S.simplify(H.subs({y:c-x, v:1-c-u})-(c*u-(1-c)*x)) == 0
D=a+(b-a)*c
CQ=a*z/(b*(1-z)+a*z)
CR=a*(1-z)/(a*(1-z)+b*z)
F=S.integrate(D**2,c)
GQ=S.integrate(z*D**2-b*c*D,c)
GR=S.integrate(z*D**2-a*(1-c)*D,c)
FZ=S.factor(6/(a*b)*(z*F.subs(c,1)-(GQ.subs(c,CQ)-GQ.subs(c,0))-(GR.subs(c,1)-GR.subs(c,CR))))
K=(a-b)**2/(a*b)
s=z*(1-z)
THEORY=s*(K*(K+2)*s+2*(K+3))/(1+K*s)**2
assert S.factor(FZ-THEORY)==0
assert S.factor(THEORY.subs(z,1-z)-THEORY)==0
assert S.factor(THEORY.subs(z,S.Rational(1,2))-(K+6)/(K+4))==0
assert S.factor(S.limit(THEORY/z,z,0)-2*(K+3))==0
assert S.factor(THEORY.subs(b,a)-6*z*(1-z))==0
# The critical scaling density and CDF follow from the exact formula.
critical=S.limit((s*(k*(k+2)*s+2*(k+3))/(1+k*s)**2).subs(z,w/k),k,S.oo)
assert S.simplify(critical-(1-(1+w)**-2))==0
assert S.simplify(S.integrate(1-(1+w)**-2, (w,0,S.Symbol('W',nonnegative=True))) - (S.Symbol('W',nonnegative=True)**2/(1+S.Symbol('W',nonnegative=True))))==0
for av,bv in [(1,1),(1,S.Rational(1,3)),(S.Rational(2,5),1),(S.Rational(3,4),S.Rational(1,5))]:
    ff=S.lambdify(z, THEORY.subs({a:av,b:bv}), 'mpmath')
    mass=M.quad(ff,[0,0.1,0.5,0.9,1]); mean=M.quad(lambda t:t*ff(t),[0,0.5,1]);
    assert abs(mass-1)<1e-12,(av,bv,mass)
    assert abs(mean-0.5)<1e-12,(av,bv,mean)
    for zi in [0.07, 0.4, 0.85]:
        q=lambda C:float(bv)*C/(float(av)*(1-C)+float(bv)*C)
        hh=lambda C: (max(zi,0)-max(zi-q(C),0)-max(zi-(1-q(C)),0))/(q(C)*(1-q(C)))
        val=M.quad(lambda C: 6*C*(1-C)*hh(C),[0,1])
        # Nonsmooth quadrature has modest (~1e-5) deterministic integration error.
        assert abs(val-ff(zi))<4e-4,(av,bv,zi,val,ff(zi))
print('TWO_LOCUS_EXACT_DENSITY_AND_CRITICAL_SCALING_OK')
