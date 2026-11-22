"""Finite algebraic and numerical diagnostics for periodic Hilbert commutators."""
from fractions import Fraction
from math import pi, sqrt
import numpy as np

def exact_check(q, pattern, M):
    n = q*M
    for r in range(q):
        for s in range(q):
            for i in range(M):
                for j in range(M):
                    original = Fraction(pattern[r]-pattern[s],q*(i+j)+r+s+1)
                    model = Fraction(pattern[r]-pattern[s],q*(i+j+1))
                    a = Fraction(r+s+1,q)
                    residual = Fraction(pattern[r]-pattern[s],q)*(Fraction(1, i+j+a)-Fraction(1,i+j+1))
                    assert original == model+residual
    return n*n

def finite_check(pattern, N):
    pattern=np.asarray(pattern,float);q=len(pattern)
    n=np.arange(N)
    H=1/(n[:,None]+n[None,:]+1.)
    D=pattern[n%q]
    K=1j*(D[:,None]-D[None,:])*H
    assert np.max(np.abs(K-K.conj().T))<1e-14
    w=np.linalg.eigvalsh(K)
    assert np.max(abs(w+w[::-1]))<1e-11
    variance = float(np.mean((pattern-pattern.mean())**2))
    return {'q':q,'N':N,'sigma':sqrt(variance),'pi_sigma':pi*sqrt(variance),'finite_norm':float(np.max(np.abs(w))),'symmetry_error':float(np.max(abs(w+w[::-1])))}

if __name__=='__main__':
    cells=0
    for p in [(1,-1),(1,0,-1),(2,-1,0,4),(3,3,3,3),(3,-2,1,0,2)]:
        cells+=exact_check(len(p),p,5)
        for N in (32,80,160):
            print(finite_check(p,N))
    print('EXACT_CELLS',cells, 'VERIFICATION_OK')
