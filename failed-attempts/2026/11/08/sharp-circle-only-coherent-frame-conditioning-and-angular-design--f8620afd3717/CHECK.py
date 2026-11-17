"""Reproducibility checks for optimal circular Fock polynomial sampling."""
import math
import numpy as np

checks = 0

def verify(cond, detail=''):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(detail)

def frame_matrix(n, x, phases, weights):
    k=np.arange(n+1)
    f=np.array([math.sqrt(math.factorial(int(a))) for a in k])
    A=np.sqrt(np.array(weights))[:,None]*np.exp(-x/2)*np.exp(1j*np.outer(phases,k))*x**(k/2)/f
    return A.conj().T@A

def theoretical(n):
    x=math.factorial(n)**(1/n)
    w=np.array([x**k/math.factorial(k) for k in range(n+1)])
    return x,w.max(),w

for n in range(1,24):
    x,ratio,w=theoretical(n)
    for m in [n+1,n+3,2*n+3]:
        phase=2*math.pi*np.arange(m)/m+0.271
        S=frame_matrix(n,x,phase,np.ones(m))
        verify(np.allclose(S,np.diag(m*math.exp(-x)*w),rtol=3e-11,atol=3e-10),(n,m,'diagonal'))
        verify(abs(np.linalg.eigvalsh(S)[-1]/np.linalg.eigvalsh(S)[0]-ratio)<3e-9,(n,m,'optimal'))
    for j in range(5):
        m=n+1+j
        rng=np.random.default_rng(100000*n+j)
        phase=rng.uniform(-math.pi,math.pi,m)
        weights=rng.uniform(.1,2,m)
        S=frame_matrix(n,x,phase,weights)
        ev=np.linalg.eigvalsh(S)
        if ev[0]>1e-12:
            verify(ev[-1]/ev[0]>=ratio-2e-8,(n,m,j,'universal'))
    for factor in [.10,.55,.97,1.03,1.75,10]:
        xx=x*factor
        ww=np.array([xx**k/math.factorial(k) for k in range(n+1)])
        verify(ww.max()/ww.min()>ratio+1e-10,(n,factor,'strict radius'))
    if n>=2:
        leading=math.sqrt(math.e)*(2*math.pi*n)**((1/math.e-1)/2)*math.exp(n/math.e)
        if n>=10:
            verify(abs(math.log(ratio/leading)) < 10*math.log(n)**2/n, (n,'asymptotic'))
print(f'PASS: {checks} independent checks')
