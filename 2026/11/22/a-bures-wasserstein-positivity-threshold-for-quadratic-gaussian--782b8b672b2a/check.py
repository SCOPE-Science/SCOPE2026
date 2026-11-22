"""Numerical consistency checks for quadratic Gaussian integral-kernel positivity.

Requires NumPy. Finite matrices are diagnostics, not proofs of an
infinite-dimensional spectral assertion.
"""
import math
import numpy as np

COUNT = 0

def verify(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def creation(dim):
    M = np.zeros((dim, dim), dtype=complex)
    for j in range(dim-1):
        M[j+1, j] = math.sqrt(j+1)
    return M

def fock_quadratures(dim):
    ad = creation(dim)
    aa = ad.conj().T
    return (aa+ad), 1j*(ad-aa)

def bw_squared(A,D):
    sa, ua = np.linalg.eigh(A)
    da = (ua*np.sqrt(np.maximum(sa,0))) @ ua.T
    M = da @ D @ da
    eig = np.linalg.eigvalsh(M)
    return float(np.trace(A)+np.trace(D)-2*np.sqrt(np.maximum(eig,0)).sum())

def scalar_coefficient_test():
    dim = 42
    Q,P=fock_quadratures(dim)
    for a,d,b in ((1.,1.,1.),(4.,1.,1.),(5.,1.,1.),(0.,0.4,1.),(2.,0.5,3.)):
        S=np.eye(dim)+(a*Q@Q+d*P@P-(a+d)*np.eye(dim))/b
        N=dim-2
        for j in range(N):
            verify(abs(S[j,j]-(1+2*(a+d)*j/b)) < 1e-10,'diagonal matrix element')
        for j in range(N-2):
            verify(abs(S[j,j+2]-(a-d)*math.sqrt((j+1)*(j+2))/b)<1e-10,'two-step entry')
        for j in range(N):
            for k in range(N):
                if abs(j-k) not in (0,2):
                    verify(abs(S[j,k])<1e-10,'band property')
        # Test the exact kernel feature factorization on bounded coordinates.
        for x,y in ((0.,0.), (0.12,-0.27), (-0.33,0.13), (0.41,0.22)):
            v=np.array([(math.sqrt(b)*x)**j/math.sqrt(math.factorial(j)) for j in range(dim)])
            w=np.array([(math.sqrt(b)*y)**j/math.sqrt(math.factorial(j)) for j in range(dim)])
            target=math.exp(b*x*y)*(1+a*(x+y)**2-d*(x-y)**2)
            verify(abs(v@S@w-target)<1e-10,'coherent kernel identity')

    # Strict scalar edges and the 2024 example gamma boundary.
    for gamma in (0.,.5,1.,3.,4.,5.,8.):
        analytic=(math.sqrt(gamma)-1.)**2
        verify((analytic<=1+1e-12)==(0.<=gamma<=4.),'scalar threshold')
        verify(abs(bw_squared(np.array([[gamma]]),np.array([[1.]]))-analytic)<1e-10,'BW scalar')

def multidimensional_test():
    A=np.diag([4.,1.])
    D=np.array([[2.5,1.5],[1.5,2.5]])
    thresh=bw_squared(A,D)
    verify(.94<thresh<.95,'noncommuting BW value')
    verify(np.linalg.norm(A@D-D@A)>1.,'noncommuting pair')
    verify(abs(thresh-(10-2*math.sqrt(20.5)))<1e-10,'two-by-two trace formula')
    N=17
    Q,P=fock_quadratures(N+2)
    I=np.eye(N+2)
    q=[np.kron(Q,I),np.kron(I,Q)]
    p=[np.kron(P,I),np.kron(I,P)]
    h=sum(A[i,j]*q[i]@q[j]+D[i,j]*p[i]@p[j] for i in range(2) for j in range(2))
    keep=[i*(N+2)+j for i in range(N) for j in range(N)]
    h=h[np.ix_(keep,keep)]
    min_energy=float(np.linalg.eigvalsh(h)[0]); E=2*math.sqrt(20.5)
    verify(min_energy>=E-1e-9,'variational lower bound')
    # These finite truncations approach the infinite ground energy from above.
    verify(min_energy<E+0.5,'finite approximation to oscillator infimum')
    # Clearly separated cases avoid relying on extremely close threshold rounding.
    for b in (1.5,2.0,.5):
        S=np.eye(len(h))+(h-np.trace(A+D)*np.eye(len(h)))/b
        observed=float(np.linalg.eigvalsh(S)[0]); predicted=1-thresh/b
        verify(observed>=predicted-1e-9,'finite compression lower bound')
        if b>thresh:
            verify(observed>=-1e-9,'allowed positive case')
        else:
            verify(observed<0,'forbidden negative case')

if __name__=='__main__':
    scalar_coefficient_test()
    multidimensional_test()
    print('PASS:', COUNT, 'numerical algebra/feature/variational assertions')
