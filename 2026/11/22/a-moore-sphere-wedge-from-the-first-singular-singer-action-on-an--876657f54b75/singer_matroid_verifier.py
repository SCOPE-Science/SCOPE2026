"""Exact cellular boundary checks for Singer cyclic quotients of rank-three projective matroid complexes.

Supports explicit Singer difference sets of the small Desarguesian planes of orders 2, 3, and 4.
Each nonempty face orbit is a CW cell; the unique 3-fold triangle stabilizer (when present)
requires division of the oriented triangle boundary by 3. For q=4 this matters.
"""
from itertools import combinations
from math import comb
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

DIFF = {2: (1,2,4), 3:(0,1,3,9), 4:(0,1,4,14,16)}

def data(q):
 N=q*q+q+1
 D=tuple(DIFF[q]); assert len(D)==q+1
 lines=[set((x+d)%N for d in D) for x in range(N)]
 assert len({frozenset(l) for l in lines})==N
 pairs={frozenset((a,b)):0 for a,b in combinations(range(N),2)}
 for line in lines:
  for a,b in combinations(sorted(line),2): pairs[frozenset((a,b))]+=1
 assert all(v==1 for v in pairs.values())
 triangles=[t for t in combinations(range(N),3) if not any(set(t)<=l for l in lines)]
 assert len(triangles)==comb(N,3)-N*comb(q+1,3)
 canon=lambda t:min(tuple(sorted((x+k)%N for x in t)) for k in range(N))
 orbits=sorted({canon(t) for t in triangles})
 exceptional=[]
 def edge(x,y):
  d=(y-x)%N
  assert d
  if d <= N//2: return d-1,1
  return N-d-1,-1
 cols=[]
 for t in orbits:
  orbit_len=len({tuple(sorted((x+k)%N for x in t)) for k in range(N)})
  stabilizer=N//orbit_len
  assert stabilizer in (1,3)
  if stabilizer==3: exceptional.append(t)
  v=[0]*(N//2)
  for (a,b),sg in [((t[1],t[2]),1),((t[0],t[2]),-1),((t[0],t[1]),1)]:
   i,s=edge(a,b);v[i]+=sg*s
  assert all(x%stabilizer==0 for x in v)
  cols.append([x//stabilizer for x in v])
 M=Matrix(N//2,len(cols),lambda i,j:cols[j][i])
 S=smith_normal_form(M,domain=ZZ)
 diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
 rank=len(diag)
 H1=[x for x in diag if x>1]
 H2=len(orbits)-rank
 chi=1-(N-1)//2+len(orbits)
 assert H2==chi-1  # H_1 must be finite
 predicted=N//3 if q%3==1 else N
 assert H1==([predicted] if predicted>1 else []), (q,H1,predicted)
 predicted_b2=len(orbits)-(N-1)//2
 assert H2==predicted_b2
 assert len(exceptional)==(1 if q%3==1 else 0)
 print(f'q={q}, N={N}, triangles={len(triangles)}, quotient cells=[1,{N//2},{len(orbits)}], exceptional={exceptional}, SNF torsion={H1}, H2=Z^{H2}')

if __name__=='__main__':
 for q in DIFF:data(q)
 print('SINGER_PROJECTIVE_MATROID_QUOTIENT_CHECKS_OK')
