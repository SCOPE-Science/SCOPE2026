"""Numerical cross-checks for two angular transitions in parabolic triangles.

The proof of the asymptotics is analytic; these checks test its geometry and
leading coefficients on finite grids. No finite test certifies an asymptotic.
"""
from math import atan, pi, sqrt

A0 = 1 / sqrt(3)
A1 = sqrt(3) / 2 + 2 * sqrt(6) / 3
Q = (0.5 + sqrt(2)) / sqrt(3)
ETA = sqrt(3 / 2)
C0 = (48 / 5) * 3 ** 0.25
C1 = 8 / (5 * A1 ** 3 * sqrt(ETA))

def radical(i, b):
    x = 0.0
    f = 1.0 / b
    while i:
        x += (i % b) * f
        i //= b
        f /= b
    return x

def angles(x, y, z):
    p, q, r = atan(x + y), atan(x + z), atan(y + z)
    return q - p, pi - (r - p), r - q

def check(n=200000):
    assert abs(angles(-A0, 0, A0)[1] - 2*pi/3) < 1e-12
    assert abs((atan(A1 - Q) + atan(2*Q)) - 2*pi/3) < 1e-12
    assert abs(1/(1+(A1-Q)**2) - 2/(1+4*Q**2)) < 1e-12
    # In each targeted box, integrate the exact angular event, then compare
    # with its analytically computed shrinking-domain volume.
    for delta in (0.005, 0.001):
        a = A0 + delta
        count = 0
        for i in range(1,n+1):
            u = radical(i,2) * 2.5*delta
            v = (radical(i,3)*4 - 2)*sqrt(delta)
            w = radical(i,5)*2.5*delta
            x,y,z = -a+u,v,a-w
            if x < y < z and angles(x,y,z)[1] < 2*pi/3:
                count += 1
        box_vol = (2.5*delta)**2 * 4*sqrt(delta)
        p = 3/(4*a**3) * box_vol * count/n
        ratio = p/delta**2.5
        assert abs(ratio/C0-1) < (0.05 if delta==0.005 else 0.025), (delta,ratio,C0)
        print('middle onset',delta,'ratio',round(ratio,6),'limit',round(C0,6))
    for delta in (0.005,0.001):
        a = A1 + delta
        count = 0
        for i in range(1,n+1):
            x = -Q + (radical(i,2)*3 - 1.5)*sqrt(delta)
            u = radical(i,3)*3*delta
            w = radical(i,5)*1.5*delta
            y,z = x+u,a-w
            if x < y < z and angles(x,y,z)[0]>2*pi/3:
                count += 1
        box_vol = 3*sqrt(delta)*3*delta*1.5*delta
        p = 2*3/(4*a**3) * box_vol * count/n
        ratio = p/delta**2.5
        assert abs(ratio/C1-1)<0.035,(delta,ratio,C1)
        print('endpoint onset',delta,'ratio',round(ratio,8),'limit',round(C1,8))
    assert abs(64/(15*3**.25)*3/(4*A0**3)-C0) < 1e-12
    assert abs(16/(15*sqrt(ETA))*2*3/(4*A1**3)-C1) < 1e-12
    print('PARABOLIC_FERMAT_TWO_ONSETS_CHECKS_OK')

if __name__ == '__main__':
    check()
