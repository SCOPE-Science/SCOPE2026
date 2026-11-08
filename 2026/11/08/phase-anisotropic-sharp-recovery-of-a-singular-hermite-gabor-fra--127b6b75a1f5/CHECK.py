"""Reproduce theta-series coefficients and local Gabor-frame stability checks.
Run: python -m pip install -r requirements.txt && python CHECK.py
All finite tests corroborate, but do not replace, the analytic theorem.
"""
import math
import cmath
import mpmath as mp
from scipy.optimize import minimize

mp.mp.dps = 55
J = range(-12,13)

def triple(gamma):
    gg=mp.mpf(gamma)
    gauss=lambda t:mp.exp(-gg*t*t)
    v = [mp.fsum(gauss(-2*j) for j in J), mp.fsum(gauss(-1-2*j) for j in J)]
    ax = [mp.fsum((1-2*gg*(2*j)**2)*gauss(-2*j) for j in J),
          mp.fsum((1-2*gg*(1+2*j)**2)*gauss(-1-2*j) for j in J)]
    bn = [mp.fsum(4*mp.pi*j*(-2*j)*gauss(-2*j) for j in J),
          mp.fsum(4*mp.pi*j*(-1-2*j)*gauss(-1-2*j) for j in J)]
    return v, ax, bn

def det(u,v):return u[0]*v[1]-u[1]*v[0]
def K(v,w):return det(v,w)**2/(w[0]**2+w[1]**2)

def pair(gamma,x,nu,z):
    # Independent direct parity Zak sums, using the frequency phase exp(4*pi*i*j*nu).
    return [sum((x-2*j-z)*cmath.exp(-gamma*(x-2*j)**2+4j*math.pi*j*nu) for j in J),
            sum((x-1-2*j-z)*cmath.exp(-gamma*(x-1-2*j)**2+4j*math.pi*j*nu) for j in J)]

def symbol(gamma,x,nu,z):return 2*sum(abs(s)**2 for s in pair(gamma,x,nu,z))

def test():
    assertions = 0
    for gamma in (mp.mpf('1'),mp.pi):
        v,ax,bn=triple(gamma);kr=K(v,ax);ki=K(v,bn)
        print('width',mp.nstr(gamma,18),'K_real',mp.nstr(kr,30),'K_imag',mp.nstr(ki,30))
        assert kr>0 and ki>0;assertions+=2
        if gamma==1:
            assert mp.mpf('1.5698') < kr < mp.mpf('1.5699')
            assert mp.mpf('.7629') < ki < mp.mpf('.7630')
        else:
            assert mp.mpf('.2440') < kr < mp.mpf('.2442')
            assert mp.mpf('.9999') < ki < mp.mpf('1.0001')
        assertions+=2
        g=float(gamma)
        for zangle in (0.0,math.pi/6,math.pi/4,math.pi/2,2*math.pi/3):
            for eps in (0.01,0.003,0.001):
                z=eps*cmath.exp(1j*zangle)
                asym=2*float(kr*z.real**2+ki*z.imag**2)
                x0=float((v[0]*ax[0]+v[1]*ax[1])/(ax[0]**2+ax[1]**2))*z.real
                nu0=float((v[0]*bn[0]+v[1]*bn[1])/(bn[0]**2+bn[1]**2))*z.imag
                res=minimize(lambda w:symbol(g,w[0],w[1],z),[x0,nu0],method='Nelder-Mead',
                             options={'xatol':1e-12,'fatol':1e-18,'maxiter':2500})
                assert res.success and res.fun>0, (gamma,z,res.message,res.fun);assertions+=1
                ratio=res.fun/asym
                assert abs(ratio-1)<100*eps, (gamma,z,ratio);assertions+=1
                if eps<0.005:assert abs(ratio-1)<15*eps;assertions+=1
        # Direct Wronskian Gaussian factor check, at off-zero samples.
        S=sum((4*j+1)*cmath.exp(-g*(4*j+1)**2/2) for j in J)
        for x,nu in [(0,.25),(.14,.11),(.3,.24),(.5,.33),(.9,.12)]:
            def parity_derivs(x,nu):
                e=sum(cmath.exp(-g*(x-2*j)**2+4j*math.pi*j*nu) for j in J)
                o=sum(cmath.exp(-g*(x-1-2*j)**2+4j*math.pi*j*nu) for j in J)
                de=pair(g,x,nu,0)[0];do=pair(g,x,nu,0)[1]
                return e,o,de,do
            e,o,de,do=parity_derivs(x,nu)
            W=de*o-e*do
            W2=S*sum((-1)**n*cmath.exp(-2*g*(x-.5-n)**2+4j*math.pi*n*nu) for n in J)
            assert abs(W-W2)<2e-10,(x,nu,W,W2); assertions+=1
    print('PASS:',assertions,'deterministic assertions; analytic proof establishes infinite case.')
if __name__=='__main__':test()
