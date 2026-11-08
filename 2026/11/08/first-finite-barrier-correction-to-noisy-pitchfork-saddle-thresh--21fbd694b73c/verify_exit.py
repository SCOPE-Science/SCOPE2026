"""Independent finite-difference checks of a first-passage asymptotic.

Requirements: Python 3, numpy and scipy. Only finite numerical tests are claimed.
"""
import math
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.integrate import cumulative_simpson, simpson
from scipy.special import ndtr


def normalized_prediction(r, beta):
    return ndtr(2*beta) + (2*beta*beta+1)*math.exp(-2*beta*beta)/(2*math.sqrt(2*math.pi)*r)


def bvp_mean(r, beta, num=6000):
    b=math.sqrt(r)+beta/math.sqrt(r)
    x=np.linspace(0,b,num+1)
    h=b/num
    drift=-r*x+x*x*x
    # Unknowns: u[0], ..., u[num-1], with u[num]=0.
    diagonal=np.full(num,-1.0/(h*h))
    lower=0.5/(h*h)-drift[1:num]/(2*h)
    upper=0.5/(h*h)+drift[:num-1]/(2*h)
    A=diags([lower,diagonal,upper],[-1,0,1],shape=(num,num),format='lil')
    rhs=np.full(num,-1.0)
    # Second-order Neumann boundary (-3u0+4u1-u2)/(2h)=0.
    A[0,:]=0
    A[0,0]=-3
    A[0,1]=4
    A[0,2]=-1
    rhs[0]=0
    # Right Dirichlet value is zero, so no right-boundary term.
    u=spsolve(A.tocsr(),rhs)
    assert np.all(np.isfinite(u)) and u[0]>0
    return float(u[0])


def quadrature_mean(r,beta,num=24001):
    b=math.sqrt(r)+beta/math.sqrt(r)
    z=np.linspace(0,b,num)
    loginner=-r*z*z+0.5*z**4
    inn=cumulative_simpson(np.exp(loginner),x=z,initial=0)
    logouter=r*z*z-0.5*z**4
    return 2*float(simpson(np.exp(logouter)*inn,x=z))


def main():
    checked=0
    for r in (3.0,4.0,5.0,6.0):
        for beta in (-1.0,0.0,1.0):
            u=bvp_mean(r,beta)
            v=quadrature_mean(r,beta)
            rel=abs(u-v)/v
            assert rel < 0.002, (r,beta,rel)
            norm=u/(math.pi/(math.sqrt(2)*r)*math.exp(r*r/2))
            estimate=normalized_prediction(r,beta)
            assert norm>0 and estimate>0
            # The asymptotic error is O(r^-2), not zero at finite r.
            assert abs(norm-estimate)*r*r < 1.5, (r,beta,norm,estimate)
            checked+=1
    # A higher-barrier case checks only the stable quadrature against the series.
    for beta in (-1.0,0.0,1.0):
        r=8.0
        value=quadrature_mean(r,beta)
        baseline=math.pi/(math.sqrt(2)*r)*math.exp(r*r/2)
        assert abs(value/baseline-normalized_prediction(r,beta))*r*r < 1.5
    # The explicit finite-r correction has the predicted strict sign.
    for beta in np.linspace(-3,3,121):
        assert normalized_prediction(8,float(beta))>ndtr(2*beta)
    print('VERIFY_OK backward_BVP_vs_quadrature=%d positive_corrections=121' % checked)


if __name__=='__main__':
    main()
