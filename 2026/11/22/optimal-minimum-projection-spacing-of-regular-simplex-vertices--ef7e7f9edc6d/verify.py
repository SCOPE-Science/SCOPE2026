#!/usr/bin/env python3
"""Finite checks for the exact random-direction vertex-resolution law.
The asymptotic and conditional weak limits are proved separately, not by the checks.
"""
import math
from fractions import Fraction

def data(d):
    m=d+1
    M=[[Fraction(min(i,j)*(m-max(i,j)),m) for j in range(1,d+1)] for i in range(1,d+1)]
    a=[Fraction(j*(m-j),2) for j in range(1,d+1)]
    A=sum(a)
    return M,a,A

def sigma(d):
    return 2*math.pi**(d/2)/math.gamma(d/2)

def coefficient(d):
    m=d+1
    A=d*(d+1)*(d+2)/12
    return 2**((3*d-1)/2)*math.sqrt(m)*A**(d-.5)/(sigma(d)*math.factorial(d-1)*math.factorial(d))

def exact_cdf_survival_d3(t, N=260):
    d=3
    m=4
    M,a,A=data(d)
    A=float(A)
    top=.5-A*t*t
    if top<=0: return 0.
    factor=math.sqrt(m)*2**((3*d-2)/2)/(sigma(d)*math.factorial(d))
    acc=0.
    # Composite midpoint integration with independent cells transformed from unit square.
    for i in range(N):
        x=(i+.5)/N
        for j in range(N):
            y=(1-x)*(j+.5)/N
            q=[x,y,1-x-y]
            v=[q[k]/float(a[k]) for k in range(d)]
            H=sum(float(M[k][l])*v[k]*v[l] for k in range(d) for l in range(d))
            s=top/(math.sqrt(t*t+top*H)+t)
            acc+=s*s/(t+s*H)*(1-x)
    return factor*acc/(N*N)

def run():
    for d in range(3,10):
        M,a,A=data(d)
        m=d+1
        assert sum(a)==Fraction(d*(d+1)*(d+2),12)
        assert [sum(M[i]) for i in range(d)] == a
        for i in range(d):
            for j in range(d):
                cartan = 2*M[i][j]-(M[i-1][j] if i else 0)-(M[i+1][j] if i+1<d else 0)
                assert cartan==int(i==j)
        assert A>0 and all(x>0 for x in a)
        assert coefficient(d)>0
    C3=coefficient(3)
    assert abs(C3-2*5**2.5/(3*math.pi)) < 1e-11
    assert abs(exact_cdf_survival_d3(0,260)-1)<2e-5
    gstar=1/math.sqrt(10)
    reference={.005:.00029532244227737877,.01:.0011764166656373846,.02:.004667917682623783}
    for eps,expected in reference.items():
        got=exact_cdf_survival_d3(gstar-eps,260)
        assert abs(got/expected-1)<3e-5,(eps,got,expected)
    # A few decreasing endpoint ratios: this is diagnostic, not proof of limits.
    ratios=[]
    for eps in (.02,.01,.005):
        ratios.append(exact_cdf_survival_d3(gstar-eps,260)/(C3*eps**2))
    assert ratios[0]<ratios[1]<ratios[2] and .97<ratios[-1]<1
    print('d=3 endpoint coefficient:',format(C3,'.12f'))
    print('d=4 endpoint coefficient:',format(coefficient(4),'.12f'))
    print('d=3 numerical endpoint ratios:', ' '.join(format(r,'.7f') for r in ratios))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__': run()
