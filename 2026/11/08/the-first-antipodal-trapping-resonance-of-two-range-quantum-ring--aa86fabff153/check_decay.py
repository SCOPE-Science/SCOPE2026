"""Direct loss-semigroup checks, independent of the Fourier class formula.
Run: python check_decay.py. Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.linalg import expm


def survival(n, ratio, strength, time):
    H=np.zeros((n,n),dtype=float)
    for x in range(n):
        for h,j in [(-1,ratio),(1,ratio),(-2,1), (2,1)]:
            H[x,(x+h)%n]+=j
    generator=-1j*H
    generator[0,0]-=strength/2
    origin=np.zeros(n,complex)
    origin[n//2]=1
    return float(np.linalg.norm(expm(generator*time)@origin)**2)

count=0
for n in (6,8,10,12):
    ratio=4*math.cos(math.pi/n)**2
    exact=8/(3*n)
    for gamma in (0.5,1.0,3.0):
        got=survival(n,ratio,gamma,1000)
        assert abs(got-exact)<5e-7,(n,gamma,got,exact)
        count+=1
    for detune in (0.06,0.1):
        a=survival(n,ratio+detune,1.0,500)
        b=survival(n,ratio+detune,1.0,3000)
        assert 0<=b<a, (n,detune,a,b)
        count+=1
print('PASS:',count,'direct non-Hermitian evolution tests (all rate and detuning cases)')
