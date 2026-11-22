"""Numerical diagnostics for fixed-budget near-singular Gaussian quadrature.

Run with standard Python 3: python verify.py. All universal limits are
proved analytically in RESULT.md; finite checks are illustrations only.
"""
from math import acos, asinh, atan, cos, cosh, isclose, log, pi, sin, sinh, sqrt, tan


def gauss01(m):
    assert isinstance(m, int) and m >= 1
    out = []
    for k in range(1, m + 1):
        x = cos(pi * (k - 0.25) / (m + 0.5))
        for _ in range(30):
            p0, p1 = 1.0, x
            if m == 1:
                pn, pm1 = p1, p0
            else:
                for j in range(2, m + 1):
                    p0, p1 = p1, ((2 * j - 1) * x * p1 - (j - 1) * p0) / j
                pn, pm1 = p1, p0
            deriv = m * (x * pn - pm1) / (x*x - 1)
            correction = pn / deriv
            x -= correction
            if abs(correction) < 1e-15:
                break
        # Nodes/weights map [-1,1] to [0,1].
        out.append(((x + 1) / 2, 1 / ((1-x*x)*deriv*deriv)))
    out.sort()
    assert all(0 < z < 1 and w > 0 for z, w in out)
    assert isclose(sum(w for _, w in out), 1, rel_tol=0, abs_tol=2e-12)
    return out


def values(m, d):
    zw = gauss01(m)
    A, U = atan(1 / d), asinh(1 / d)
    H = 1 / (d*d*sqrt(1+d*d))
    # f(x)=1+x^2; exactly integrated without numerical quadrature.
    I2 = A / d + 1 - d*A
    I3 = H + U - 1/sqrt(1+d*d)
    # β=1 sinh transformation, β=2 tangent, β=3 algebraic.
    sh2 = sum(w*U/d*(1+d*d*sinh(U*z)**2)/cosh(U*z) for z,w in zw)
    sh3 = sum(w*U/(d*d)*(1+d*d*sinh(U*z)**2)/cosh(U*z)**2 for z,w in zw)
    tn2 = A/d*sum(w*(1+d*d*tan(A*z)**2) for z,w in zw)
    alg3 = H*sum(w*(1+d*d*z*z/(1+d*d-z*z)) for z,w in zw)
    # Cancellation-free exact error expressions.
    et = 1-d*A*(1+sum(w*tan(A*z)**2 for z,w in zw))
    ea = U-1/sqrt(1+d*d)*(1+sum(w*z*z/(1+d*d-z*z) for z,w in zw))
    assert isclose(tn2, I2-et, rel_tol=2e-12)
    assert isclose(alg3, H+U-1/sqrt(1+d*d)-ea, rel_tol=2e-12)
    return I2,I3,sh2,sh3,tn2,alg3,et,ea


def main():
    checks = 0
    for m in (1,2,3,4,8,12):
        for d in (0.1,0.01,0.0001,0.000001):
            I2,I3,sh2,sh3,tan2,alg3,et,ea=values(m,d)
            for x in (I2,I3,sh2,sh3,tan2,alg3):
                assert x>0
                checks += 1
            assert isclose(I2-tan2,et,rel_tol=1e-7,abs_tol=2e-9)
            assert isclose(I3-alg3,ea,rel_tol=1e-3,abs_tol=0.005)  # cancellation at tiny d
            checks += 2
    # Quantitative limiting ratios for m=1; independent of an infinite proof.
    for d in (1e-7,1e-9,1e-11):
        I2,I3,sh2,sh3,_,_,et,ea=values(1,d)
        assert abs(et-1)<1e-5
        assert abs(ea/log(1/d)-1)<0.06
        assert sh2/I2<0.01
        assert sh3/I3<0.0001
        checks+=4
    # For a distinct polynomial f=1+x^2+x^4,
    # the inverse-square finite limiting error is ∫(1+x²)dx=4/3.
    for m in (1,2,4,8):
        zw=gauss01(m)
        d=1e-7
        A=atan(1/d)
        em2=(1-d*A) + (1/3-d*d+d**3*A)
        Qt=A/d*sum(w*(1+ (d*tan(A*z))**2+(d*tan(A*z))**4) for z,w in zw)
        Ia=A/d+em2
        assert abs((Ia-Qt)-4/3)<0.01
        checks+=1
    print('PASS',checks,'positive, error-identity and asymptotic diagnostics')


if __name__=='__main__':
    main()
