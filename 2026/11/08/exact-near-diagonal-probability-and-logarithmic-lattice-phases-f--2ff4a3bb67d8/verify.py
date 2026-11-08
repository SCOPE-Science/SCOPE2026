"""Standalone checks for the exact stationary pair-distance law.

Only the Python standard library is required. These finite tests supplement,
but do not replace, the elementary proof in RESULT.md.
"""
from fractions import Fraction as F
from math import log, isclose

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def h(u):
    return 1 if u >= 1 else 2*u-u*u

def mass(m, r, eps):
    assert isinstance(eps, F) and 0 < eps < 1
    n = 0
    while eps*m**(n+1) <= 1:
        n += 1
    return (1-r)*(2*eps*sum((m*r)**j for j in range(n+1))
                  - eps*eps*sum((m*m*r)**j for j in range(n+1))) + r**(n+1)

def independent_mass(m, r, eps):
    n = 0
    while eps*m**(n+1) <= 1:
        n += 1
    return (1-r)*sum(r**j*h(eps*m**j) for j in range(n+1)) + r**(n+1)

for m in (2,3,4,5):
    for r in (F(1,5), F(1,m), F(3,5), F(4,5)):
        if r >= 1: continue
        p=1/(1+r)
        check(p>F(1,2),'positive Lyapunov condition')
        for n in range(1,15):
            b=lambda j:(1-r)*r**j
            check(b(0)==p*(b(0)+b(1)),'reflected walk boundary')
            check(b(n)==p*b(n+1)+(1-p)*b(n-1),'balance equation')
            for t in (F(1,2),F(2,3),F(7,8), F(1,1)):
                eps=t/F(m**n)
                if eps >= 1:continue
                check(mass(m,r,eps)==independent_mass(m,r,eps),'closed form vs independent mixture')

# At a noncritical value the log-periodic amplitude is nonconstant.
m=3; r=F(1,2); alpha=-log(float(r))/log(m)
def phi(t):
    return float(t)**(-alpha)*(float(r)+(1-float(r))*(2*m*float(r)*float(t)/(m*float(r)-1)-m*m*float(r)*float(t)**2/(m*m*float(r)-1)))
check(abs(phi(1)-phi(F(17,20)))>1e-5,'genuine log-periodic phase variation')
check(isclose(phi(1),phi(F(1,m)),rel_tol=2e-14),'matching phase endpoints')
for t in (F(1),F(17,20),F(1,2)):
    for n in (10,20,30,40):
        eps=t/F(m**n)
        rnum=float(mass(m,r,eps)) / float(eps)**alpha
        err=abs(rnum-phi(t))
        check(err < 7*float(eps)**(1-alpha),'exact remainder estimate')

# Critical coefficient and bounded-density coefficient follow quantitatively.
for m in (2,3,5):
    r=F(1,m)
    for n in (20,30,45):
        e=F(1,m**n)
        v=float(mass(m,r,e))/(float(e)*n)
        check(abs(v-2*(1-1/m))<4/n,'critical logarithmic coefficient')
    r=F(1,2*m)
    for n in (20,30,45):
        e=F(1,m**n)
        v=float(mass(m,r,e)/e)
        check(abs(v-2*(1-float(r))/(1-m*float(r))) < .1,'bounded-density coefficient')
print(f'PASS: {checks} finite exact/float checks')
