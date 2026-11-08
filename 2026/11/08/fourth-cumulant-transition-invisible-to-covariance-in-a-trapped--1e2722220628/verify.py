"""Deterministic finite-state moment check for a Markov-speed RTP in a harmonic trap."""
from fractions import Fraction as F
from itertools import product
import sympy as s


def exact_moments(mu,gamma,a,b,rho,D=F(0),order=4):
    vals=[(-1,-1),(-1,1),(1,-1),(1,1)] # speed label z, direction u
    speed={-1:F(a),1:F(b)}
    # transition forward rows T_ij from (z,u) -> (znew,unew)
    T=s.Matrix([[s.Rational(1+z*zn*s.Rational(rho),4) for zn,un in vals] for z,u in vals]); assert all(sum(T[i,j] for j in range(4))==1 for i in range(4))
    velocities=s.diag(*[speed[z]*u for z,u in vals]); L=s.eye(4)*s.Rational(gamma)-s.Rational(gamma)*T.T
    m={0:s.Matrix([s.Rational(1,4)]*4)}
    for k in range(1,order+1):
        forcing=k*velocities*m[k-1]
        if k>=2: forcing+=k*(k-1)*s.Rational(D)*m[k-2]
        m[k]=(L+k*s.Rational(mu)*s.eye(4)).inv()*forcing
    return [s.factor(sum(m[k])) for k in range(order+1)]


def theorem(mu,gamma,a,b,rho):
    mu,gamma,a,b,rho=map(s.Rational,[mu,gamma,a,b,rho]); alpha=gamma/mu
    s0=(a*a+b*b)/2;s1=(a*a-b*b)/2;c=(s1/s0)**2
    k4=6*s0**2/(mu**4*(alpha+1)**2*(alpha+3))*(c*(alpha+1)/(2+alpha*(1-rho))-1)
    var=s0/(mu*(mu+gamma))
    return s.factor(var),s.factor(k4)

checks=0
for mu,gamma,a,b,rho,D in product([1,2],[1,3,4],[1,2],[3,5],[-1,F(-1,2),0,F(1,2),F(7,10),F(9,10),1],[0,F(1,3)]):
    v=s.Rational; m=exact_moments(mu,gamma,a,b,rho,D)
    variance,k4=theorem(mu,gamma,a,b,rho)
    assert s.factor(m[2]-(variance+v(D)/v(mu)))==0
    assert s.factor(m[4]-3*m[2]**2-k4)==0
    assert m[1]==0 and m[3]==0
    checks+=4
# Exact threshold witness for a=1,b=3,gamma/mu=4
_,z=theorem(1,4,1,3,s.Rational(7,10));assert z==0
assert theorem(1,4,1,3,0)[1]<0
assert theorem(1,4,1,3,s.Rational(9,10))[1]>0
# Marginal covariance independent of rho and stationary variance with Gaussian source verified above.
print('PASS',checks+3,'exact checks; threshold rho=7/10')
