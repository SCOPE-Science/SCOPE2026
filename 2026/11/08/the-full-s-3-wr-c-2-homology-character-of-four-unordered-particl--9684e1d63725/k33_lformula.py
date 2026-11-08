# Separate rational equivariant Lefschetz trace by the local modules' determinant identity.
import json
from try_k33_4 import E,incident
from try_k33_char import G
REF=json.load(open('k33four_chars.json'))
class EPoly:
 @staticmethod
 def mul(a,b):return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(5)]

def matmul(a,b):return [[a[i][0]*b[0][j]+a[i][1]*b[1][j] for j in range(2)] for i in range(2)]
def mat(v,g):
 w=g[v]
 image=[E.index(tuple(sorted((g[a],g[b])))) for a,b in E]
 def d(i):
  new=incident[w].index(image[incident[v][i]])
  ret=[0,0]
  if new>0:ret[new-1]+=1
  return ret
 a=d(0);b=d(1);c=d(2)
 return [[b[i]-a[i],c[i]-a[i]] for i in range(2)]
def orbit_g(g,n):
 left=set(range(n))
 while left:
  i=min(left);q=[];j=i
  while j not in q:q.append(j);left.discard(j);j=g[j]
  assert j==i
  yield q

def orbit_permutation(f,n):
 left=set(range(n))
 while left:
  i=min(left);q=[];j=i
  while j not in q:q.append(j);left.discard(j);j=f[j]
  assert j==i
  yield q

def calc(g):
 poly=[1,0,0,0,0]
 for vv in orbit_g(g,6):
  M=[[1,0],[0,1]]
  for v in vv:M=matmul(mat(v,g),M)
  l=len(vv);a=[1,0,0,0,0]
  if l<=4:a[l]-=M[0][0]+M[1][1]
  poly=EPoly.mul(poly,a)
 eperm=[E.index(tuple(sorted((g[a],g[b])))) for a,b in E]
 for ee in orbit_permutation(eperm,9):
  l=len(ee);a=[int(k%l==0) for k in range(5)]
  poly=EPoly.mul(poly,a)
 return poly[4]

for g,r in zip(G,REF):
 got=calc(g);assert got==r['L'],(g,got,r['L'])
print('INDEPENDENT_DETERMINANT_LEFSCHETZ_ALL_72_PASS')
