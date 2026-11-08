"""Exact rational consistency checks for the negative-doubling eight-cycle escape law."""
from fractions import Fraction as Q
import sympy as s
h=Q(7,17); safe=[(Q(0),h),(1-h,Q(1))]
T=lambda x:1-2*x if x<Q(1,2) else 2-2*x
endpoints={Q(0),Q(1),h,1-h}
for start in (h,1-h):
 p=start
 for _ in range(8):endpoints.add(p);p=T(p)
 assert p==start
points=sorted(endpoints)
cell=[(a,b) for a,b in zip(points,points[1:]) if b<=h or a>=1-h]
assert len(cell)==8
B=s.zeros(8)
for i,(a,b) in enumerate(cell):
 lo,hi=sorted((T(a),T(b)))
 for j,(c,d) in enumerate(cell):
  if c>=lo and d<=hi:B[i,j]=1
lengths=s.Matrix([s.Rational(b.numerator,b.denominator)-s.Rational(a.numerator,a.denominator) for a,b in cell]);one=s.ones(8,1)
z=s.symbols('z');G=s.factor((one.T*(s.eye(8)-z*B).inv()*lengths)[0]);expected=2*(7-3*z-6*z*z+5*z**3)/(17*(1-z)**3*(1+z));assert s.cancel(G-expected)==0
n=s.symbols('n',integer=True,positive=True)
# Independent pullback calculation without relying on Markov matrix.
intervals=safe[:]
for step in range(1,16):
 size=sum((b-a for a,b in intervals),Q(0))
 predicted=Q(6*step*step+12*step+39+(-1)**step,34*2**step)
 assert size==predicted,(step,size,predicted)
 next_intervals=[]
 for a,b in intervals:
  for lo,hi in safe:
   for x,y in [((1-b)/2,(1-a)/2),((2-b)/2,(2-a)/2)]:
    u,v=max(lo,x),min(hi,y)
    if v>u:next_intervals.append((u,v))
 intervals=next_intervals
# Independent four-cycle comparison, including exact generating expression.
pts=[Q(0),Q(1,5),Q(2,5),Q(3,5),Q(4,5),Q(1)]
c4=[(a,b) for a,b in zip(pts,pts[1:]) if b<=Q(2,5) or a>=Q(3,5)]
M=s.zeros(4)
for i,(a,b) in enumerate(c4):
 lo,hi=sorted((T(a),T(b)))
 for j,(c,d) in enumerate(c4):
  if c>=lo and d<=hi:M[i,j]=1
l4=s.Matrix([s.Rational(b.numerator,b.denominator)-s.Rational(a.numerator,a.denominator) for a,b in c4])
assert s.cancel((s.ones(1,4)*(s.eye(4)-z*M).inv()*l4)[0]-2*(2-z)/(5*(1-z)**2))==0
print('VERIFY_OK exact_markov_cells=8 symbolic_generating_identity=1 independent_inverse_horizons=15 four_cycle_comparison=1')
