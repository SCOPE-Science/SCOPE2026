"""Reproducible consistency checks for a semi-Markov fluorescent emitter.
Requires Python 3, sympy, mpmath. No external data files.
"""
import random
import sympy as sp
import mpmath as mp


def symbolic_two_dark_check():
    p,g,r,s1,s2,u1,u2,z,y=sp.symbols('p g r s1 s2 u1 u2 z y', positive=True)
    M=sp.Matrix([
        [-p,p,0,0],
        [r+g*y,-(g+s1+s2+r),s1,s2],
        [u1+r,0,-u1-r,0],
        [u2+r,0,0,-u2-r]
    ])
    # Row generator: det(zI-M) is unchanged under transpose.
    P=(z+u1+r)*(z+u2+r)
    H=(p+z)*(g+s1+s2+r+z)-p*(r+s1*(u1+r)/(z+u1+r)+s2*(u2+r)/(z+u2+r))
    assert sp.factor((z*sp.eye(4)-M).det() - P*(H-p*g*y))==0
    A=sp.factor(sp.diff(H,z).subs(z,0))
    B=sp.factor(sp.diff(H,z,2).subs(z,0))
    C=sp.factor(sp.diff(H,z,3).subs(z,0))
    assert sp.factor(A-(g+s1+s2+r+p+p*s1/(u1+r)+p*s2/(u2+r)))==0
    assert sp.factor(B-(2-2*p*s1/(u1+r)**2-2*p*s2/(u2+r)**2))==0
    assert sp.factor(C-(6*p*s1/(u1+r)**3+6*p*s2/(u2+r)**3))==0
    # Cross check the one-shelving result of the established limiting case.
    F=1-p*g*B/A**2
    H1=(u1+r)*(g+p+s1+r)+p*s1
    F1=1+2*g*p*(p*s1-(u1+r)**2)/H1**2
    assert sp.factor(F.subs(s2,0)-F1)==0
    return True


def rates(p,g,r,channels):
    # Each channel: (s, m_1, m_2, m_3) for min(U, Exp(r)).
    A=g+sum(c[0] for c in channels)+r+p+p*sum(s*m1 for s,m1,m2,m3 in channels)
    B=2-p*sum(s*m2 for s,m1,m2,m3 in channels)
    C=p*sum(s*m3 for s,m1,m2,m3 in channels)
    J=p*g/A
    F=1-p*g*B/A**2
    third=1-3*p*g*B/A**2*F-(p*g)**2*C/A**3
    return J,F,third


def numeric_generator_check():
    mp.mp.dps=45
    rnd=random.Random(1729)
    for _ in range(40):
        p,g,r=[mp.mpf(str(10**rnd.uniform(-1,1))) for i in range(3)]
        s1,s2,u1,u2=[mp.mpf(str(10**rnd.uniform(-1,1))) for i in range(4)]
        channels=[(s,1/(u+r),2/(u+r)**2,6/(u+r)**3) for s,u in [(s1,u1),(s2,u2)]]
        J,F,T=rates(p,g,r,channels)
        def secular(z,x):
            a1=u1+r+z;a2=u2+r+z
            H=(p+z)*(g+s1+s2+r+z)-p*(r+s1*(u1+r)/a1+s2*(u2+r)/a2)
            return H-p*g*mp.exp(x)
        def scgf(x):
            return mp.findroot(lambda z:secular(z,x), (mp.mpf('0'),mp.mpf('0.00001')),solver='secant')
        deriv=[mp.diff(scgf,0,k) for k in (1,2,3)]
        assert mp.almosteq(deriv[0],J,rel_eps=mp.mpf('1e-17')),(deriv[0],J)
        assert mp.almosteq(deriv[1]/deriv[0],F,rel_eps=mp.mpf('1e-17'))
        assert mp.almosteq(deriv[2]/deriv[0],T,rel_eps=mp.mpf('1e-17')),(deriv[2]/deriv[0],T)
    return 40


def nonexponential_checks():
    mp.mp.dps=35
    # At fixed deterministic dark time, three independent constructions of truncated moments.
    t0=mp.mpf('2'); r=mp.mpf('.4')
    psi=lambda z:(r+z*mp.exp(-(r+z)*t0))/(r+z)
    for k in (1,2,3):
        by_psi=(-1)**k*mp.diff(psi,0,k)
        by_survival=k*mp.quad(lambda t: t**(k-1)*mp.exp(-r*t),[0,t0])
        assert mp.almosteq(by_psi,by_survival,rel_eps=mp.mpf('1e-25'))
    # Pareto dark times with infinite second moment; any r>0 regularizes.
    alpha=mp.mpf('1.5');s=mp.mpf('.7');p=mp.mpf('.4')
    K=lambda rr:s*mp.quad(lambda t:t*mp.exp(-rr*t)/(1+t)**alpha,[0,mp.inf])
    def bisect_root(fun, lo, hi):
        assert fun(lo)>0 and fun(hi)<0
        for _ in range(140):
            mid=(lo+hi)/2
            if fun(mid)>0:lo=mid
            else: hi=mid
        return (lo+hi)/2
    rstar=bisect_root(lambda rr:p*K(rr)-1,mp.mpf('.05'),mp.mpf('.1'))
    assert rstar>0
    assert p*K(rstar/2)>1>p*K(2*rstar)
    # Weak pumping predicts the nonanalytic Pareto threshold power 2.
    for smallp in [mp.mpf('.003'),mp.mpf('.0003')]:
        pred=(smallp*s*mp.gamma(2-alpha))**(1/(2-alpha))
        rr=bisect_root(lambda x: smallp*K(x)-1,pred*.05,pred*3)
        assert rr>0
        assert abs(rr/pred-1)<mp.mpf('.25')
    return str(mp.nstr(rstar,16))

if __name__=='__main__':
    assert symbolic_two_dark_check()
    n=numeric_generator_check()
    threshold=nonexponential_checks()
    print('PASS: symbolic generator determinant, first three derivatives, one-dark limiting case')
    print('PASS:',n,'independent two-dark tilted-generator cumulant comparisons')
    print('PASS: deterministic dark-time derivatives and heavy-tail crossover tests')
    print('Pareto(alpha=3/2,p=0.4,s=0.7) threshold:',threshold)
