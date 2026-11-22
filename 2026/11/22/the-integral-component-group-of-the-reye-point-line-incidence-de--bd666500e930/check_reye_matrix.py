import itertools
from collections import Counter
from sympy import Matrix,eye,zeros,ZZ,prod,factorint
from sympy.matrices.normalforms import smith_normal_form
V=list(itertools.product((0,1),repeat=3)); pidx={p:i for i,p in enumerate(V)}
# cube vertices 0-7, 8 center, 9-11 infinity along each coordinate
lines=[]
for i in range(3):
 for other in itertools.product((0,1),repeat=2):
  p=list(other);p.insert(i,0);a=tuple(p);p[i]=1;b=tuple(p)
  lines.append((pidx[a],pidx[b],9+i))
for p in V:
 q=tuple(1-x for x in p)
 if p<q:lines.append((pidx[p],pidx[q],8))
assert len(lines)==16 and len(set(lines))==16
assert Counter(u for line in lines for u in line)==Counter({x:4 for x in range(12)})
M=zeros(12,16)
for j,line in enumerate(lines):
 for i in line:M[i,j]=1
L=zeros(28)
for i in range(12):L[i,i]=4
for j in range(16):L[12+j,12+j]=3
for i in range(12):
 for j in range(16):
  if M[i,j]:L[i,12+j]=L[12+j,i]=-1
R=L[:27,:27]
D=smith_normal_form(R,domain=ZZ)
v=[abs(D[i,i]) for i in range(27)]
assert all(u for u in v)
assert all(v[i+1]%v[i]==0 for i in range(26))
print('Reye',len(lines),Counter(v),factorint(prod(v)), 'rank',R.rank(),'charpoly',L.charpoly().as_expr().factor())
