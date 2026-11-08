"""Exact verification of two-state Gauss collocation stage positivity classification."""
import sympy as s
from fractions import Fraction
from random import Random

z,a,b=s.symbols('z a b', positive=True)
rt3=s.sqrt(3); c=rt3/6
A=s.Matrix([[s.Rational(1,4),s.Rational(1,4)-c],
            [s.Rational(1,4)+c,s.Rational(1,4)]])
D=1+z/2+z*z/12
G=(s.eye(2)+z*A).inv()*s.ones(2,1)
g1=(1+c*z)/D
g2=(1-c*z)/D
assert all(s.simplify(G[j]-u)==0 for j,u in enumerate([g1,g2]))
lam=a+b
Q=s.Matrix([[-a,a],[b,-b]])
Pi=s.Matrix([[b/lam,a/lam],[b/lam,a/lam]])
assert s.simplify(Q+lam*(s.eye(2)-Pi))==s.zeros(2)
R=(1-z/2+z*z/12)/D
S1=Pi+g1*(s.eye(2)-Pi)
S2=Pi+g2*(s.eye(2)-Pi)
E=Pi+R*(s.eye(2)-Pi)
assert all(s.simplify(v)==0 for v in S1*s.ones(2,1)-s.ones(2,1))
assert all(s.simplify(v)==0 for v in S2*s.ones(2,1)-s.ones(2,1))
assert all(s.simplify(v)==0 for v in E*s.ones(2,1)-s.ones(2,1))
# Exact stage equations: row-vector stage matrices S_i = I + h sum_j a_ij S_j Q.
for i,Si in enumerate([S1,S2]):
 rhs=s.eye(2)+sum(((z/lam)*A[i,j]*Sj*Q for j,Sj in enumerate([S1,S2])),s.zeros(2))
 assert all(s.simplify(v)==0 for v in Si-rhs)
# Endpoint identity from quadrature weights 1/2,1/2.
Et=s.eye(2)+(z/(2*lam))*(S1+S2)*Q
assert all(s.simplify(v)==0 for v in E-Et)
# The rate-ratio threshold and the quadratic factor.
r=s.symbols('r',positive=True)
p=s.expand(12*(D+r*(1-c*z)))
assert s.simplify(p-(z*z+(6-2*rt3*r)*z+12*(1+r)))==0
B=4+2*rt3
Delta=s.expand((6-2*rt3*r)**2-48*(1+r))
assert s.simplify(Delta-12*(r*r-B*r-1))==0
rcrit=(B+s.sqrt(B*B+4))/2
assert s.simplify(rcrit*rcrit-B*rcrit-1)==0
zstar=s.sqrt(3)*rcrit-3
assert s.simplify(p.subs({z:zstar,r:rcrit}))==0
assert s.simplify(s.diff(p,z).subs({z:zstar,r:rcrit}))==0
# Exact concrete counterexample a=9,b=1,z=10
assert s.simplify(S2[0,0].subs({a:9,b:1,z:10})-(14-9*rt3)/86)==0
assert (14-9*rt3).evalf()<0
assert s.simplify(E[0,0].subs({a:9,b:1,z:10})-s.Rational(16,43))==0
assert s.simplify(E[0,1].subs({a:9,b:1,z:10})-s.Rational(27,43))==0
assert s.simplify(S2[0,0].subs({a:9,b:1,z:10})*s.Rational(99,100)+S2[1,0].subs({a:9,b:1,z:10})/100).evalf()<0
# Independent numerical 4x4 coupled stage solve and classification over sampled examples.
rng=Random(37919);n=0
for i in range(50):
 aa=s.Rational(rng.randint(1,60),rng.randint(1,20))
 bb=s.Rational(rng.randint(1,60),rng.randint(1,20))
 hh=s.Rational(rng.randint(1,160),rng.randint(1,30))
 ll=aa+bb;zz=hh*ll
 QQ=s.Matrix([[-aa,aa],[bb,-bb]])
 # Stage matrices act on row vectors, represented row-major via independent e1, e2.
 lhs=s.BlockMatrix([[(s.eye(2) if i==j else s.zeros(2))-hh*A[i,j]*QQ.T for j in range(2)] for i in range(2)]).as_explicit()
 direct=lhs.inv()*s.Matrix([1,0,1,0])
 d1=s.Matrix([S1.subs({a:aa,b:bb,z:zz})[0,0],S1.subs({a:aa,b:bb,z:zz})[0,1]])
 d2=s.Matrix([S2.subs({a:aa,b:bb,z:zz})[0,0],S2.subs({a:aa,b:bb,z:zz})[0,1]])
 assert all(s.simplify(v)==0 for v in direct-s.Matrix(list(d1)+list(d2)))
 vals=[s.N(v) for v in S2.subs({a:aa,b:bb,z:zz})]
 stagepos=min(vals)>=-s.Float('1e-32')
 rr=max(float(aa/bb),float(bb/aa))
 polynomial=float(p.subs({r:rr,z:float(zz)}))
 assert stagepos==(polynomial>=-1e-8)
 n+=1
print('PASS: all symbolic identities, exact witness, and',n,'independent stage block solves/classifications')
print('critical rate ratio',rcrit.evalf(16),'critical scaled step',zstar.evalf(16))
