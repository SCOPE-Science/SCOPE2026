"""Numerical consistency checks for degree-fixed Matérn-window Gabor-frame asymptotics.
Run with Python 3 standard library. Finite sampling is not a proof of optimal bounds.
"""
import cmath
import math
from fractions import Fraction


def coeffs(m):
    n=m-1
    return [Fraction(math.factorial(n)*math.factorial(2*n-j)*2**j,
                     math.factorial(2*n)*math.factorial(n-j)*math.factorial(j))
            for j in range(n+1)]


def poly(m,s):
    return sum(float(c)*s**j for j,c in enumerate(coeffs(m)))


def window(m,lam,x):
    s=lam*abs(x)
    return math.exp(-s)*poly(m,s)


def zak(m,lam,x,w):
    return sum(window(m,lam,x-k)*cmath.exp(2j*math.pi*k*w)
               for k in range(-6,7))


def symbol(m,lam,x,w):
    return abs(zak(m,lam,x,w))**2 + abs(zak(m,lam,x,w+0.5))**2


def run():
    count=0
    for m in range(2,7):
        c=coeffs(m)
        assert c[0]==1
        assert c[1]==1
        assert c[-1]==Fraction(2**(m-1)*math.factorial(m-1),math.factorial(2*m-2))
        for j in range(len(c)-1):
            assert (j+1)*c[j+1]<=c[j]
            count+=4
    for m in (2,3,4,5,6):
        for lam in (8.0,12.0,20.0,30.0):
            mid=window(m,lam,0.5)
            center=symbol(m,lam,0.5,0.0)
            target=4*mid*mid
            assert abs(center-target)/target < 0.07
            count+=1
            vmin=math.inf
            vmax=-1
            xmin=None
            for i in range(41):
                x=0.5*i/40
                for j in range(21):
                    w=0.5*j/20
                    v=symbol(m,lam,x,w)
                    if v<vmin:
                        vmin=v; xmin=x
                    vmax=max(vmax,v)
                    count+=1
            assert abs(vmin-center)/center < 0.07
            assert xmin>0.48
            assert vmax <= 2.15
            lead=4*(math.factorial(m-1)/math.factorial(2*m-2))**2 * lam**(2*m-2)*math.exp(-lam)
            assert vmin>0 and (vmin/lead)>0.98
            print('m',m,'lambda',lam,'A_grid',round(vmin,12),'A/lead',round(vmin/lead,6),'B_grid',round(vmax,8))
    print('MATERN_GABOR_ASYMPTOTICS_CHECKS_PASSED',count)


if __name__=='__main__':
    run()
