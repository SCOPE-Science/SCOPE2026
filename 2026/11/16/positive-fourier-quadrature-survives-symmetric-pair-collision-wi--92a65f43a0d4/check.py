"""Finite consistency checks for symmetric adjacent-node trigonometric quadrature.

These checks are supplemental and do not establish the all-order theorem.
"""
import math
import numpy as np

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def dker(n, t):
    # numerically continuous at integer multiples of 2*pi
    v = math.sin(t/2)
    if abs(v) < 1e-14:
        return n
    return math.sin(n*t/2) / v

def weights(n, a):
    h = 2*math.pi/n
    A = dker(n, a*h)+dker(n, (1-a)*h)
    w = np.zeros(n)
    w[0] = w[1] = 1/A
    for j in range(2,n):
        w[j] = (1-(dker(n,(j-a)*h)+dker(n,(j-1+a)*h))/A)/n
    return w

def sample_nodes(n,a):
    h=2*math.pi/n
    return np.array([a*h,(1-a)*h]+[j*h for j in range(2,n)])

for n in range(3,64,2):
    freq = np.arange(-(n//2),n//2+1)
    for a in [0.0,0.001,0.1,0.23,0.25,0.40,0.49,0.499999,0.5]:
        x = sample_nodes(n,a)
        w = weights(n,a)
        moment = (w[:,None]*np.exp(1j*x[:,None]*freq)).sum(axis=0)
        target = (freq==0).astype(float)
        check(np.min(w)>0, f'positive weights n={n},a={a}')
        check(abs(sum(w)-1)<4e-11, f'mass n={n},a={a}')
        check(np.max(abs(moment-target)) < 6e-11, f'moments n={n},a={a}')
        check(abs(w[0]-w[1])<1e-13, f'symmetric n={n},a={a}')
        if a==0.5:
            check(abs(w[0] - 0.5*math.sin(math.pi/(2*n)))<1e-12, f'collision weight n={n}')
            check(np.linalg.matrix_rank(np.exp(1j*x[:,None]*freq)[1:,:],tol=1e-9)==n-1, f'collision rank n={n}')
        if a==0.0:
            check(max(abs(w-1/n))<1e-11,f'uniform n={n}')

for n in [3,5,7,9,13,21,31,51]:
    h = 2*math.pi/n
    C = 2*math.pi*math.cos(math.pi/(2*n))/(n*n*math.sin(math.pi/(2*n))**2)
    freq=np.arange(-(n//2),n//2+1)
    for eps in [1e-3,1e-4]:
        x=sample_nodes(n,0.5-eps)
        F=np.exp(1j*x[:,None]*freq)/math.sqrt(n)
        sigma=np.linalg.svd(F,compute_uv=False)[-1]
        check(abs(sigma/eps/C - 1)<0.035, f'collision coefficient n={n},eps={eps}: {sigma/eps/C}')
check(abs(2*math.pi*math.cos(math.pi/(2*10001))/(10001**2*math.sin(math.pi/(2*10001))**2)-8/math.pi) < 1e-6,'large n coefficient limit')
print(f'PASS {COUNT} assertions: positivity, all Fourier moments, collision rank, sharp singular slope')
