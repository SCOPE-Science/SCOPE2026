"""Direct finite numerical corroboration of the directed cyclic two-snapshot theorem.
Requires Python 3 and NumPy/SciPy. Analytic claims do not rely on this sampler.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar

def fiber(N,drift,delay,k):
    angle=2*math.pi*k/N
    l1=1-math.cos(angle)-1j*drift*math.sin(angle)
    l2=2-l1
    z1,z2=np.exp(-delay*l1),np.exp(-delay*l2)
    Q=np.array([[1,1],[z1,z2]],dtype=complex)/math.sqrt(2)
    return np.linalg.eigvalsh(Q.conj().T@Q)[0]

def direct(N,drift,delay):
    eye=np.eye(N)
    shift_forward=np.roll(eye,1,axis=1)
    shift_backward=np.roll(eye,-1,axis=1)
    L=eye-(1+drift)*shift_forward/2-(1-drift)*shift_backward/2
    measurements=np.vstack([eye[::2],expm(-delay*L)[::2]])
    return np.linalg.eigvalsh(measurements.T@measurements)[0]

checks=0
for N in (4,6,8,10,12,14,16,20):
    for drift in (0.0,0.07,0.31,-0.6):
        for delay in (0.2,0.7,1.108857552878572,2.8):
            a=min(fiber(N,drift,delay,k) for k in range(N//2))
            b=direct(N,drift,delay)
            assert abs(a-b)<3e-12,(N,drift,delay,a,b)
            checks+=1
for N in (4,8,12,20):
    drift=.4
    t=math.pi/abs(drift)
    assert min(fiber(N,drift,t,k) for k in range(N//2))<1e-12
    assert min(fiber(N,drift,t/2,k) for k in range(N//2))>0
    checks+=2
for drift in (.04,.02,.01):
    N=8
    optimize=lambda t:min(fiber(N,drift,t,k) for k in range(N//2))
    result=minimize_scalar(lambda t:-optimize(t),bounds=(.6,1.6),method='bounded',options={'xatol':1e-10})
    assert result.success
    assert abs(result.x-1.108857552878572)<.04
    assert abs((-result.fun)/drift**2 - 0.12070751969725028)<.001
    checks+=2
print('CHECK_OK direct_gram_comparisons=128 resonant_checks=8 small_drift_checks=6 total='+str(checks))
