"""Exact nonabelian Fourier-block checks for 4-tap functions on the dihedral group of order ten.
Uses SymPy symbolic arithmetic in algebraic number fields.
"""
import sympy as s
from collections import defaultdict
sq=s.sqrt(5); c1=(sq-1)/2; c2=(-sq-1)/2
h=s.sqrt((sq-1)/2); tau=(sq-1)/2

def simp(x):return s.simplify(s.expand(x))
def nz(x):return simp(x)!=0

def rank_of(rot,refl):
  # Rotations and reflections: dict of exponent 0,...,4 to coefficient.
  # Scalar blocks A0+B0, A0-B0; nontrivial 2D blocks j=1,2.
  a0=sum(rot.values());b0=sum(refl.values())
  zero_s=[int(not nz(a0+b0)),int(not nz(a0-b0))]
  block_d=[]
  # cos(j*d) for d mod 5
  cc={0:s.Integer(2),1:c1,4:c1,2:c2,3:c2}
  for j in [1,2]:
    def prod(d):
      es=sorted(d)
      return simp(sum(v*v for v in d.values())+sum(d[i]*d[k]*cc[(j*(i-k))%5] for ii,i in enumerate(es) for k in es[ii+1:]))
    determinant=simp(prod(rot)-prod(refl))
    block_d.append(int(not nz(determinant)))
  return 10-sum(zero_s)-2*sum(block_d),zero_s,block_d

def make(w,kind):
  if kind=='40':return dict(zip([0,1,2,3],w)),{}
  if kind=='31':return dict(zip([0,1,2],w[:3])),{0:w[3]}
  if kind=='22p':return dict(zip([0,1],w[:2])),dict(zip([0,1],w[2:]))
  if kind=='22s':return dict(zip([0,1],w[:2])),dict(zip([0,2],w[2:]))
  assert False

# For 4+0 rank 4: Fourier inverse 2 nonzero, one time zero.
# rank 6: inverse 3 nonzero and one time zero. rank 8: inverse 4 nonzero and one time zero.
z=s.exp(2*s.pi*s.I/5)
# exact root via algebraic symbolic roots of unity may be left as trig, normalized analytically
# time domain of inverse frequencies: f(t) = sum_{j in freqs} Cj z^{j*t}
# t=0 is zero, rotate to support {1,2,3,4}, allowed shift to {0,1,2,3} by group rotation.
def inverse_w(freq):
  # drop time0, shift t=1..4 to time0..3
  return [s.expand(sum(c*z**(j*(t+1)) for j,c in freq.items())) for t in range(4)]

witnesses=[
 ('40',4,inverse_w({0:-1,1:1})),
 ('40',6,inverse_w({0:-3,1:1,2:2})),
 ('40',8,inverse_w({0:-6,1:1,2:2,3:3})),
 ('40',10,[1,1,1,1]),
 ('31',6,[1,s.Rational(1,2),1,s.sqrt(5)/2]),
 ('31',7,[1,-(3+sq)/4,1,2-(3+sq)/4]),
 ('31',8,[1,1,2,s.sqrt(6+3*c1+2*c2)]),
 ('31',9,[1,1,1,3]),
 ('31',10,[1,1,1,2]),
 ('22p',4,[1,-1,1,-1]),
 ('22p',5,[1,1,1,1]),
 ('22p',8,[1,-1,2,-2]),
 ('22p',9,[1,1,3,-1]),
 ('22p',10,[1,1,1,2]),
 ('22s',6,[1,-1,tau,-tau]),
 ('22s',7,[1,1,1+h,1-h]),
 ('22s',8,[1,-1,1,-1]),
 ('22s',9,[1,1,1,1]),
 ('22s',10,[1,1,1,2]),
]
pure_certificates={4:[-1,1],6:[-3,1,2],8:[-6,1,2,3]}
x=s.Symbol('x')
phi=s.Poly(x**4+x**3+x**2+x+1,x,domain=s.QQ)
for kind,r,w in witnesses:
  rot,refl=make(w,kind)
  if kind=='40':
    if r!=10:
      d=pure_certificates[r]
      D=sum(v*x**j for j,v in enumerate(d))
      # The Fourier series is f(t) = D(zeta^t), t=1,...,4,
      # with f(0)=0. Show all four time entries are nonzero exactly
      # by reduction modulo the fifth cyclotomic polynomial.
      assert sum(d)==0
      assert all(not s.Poly(D.subs(x,x**t),x,domain=s.QQ).rem(phi).is_zero for t in range(1,5))
      # Fourier inversion gives five times the coefficient d[-j],
      # up to a nonzero phase factor, with no approximations.
      found=2*sum(int(v!=0) for v in d)
    else:
      # 1+x+x^2+x^3 has transform 4 at 0 and -x^4 at other fifth roots.
      assert w==[1,1,1,1]
      found=10
    print(kind,r,'exact rank',found)
  else:
    found,sc,bl=rank_of(rot,refl)
    print(kind,r,'found',found,'scalar zeros',sc,'block zeros',bl, 'coeff',str(w)[:110])
  assert found==r,(kind,r,found)
print('ALL WITNESSES PASS')
