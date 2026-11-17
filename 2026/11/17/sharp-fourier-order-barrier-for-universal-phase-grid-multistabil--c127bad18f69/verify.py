"""Reproduce finite-grid tests for phase-coloring stability; Python 3 standard library only.
Finite testing corroborates but does not replace the all-order Fourier argument.
"""
import itertools
import math

def vector_field(theta, q, gain=1.0):
    return [gain*sum(math.sin(q*(theta[j]-theta[i])) for j in range(len(theta)) if j!=i) for i in range(len(theta))]

def jacobian(theta, q, gain=1.0):
    n=len(theta)
    j=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if i != k:
                j[i][k]=gain*q*math.cos(q*(theta[k]-theta[i]))
        j[i][i]=-sum(j[i][k] for k in range(n) if k!=i)
    return j

def check():
    ntests=0
    for n in range(2,7):
        for q in range(2,8):
            for labels in itertools.product(range(q), repeat=n-1):
                theta=[0.0]+[2*math.pi*k/q for k in labels]
                assert max(abs(v) for v in vector_field(theta,q))<2e-13
                J=jacobian(theta,q)
                for i in range(n):
                    for k in range(n):
                        expected=q*(1-n if i==k else 1)
                        assert abs(J[i][k]-expected)<3e-13
                ntests+=1
            for d in range(1,q):
                assert abs(sum(math.cos(2*math.pi*d*k/q) for k in range(q)))<5e-12
                assert abs(sum(math.sin(2*math.pi*d*k/q) for k in range(q)))<5e-12
    print('PASS:',ntests,'grid configuration/Jacobian tests and all checked root-sums')
if __name__=='__main__': check()
