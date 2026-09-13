import numpy as np

def gue(n):
    A = np.random.randn(n,n)+1j*np.random.randn(n,n)
    A = (A+A.conj().T)/2
    # normalize so that limiting spectral radius =2, variance 1: GUE with var 1/n off diag?
    # standard: entries N(0,1/n)?? Let's set A/sqrt(n) *? For GUE, semicircle radius 2 with variance 1 corresponds to entries variance 1/n.
    # Our A has variance 1 per real part... need scale: divide by sqrt(2n)? Let's compute: (randn+ i randn)/2 has E|Aij|^2=1 for i!=j? Actually var = (1+1)/4=0.5. Hermitian symmetrize doubles? Simpler: generate with variance 1/n.
    return A

def scaled_gue(n):
    X = np.random.randn(n,n) + 1j*np.random.randn(n,n)
    X = (X+X.conj().T)/2/np.sqrt(2*n)
    # E|Xij|^2 = (1+1)/4/(2n)*? For i!=j: after symmetrize, variance = (0.5+0.5)/ (2n)? Let's just check spectral radius ~2.
    return X

# check
for n in [200]:
    X = scaled_gue(n)
    ev = np.linalg.eigvalsh(X)
    print(ev.min(), ev.max())

