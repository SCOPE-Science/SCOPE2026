"""Direct matrix and information checks for a Bell-reset Ising dimer.

Requires numpy and scipy. The analytic inequalities in RESULT.md prove the
all-parameter conclusion; these finite checks are diagnostic, not that proof.
"""
import numpy as np
from scipy.linalg import expm
from math import log2, pi

X = np.array([[0,1],[1,0]], complex)
Z = np.diag([1,-1]).astype(complex)
I = np.eye(2, dtype=complex)
BELL = np.array([1,0,0,1],complex)/np.sqrt(2)

def entropy(z):
    z = float(np.clip(z,0,1))
    return 0.0 if z in (0,1) else -z*log2(z)-(1-z)*log2(1-z)

def matrix_gap(p,J,Omega, cutoff=1e-12):
    H = -J*np.kron(Z,Z)+Omega/2*(np.kron(X,I)+np.kron(I,X))
    U = expm(-1j*H)
    state=BELL.copy()
    weight=p
    mean=np.zeros((2,2),complex)
    avgent=0.
    t=0
    while weight>cutoff*p and t<10000:
        rho = np.outer(state,state.conj()).reshape(2,2,2,2)
        reduced=np.trace(rho,axis1=1,axis2=3)
        mean+=weight*reduced
        eig=np.linalg.eigvalsh(reduced)
        avgent+=weight*entropy(eig[-1])
        state=U@state
        weight*=1-p
        t+=1
    return entropy(np.linalg.eigvalsh(mean)[-1])-avgent

def analytic_gap(p,J,Omega,cutoff=1e-12):
    q=1-p
    strength=2*J*Omega/(J*J+Omega*Omega)
    phi=np.hypot(J,Omega)
    weights=p
    t=0
    mean=0.
    avg=0.
    while weights>cutoff*p and t<10000:
        y=strength*np.sin(phi*t)**2
        mean+=weights*y
        avg+=weights*entropy((1+y)/2)
        weights*=q
        t+=1
    return entropy((1+mean)/2)-avg

def bound(p):
    mu=(1-p)/(2-p)
    return entropy((1+mu)/2)-1+mu

max_difference=0.
for p in [0.015, 0.05, .17, .33, .67, .9]:
    for J, Omega in [(0.3,1.8),(.9,1.2),(2.4,.8),(1.75,2.75),(1,1)]:
        got=matrix_gap(p,J,Omega)
        expected=analytic_gap(p,J,Omega)
        max_difference=max(max_difference,abs(got-expected))
        assert abs(got-expected)<2e-8,(p,J,Omega,got,expected)
        assert got<=bound(p)+2e-9, (p,J,Omega,got,bound(p))
for k in range(4):
    j=(2*k+1)*pi/(2*np.sqrt(2))
    for p in [.05,.1,.3,.7,.95]:
        got=matrix_gap(p,j,j)
        b=bound(p)
        assert abs(got-b)<2e-9,(k,p,got,b)
assert bound(.3)>bound(.5)>bound(.7)>0
print('PASS: 30 direct 4x4 matrix vs conditional-state comparisons, 20 exact optimizer cases')
print('largest direct-matrix discrepancy',max_difference)
print('p=0.1 sharp bound in bits',bound(.1))
print('limiting absolute cap in bits',entropy(.75)-.5)
