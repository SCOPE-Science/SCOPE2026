"""Reproduction of the premium-spoke heat-trace activation theorem.

Requires Python 3, NumPy, SciPy, and SymPy. Analytical arguments in RESULT.md
establish the all-parameter claims; numerical tests are finite corroboration.
Run: python verify.py
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar, brentq


def lap(m, weights):
    L = np.zeros((m + 1, m + 1))
    for j, w in enumerate(weights, start=1):
        L[0, 0] += w
        L[j, j] += w
        L[j, 0] -= w
        L[0, j] -= w
    return L


def heat(m, weights, t):
    return float(np.exp(-t * np.linalg.eigvalsh(lap(m, weights))).sum())


def threshold(m, z):
    s = math.exp(-z)
    a = math.exp(-m * z)
    return (m - 1) * (m + 1 + (m - 1) * a) / (m * (m * a + (m - 2) * s))


def design(m, B, r, x):
    return [x] + [(B-r*x)/(m-1)] * (m-1)


def run():
    checks = 0
    # The exact derivative numerator of the threshold wrt s=e^{-z}.
    s = sp.symbols('s', positive=True)
    for m in range(3, 20):
        Nm = (m+1)+(m-1)*s**m
        Dm = m*s**m+(m-2)*s
        raw = sp.expand(sp.diff(Nm, s)*Dm-Nm*sp.diff(Dm, s))
        target = (m-1)**2*(m-2)*s**m-m*m*(m+1)*s**(m-1)-(m-2)*(m+1)
        assert sp.simplify(raw-target)==0
        checks+=1

    # Exact characteristic polynomial of a star with one zero spoke.
    x, y, lam = sp.symbols('x y lam')
    for m in range(3, 10):
        M=sp.zeros(m+1)
        for j in range(2, m+1):
            M[0,0]+=y;M[j,j]+=y;M[0,j]-=y;M[j,0]-=y
        cp=sp.factor((lam*sp.eye(m+1)-M).det())
        assert sp.simplify(cp-lam**2*(lam-y)**(m-2)*(lam-m*y))==0
        checks+=1

    # Exp(-tL) at zero distinguished conductance: exact spectral projectors.
    for m in range(3, 12):
        B = 1.
        y=B/(m-1)
        M=lap(m,[0]+[y]*(m-1))
        vals, U=np.linalg.eigh(M)
        for t in (0.07,0.6,2.7):
            P=(U*np.exp(-t*vals))@U.T
            E=math.exp(-m*t*y)
            e=math.exp(-t*y)
            bc=np.zeros(m+1);bc[0]=1;bc[1]=-1
            bo=np.zeros(m+1);bo[0]=1;bo[2]=-1
            A=float(bc@P@bc)
            C=float(bo@P@bo)
            expected_A=(m+1+(m-1)*E)/m
            expected_C=(m*E+(m-2)*e)/(m-1)
            assert abs(A-expected_A)<1e-12
            assert abs(C-expected_C)<1e-12
            assert abs(A/C-threshold(m,t*y))<1e-11
            checks+=3

    # Every cheap edge remains active for r>1, a boundary-direction test.
    for m in range(3, 12):
        for r in (1.03,1.2,2.,10.,100.):
            for Bt in (0.2,1.,4.,15.):
                E=math.exp(-2*Bt/r)
                direction=(m-1)*Bt*(2*E/r-(3+E)/2)
                assert direction<0
                checks+=1

    # Compare the exact active-set condition with unrestricted 1d minimization
    # (the unrestricted vector problem is strictly convex and permutation-invariant).
    for m in (3,4,5,7,10,16):
        for r in (1.05,1.3,2.,5.,20.):
            B=1.
            rt=brentq(lambda T:threshold(m,B*T/(m-1))-r,1e-14,80*m)
            assert abs(threshold(m, B*rt/(m-1))-r)<1e-9
            for factor in (0.15,0.55,0.9,1.1,1.8,4.0):
                t=rt*factor
                f=lambda xx: heat(m,design(m,B,r,xx),t)
                sol=minimize_scalar(f,bounds=(0.,B/r),method='bounded',
                                    options={'xatol':2e-13})
                if factor<1:
                    assert f(0)<=sol.fun+1e-8
                    assert sol.x<2e-6/r
                else:
                    assert sol.x>1e-8/r
                    assert sol.fun<f(0)-1e-11
                assert sol.fun<=f(B/r)+1e-8
                checks+=3

    # Large-size crossover: Bt_crit/(m-1) approaches log r.
    for r in (1.1,1.5,3.,10.):
        seq=[]
        for m in (20,40,80,160,320):
            z=brentq(lambda z:threshold(m,z)-r,1e-12,max(15.,math.log(r)*4))
            seq.append(abs(z-math.log(r)))
            checks+=1
        assert seq[-1]<0.04 and seq[-1]<seq[0]
        checks+=1

    print(f'VERIFY_OK {checks} checks')


if __name__=='__main__':
    run()
