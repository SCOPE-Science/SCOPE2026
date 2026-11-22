"""Numerical checks for regular circular Fock first-jet frames."""
import math
import numpy as np
from scipy.special import gammaln, logsumexp
from scipy.optimize import minimize_scalar

def log_condition(m,x):
    assert m>=2 and x>0
    n=np.arange(m,dtype=float)
    q=n+m
    a=-x+n*np.log(x)-gammaln(n+1)
    b=-x+q*np.log(x)-gammaln(q+1)
    va=1+(n-x)**2/x
    vb=1+(q-x)**2/x
    logtr=np.logaddexp(a+np.log(va),b+np.log(vb))
    # trace T; determinant D. eigenvalues = (T +/- sqrt(T^2-4D))/2
    logdet=a+b+2*np.log(m)-np.log(x)
    eta=np.exp(np.minimum(logdet-2*logtr,np.log(0.25)))
    # stable root expression; if eta close 1/4 need protect
    loglarge=logtr+np.log((1+np.sqrt(np.maximum(0,1-4*eta)))/2)
    logsmall=logdet-loglarge
    return float(np.max(loglarge)-np.min(logsmall))

def rate(rho):
    I0=rho
    I2=rho-2+2*math.log(2/rho)
    low=0.0 if rho<=2 else I2
    return max(I0,I2)-low

if __name__=='__main__':
    for m in [2,3,4,8,16,32,64,128,256,512]:
        opt=minimize_scalar(lambda logr:log_condition(m,math.exp(logr)),bounds=(math.log(.1*m),math.log(3*m)),method='bounded',options={'xatol':1e-10})
        x=math.exp(opt.x)
        assert opt.success
        print(f'{m:4d} x/M={x/m:.10f} logK/M={opt.fun/m:.10f} predicted={2/math.e:.10f}')
    for rho in [.3, 2/math.e, 1.,1.5,2.5,4.]:
        m=256
        value=log_condition(m,rho*m)/m
        print('fixed',rho,'observed',value,'rate',rate(rho))
        assert abs(value-rate(rho))<.16
    # verify the block identity against literal 2m by 2m complex sampling matrix
    for m in [2,3,4,6,8]:
        x=.85*m
        z=np.sqrt(x)*np.exp(2j*np.pi*np.arange(m)/m)
        S=np.zeros((2*m,2*m),dtype=complex)
        for n in range(2*m):
            vals=np.exp(-x/2)*z**n/math.sqrt(math.factorial(n))/math.sqrt(m)
            S[:m,n]=vals
            S[m:,n]=(n-x)/math.sqrt(x)*vals
        s=np.linalg.svd(S,compute_uv=False)
        direct=2*np.log(s.max()/s.min())
        error=abs(direct-log_condition(m,x))
        print('matrix',m,'error',error)
        assert error<1e-9
    print('ALL TESTS PASSED')

# A second, independent check of the determinant law can be run by importing
# this file and calling check_det_formula below.
def check_det_formula():
    for m in (2,3,4,5,7):
        for x in (.3*m, .8*m, 1.7*m):
            z=np.sqrt(x)*np.exp(2j*np.pi*np.arange(m)/m)
            S=np.zeros((2*m,2*m),dtype=complex)
            for n in range(2*m):
                v=np.exp(-x/2)*z**n/math.sqrt(math.factorial(n))/math.sqrt(m)
                S[:m,n]=v
                S[m:,n]=(n-x)/math.sqrt(x)*v
            logdet_num=2*np.linalg.slogdet(S)[1]
            logdet_exact=2*m*np.log(m)-2*m*x+2*m*(m-1)*np.log(x)-sum(gammaln(np.arange(2*m)+1))
            assert abs(logdet_num-logdet_exact)<1e-9
    print('DETERMINANT CHECKS PASSED')

if __name__ == '__main__':
    check_det_formula()
