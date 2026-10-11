#!/usr/bin/env python3
import math


def q(k,a,L):
    if abs(k-a)<1e-14:
        return a
    t=math.tanh(k*L)
    return k*(a-k*t)/(k-a*t)


def secular(k,alpha,L):
    return 2*q(k,1.5,1.0)+q(k,2.0,L)-alpha



def main():
    e4=math.exp(4.0)
    exact=2*(21-e4)/(e4+7)
    assert abs(exact-(-1.090881788335074))<2e-14

    # Critical matching is length independent.
    for L in (0.05,0.1,0.3,0.7,1.0,2.0,5.0,10.0):
        assert abs(q(2.0,2.0,L)-2.0)<2e-13
        crit=2*q(2.0,1.5,1.0)+q(2.0,2.0,L)
        assert abs(crit-exact)<3e-13

    # Check the analytic L derivative of the axial logarithmic derivative.
    derivative_checks=0
    for k in (1.2,1.7,1.95,2.05,2.4,3.0):
        for L in (0.2,0.7,1.5,3.0):
            h=1e-6
            num=(q(k,2.0,L+h)-q(k,2.0,L-h))/(2*h)
            ana=(k*k*(4-k*k)/(k-2*math.tanh(k*L))**2)/(math.cosh(k*L)**2)
            assert abs(num-ana)<2e-5*max(1.0,abs(ana)),(k,L,num,ana)
            assert (ana>0)==(k<2.0)
            derivative_checks+=1

    print('VERIFY_OK')
    print('alpha_crit =',format(exact,'.15f'))
    print('critical_length_checks = 8')
    print('derivative_checks =',derivative_checks)

if __name__=='__main__':
    main()
