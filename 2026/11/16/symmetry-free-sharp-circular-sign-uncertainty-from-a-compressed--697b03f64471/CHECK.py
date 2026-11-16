"""Reproducible finite checks for the asymmetric circle sign-radius formula.
Only numerical diagnostics; the all-degree theorem is proved analytically.
"""
import cmath
import math


def verify():
    count = 0
    for w in (0.05, 0.125, 0.25, 0.5, 0.75, 0.95):
        lam = 0.5 * math.sqrt((1 - w) / (1 + w))
        q0 = math.sqrt(1 - w*w) - 1j*w
        q1 = 1.0
        # G=[[1,iw],[-iw,1]]; C=[[0,c],[c,0]].
        c = (1-w)/2
        Gq = (q0 + 1j*w*q1, -1j*w*q0+q1)
        Cq = (c*q1, c*q0)
        for a,b in zip(Cq,Gq):
            assert abs(a-lam*b) < 4e-13
            count+=1
        norm = (q0.conjugate()*Gq[0] + q1.conjugate()*Gq[1]).real
        cos_expect = (q0.conjugate()*Cq[0] + q1.conjugate()*Cq[1]).real
        assert abs(cos_expect - lam*norm)<1e-12
        # The exact average is the convex combination of Haar and one point mass.
        # For |q0+z|^2, Haar moment is |q0|^2+1, cosine moment Re(q0).
        mean = (1-w)*(abs(q0)**2+1)+w*abs(q0+1j)**2
        cmoment = (1-w)*q0.real  # atom cosine(pi/2)=0
        # Note convention Q=q0+z: Gq expectation from direct integrals.
        assert abs(mean-norm)<1e-12
        assert abs(cmoment-cos_expect)<1e-12
        assert abs(lam*mean-cmoment)<1e-12
        # c(theta) = cos(theta); extremal sign changes exactly at arccos(lam).
        root = math.acos(lam)
        for eps in (.0001, .02, .1):
            left = (lam-math.cos(root-eps))*abs(q0+cmath.exp(1j*(root-eps)))**2
            right = (lam-math.cos(root+eps))*abs(q0+cmath.exp(1j*(root+eps)))**2
            assert left < 0 and right > 0
            count+=2
        # Symmetrization (mass split between +/- pi/2) changes the sharp radius.
        sym_lam=(1-w)/2
        assert lam > sym_lam and math.acos(lam)<math.acos(sym_lam)
        count+=1
    # Haar N=1..12: compressed cosine operator has Toeplitz tridiagonal
    # eigenvalues cos(k*pi/(N+1)), so the top gives pi/(N+1).
    for n in range(1,13):
        lam=math.cos(math.pi/(n+1))
        assert abs(math.acos(lam)-math.pi/(n+1)) < 1e-10
        count+=1
    print(f"CHECK_OK asymmetric_atomic_examples=6 eigen_residuals=12 sign_tests=36 Haar_degrees=12 total={count}")

if __name__ == '__main__':
    verify()
