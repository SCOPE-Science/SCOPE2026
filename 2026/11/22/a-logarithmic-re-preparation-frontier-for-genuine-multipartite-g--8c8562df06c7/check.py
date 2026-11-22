"""Reproducible checks for a Poisson-reprepared amplitude-damped GHZ state."""
from math import comb
import numpy as np
from scipy.special import beta, gammaln, logsumexp
from scipy.optimize import brentq
from scipy.linalg import solve

count = 0

def check(condition, message):
    global count
    assert condition, message
    count += 1

def probabilities(n, a):
    return [0.5 * (1.0 if b == 0 else 0.0) + a * beta(a+b,n-b+1)/2 for b in range(n+1)]

def coherence(n, a):
    return a/(2*a+n)

def ratio(n, a):
    b = np.arange(1,n,dtype=float)
    terms = 0.5*(gammaln(a+b)-gammaln(b+1)+gammaln(a+n-b)-gammaln(n-b+1))
    return np.exp(np.log(n+2*a)-np.log(4)+gammaln(n+1)-gammaln(n+a+1)+logsumexp(terms))

def direct_ratio(n, a):
    p = probabilities(n,a)
    s = sum(comb(n,b)*np.sqrt(p[b]*p[n-b]) for b in range(1,n))/2
    return s/coherence(n,a)

def exact_stationary(n,a):
    d=2**n
    ghz=np.zeros(d,complex)
    ghz[0]=ghz[-1]=1/np.sqrt(2)
    initial=np.outer(ghz,ghz.conj())
    annih=np.array([[0,1],[0,0]],complex)
    eye2=np.eye(2,dtype=complex)
    lind=np.zeros((d*d,d*d),complex)
    I=np.eye(d,dtype=complex)
    for k in range(n):
        op=np.array([[1.]],complex)
        for j in range(n):
            op=np.kron(op, annih if j==k else eye2)
        number=op.conj().T@op
        lind += np.kron(op.conj(),op)-0.5*(np.kron(I,number)+np.kron(number.T,I))
    mat = solve(a*np.eye(d*d)-lind,a*initial.reshape(-1,order='F'))
    return mat.reshape((d,d),order='F')

for n in range(2,9):
    for a in [0.15,0.75,1.0,3.2,11.0]:
        p=probabilities(n,a)
        c=coherence(n,a)
        check(abs(sum(comb(n,b)*p[b] for b in range(n+1))-1)<2e-12,'normalization')
        check(abs(ratio(n,a)-direct_ratio(n,a))<3e-12,'ratio')
        check(p[0]*p[n]>=c*c-1e-12,'positive GHZ block')
        check(all(v>0 for v in p),'positive populations')

for n in [2,3,4]:
    for a in [0.35,1.,3.,10.]:
        rho=exact_stationary(n,a)
        p=probabilities(n,a)
        check(np.linalg.norm(rho-rho.conj().T)<1e-11,'Hermiticity')
        check(abs(np.trace(rho)-1)<1e-11,'trace')
        check(np.linalg.eigvalsh(rho).min()>-1e-11,'positive density')
        check(abs(rho[0,-1]-coherence(n,a))<2e-11,'coherence from Lindblad')
        check(max(abs(rho[i,i]-p[i.bit_count()]) for i in range(2**n))<2e-11,'populations from Lindblad')
        check(np.linalg.norm(rho-np.diag(np.diag(rho))-np.diag([coherence(n,a)],k=2**n-1)-np.diag([coherence(n,a)],k=1-2**n))<2e-11,'X shape')

for n in range(3,52):
    check(ratio(n,1e-8)>1,'low-rate biseparable side')
    check(ratio(n,100.)<1,'high-rate GME side')
    grid=np.geomspace(1e-3,100,31)
    check(all(ratio(n,float(grid[i]))>ratio(n,float(grid[i+1])) for i in range(30)),'monotonic grid')
    ac=brentq(lambda a: np.log(ratio(n,a)),1e-10,100)
    check(abs(ratio(n,ac)-1)<1e-10,'root')

for n in [1000,5000,10000,20000]:
    ac=brentq(lambda a: np.log(ratio(n,a)),1e-9,50)
    ln=np.log(n)
    asym=(ln-.5*np.log(ln)+np.log(np.sqrt(2*np.pi*np.log(2))/4))/np.log(2)
    check(abs(ac-asym)<0.3,'asymptotic window')

check(abs(ratio(2,.7)-1/2.7)<1e-12,'two-qubit simplification')
print(f'PASS {count} assertions: generator, stationary matrix, concurrence ratio, threshold, and large-size scaling')
