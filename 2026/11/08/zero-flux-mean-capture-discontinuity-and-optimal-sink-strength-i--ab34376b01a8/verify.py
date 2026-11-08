"""Reproduce the exact quantum-sink absorption-time identities.

Requires Python 3, SymPy, NumPy and SciPy. No external data or network access.
"""
import math
import sympy as sp
import numpy as np
from scipy.linalg import solve_continuous_lyapunov


def symbolic_certificate():
    A, B, k = sp.symbols('A B k', positive=True, real=True)
    I = sp.I
    s = A**2 + B**2
    d = A**2 - B**2
    H = sp.Matrix([[0,A,0,0],[A,0,0,0],[0,0,0,B],[0,0,B,0]])
    w = sp.Matrix([1,0,1,0])/sp.sqrt(2)
    v = sp.Matrix([1,0,-1,0])/sp.sqrt(2)
    K = -I*H - k*w*w.T/2
    Y = sp.Matrix([
        [1/k+k*s/(4*d*d),0,-k*s/(4*d*d),I*B/d],
        [0,1/k+k*A*A/(2*d*d),I*A/d,-k*A*B/(2*d*d)],
        [-k*s/(4*d*d),-I*A/d,1/k+k*s/(4*d*d),0],
        [-I*B/d,-k*A*B/(2*d*d),0,1/k+k*B*B/(2*d*d)]
    ])
    residual=K*Y+Y*K.conjugate().T+v*v.T
    assert all(sp.cancel(z)==0 for z in residual), 'main Lyapunov certificate'
    assert sp.cancel(sp.trace(Y)-(4/k+k*s/d**2))==0
    # Both zero-flux endpoints: remove the spurious decoupled mode.
    Y0=Y.subs(B,0)
    Y0[3,3]=0
    K0=K.subs(B,0)
    assert all(sp.cancel(z)==0 for z in (K0*Y0+Y0*K0.conjugate().T+v*v.T))
    assert sp.cancel(sp.trace(Y0)-(3/k+k/A**2))==0
    Y2=Y.subs(A,0)
    Y2[1,1]=0
    K2=K.subs(A,0)
    assert all(sp.cancel(z)==0 for z in (K2*Y2+Y2*K2.conjugate().T+v*v.T))
    assert sp.cancel(sp.trace(Y2)-(3/k+k/B**2))==0
    # Half flux: initial state is in an invariant detector-orthogonal subspace.
    Hpi=H.subs(B,A)
    assert sp.simplify(w.T*v)==sp.zeros(1,1)
    assert all(sp.simplify((w.T*(Hpi**n)*v)[0])==0 for n in range(8))
    x,J,phi=sp.symbols('x J phi',real=True, positive=True)
    t=4/x+x/(4*J**2*sp.cos(phi/2)**2)
    assert sp.simplify(t.subs(x,4*J*sp.cos(phi/2))-2/(J*sp.cos(phi/2)))==0
    t0=3/x+x/(4*J**2)
    assert sp.simplify(t0.subs(x,2*sp.sqrt(3)*J)-sp.sqrt(3)/J)==0
    print('symbolic matrix certificate, degenerate endpoints, and optima: PASS')


def independent_site_basis_checks():
    # This Hamiltonian is constructed independently in the physical site basis.
    # No block-diagonal canonical matrix is used for these checks.
    J=1.7
    initial=np.eye(4, dtype=complex)[:,2]
    target=np.eye(4, dtype=complex)[:,0]
    tests=0
    for phi in [0.0, 0.08, 0.19, 0.7, 1.3, 2.6, 3.7, 4.8, 5.8, 6.14, 2*math.pi]:
        H=np.zeros((4,4),dtype=complex)
        for j in range(4):
            l=(j+1)%4
            H[l,j] += J*np.exp(1j*phi/4)
            H[j,l] += J*np.exp(-1j*phi/4)
        for k in [0.35, 1.2, 3.1, 7.0]:
            K=-1j*H-k*np.outer(target,target.conj())/2
            if phi in (0.0, 2*math.pi):
                krylov=np.column_stack([np.linalg.matrix_power(H,m)@initial for m in range(4)])
                U, singular_values, _=np.linalg.svd(krylov, full_matrices=False)
                assert sum(singular_values>1e-8)==3
                U=U[:,:3]
                Kr=U.conj().T@K@U
                vr=U.conj().T@initial
                C=solve_continuous_lyapunov(Kr,-np.outer(vr,vr.conj()))
                residual=Kr@C+C@Kr.conj().T+np.outer(vr,vr.conj())
            else:
                C=solve_continuous_lyapunov(K,-np.outer(initial,initial.conj()))
                residual=K@C+C@K.conj().T+np.outer(initial,initial.conj())
            numeric=float(np.trace(C).real)
            if phi in (0.0,2*math.pi):
                expected=3/k+k/(4*J**2)
            else:
                expected=4/k+k/(4*J**2*math.cos(phi/2)**2)
            assert abs(numeric-expected) < 2e-9*(1+expected), (phi,k,numeric,expected)
            assert np.linalg.norm(residual) < 5e-9
            tests += 2
    # At half flux there is zero detector amplitude for any time.
    phi=math.pi
    H=np.zeros((4,4),dtype=complex)
    for j in range(4):
        l=(j+1)%4
        H[l,j] += J*np.exp(1j*phi/4)
        H[j,l] += J*np.exp(-1j*phi/4)
    assert all(abs(np.vdot(target,np.linalg.matrix_power(H,m)@initial))<1e-10 for m in range(9))
    print(f'independent site-basis Lyapunov comparisons: PASS ({tests} numerical checks)')


if __name__=='__main__':
    symbolic_certificate()
    independent_site_basis_checks()
    print('ALL CHECKS PASSED')
