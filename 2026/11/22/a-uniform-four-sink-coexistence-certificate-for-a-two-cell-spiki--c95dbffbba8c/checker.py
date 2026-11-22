# Exact-rational, conservative face-sign certificate for a two-cell sigmoid map.
# All operations are rational; analytic exponential comparisons are proved
# separately by positive Taylor truncations below.
from fractions import Fraction as Q
from itertools import product
F=lambda x:Q(str(x))
# Exact rational interval operations
class I:
 def __init__(self,a,b=None): self.a=Q(a);self.b=Q(a if b is None else b)
 def __add__(self,o): o=asI(o);return I(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,o):return self+-asI(o)
 def __rsub__(self,o):return asI(o)+-self
 def __mul__(self,o):
  o=asI(o); v=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b];return I(min(v),max(v))
 __rmul__=__mul__
 def __repr__(self): return f'[{float(self.a):.6f},{float(self.b):.6f}]'
def asI(v):return v if isinstance(v,I) else I(v)
def atanh_ub(t):
 t=max(abs(t.a),abs(t.b))
 for bound,value in [('0.14','0.15'),('0.29','0.30'),('0.35','0.375'),('0.55','0.625'),('0.7','0.9'),('0.94','1.75')]:
  if t<=F(bound):return F(value)
 raise ValueError(f'no atanh ub for {t}')
def coord(k,interval):
 if k=='u' or k=='v':
  t=interval
  A=atanh_ub(t)/6
  if t.a>=0: return (I(0,A),t)
  if t.b<=0: return (I(-A,0),t)
  return (I(-A,A),t)
 # physical x or y
 t=interval
 if t.a>=F('.34') or t.b<=-F('.34'):
  mn=min(abs(t.a),abs(t.b)) if t.a*t.b>0 else Q(0)
  L=F('.999') if mn>=F('.9') else F(29)/30
  sign=1 if t.a>0 else -1
  return (t,I(L,1) if sign==1 else I(-1,-L))
 raise ValueError(f'low physical magnitude: {k} {t}')
# name, xtype, xmin,max,ytype, ymin,max
boxes=[
 ('C++','x','.34','.45','y','2.90','3.10'),
 ('C+-','x','2.3','2.5','y','-.45','-.34'),
 ('C-+','x','-3.2','-2.8','y','.9','1.1'),
 ('C--','x','-1.2','-.8','y','-2.6','-2.2'),
 ('X+','u','.70','.94','y','2.65','2.98'),
 ('X-','u','-.55','-.35','y','-2.00','-1.65'),
 ('Y+','x','2.05','2.37','v','-.94','-.70'),
 ('Y-','x','-2.60','-2.34','v','.35','.55'),
 ('center','u','0','.14','v','-.29','-.13'),
]
def bounds(kx,xi,ky,yi):
 x,u=coord(kx,xi);y,v=coord(ky,yi)
 H1=F(17)/10*u-v-F(3)/10-x
 H2=u+F(17)/10*v+F(3)/10-y
 return H1,H2
for nm,kx,a,b,ky,c,d in boxes:
 xa=I(F(a));xb=I(F(b));yf=I(F(c),F(d));xf=I(F(a),F(b));ya=I(F(c));yb=I(F(d))
 hL=bounds(kx,xa,ky,yf)[0];hR=bounds(kx,xb,ky,yf)[0]
 hB=bounds(kx,xf,ky,ya)[1];hT=bounds(kx,xf,ky,yb)[1]
 signs=(hL.a>0,hR.b<0,hB.a>0,hT.b<0)
 assert ((hL.a>0 and hR.b<0) or (hL.b<0 and hR.a>0)), (nm,'x signs',hL,hR)
 assert ((hB.a>0 and hT.b<0) or (hB.b<0 and hT.a>0)), (nm,'y signs',hB,hT)
 print(nm,'strict-face-signs: PASS',hL,hR,hB,hT)

# For positive rational z, the finite Taylor sum is a rigorous lower bound for exp(z).
def exp_lower(z,n=32):
 s=Q(1);p=Q(1)
 for k in range(1,n+1):
  p*=z/k;s+=p
 return s
assert exp_lower(Q(102,25))>59 # exp(4.08)>59 gives tanh(2.04)>29/30.
assert exp_lower(Q(54,5))>1999 # exp(10.8)>1999 gives tanh(5.4)>999/1000.
assert exp_lower(Q(99,5))>1999 # exp(19.8)>1999.
for t,A in [(Q(14,100),Q(3,20)),(Q(29,100),Q(3,10)),
            (Q(35,100),Q(3,8)),(Q(55,100),Q(5,8)),
            (Q(7,10),Q(9,10)),(Q(94,100),Q(7,4))]:
 assert exp_lower(2*A)>(1+t)/(1-t), (t,A)
# Explicit rational uniform Jacobian estimates at every witness.
dsmall=Q(24,59); dtiny=Q(24,1999)
assert Q(17,10)*dsmall+dtiny<1
assert dsmall+Q(17,10)*dtiny<1
active_min=6*(1-Q(94,100)**2)
assert 1-(Q(17,10)-Q(389,100)*dtiny)*active_min<0
assert Q(389,100)*Q(144,1999)<1
center_min=6*(1-Q(29,100)**2)
assert Q(27,10)/(Q(389,100)*center_min)<1
# Physical boxes are disjoint: the scaled coordinates have |x| or |y|
# less than 7/24 on their small axes, and all saturated corners have
# the indicated separated ranges. This is separately inspected in the proof.
print('Uniform rational derivative, exponential, and inverse bounds: PASS')
