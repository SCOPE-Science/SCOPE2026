"""Reproducibility checks for first-Hermite circular/elliptic localization.

Run with Python 3, numpy and scipy. Finite checks supplement an analytic proof.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigvalsh
from scipy.special import gammainc

COUNT = 0

def check(test, label):
    global COUNT
    if not test:
        raise AssertionError(label)
    COUNT += 1

def poisson_pmf(n, x):
    return math.exp(-x + n * math.log(x) - math.lgamma(n + 1))

def radial_eigenvalue(j, T):
    p = poisson_pmf(j, T)
    return float(gammainc(j, T)) + (j - 1 - T)*p if j else 1-(T+1)*math.exp(-T)

def matrix(N, tau, J, nang=128, nrad=40):
    nodes, weights = leggauss(nrad)
    thetas = 2*math.pi*np.arange(nang)/nang
    result = np.zeros((J,J), dtype=np.complex128)
    indices = np.arange(J)
    gammas = np.array([math.lgamma(j+1) for j in indices])
    for theta in thetas:
        upper = N / (math.exp(-2*tau)*math.cos(theta)**2 + math.exp(2*tau)*math.sin(theta)**2)
        radii = upper*(nodes+1)/2
        radial_weights = upper*weights/2
        j = indices[:,None]
        s = radii[None,:]
        amplitude = (j-s)*np.exp((j-1)*np.log(s)/2 - gammas[:,None]/2 - s/2)
        vector = amplitude*np.exp(1j*(j-1)*theta)
        result += (vector*radial_weights)@vector.conj().T/nang
    return (result+result.conj().T)/2

for N in [1,2,3,4,5,7,10]:
    J = max(N+9, 16)
    p = poisson_pmf(N,N)
    c = p*math.sqrt(N/(N+1))
    spectrum = np.array([radial_eigenvalue(j,N) for j in range(J)])
    for j in range(J-1):
        predicted = (N-j)*(j+1-N)*poisson_pmf(j,N)/(j+1)
        check(abs(spectrum[j+1]-spectrum[j]-predicted)<4e-13,f'forward difference N={N}, j={j}')
    check(max(spectrum[N-1:N+2])-min(spectrum[N-1:N+2])<4e-13,f'triple tie N={N}')
    if N>=2:
        check(abs(spectrum[N-2]-spectrum[N]-2*p/N)<5e-13,f'left gap N={N}')
    check(abs(spectrum[N]-spectrum[N+2]-2*N*p/((N+1)*(N+2)))<5e-13,f'right gap N={N}')
    H0=matrix(N,0,J)
    check(np.max(abs(np.diag(H0)-spectrum))<5e-11,f'radial diagonal N={N}')
    check(np.max(abs(H0-np.diag(np.diag(H0))))<5e-12,f'angular cancellation N={N}')
    step=0.00002
    Hp=matrix(N,step,J)
    Hm=matrix(N,-step,J)
    D=(Hp-Hm)/(2*step)
    check(abs(D[N-1,N+1]+c)<2e-8,f'elliptic coupling N={N}')
    check(abs(D[N,N])<1e-9,f'elliptic diagonal N={N}')
    for H,sgn in ((Hp,+1),(Hm,-1)):
        vals=eigvalsh(H)[::-1]
        check(abs(vals[N-1]-(spectrum[N]+c*step))<2e-8,f'upper branch N={N}')
        check(abs(vals[N]-(spectrum[N]))<2e-8,f'center branch N={N}')
        check(abs(vals[N+1]-(spectrum[N]-c*step))<2e-8,f'lower branch N={N}')
        check(abs(vals[N-1]-vals[N]-c*step)<2e-8,f'Fermi gap N={N}')
        if N>=2:
            check(vals[N-2]>vals[N-1],f'upper gap remains N={N}')
        check(vals[N+1]>vals[N+2],f'lower gap remains N={N}')
        # The unique top Fermi vector resolves into the indicated two-mode line.
        ew, ev=np.linalg.eigh(H)
        top=ev[:,-N]
        sign = -1 if sgn>0 else +1
        target=np.zeros(J,dtype=np.complex128)
        target[N-1]=1/math.sqrt(2)
        target[N+1]=sign/math.sqrt(2)
        check(abs(np.vdot(top,target))**2>0.99990,f'branch eigenvector N={N}, sgn={sgn}')

print('HERMITE_ELLIPSE_CHECKS_PASS',COUNT)
