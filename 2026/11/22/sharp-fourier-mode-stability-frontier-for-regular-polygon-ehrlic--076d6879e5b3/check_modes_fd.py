"""Finite directional-difference checks for the simultaneous polygon update."""
import cmath
from math import pi

def E(z):
    n = len(z)
    ans = []
    for i, u in enumerate(z):
        p = u**n-1
        ans.append(u-p/(n*u**(n-1)-p*sum(1/(u-v) for j,v in enumerate(z) if j != i)))
    return ans

worst = 0.
count = 0
for n in range(2, 10):
    zeta = cmath.exp(2j*pi/n)
    for w in (.15, .78+.19j, 1.21, (((n+1)/(n-1))**(1/n))*cmath.exp(1j*pi/n)):
        z = [w*zeta**j for j in range(n)]
        t = w**n
        if t.real < 0 and abs(t.imag)<1e-12:
            assert max(map(abs,E(z)))<1e-12
        for k in range(1,n+1):
            v = [zeta**(k*j) for j in range(n)]
            D = (n*n-1-2*(k-1)*(n+1-k)) * ((t-1)/((n+1)*t+n-1))**2
            d = 2e-6
            a = E([u+d*x for u,x in zip(z,v)])
            b = E([u-d*x for u,x in zip(z,v)])
            err = max(abs((x-y)/(2*d)-D*q) for x,y,q in zip(a,b,v))/(1+abs(D))
            worst = max(worst,err)
            assert err<2e-7,(n,w,k,err)
            count += 1
print('finite difference mode comparisons',count,'worst scaled error',worst)
