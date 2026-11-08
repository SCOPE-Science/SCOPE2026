"""Construct exact Jacobian-ideal certificates in every projective affine chart.

The polynomial is homogeneous of degree ten over GF(7). The Buchberger
calculation reduces an S-polynomial to 1, certifying the unit ideal in each
chart and therefore geometric smoothness over the algebraic closure.
Use: python3 verify_smoothness.py (Python standard library only).
"""
from collections import deque
p=7

def canon(f):return {e:c%p for e,c in f.items() if c%p}
def add(f,g,scale=1):
 h=f.copy()
 for e,c in g.items():h[e]=(h.get(e,0)+scale*c)%p
 return canon(h)
def scale_shift(f,e,c):return canon({(a+e[0],b+e[1]):c*v for (a,b),v in f.items()})
def lt(f):return max(f)
def div(a,b):return a[0]>=b[0] and a[1]>=b[1]
def norm(f):
 a=lt(f);inv=pow(f[a],-1,p);return {e:c*inv%p for e,c in f.items()}
def reduction(f,G):
 r={};f=f.copy(); counter=0
 while f:
  counter+=1
  if counter>100000:raise RuntimeError('too much')
  a=lt(f); c=f[a]
  for g in G:
   b=lt(g)
   if div(a,b):
    f=add(f,scale_shift(g,(a[0]-b[0],a[1]-b[1]),1),-c)
    break
  else:
   r[a]=c;del f[a]
 return r

def groebner(G):
 G=[norm(g) for g in G if g]
 pairs=deque((i,j) for i in range(len(G)) for j in range(i+1,len(G)))
 total=0
 while pairs:
  i,j=pairs.popleft();total+=1
  a=lt(G[i]);b=lt(G[j]); l=(max(a[0],b[0]),max(a[1],b[1]))
  if l==(a[0]+b[0],a[1]+b[1]):continue # product criterion
  S=add(scale_shift(G[i],(l[0]-a[0],l[1]-a[1]),1),scale_shift(G[j],(l[0]-b[0],l[1]-b[1]),1),-1)
  r=reduction(S,G)
  if r:
   r=norm(r)
   if len(r)==1 and (0,0) in r:return True,len(G),total
   for h in range(len(G)):pairs.append((h,len(G)))
   G.append(r)
 return False,len(G),total

def derivatives(k,patch=2):
 # F in x y z exps
 F={}
 def a(e,c):F[e]=(F.get(e,0)+c)%p
 q=7
 a((q+2,1,0),1);a((3,q,0),-1);a((0,q+2,1),1);a((0,3,q),-1)
 a((1,0,q+2),1);a((q,0,3),-1);a((3,0,q),k);a((q+2,0,1),-k)
 Fs=[]
 for t in range(3):
  D={}
  for e,c in F.items():
   if e[t]:
    f=list(e);f[t]-=1
    ee=tuple(f[j] for j in range(3) if j!=patch)
    D[ee]=(D.get(ee,0)+e[t]*c)%p
  Fs.append(canon(D))
 return Fs
if __name__ == '__main__':
    for k in (1, 3):
        for chart in (0, 1, 2):
            unit, basis_size, pairs = groebner(derivatives(k, chart))
            assert unit
            print('JACOBIAN_UNIT_IDEAL_PASS', k, 'chart', chart,
                  'basis_size', basis_size, 'processed_pairs', pairs)
    print('GEOMETRIC_SMOOTHNESS_PASS')
