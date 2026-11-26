"""Reproducible arithmetic checks of a Markov reciprocal-ratio BDF2 moment frontier."""
from fractions import Fraction as F
import math

def q(r):
    return r*r/(1+2*r)

def thresholds(r, power):
    a,b=q(r),q(1/r)
    A,B=a**power,b**power
    return (1-A*B)/(A+B-2*A*B)

def mat(p,a,b,t):
    A,B=float(a)**t,float(b)**t
    return ((p*A,(1-p)*A),((1-p)*B,p*B))

def rho(m):
    x,y=m[0]; z,w=m[1]
    return ((x+w)+math.sqrt((x-w)**2+4*y*z))/2

def run():
    assert q(F(3))==F(9,7)
    assert q(F(1,3))==F(1,15)
    assert q(F(3))*q(F(1,3))==F(3,35)
    assert thresholds(F(3),1)==F(24,31)
    assert thresholds(F(3),2)==F(171,283)
    assert thresholds(F(3),3)==F(289224,614815)
    for r in [F(1),F(6,5),F(2),F(5,2),F(3),F(4),F(10)]:
        a,b=q(r),q(1/r)
        assert a*b<1
        for t in [F(1,2),1,2,3,5]:
            if a>1:
                pc=float(thresholds(r,t))
                assert 0<pc<1
                for p in [pc/2, pc, (pc+1)/2]:
                    eig=rho(mat(p,a,b,float(t)))
                    assert abs(eig-1)<1e-9 if p==pc else (eig<1 if p<pc else eig>1)
            else:
                for p in [0,.2,.5,.9,.999]:
                    assert rho(mat(p,a,b,float(t)))<1
    # Independently verify the zero-test BDF2 recursion with exact rational solutions.
    for steps in [(F(3),F(1,3),F(3)),(F(2),F(5,2),F(1,2)),(F(1,2),)*3]:
        h=[F(1)]; y=[F(0),F(1)]; h.append(F(1))
        for ratio in steps:
            h.append(h[-1]*ratio)
            # d0*(y[n]-y[n-1])/h_n + d1*(y[n-1]-y[n-2])/h_(n-1)=0
            diff=q(ratio)*(y[-1]-y[-2]); yn=y[-1]+diff
            lhs=F(1+2*ratio,1+ratio)*diff/h[-1]-F(ratio,1+ratio)*(y[-1]-y[-2])/h[-2]
            assert lhs==0
            y.append(yn)
    print('CHECKS_PASSED: exact BDF2 recurrence, three rational threshold certificates, spectral sign grids')
if __name__=='__main__':run()
