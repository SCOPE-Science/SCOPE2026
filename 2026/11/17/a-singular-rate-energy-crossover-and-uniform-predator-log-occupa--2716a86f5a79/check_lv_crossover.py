"""Numerical corroboration of a singular Lotka-Volterra orbit-time limit.
The infinite-energy theorem uses a separate analytic proof; finite computations
are checks, not certification of an infinite limit.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import lambertw

def f(y):
    return math.expm1(y)-y

def turning_point(h, sign):
    if sign<0:
        return brentq(lambda y: f(y)-h,-h-2.0,0.0,xtol=1e-13)
    return brentq(lambda y: f(y)-h,0.0,max(5.0,h+3.0),xtol=1e-13)

def branch_densities(z):
    if z<=0.0:
        return float('inf'),float('inf')
    if z<1e-7:
        q=1/math.sqrt(2*z)
        return q+1/3,q-1/3
    if z>650:
        # x_+ is log of the positive solution of X-log(X)-1=z.
        p=z+1+math.log(z+1)
        for _ in range(6): p=z+1+math.log(p)
        return 1.0,1/(p-1)
    a=-math.exp(-1-z)
    sm=-z-1-lambertw(a,0).real
    sp=-z-1-lambertw(a,-1).real
    return -1/math.expm1(sm),1/math.expm1(sp)

def finite_integrals(E,c):
    lam=c*E
    M=lam*E
    ya=turning_point(1/c,-1)
    yb=turning_point(1/c,+1)
    mid=(ya+yb)/2
    half=(yb-ya)/2
    def pieces(t):
        y=mid+half*math.cos(t)
        g=max(0.,1-c*f(y))
        dminus,dplus=branch_densities(M*g)
        jac=half*math.sin(t)
        return y,g,dminus,dplus,jac
    def integra(k):
        def v(t):
            if t<=0 or t>=math.pi:return 0.0
            y,g,dm,dp,j=pieces(t)
            if k=='both':return (dm+dp)*j
            if k=='plus':return dp*j
            if k=='y':return y*(dm+dp)*j
            if k=='q':return g*dm*j
            raise ValueError(k)
        return quad(v,0,math.pi,epsrel=1e-8,epsabs=1e-9,limit=250)[0]
    return {'E':E,'c':c,'L':yb-ya,'T_over_lambda':integra('both'),
      'plus_time_over_lambda':integra('plus'),
      'mean_y':integra('y')/integra('both'),
      'lim_mean_y':mid,
      'mean_q_minus':integra('q')/integra('both'),
      'lim_mean_q':quad(lambda y:1-c*f(y),ya,yb)[0]/(yb-ya)}

def main():
    for c in (0.5,1.,2.):
        previous=None
        for E in (10.,30.,100.):
            row=finite_integrals(E,c)
            L=row['L'];T=row['T_over_lambda']
            assert T>L and T/L<1.2
            assert 0<row['plus_time_over_lambda']<T
            assert abs(row['mean_y']-row['lim_mean_y'])<.15
            assert abs(row['mean_q_minus']-row['lim_mean_q'])<.15
            if previous is not None:
                assert (T-L)<previous
            previous=T-L
            print('c={:.2f}, E={:5.0f}, (T/lambda)-W={:.7f}, plus/total={:.7f}, y mean error={:.7f}, q mean error={:.7f}'.format(c,E,T-L,row['plus_time_over_lambda']/T,row['mean_y']-row['lim_mean_y'],row['mean_q_minus']-row['lim_mean_q']))
    print('RARE_RATE_LOTKA_VOLTERRA_CROSSOVER_CHECK_OK')

if __name__=='__main__':main()
