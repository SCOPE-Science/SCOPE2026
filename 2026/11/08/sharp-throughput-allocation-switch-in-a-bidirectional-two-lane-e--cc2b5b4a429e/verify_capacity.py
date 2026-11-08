"""Independent exact-rational checks of the two-lane capacity theorem.

Run with Python 3 and SymPy; no external data or file dependencies.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import isclose
import sympy as S

checks = 0

def check(condition, context):
    global checks
    assert condition, context
    checks += 1

z, x, y, d, u, v = S.symbols('z x y d u v', real=True)
F = u*(1-u)*(1+z*v) + v*(1-v)*(1+z*u)
G = S.expand(F.subs({u:x+d, v:x-d}))
check(S.expand(G-2*x*(1-x)*(1+z*x)-2*(z*(x-1)-1)*d*d)==0,'symmetric-coordinate identity')
check(S.factor(S.resultant(S.diff(2*x*(1-x)*(1+z*x),x), 2*x*(1-x)*(1+z*x)-S.Rational(1,4),x)) == z*(32*z**3+85*z**2+80*z+32)/2, 'critical resultant')
check(S.expand(S.diff(G,d,2)-4*(z*(x-1)-1))==0, 'transverse Hessian')
check(S.expand(S.diff(G,x,d)-4*z*d)==0,'mixed Hessian')

# Check the stationarity of the uniform distribution on every particle sector,
# by comparing exact total outgoing and incoming rates for all states.
# Each rate is (R +/- (1+q*other-pair-occupancy/2))/2.
def ring_states(L,n):
    for ones in combinations(range(L),n):
        b=[0]*L
        for i in ones:b[i]=1
        yield tuple(b)

def rate_difference(q,other,i):
    return Q(1)+q*Q(other[i]+other[(i+1)%len(other)],2)

def rates_for_bond(q,own,other,i):
    val=rate_difference(q,other,i)
    R=Q(10)+abs(q)
    return (R+val)/2,(R-val)/2

for L in [3,4,5]:
    for n in range(L+1):
        for m in range(L+1):
            for own in ring_states(L,n):
                for other in ring_states(L,m):
                    for q in [Q(-5,2),Q(-3,2),Q(-1),Q(-1,2),Q(0),Q(1,3),Q(4)]:
                        net=Q(0)
                        for i in range(L):
                            k=(i+1)%L
                            if own[i]!=own[k]:
                                rp,rm=rates_for_bond(q,own,other,i)
                                net+=(rp-rm)*(own[i]-own[k])
                            if other[i]!=other[k]:
                                rp,rm=rates_for_bond(q,other,own,i)
                                net+=(rp-rm)*(other[i]-other[k])
                        check(net==0,('global balance',L,n,m,own,other,q))

# Independently average the exact microscopic net flux in each canonical
# sector and compare the closed finite-L formula.
for L in [3,4,5]:
    for n in range(L+1):
        for m in range(L+1):
            states=list(product(ring_states(L,n),ring_states(L,m)))
            for q in [Q(-5,2),Q(-3,2),Q(0),Q(5,3)]:
                flux1=Q(0); flux2=Q(0)
                for own,other in states:
                    i,k=0,1
                    r1,l1=rates_for_bond(q,own,other,i)
                    r2,l2=rates_for_bond(q,other,own,i)
                    flux1+= own[i]*(1-own[k])*r1 - own[k]*(1-own[i])*l1
                    flux2+= other[i]*(1-other[k])*r2 - other[k]*(1-other[i])*l2
                flux1/=len(states);flux2/=len(states)
                expected1=Q(n*(L-n),L*(L-1))*(1+q*Q(m,L))
                expected2=Q(m*(L-m),L*(L-1))*(1+q*Q(n,L))
                check(flux1==expected1,('canonical flux1',L,n,m,q))
                check(flux2==expected2,('canonical flux2',L,n,m,q))

# Analytic extremizer: its one-variable cubic value and symbolic stationary equation.
sq=S.sqrt(z*z+z+1)
xstar=(z-1+sq)/(3*z)
check(S.simplify(S.diff(2*x*(1-x)*(1+z*x),x).subs(x,xstar))==0,'critical point')
critical=float(S.nroots(32*z**3+85*z*z+80*z+32)[0])
check(-1.5<critical<-1.0,'critical location')
check(abs(critical+1.357003205304976)<1e-12,'critical value')
for qval in [-8,-3,-1.5,critical-0.001,critical,critical+0.001,-1,0,0.3,1,4,20]:
    if qval==0: xx=0.5
    else: xx=(qval-1+(qval*qval+qval+1)**0.5)/(3*qval)
    smax=2*xx*(1-xx)*(1+qval*xx)
    expected=max(0.25,smax) if qval<0 else smax
    for k in range(81):
        a=k/80
        for l in range(81):
            b=l/80
            val=a*(1-a)*(1+qval*b)+b*(1-b)*(1+qval*a)
            check(val<=expected+2e-11,('grid global',qval,a,b))
    check(isclose(smax,2*xx*(1-xx)*(1+qval*xx),rel_tol=1e-12),'symmetric value')
print(f'PASS {checks} exact/algebraic/finite-state and bounded-grid checks')
