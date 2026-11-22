"""Supplementary finite tests of the signed Cesaro commutator theorem.
These checks do not constitute the proof of the infinite-dimensional claim.
"""
import math
import numpy as np
from scipy.linalg import eigvalsh


def exact_compression(t,n):
    q=t*t
    M=n+600
    S=np.empty(M+1)
    S[M]=1/(M+1)**2/(1-q)
    for j in range(M-1,-1,-1):
        S[j]=1/(j+1)**2+q*S[j+1]
    i,j=np.indices((n,n))
    lo=np.minimum(i,j);hi=np.maximum(i,j)
    return t**(hi-lo)*(S[hi]-(1-t**(2*(lo+1)))/((i+1)*(j+1)*(1-q)))

def b(t,k):
    return -t**abs(k)*(abs(k)/(1-t*t)+2*t*t/(1-t*t)**2)

def check():
    checks=0
    for t in (0.2,0.5,0.8):
        expected=math.acos(t)/math.pi
        prev=None
        for n in (60,120,220):
            H=exact_compression(t,n)
            assert np.max(np.abs(H-H.T))<1e-14
            E=eigvalsh(H)
            neg=(E<0).sum()/n
            print('t',t,'n',n,'negative_fraction',neg,'target',expected)
            if n>=120:assert abs(neg-expected)<0.055
            checks+=2
        H=exact_compression(t,280)
        for k in range(0,5):
            i=220; j=i+k
            scaled=((i+1)*(j+1))**1.5*H[i,j]
            assert abs(scaled-b(t,k))<0.12*(1+abs(b(t,k)))
            checks+=1
        N=140
        rows=np.arange(N); Q=t**(rows[:,None]-rows[None,:])/(rows[:,None]+1)
        Q=np.tril(Q)
        HH=exact_compression(t,40)
        approx=Q.T@Q-Q@Q.T
        assert abs(approx[0,0]-HH[0,0])<1e-8
        checks+=1
        theta=np.linspace(-math.pi,math.pi,40001)
        symb=2*t*(t-np.cos(theta))/(1-2*t*np.cos(theta)+t*t)**2
        for k in range(5):
            bk=np.trapezoid(symb*np.cos(k*theta),theta)/(2*math.pi)
            assert abs(bk-b(t,k))<1e-8
            checks+=1
    print('PASS supplementary checks:',checks)

if __name__=='__main__':check()
