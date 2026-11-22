#!/usr/bin/env python3
"""Independent exact-arithmetic and direct-harmonic checks of equatorial jet sampling.
Run: python3 VERIFY.py. Dependencies: Python standard library, NumPy, SciPy.
"""
from fractions import Fraction
from math import comb, factorial, pi, sqrt
import numpy as np
from scipy.special import sph_harm_y


def lambda_exact(ell, m):
    m = abs(m)
    if not (0 <= m <= ell and ell >= 1):
        raise ValueError('out of range')
    if (ell+m)%2 == 0:
        a, b = (ell+m)//2, (ell-m)//2
        return Fraction((2*ell+1)*comb(2*a,a)*comb(2*b,b), 4**ell)
    a, b = (ell+m-1)//2, (ell-m-1)//2
    return Fraction((2*ell+1)*factorial(2*a+1)*factorial(2*b+1),
                    4**(ell-1)*factorial(a)**2*factorial(b)**2*ell*(ell+1))


def predicted_rank(ell,M):
    if M % 2:
        return min(M,ell+1)+min(M,ell)
    return min(M,2*ell+1)


def direct_matrix(ell,M):
    # Direct special-function derivatives, independent of factorial formulas.
    z=np.zeros((2*M, 2*ell+1),dtype=np.complex128)
    for j in range(M):
        for k,m in enumerate(range(-ell,ell+1)):
            val, grad=sph_harm_y(ell,m,pi/2,2*pi*j/M,diff_n=1)
            z[j,k]=sqrt(4*pi/M)*val
            z[M+j,k]=sqrt(4*pi/(M*ell*(ell+1)))*grad[0]
    return z


def predicted_spec(ell,M):
    # Gram nonzero eigenvalues are the sums over each (DFT-residue, parity-channel).
    groups={}
    for m in range(-ell,ell+1):
        key=(m%M,(ell+m)%2)
        groups[key]=groups.get(key,Fraction(0,1))+lambda_exact(ell,m)
    return sorted([float(v) for v in groups.values() if v>0]
                  + [0.]*(2*ell+1-len(groups)))


def main():
    exact_assertions=0
    for ell in range(1,65):
        vals=[lambda_exact(ell,m) for m in range(-ell,ell+1)]
        vmax=max(vals);vmin=min(vals)
        assert vmax==lambda_exact(ell,ell)
        assert vmin==lambda_exact(ell,ell-1)
        assert vmax/vmin==Fraction(ell+1,2)
        assert lambda_exact(ell,0)==lambda_exact(ell,1)
        exact_assertions+=4
        for M in range(1,4*ell+5):
            classes={(m%M,(ell+m)%2) for m in range(-ell,ell+1)}
            rank=len(classes)
            assert rank==predicted_rank(ell,M)
            exact_assertions+=1
            full=rank==2*ell+1
            assert full == (M>=ell+1 if M%2 else M>2*ell)
            exact_assertions+=1
            if full:
                assert all(sum(1 for m in range(-ell,ell+1)
                               if (m%M,(ell+m)%2)==c)==1 for c in classes)
                exact_assertions+=1
    matrix_checks=0
    max_err=0.0
    for ell in range(1,12):
        for M in range(1,2*ell+5):
            Z=direct_matrix(ell,M)
            mat=Z.conj().T@Z
            spectrum=np.linalg.eigvalsh(mat)
            expect=np.array(predicted_spec(ell,M),dtype=float)
            err=float(np.max(abs(spectrum-expect)))
            max_err=max(max_err,err)
            assert err<4e-11, (ell,M,err)
            assert np.linalg.matrix_rank(Z,tol=2e-9)==predicted_rank(ell,M)
            if (M%2 and M>=ell+1) or (M%2==0 and M>2*ell):
                expected_diag=np.array([float(lambda_exact(ell,m)) for m in range(-ell,ell+1)])
                assert np.max(abs(mat-np.diag(expected_diag)))<4e-11
            matrix_checks+=1
    print(f'EQUATOR_JET_PASS exact_assertions={exact_assertions} direct_matrices={matrix_checks} max_spectral_error={max_err:.3g}')

if __name__=='__main__': main()
