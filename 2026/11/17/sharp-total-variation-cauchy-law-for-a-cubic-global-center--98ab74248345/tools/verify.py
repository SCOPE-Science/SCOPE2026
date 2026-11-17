"""Standard-library numerical diagnostics for a cubic center's sharp TV law.
Only finite numerical tests; analytic limit proof is supplied separately.
"""
from math import pi,log,cos,sin,asin,atan,sqrt,exp,expm1

def simpson(fn,a,b,n=60000):
    if n%2:n+=1
    h=(b-a)/n
    res=fn(a)+fn(b)
    for j in range(1,n):
        res+=(4 if j%2 else 2)*fn(a+j*h)
    return res*h/3

def integrand(t,L):
    if t==0: return 2*sqrt(L)
    u=L*sin(t)**2
    return 2*L*sin(t)/sqrt(expm1(u))

def J(L):return simpson(lambda t:integrand(t,L),0,pi/2)

def P_le(s,L,Jv):
    th=asin(sqrt(s/L))
    return simpson(lambda t:integrand(t,L),0,th)/Jv

def Cauchy_le(s):return 2/pi*atan(sqrt(expm1(s)))

print('Mean log-Cauchy=',2*log(2))
c=2/pi*simpson(lambda t: log(2*cos(t)),0,pi/3,12000)
print('Predicted q*TV=',c)
for L in [10,20,40,80,160]:
    j=J(L)
    cut=L*(1-(pi/j)**2)
    tv=Cauchy_le(cut)-P_le(cut,L,j)+1-Cauchy_le(L)
    print('L %3d  J %.12f cut %.9f  L*TV %.11f err %.3g'%(L,j,cut,L*tv,L*tv-c))
    assert cut>0 and 0<tv<1
    assert abs((j/pi-1)*L-log(2))<0.5
assert abs(L*tv-c)<0.04
print('CUBIC_TV_DIAGNOSTICS_OK')
