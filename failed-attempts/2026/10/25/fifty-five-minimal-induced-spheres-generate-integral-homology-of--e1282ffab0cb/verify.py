"""Exact integral homology certificate for the Paley-11 directed flag complex.

Dependencies: numpy and sympy. Executes exhaustively over 462 five-subsets.
"""
import itertools, numpy as np, sympy as sp
from collections import Counter,defaultdict
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=11; Q={i*i%p for i in range(1,p)}
def order(s):
 z=sorted(s,key=lambda i:-sum(((j-i)%p in Q) for j in s if i!=j))
 return tuple(z) if all((z[j]-z[i])%p in Q for i in range(len(z)) for j in range(i+1,len(z))) else None
faces={d:[o for ss in itertools.combinations(range(p),d+1) if (o:=order(ss))] for d in range(4)}
idx={d:{frozenset(z):i for i,z in enumerate(v)} for d,v in faces.items()}
B={}
for d in (1,2,3):
 M=np.zeros((len(faces[d-1]),len(faces[d])),dtype=int)
 for j,t in enumerate(faces[d]):
  for i in range(len(t)):
   M[idx[d-1][frozenset(t[:i]+t[i+1:])],j]=(-1)**i
 B[d]=M
print('f',list(map(len,faces.values())),flush=True)
assert np.array_equal(B[2]@B[3],np.zeros((55,55),dtype=int))
# Exhaustive local mod-two homology census for induced subcomplexes.
def gf2_rank(columns):
 pivots={}
 for v in columns:
  while v:
   b=v.bit_length()-1
   if b in pivots:v^=pivots[b]
   else:pivots[b]=v;break
 return len(pivots)
def local_h2(W):
 ss={d:[frozenset(t) for t in faces[d] if set(t)<=set(W)] for d in range(4)}
 ii={d:{f:i for i,f in enumerate(ss[d])} for d in range(4)}
 b2=[sum(1<<ii[1][f-{x}] for x in f) for f in ss[2]]
 b3=[sum(1<<ii[2][f-{x}] for x in f) for f in ss[3]]
 return len(ss[2])-gf2_rank(b2)-gf2_rank(b3)
assert all(local_h2(w)==0 for k in range(1,5) for w in itertools.combinations(range(p),k))
all_h2={w:local_h2(w) for w in itertools.combinations(range(p),5)}
assert Counter(all_h2.values())==Counter({0:407,1:55})
# sphere cycles from 5 vertices
CS=[]; SUP=[]
for w in itertools.combinations(range(p),5):
 W=set(w); tris=[j for j,t in enumerate(faces[2]) if set(t)<=W]
 tetras=[j for j,t in enumerate(faces[3]) if set(t)<=W]
 if len(tris)!=6 or len(tetras)!=0:continue
 local=B[2][:,tris]
 erows=[i for i in range(55) if np.count_nonzero(local[i,:])]
 if len(erows)!=9 or not all(np.count_nonzero(local[i,:])==2 for i in erows):continue
 c={0:1};changed=True
 while changed:
  changed=False
  for ei in erows:
   a,b=np.nonzero(local[ei,:])[0]
   if a in c and b not in c:c[b]=-int(local[ei,a])*c[a]//int(local[ei,b]);changed=True
   elif b in c and a not in c:c[a]=-int(local[ei,b])*c[b]//int(local[ei,a]);changed=True
 if len(c)!=6:continue
 v=np.zeros(110,dtype=int)
 for i,j in enumerate(tris):v[j]=c[i]
 assert np.all(B[2]@v==0)
 CS.append(v);SUP.append(w)
print('minimal-spheres',len(CS),'example',SUP[0],flush=True)
assert set(SUP)=={w for w,v in all_h2.items() if v==1}
C=np.array(CS,dtype=int).T
# universal trivialization of reduced B2 (cycle-space coords on nonstar edges)
nonstar=[i for i,e in enumerate(faces[1]) if 0 not in e]
A=np.array(B[2][nonstar,:],dtype=object)
V=np.eye(110,dtype=object); Winv=np.eye(110,dtype=object)
for k in range(45):
 opts=[(i,j) for i in range(k,45) for j in range(k,110) if abs(A[i,j])==1]
 if not opts:raise ValueError('no ±1 pivot '+str(k))
 i,j=opts[0]
 if i!=k: A[[i,k],:]=A[[k,i],:]
 if j!=k:
  A[:,[j,k]]=A[:,[k,j]];V[:,[j,k]]=V[:,[k,j]];Winv[[j,k],:]=Winv[[k,j],:]
 s=A[k,k];
 if s==-1:A[k,:]=-A[k,:]
 for i in range(k+1,45):
  if A[i,k]:A[i,:]-=A[i,k]*A[k,:]
 for j in range(k+1,110):
  a=A[k,j]
  if a:
   A[:,j]-=a*A[:,k];V[:,j]-=a*V[:,k];Winv[k,:]+=a*Winv[j,:]
 
assert np.array_equal(A[:,:45],np.eye(45,dtype=object))
assert not np.any(A[:,45:]);
assert np.array_equal(Winv@V,np.eye(110,dtype=object))
assert not np.any((Winv[:45,:]@B[3].astype(object)))
assert not np.any((Winv[:45,:]@C.astype(object)))
T=np.array(Winv[45:,:]@B[3].astype(object),dtype=int)
U=np.array(Winv[45:,:]@C.astype(object),dtype=int)
print('B3 Smith start',T.shape,flush=True)
s=smith_normal_form(sp.Matrix(T),domain=ZZ)
print('B3 nonzero',Counter(abs(int(s[i,i])) for i in range(min(s.shape)) if s[i,i]),flush=True)
print('M=[B3,C] Smith start',flush=True)
s2=smith_normal_form(sp.Matrix(np.hstack((T,U))),domain=ZZ)
print('joint nonzero',Counter(abs(int(s2[i,i])) for i in range(min(s2.shape)) if s2[i,i]),flush=True)
print('sphere-support-count',len(SUP),'representative',SUP[0],flush=True)
assert len(SUP)==55
assert len({tuple(sorted((a*x+b)%11 for x in SUP[0])) for a in Q for b in range(11)})==55
assert set(SUP)=={tuple(sorted((a*x+b)%11 for x in SUP[0])) for a in Q for b in range(11)}
assert sorted(abs(int(s[i,i])) for i in range(min(s.shape)) if s[i,i]) == [1]*54+[2]
assert sorted(abs(int(s2[i,i])) for i in range(min(s2.shape)) if s2[i,i]) == [1]*65
print('VERIFY_OK_PALEY11_MINIMAL_SPHERE_GENERATORS')
