"""Supplementary tests for the Legendre-phase singular-value law.
Run with Python 3, NumPy. Tests do not replace the analytic proof.
"""
import numpy as np
from math import pi,cos,sin,sqrt

def leg(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def primal(p):return p>=3 and all(p%d for d in range(2,int(sqrt(p))+1))

def block(p):
    theta=2*pi/p; C=cos(theta); S=sin(theta); w=np.exp(1j*theta); n=p-1
    B=np.array([[w,sqrt(n)*w],[sqrt(n)*w,1+n*C-w]],dtype=np.complex128)
    return B

def predicted(p):
    th=2*pi/p; C=cos(th); S=sin(th); delta=1-C
    T=2*p-1+abs(1+(p-1)*C-np.exp(1j*th))**2
    D=delta**2+p*p*S*S
    sgmax=sqrt((T+sqrt(T*T-4*D))/2)
    return 2*sin(pi/p), sgmax

def run():
    tests=0
    for p in [5,7,11,13,17,19,23,29,31,37]:
        assert primal(p)
        minimum, maximum=predicted(p)
        for c in [1,2,p-1]:
            a=np.array([[np.exp(2j*pi/p*leg((x*y+c)%p,p)) for y in range(p)] for x in range(p)],dtype=complex)
            sig=np.linalg.svd(a,compute_uv=False)
            assert abs(sig[-1]-minimum)<1e-8, (p,c,sig[-1],minimum)
            assert abs(sig[0]-maximum)<1e-8, (p,c,sig[0],maximum)
            v=np.array([leg(t,p) for t in range(p)],dtype=complex)
            AAt=a.conj().T@a
            assert np.linalg.norm(AAt@v-minimum**2*v)<1e-7
            if len(sig)>1:assert sig[-2]-sig[-1]>1e-6
            tests+=4
        B=block(p)
        sd=np.linalg.svd(B,compute_uv=False)
        assert abs(sd[0]-maximum)<1e-9
        assert sd[-1]>minimum
        tests+=2
    print('PASS',tests,'singular-value, unique-minimal-mode and block checks')
if __name__=='__main__': run()
