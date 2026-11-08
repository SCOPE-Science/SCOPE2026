"""Independent normalized-triple certificate for Paley tournament extension minima.

All fields are represented independently.  For order 27, X is primitive in
F_3[X]/(X^3+2X+1), with multiplication by X given by a 3-coordinate shift.
Affine transformations, including nonsquare scalings that reverse all arrows,
preserve the minimum over the eight patterns, so (0,1,t) are exhaustive.
"""
EXPECTED={3:0,7:0,11:0,19:1,23:1,27:2,31:2,43:3,47:4,59:5}

def rows(q):
 if q!=27:
  residue={pow(i,2,q) for i in range(1,q)}
  def diff(x,y): return (x-y)%q
 else:
  def step(a):
   u,v,w=(a%3,a//3%3,a//9%3)
   return (2*w)%3+3*((u+w)%3)+9*v
  residue=set()
  z=1; powers=[]
  for k in range(26):
   assert z not in powers
   powers.append(z)
   if k%2==0: residue.add(z)
   z=step(z)
  assert z==1 and set(powers)==set(range(1,27))
  def diff(x,y):
   return sum((((x//(3**i))%3-(y//(3**i))%3)%3)*(3**i) for i in range(3))
 assert len(residue)==(q-1)//2
 minimum=q
 best=None
 for t in range(2,q):
  counts=[0]*8
  for x in range(q):
   if x in (0,1,t):continue
   mask=int(diff(x,0) in residue)+2*int(diff(x,1) in residue)+4*int(diff(x,t) in residue)
   counts[mask]+=1
  assert sum(counts)==q-3
  v=min(counts)
  if v<minimum:minimum=v;best=(t,counts)
 return minimum,best

if __name__=='__main__':
 for q,v in EXPECTED.items():
  found,best=rows(q)
  assert found==v,(q,found,v)
  print('q=%d normalized_minimum=%d witness_t=%d PASS'%(q,found,best[0]))
 print('ALL_AFFINE_CHECKS_PASS')
