"""Reproduce algebraic identities and numerical checks for the two-rate noise-floor law.

Requires Python 3.10+ and SymPy 1.10+. All identities are exact;
finite numerical tests are diagnostics rather than substitutes for proof.
"""
from fractions import Fraction
from random import Random
import sympy as sp


def main():
    h, d, p, sig2 = sp.symbols('h d p sig2', real=True)
    hp, hm = h * (1 + d), h * (1 - d)
    ap, am = 1 - hp, 1 - hm
    alpha, beta = ap**2, am**2
    P = sp.Matrix([[p, 1-p], [1-p, p]])
    T = P.T * sp.diag(alpha, beta)
    D = 1 - p*(alpha+beta) + (2*p-1)*alpha*beta
    z = (sp.eye(2)-T).inv() * (P.T*sp.Matrix([hp**2,hm**2])*sig2/2)
    V = sp.factor(sum(z))
    Vc = sig2*h/(2-h)
    t = h*h*(1-d*d)
    Vclosed = sig2*(hp**2+hm**2+(1-2*p)*(beta*hp**2+alpha*hm**2))/(2*D)
    gap = 2*sig2*h*h*d*d*(2-t+2*p*(t-1))/((2-h)*D)
    der = 8*sig2*d*d*h**4*(1-d*d)*(h-1)/D**2
    iid = sig2*h*(1+d*d)/(2-h*(1+d*d))
    assert sp.cancel(V-Vclosed) == 0
    assert sp.cancel(V-Vc-gap) == 0
    assert sp.cancel(sp.diff(Vclosed,p)-der) == 0
    assert sp.cancel(Vclosed.subs(p,sp.Rational(1,2))-iid) == 0
    assert sp.factor(D - (p*(1-alpha)*(1-beta)+(1-p)*(1-alpha*beta))) == 0
    print('5 exact symbolic identities: PASS')
    count=5
    example={h:sp.Rational(8,5),d:sp.Rational(1,8),sig2:sp.S.One}
    expect=[(0,sp.Rational(2179,561)),(sp.Rational(1,10),sp.Rational(383,97)),
            (sp.Rational(13,76),sp.S(4)),(sp.Rational(1,2),sp.Rational(13,3))]
    for q, target in expect:
        observed=sp.factor(Vclosed.subs({**example,p:q}))
        assert observed==target,(q, observed,target)
        print('p=',q, 'V=',observed)
        count+=1
    assert sp.factor((t-2)/(2*(t-1))).subs(example)==sp.Rational(13,76)
    count+=1

    # Independent iteration of the two-state conditional moment recurrence.
    rng=Random(173)
    for i in range(240):
        hh=0.20+1.65*rng.random()
        dd=(min(0.95,2/hh-1)*0.99)*rng.random()
        pp=rng.random()*0.999
        a_plus=(1-hh*(1+dd))**2
        a_minus=(1-hh*(1-dd))**2
        u_plus=hh**2*(1+dd)**2
        u_minus=hh**2*(1-dd)**2
        determinant=1-pp*(a_plus+a_minus)+(2*pp-1)*a_plus*a_minus
        assert determinant>0
        predicted=(u_plus+u_minus+(1-2*pp)*(a_minus*u_plus+a_plus*u_minus))/(2*determinant)
        za,zb=0.0,0.0
        for k in range(4000):
            ya=a_plus*za+u_plus/2
            yb=a_minus*zb+u_minus/2
            za,zb=pp*ya+(1-pp)*yb,(1-pp)*ya+pp*yb
        error=abs((za+zb)-predicted)
        assert error < 2e-7*(1+abs(predicted)),(i,hh,dd,pp,error)
        count+=1
    print('240 independent conditional-moment recurrences: PASS')
    print('TOTAL CHECKS:',count)

if __name__=='__main__':
    main()
