"""Deterministic boundary-arc tests for the regular Reuleaux odd-gon theorem."""
import math
from scipy.integrate import quad


def local_area(n, eps):
    alpha = math.pi/n
    q = 2*eps-eps*eps
    def top(s):
        if s == 0:
            return alpha
        a = math.sin(s/2)
        bmax = 4*a*(math.sin(s/2+alpha)-a)
        if q >= bmax:
            return alpha
        return math.asin(a+q/(4*a))-s/2
    return quad(top, 0, alpha, points=[eps, min(10*eps, alpha/2)], epsabs=2e-12, limit=300)[0]


def check():
    for n in (3,5,7,9):
        alpha = math.pi/n
        assert abs(n*alpha-math.pi)<1e-13
        constant=1+2*math.log(2*math.tan(alpha/2))
        for eps in (1e-5, 1e-6, 1e-7):
            got=local_area(n,eps)/eps-math.log(1/eps)
            assert abs(got-constant)<.002, (n,eps,got,constant)
        if n==3:
            assert abs(constant-(1+math.log(4/3)))<1e-12
    print('REULEAUX_ODD_POLYGON_CHECKS_OK')

if __name__=='__main__':
    check()
