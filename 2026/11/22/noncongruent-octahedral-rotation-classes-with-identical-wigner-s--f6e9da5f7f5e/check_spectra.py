"""Independent finite checks for two cubic rotation configurations.

Usage: python check_spectra.py
Requires Python 3 and NumPy. Finite checks supplement the all-degree proof.
"""
import itertools
import math
import numpy as np

SQ = math.sqrt(0.5)
AXES = np.eye(3)


def configurations():
    c4 = []
    c2 = []
    for i in range(3):
        for sign in (1, -1):
            c4.append(np.r_[SQ, SQ * sign * AXES[i]])
            j, k = [v for v in range(3) if v != i]
            direction = SQ * (AXES[j] + sign * AXES[k])
            c2.append(np.r_[0.0, direction])
    return c4, c2


def relative_trace(x, y):
    # SO(3) relative rotation angle theta has cos(theta/2)=abs(<x,y>).
    dot = float(np.dot(x,y))
    return 4*dot*dot-1  # Tr(R_x^{-1}R_y) = 1 + 2 cos(theta)


def su2(q):
    a, x, y, z = q
    return np.array([[a+1j*z,y+1j*x],[-y+1j*x,a-1j*z]], dtype=complex)


def symmetric_power(U, n):
    """Spin-n/2 action on the normalized symmetric tensor basis."""
    M=np.zeros((n+1,n+1),dtype=complex)
    for k in range(n+1):
        for r in range(n+1):
            coeff=0j
            for p in range(max(0,r-k),min(r,n-k)+1):
                q=r-p
                coeff += (math.comb(n-k,p)*math.comb(k,q)
                          * U[0,0]**(n-k-p)*U[1,0]**p
                          * U[0,1]**(k-q)*U[1,1]**q)
            M[r,k] = coeff*math.sqrt(math.comb(n,k)/math.comb(n,r))
    return M


def kernel_formula(ell):
    d=2*ell+1
    a=(-1)**ell
    b=(1,0,-1)[ell%3]
    K=np.full((6,6),b,dtype=float)
    np.fill_diagonal(K,d)
    for p in range(3):
        K[2*p,2*p+1]=a
        K[2*p+1,2*p]=a
    return K/d


def predicted_levels(ell):
    d=2*ell+1
    a=(-1)**ell
    b=(1,0,-1)[ell%3]
    return sorted([ (d-a)/d ]*3+[(d+a-2*b)/d]*2+[(d+a+4*b)/d])


def run():
    X, Y = configurations()
    for Z in (X,Y):
        assert len(Z)==6
        assert all(abs(np.dot(z,z)-1)<1e-12 for z in Z)
        assert np.linalg.matrix_rank(np.array(Z),tol=1e-10)==(4 if Z is X else 3)
        for i,j in itertools.product(range(6),repeat=2):
            tr = relative_trace(Z[i],Z[j])
            expected = 3 if i==j else (-1 if i//2==j//2 else 0)
            assert abs(tr-expected)<1e-12, (i,j,tr,expected)
    print('Geometric pair angles and projective linear ranks: PASS')
    for ell in range(1,7):
        K=kernel_formula(ell)
        for Z in (X,Y):
            D=[symmetric_power(su2(z),2*ell) for z in Z]
            assert all(np.linalg.norm(T.conj().T@T-np.eye(2*ell+1))<2e-10 for T in D)
            K_rep=np.array([[np.trace(D[i]@D[j].conj().T)/(2*ell+1)
                             for j in range(6)] for i in range(6)])
            assert np.max(np.abs(K-K_rep))<2e-10, (ell,K_rep)
            assert np.max(np.abs(np.linalg.eigvalsh(K)-predicted_levels(ell)))<2e-10
        print('Independent spin representation, degree',ell,': PASS')
    for ell in range(1,10001):
        e=predicted_levels(ell)
        assert e[0]>0
        assert e[0]>=2/5-1e-12 and e[-1]<=8/5+1e-12
        if ell != 2:
            assert e[0]>2/5 and e[-1]<8/5
    print('Finite degree scan 1..10000: PASS (not a proof of infinite claim)')
    for ell in (1,2,3,4,5,6,7,8,9,10):
        G=kernel_formula(ell)
        # Symmetrization inequality: arbitrary weights cannot improve extremes.
        gmin,gmax=np.linalg.eigvalsh(G)[[0,-1]]
        rng=np.random.default_rng(231+ell)
        for _ in range(100):
            w=np.exp(rng.normal(0,1,6));w=6*w/sum(w)
            W=np.diag(np.sqrt(w))
            mine,maxe=np.linalg.eigvalsh(W@G@W)[[0,-1]]
            assert mine<=gmin+1e-10 and maxe>=gmax-1e-10
    print('Finite weighted check: PASS (analytic symmetrization proves general case)')

if __name__=='__main__':
    run()
