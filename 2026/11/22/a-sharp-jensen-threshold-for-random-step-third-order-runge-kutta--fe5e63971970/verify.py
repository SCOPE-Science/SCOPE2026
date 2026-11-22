"""Standalone exact checks and supplementary numerical checks for a sharp RK3 timestep-curvature theorem.
Run: python3 verify.py (standard library only).
"""
from fractions import Fraction as F
from math import factorial, sqrt

def add(a,b):
    o=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): o[i]+=v
    for i,v in enumerate(b): o[i]+=v
    return o

def mul(a,b):
    o=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): o[i+j]+=v*w
    return o

def stable_coeffs(a,b,order):
    # Coefficients of |sum_{j=0}^order (-a+i*b)^j h^j/j!|^2
    powers=[(F(1),F(0))]
    for j in range(1,order+1):
        x,y=powers[-1]
        powers.append((-a*x-b*y, b*x-a*y))
    re=[v[0]/factorial(j) for j,v in enumerate(powers)]
    im=[v[1]/factorial(j) for j,v in enumerate(powers)]
    return add(mul(re,re),mul(im,im))

def evaluate(a,x):
    o=F(0)
    for v in a[::-1]:o=o*x+v
    return o

def deriv(a):return [i*a[i] for i in range(1,len(a))]

# Exact coefficient identities for several rational generator parameters.
for a,b in [(F(1),F(0)),(F(1),F(3)),(F(2,3),F(5,2)),(F(3,4),F(7,8))]:
    r2=a*a+b*b
    expected3=[F(1),-2*a,2*a*a,-F(4,3)*a**3,
               r2*(8*a*a-r2)/12,-a*r2*r2/6,r2**3/36]
    assert stable_coeffs(a,b,3)==expected3
    expected2=[F(1),-2*a,2*a*a,-a*r2,r2*r2/4]
    assert stable_coeffs(a,b,2)==expected2
    for h in [F(0),F(1,10),F(1,4),F(3,10),F(2,3)]:
        # RK2 second derivative = a^2 + 3*r^4*(h-a/r^2)^2.
        actual=evaluate(deriv(deriv(expected2)),h)
        assert actual == a*a+3*r2*r2*(h-a/r2)**2
        # RK3 curvature normalized by t=r^2*h/a and v=a^2/r^2.
        t=r2*h/a;v=a*a/r2
        polyP=t*(5*t**3-20*t*t+48*t-48)/6
        actual=evaluate(deriv(deriv(expected3)),h)
        assert actual == a*a*(4-t*t+v*polyP)

# Derivative of R(t)=(t^2-4)/P(t). This numerator is exact after cancellation.
T=[F(0),-8,F(8),-F(10,3),F(5,6)]
q=[F(96),F(-192),F(144),F(-40),F(-10),F(5)]
# P'(t)*(t^2-4) - 2t*P(t) = q(t)/3: check sign convention.
lhs=add(mul(deriv(T),[-4,0,1]),[-v for v in mul(T,[0,2])])
assert lhs==[v/F(3) for v in q],(lhs,q)
# Correct Descartes-shift coefficients for q(t+2): constant to highest power.
from math import comb
shift=[sum(q[j]*comb(j,i)*F(2)**(j-i) for j in range(i,len(q))) for i in range(len(q))]
assert shift == [F(-32),F(-16),F(64),F(80),F(40),F(5)]
assert evaluate(q,F(2))==-32 and evaluate(q,F(3))==141

# Exact counterexample at a=1, b=3, mean H=3/10.
g=stable_coeffs(F(1),F(3),3)
mean=F(3,10); endpoints=[F(1,5),F(2,5)]
gap=evaluate(g,mean)-(evaluate(g,endpoints[0])+evaluate(g,endpoints[1]))/2
assert gap==F(401,36000),gap

# Numerical check of the isolated threshold and the global positivity/nonpositivity claims.
def poly(t):return 5*t**5-10*t**4-40*t**3+144*t*t-192*t+96
lo,hi=2.0,3.0
for _ in range(85):
    mid=(lo+hi)/2
    if poly(mid)>0:hi=mid
    else:lo=mid
root=(lo+hi)/2
p=root*(5*root**3-20*root**2+48*root-48)/6
vcrit=(root**2-4)/p
assert 2.57<root<2.58 and .2161<vcrit<.2162
assert 1.904<sqrt(1/vcrit-1)<1.905
for v in [vcrit, .3, .5, 1.0]:
    for j in range(20001):
        t=j/1000
        pt=t*(5*t**3-20*t*t+48*t-48)/6
        assert 4-t*t+v*pt > -5e-12,(v,t)
assert 4-9+F(1,10)*evaluate(T,F(3)) == F(-49,20)
print('VERIFICATION_OK; t_star=%.12f; v_star=%.12f; b/a threshold=%.12f; exact witness gain=%s' % (root,vcrit,sqrt(1/vcrit-1),gap))
