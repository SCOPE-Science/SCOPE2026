"""Exact checks for the cubic RK Markov-star positivity phase theorem.

Requires Python 3 and SymPy. Finite tests supplement the analytic proof.
"""
from fractions import Fraction
import sympy as s

M,a,b,h,r=s.symbols('M a b h r', positive=True)
P=lambda z:1-z+z*z/s.Integer(2)-z**3/s.Integer(6)
lam=a+M*b
hub=(a+M*b*P(lam*h))/lam
edge_out=b*(1-P(lam*h))/lam
edge_in=a*(1-P(lam*h))/lam
pair=b/lam+a*P(lam*h)/(M*lam)-P(a*h)/M
leaf=b/lam+a*P(lam*h)/(M*lam)+(1-1/M)*P(a*h)
assert s.simplify(pair-a*b*h*h*(s.Rational(1,2)-(2*a+M*b)*h/6))==0
assert s.simplify(edge_out-b*h*(1-lam*h/2+lam**2*h**2/6))==0
assert s.simplify(edge_in-a*h*(1-lam*h/2+lam**2*h**2/6))==0
hpair=s.Rational(3,1)/(2*a+M*b)
F=16*r**3+9*r**2-3*r-4
G=2+6*r+9*r**2+r**3
assert s.simplify((hub.subs(h,hpair)-F/(2*(1+2*r)**3)).subs(a,r*M*b))==0
assert s.simplify((leaf.subs(h,hpair)-G/(2*(1+2*r)**3)).subs(a,r*M*b))==0
assert s.simplify(s.diff(F,r)-3*(2*r+1)*(8*r-1))==0
assert s.simplify(s.diff(P(s.Symbol('x')),s.Symbol('x')) +(s.Symbol('x')**2-2*s.Symbol('x')+2)/2)==0

cases=0
for m in (2,3,4,5,8,13):
    for aa,bb in ((1,1),(2,1),(1,3),(5,2),(3,7),(17,1),(1,17)):
        Q=s.zeros(m+1)
        for j in range(1,m+1):
            Q[0,j]=bb
            Q[j,0]=aa
            Q[j,j]=-aa
        Q[0,0]=-m*bb
        Q2=Q*Q; Q3=Q2*Q
        for hh in (s.Rational(1,19),s.Rational(1,3),s.Rational(5,7)):
            A=s.eye(m+1)+hh*Q+hh**2*Q2/2+hh**3*Q3/6
            subs={M:m,a:aa,b:bb,h:hh}
            assert A[0,0]==s.cancel(hub.subs(subs))
            assert A[0,1]==s.cancel(edge_out.subs(subs))
            assert A[1,0]==s.cancel(edge_in.subs(subs))
            assert A[1,2]==s.cancel(pair.subs(subs))
            assert A[1,1]==s.cancel(leaf.subs(subs))
            assert all(sum(A[i,j] for j in range(m+1))==1 for i in range(m+1))
            cases += (m+1)**2
print('PASS symbolic all-parameter identities; exact matrix-entry checks:',cases)

# Both mechanisms occur and the exact crossover is unique by the displayed derivative.
root=s.nroots(F,maxsteps=100)[0]
root=next(s.re(z) for z in s.nroots(F,maxsteps=100) if abs(s.im(z))<s.Rational(1,10**8) and s.re(z)>0)
assert s.Rational(1,2)<root<s.Rational(3,5)
for rr,expect in ((s.Rational(1,4),'hub'),(s.Rational(1,2),'hub'),(s.Rational(3,5),'pair'),(1,'pair')):
    sign=s.sign(F.subs(r,rr))
    assert (sign<0 and expect=='hub') or (sign>0 and expect=='pair')
    assert G.subs(r,rr)>0
print('PASS exact phase witnesses; unique crossover:',s.N(root,18))
print('LIMIT: symbolic identities and a derivative/positivity argument establish the theorem; sampled matrices are non-exhaustive checks')
