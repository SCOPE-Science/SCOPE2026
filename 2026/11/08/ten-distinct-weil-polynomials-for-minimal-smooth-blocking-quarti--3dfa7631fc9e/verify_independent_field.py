"""Independent finite-field point-count audit for the ten explicit ternary quartics.
Uses unrelated irreducible polynomials and a full element-pair multiplication table.
Run: python verify_independent_field.py (from same directory as representatives.json).
"""
import json
from pathlib import Path
from itertools import product
rows=json.loads((Path(__file__).parent/'representatives.json').read_text())['entries']
monomials=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
class GF:
 def __init__(self,coeff):
  self.coeff=coeff;self.n=len(coeff);self.size=3**self.n
  self.v=[tuple((i//(3**j))%3 for j in range(self.n)) for i in range(self.size)]
  self.product=[[self._multiply(a,b) for b in range(self.size)] for a in range(self.size)]
  self.powers=[[1]+[0]*4 for _ in range(self.size)]
  for u in range(self.size):
   for j in range(1,5):self.powers[u][j]=self.product[self.powers[u][j-1]][u]
  assert all(self._power(u,self.size)==u for u in range(self.size))
 def _multiply(self,a,b):
  n=self.n;v=[0]*(2*n-1)
  for i,x in enumerate(self.v[a]):
   for j,y in enumerate(self.v[b]):v[i+j]+=x*y
  for i in range(2*n-2,n-1,-1):
   lead=v[i]%3
   for j in range(n):v[i-n+j]-=lead*self.coeff[j]
  return sum((v[i]%3)*3**i for i in range(n))
 def _power(self,a,p):
  r=1
  while p:
   if p&1:r=self.product[r][a]
   a=self.product[a][a];p//=2
  return r
 def eval(self,coeff,coords):
  acc=0
  for c,(i,j,k) in zip(coeff,monomials):
   if c:
    t=self.product[self.powers[coords[0]][i]][self.powers[coords[1]][j]]
    t=self.product[t][self.powers[coords[2]][k]]
    if c==2:t=self.product[2][t]
    acc=sum(((a+b)%3)*3**j for j,(a,b) in enumerate(zip(self.v[acc],self.v[t])))
  return acc
 def count(self,coeff):
  total=0
  for a in range(self.size):
   for b in range(self.size):total+=self.eval(coeff,(1,a,b))==0
  for a in range(self.size):total+=self.eval(coeff,(0,1,a))==0
  total+=self.eval(coeff,(0,0,1))==0
  return total
fields=(GF((0,)),GF((2,1)),GF((2,2,0)))
assert [G.size for G in fields]==[3,9,27]
assert len(rows)==10
for row in rows:
 coeff=row['coefficients'];counts=tuple(G.count(coeff) for G in fields)
 assert list(counts)==row['point_counts_n1_to_3'], (coeff,counts,row['point_counts_n1_to_3'])
 s=[3**j+1-counts[j-1] for j in (1,2,3)]
 c1=-s[0];c2=(s[0]*s[0]-s[1])//2;c3=(-s[0]**3+3*s[0]*s[1]-2*s[2])//6
 assert row['weil_numerator_coefficients']==[1,c1,c2,c3,3*c2,9*c1,27]
assert len({tuple(row['weil_numerator_coefficients']) for row in rows})==10
assert sorted(row['orbit_size'] for row in rows)==[6]+[24]*9
print('BLOCKING_QUARTIC_INDEPENDENT_FIELD_PASS',flush=True)
