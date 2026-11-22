"""Recompute the quadratic-harmonic polar-cap concentration spectrum."""
import math
import mpmath as mp

mp.mp.dps = 60
count = 0

def check(d, a):
    global count
    a=mp.mpf(a); d=mp.mpf(d)
    c=mp.gamma(d/2)/(mp.sqrt(mp.pi)*mp.gamma((d-1)/2))
    # Equal two polar caps; independently integrate moment weights.
    J = lambda m: 2*c*mp.quad(lambda t:t**m*(1-t*t)**((d-3)/2),[a,1])
    j0,j2,j4=J(0),J(2),J(4)
    Z=(j4-2*j2/d+j0/d**2)/(2*(d-1)/(d*d*(d+2)))
    M=d*(d+2)/(d-1)*(j2-j4)
    Q=d*(d+2)/((d-1)*(d+1))*(j0-2*j2+j4)
    F=2*c*a*(1-a*a)**((d-1)/2)
    K=d*(d+2)/(2*(d-1))
    pairs=[(Z-M,K*F*(a*a-1/d)),
           (M-Q,2*K*F*(1-a*a)/(d+1)),
           (Z-Q,K*F*(d-1)/(d+1)*(a*a+1/d))]
    for lhs,rhs in pairs:
        assert mp.almosteq(lhs,rhs,rel_eps=mp.mpf('1e-47'),abs_eps=mp.mpf('1e-48')), (d,a,lhs,rhs)
        count+=1
    assert mp.mpf('0')<Q<min(Z,M)<mp.mpf('1')
    count+=1
    if abs(a*a-1/d)>mp.mpf("1e-45"):
        if a*a<1/d: assert M>Z>Q, (d,a,Z,M,Q)
        else: assert Z>M>Q, (d,a,Z,M,Q)
    else:
        assert mp.almosteq(Z,M,rel_eps=mp.mpf("1e-47"),abs_eps=mp.mpf("1e-48"))
    count+=1

for d in range(3,15):
    for a in ['0.04','0.2','0.37','0.6','0.84','0.97',1/mp.sqrt(d)]:
        check(d,a)
print('POLAR_CAP_CHECKS_PASS',count)
