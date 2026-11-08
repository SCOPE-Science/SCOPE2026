"""Independent deterministic tests of the two-person evolving-tie theorem.
Requires numpy and scipy. Execute: python verify.py
"""
from math import exp, log, tanh, atanh
from scipy.integrate import solve_ivp
from scipy.special import expi
from scipy.optimize import brentq


def H(a,d):
    return expi(a*d)/2-log(d)


def critical(a,d):
    dc=log(2)/a
    if d<=dc: return 0.
    return tanh(H(a,d)-H(a,dc))


def rhs(a):
    def f(t,y):
        d,w=y
        p=exp(-a*d)
        return [-2*w*p*d/(1+w), w*(1-w)*(2*p-1)]
    return f


def integral(a,d,w):
    return atanh(w)-H(a,d)


def expected_polar(a,d0,w0):
    dc=log(2)/a
    return brentq(lambda x:H(a,x)-H(a,d0)+atanh(w0),dc,d0)


def run():
    tests=0
    # Symbolic-algebra consequence of the reduced equations, checked
    # independently at non-special rational-grid points.
    for a in (0.3,0.7,1,2,3,6):
        for d in (.05,.15,.25,.5,1,1.7):
            for w in (.02,.17,.5,.8,.97):
                dp,wp=rhs(a)(0,(d,w))
                Hprime=(exp(a*d)/2-1)/d
                drift=wp/(1-w*w)-Hprime*dp
                assert abs(drift)<1e-12
                tests+=1
    # ODE integrations check invariant AND all sides of the threshold.
    a,d0=2.,1.
    dc=log(2)/a
    wc=critical(a,d0)
    assert .7137<wc<.7139
    for w0,case in ((.1,'polar'),(.4,'polar'),(.65,'polar'),(.8,'cons'),(.95,'cons'),(wc,'critical')):
        T=600 if case!='cons' else 35
        sol=solve_ivp(rhs(a),(0,T),[d0,w0],method='RK45',rtol=1e-10,atol=1e-12,max_step=.3,dense_output=True)
        assert sol.success
        for t in (0,.1,1,3,5,10):
            d,w=sol.sol(t)
            assert d>0 and 0<w<1
            assert abs(integral(a,d,w)-integral(a,d0,w0))<3e-9
            tests+=1
        d_end,w_end=sol.sol(T)
        if case=='polar':
            dstar=expected_polar(a,d0,w0)
            assert abs(d_end-dstar)<5e-8, (w0,d_end,dstar)
            assert w_end<1e-12
        if case=='cons':
            assert d_end<1e-10 and w_end>1-1e-9
        if case=='critical':
            # at long times the critical asymptotic leading constants
            # are approached from finite time.
            assert dc<d_end<dc+0.005, d_end
            assert 0<w_end<3e-5
            assert abs(600*(d_end-dc)-2/a)<.10, 600*(d_end-dc)
            assert abs(600*600*w_end-2/log(2))<.7, 600*600*w_end
        tests+=1
    print('PASS:',tests,'first-integral and phase checks; wc =',wc,'dc =',dc)

if __name__=='__main__': run()
