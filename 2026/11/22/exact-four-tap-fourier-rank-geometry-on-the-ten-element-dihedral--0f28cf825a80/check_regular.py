"""Independent regular-matrix numerical consistency test for the 210 supports.
Does not use the representation/determinant identities.
"""
import itertools,math
import numpy as np
from check_dihedral import witnesses,make
G=[(i,e) for e in range(2) for i in range(5)]
idx={g:i for i,g in enumerate(G)}
def mult(a,b):return ((a[0]+(-1)**a[1]*b[0])%5, (a[1]+b[1])%2)
def aut(a,k,v):return ((k*a[0]+v*a[1])%5,a[1])
def transform(a,g,h,k,v):return mult(mult(g,aut(a,k,v)),h)
def group_matrix(coeff):
    # left multiplication matrix: columns input y, rows output x=xy
    M=np.zeros((10,10),dtype=complex)
    for z,c in coeff.items():
      for y in G:M[idx[mult(z,y)],idx[y]]+=complex(c)
    return M

def rank(M):
    sv=np.linalg.svd(M,compute_uv=False)
    return int(np.count_nonzero(sv>1e-8)),sv
S={kind:{} for kind in ['40','31','22p','22s']}
for kind,r,w in witnesses:
 rot,refl=make(w,kind)
 coeff={(i,0):complex(z.evalf(30) if hasattr(z,'evalf') else z) for i,z in rot.items()}
 coeff.update({(i,1):complex(z.evalf(30) if hasattr(z,'evalf') else z) for i,z in refl.items()})
 assert rank(group_matrix(coeff))[0]==r,(kind,r)
 S[kind][r]=coeff
U={}
for kind, rw in S.items():
 base=frozenset(next(iter(rw.values())))
 for g in G:
  for h in G:
   for k in range(1,5):
    for v in range(5):
     images={a:transform(a,g,h,k,v) for a in base}
     target=frozenset(images.values())
     if target not in U:U[target]=(kind,images)
expected={kind:dict.fromkeys(rw) for kind,rw in S.items()}
actual={kind:0 for kind in S}
num_tests=0
min_positive=float('inf')
max_numerical_zero=0.0
for support,(kind,images) in U.items():
 actual[kind]+=1
 for expected_rank,basecoeff in S[kind].items():
  num_tests+=1
  coeff={images[a]:z for a,z in basecoeff.items()}
  found,sv=rank(group_matrix(coeff))
  min_positive=min(min_positive,float(sv[sv>1e-8].min()))
  if found<10:max_numerical_zero=max(max_numerical_zero,float(sv[sv<=1e-8].max()))
  assert found==expected_rank,(support,kind,expected_rank,found,sv)
assert len(U)==210, (len(U),actual)
assert actual=={'40':10,'31':100,'22p':50,'22s':50},actual
assert num_tests==1040,num_tests
print(f'ALL 210 FOUR-ELEMENT SUPPORTS TRANSPORTED; {num_tests} FULL REGULAR MATRIX RANK TESTS PASS')
print('support geometry census',actual)
print('attainable ranks',{k:sorted(v) for k,v in S.items()})
print('smallest positive singular value observed',format(min_positive,'.15g'))
print('largest numerical zero singular value observed',format(max_numerical_zero,'.15g'))
