"""Independent calculations for the three-category centered cyclic-variation theorem.

Requirements: Python 3.10+, SymPy, SciPy. This is a finite symbolic/numeric
cross-check; the proof for all sample sizes is given in RESULT.md.
"""
import math
import sympy as s
from scipy.integrate import quad

assertions = 0

def check(condition, message):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)

pi = s.pi
a = s.symbols('a', positive=True)
t = 3*s.sqrt(1-2*a)
F = lambda x: 1+x*x + (2/pi)*((3-x*x)*s.atan(1/x) +3*x -(1+s.sqrt(1+x*x))**2)
V = 2*a*F(t)
u = s.Rational(1, 3)
check(s.simplify(V.subs(a, u) - (s.Rational(8,3)+(4*s.sqrt(3)-12)/pi)) == 0,
      'uniform coefficient')
check(s.simplify(s.diff(V,a).subs(a,u)) == 0, 'uniform derivative')
curv = 3*(81-16*pi-24*s.sqrt(3))/pi
check(s.simplify(s.diff(V,a,2).subs(a,u)-curv) == 0,
      'uniform second derivative')
check(float(curv)<0, 'strict curvature')
edge = 4*(1-2/pi)
z=s.symbols('z',positive=True)
check(s.simplify(s.limit(F(z),z,0,dir='+')-edge)==0,
      'edge coefficient')
check(float(edge - V.subs(a,u))>0, 'edge larger than uniform')

for x in [0.0,0.1,0.5,1.0,math.sqrt(3),2.4,3.0]:
    angle = math.atan2(1.0,x)
    def angular(theta):
        return math.cos(theta)+max(math.cos(theta),x*math.sin(theta))
    meanang = 2/math.pi*(quad(angular,0,angle,epsabs=1e-12)[0]+quad(angular,angle,math.pi/2,epsabs=1e-12)[0])
    sqang = 2/math.pi*(quad(lambda th:angular(th)**2,0,angle,epsabs=1e-12)[0]+quad(lambda th:angular(th)**2,angle,math.pi/2,epsabs=1e-12)[0])
    mean = math.sqrt(math.pi/2)*meanang
    second = 2*sqang
    expected_mean = math.sqrt(2/math.pi)*(1+math.sqrt(1+x*x))
    expected_sq = 1+x*x + 2/math.pi*((3-x*x)*angle+3*x)
    check(abs(mean-expected_mean)<1e-10,'polar first moment')
    check(abs(second-expected_sq)<1e-10,'polar second moment')

# Enumerate the trinomial law directly, without any Gaussian approximation.
def finite_variance(n, p):
    m1=m2=0.0
    logs=[math.lgamma(j+1) for j in range(n+1)]
    for j in range(n+1):
        for k in range(n-j+1):
            z=n-j-k
            mass=math.exp(logs[n]-logs[j]-logs[k]-logs[z]
                          + sum(count*math.log(prob)
                                for count,prob in zip((j,k,z),p) if count))
            d=0.0
            cnt=(j,k,z)
            for i in range(3):
                nxt=(i+1)%3
                d+=abs((cnt[nxt]-cnt[i])-n*(p[nxt]-p[i]))
            m1+=mass*d; m2+=mass*d*d
    return (m2-m1*m1)/n

for prob in [(1/3,1/3,1/3),(0.4,0.2,0.4),(0.49,0.02,0.49)]:
    x=prob[0]
    for n,tolerance in [(90,.12),(240,.055)]:
        numeric=finite_variance(n,prob)
        gaussian=float(V.subs(a,s.Rational(str(x))))
        check(abs(numeric-gaussian)<tolerance,
              'trinomial-to-Gaussian variance cross-check')

print(f'passed {assertions} assertions')
print('V(uniform) =', float(V.subs(a,u)))
print('V(edge) =', float(edge))
print('second derivative along (1,-2,1) =', float(curv))
