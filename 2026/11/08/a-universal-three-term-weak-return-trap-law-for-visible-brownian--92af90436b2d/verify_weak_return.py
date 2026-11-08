#!/usr/bin/env python3
"""Independent numerical BVP and moment checks for a Brownian search with visible OU return."""
import math
import numpy as np
from scipy.integrate import quad, solve_bvp
from scipy.special import erf, erfc, erfcx

D=L=1.0
c=math.sqrt(math.pi/(2*D))
def exit_mean(k):
    mesh=np.linspace(0,L,60)
    initial=np.vstack((mesh*(L-mesh)/(2*D), (L-2*mesh)/(2*D)))
    sol=solve_bvp(lambda x,y: np.vstack((y[1],(k*x*y[1]-1)/D)),
                  lambda ya,yb: np.array([ya[0],yb[0]]), mesh,initial,tol=1e-10,max_nodes=10000)
    assert sol.status==0
    return lambda x: sol.sol(x)[0]
def p_exit(k,x):
    num=quad(lambda y:math.exp(k*y*y/(2*D)),0,x,epsabs=1e-12)[0]
    den=quad(lambda y:math.exp(k*y*y/(2*D)),0,L,epsabs=1e-12)[0]
    return num/den
def uneg_derivative(k,a):
    return c/math.sqrt(k)*erfcx(a*math.sqrt(k/(2*D)))
def pure_ou(k):
    return quad(lambda x:c/math.sqrt(k)*math.exp(k*x*x/(2*D))*(1+erf(x*math.sqrt(k/(2*D)))),0,L,epsabs=1e-11)[0]

def reset_model(kind,par,k):
    epos=exit_mean(k)
    if kind=='poisson':
        q=math.sqrt(par/D)
        target=math.exp(-q*L)
        Es=(1-target)/par
        h=lambda x:q/2*(math.exp(-q*x)-math.exp(-q*(2*L-x)))
        tail=lambda a:(1-math.exp(-2*q*L))/2*math.exp(-q*a)
        Esplus=target/par
        p0=(1-math.exp(-2*q*L))/(2*q*L)
        ratio=1+6/(q*L*math.sinh(q*L))
    else:
        t=par
        target=erfc(L/math.sqrt(4*D*t))
        Es=quad(lambda s:erf(L/math.sqrt(4*D*s)),0,t,epsabs=1e-11)[0]
        normal=1/math.sqrt(4*math.pi*D*t)
        h=lambda x:normal*(math.exp(-x*x/(4*D*t))-math.exp(-(2*L-x)**2/(4*D*t)))
        tail=lambda a:0.5*(erfc(a/math.sqrt(4*D*t))-erfc((2*L+a)/math.sqrt(4*D*t)))
        Esplus=quad(lambda s:erfc(L/math.sqrt(4*D*s)),0,t,epsabs=1e-11)[0]
        p0=target+quad(lambda x:h(x)*x/L,0,L,epsabs=1e-11)[0]
        ratio=None
    p=target+quad(lambda x:h(x)*p_exit(k,x),0,L,epsabs=1e-10)[0]
    neg=quad(lambda a:uneg_derivative(k,a)*tail(a),0,np.inf,epsabs=1e-10)[0]
    pos=quad(lambda x:h(x)*epos(x),0,L,epsabs=1e-10)[0]
    M=(Es+neg+pos)/p
    leading=c*L/math.sqrt(k)+L*L/(2*D)
    delta=c*L*Esplus/p0*math.sqrt(k)
    return M,leading,delta,p0,ratio

if __name__=='__main__':
    checks=0
    for kind,param in [('poisson',0.25),('poisson',1.0),('poisson',4.0),('deterministic',0.4),('deterministic',2.0)]:
        print(kind,param)
        for k in [0.02,0.005,0.001,0.0002]:
            M,leading,delta,p0,ratio=reset_model(kind,param,k)
            base=pure_ou(k)
            err=(M-base)/delta
            print('k %.5g M %.10g scaled %.8f excess_ratio %.7f'%(k,M,math.sqrt(k)*M/c,err))
            assert M>base and 0.5<err<1.25, (kind,param,k,err)
            checks+=2
            if ratio is not None:
                b=c/6*ratio
                approximate=leading+b*math.sqrt(k)
                print("approx_error",M-approximate,"scaled",(M-approximate)/k)
                assert abs(M-approximate) < 18*k, (kind,param,k,M-approximate)
                checks+=1
    print('PASS numerical checks:',checks)
