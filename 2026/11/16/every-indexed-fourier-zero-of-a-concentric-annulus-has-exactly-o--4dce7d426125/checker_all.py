"""Finite numerical corroboration of annular radial Fourier-zero migration.
For all real dimensions tested, compare independent root-solving, derivative signs,
strict inner scaled-radius monotonicity, and the predicted turning points.
Not a substitute for the general Bessel-energy proof.
Dependencies: Python 3, NumPy, SciPy.
"""
import numpy as np
from scipy.special import jv, jn_zeros
from scipy.optimize import brentq

def bessel_zeros(order, n):
    if float(order).is_integer():
        return jn_zeros(int(order), n)
    z = []
    x = 1e-5
    f_old = jv(order,x)
    while len(z) < n:
        y=x+0.08
        f_new=jv(order,y)
        if f_old*f_new < 0:
            z.append(brentq(lambda v: jv(order,v),x,y,xtol=2e-14))
        x,f_old=y,f_new
    return np.array(z)

def H(nu,t):
    return t**nu * jv(nu,t)

def node(nu,roots,k,a):
    return brentq(lambda t:H(nu,t)-H(nu,a*t),roots[k-1],roots[k],xtol=3e-13)

def run():
    tests=0
    for d in (2,3,4,5,6,8):
        nu=d/2
        z=bessel_zeros(nu-1,19)
        for k in range(1,12):
            rr=[];ss=[]
            for a in np.r_[np.geomspace(0.00001,0.45,18),np.linspace(.46,.999,35)]:
                t=node(nu,z,k,a)
                s=a*t
                b=jv(nu-1,t)
                c=jv(nu-1,s)
                den=b-a**(nu+1)*c
                assert z[k-1]<t<z[k]
                assert abs(H(nu,t)-H(nu,s))/t**nu<1e-10, (d,k,a,t,s,H(nu,t),H(nu,s))
                assert np.sign(den)==np.sign(b)
                assert t*b/den>0
                assert np.sign(a**nu*t*c/den)==np.sign(c)*np.sign(b)
                ss.append(s);rr.append(t)
                tests+=5
            assert np.min(np.diff(ss))>0
            tests+=1
            for ell in range(1,k):
                u=z[ell-1]
                t=brentq(lambda x:H(nu,x)-H(nu,u),z[k-1],z[k],xtol=3e-13)
                a=u/t
                assert 0<a<1 and abs(node(nu,z,k,a)-t)<1e-8
                assert abs(jv(nu-1,a*t))<1e-10
                tests+=2
    zz=jn_zeros(0,4)
    tstar=brentq(lambda x:H(1,x)-H(1,zz[0]),zz[1],zz[2],xtol=5e-14)
    print('planar_second_dark_ring_optimum_radius=',format(zz[0]/tstar,'.14f'))
    print('planar_second_dark_ring_max_frequency=',format(tstar,'.14f'))
    print('verified_numerical_checks=',tests)
    print('PASS')

if __name__=='__main__':
    run()
