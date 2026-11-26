import itertools
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from collections import Counter
P=list(itertools.product((-1,1),repeat=3))
inc=[]
# all cube edges: pair vertices differing in one coordinate, infinity per direction
for a in P:
 for i in range(3):
  b=list(a);b[i]*=-1;b=tuple(b)
  if a<b:inc.append(tuple(sorted((P.index(a),P.index(b),9+i))))
# four long diagonals, centroid 8
for a in P:
 b=tuple(-u for u in a)
 if a<b:inc.append(tuple(sorted((P.index(a),P.index(b),8))))
assert len(set(inc))==16
X=s.zeros(28)
for j,ln in enumerate(inc):
 for i in ln:
  X[i,i]+=1;X[12+j,12+j]+=1
  X[i,12+j]=X[12+j,i]=-1
assert all(sum(X.row(i))==0 for i in range(28))
assert X.charpoly().as_expr().factor()==s.Symbol('lambda')*(s.Symbol('lambda')-7)*(s.Symbol('lambda')-4)**2*(s.Symbol('lambda')-3)**6*(s.Symbol('lambda')**2-7*s.Symbol('lambda')+8)**9
for root in (0,8,11,12,27):
 I=[i for i in range(28) if i!=root]
 R=X.extract(I,I)
 d=smith_normal_form(R,domain=s.ZZ)
 c=Counter(abs(d[i,i]) for i in range(27)); assert c=={1:18,2:1,8:2,24:4,96:2},(root,c)
 assert R.det()==2**29*3**6
print('REYE_5_ROOTS_SPECTRUM_SMITH_OK')
