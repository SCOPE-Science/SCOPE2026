import math
from collections import Counter
import curve_geometry as f
from sympy import Matrix,ZZ,eye
from sympy.matrices.normalforms import smith_normal_form
I=f.I
L=Matrix([[27 if i==j else -int(I[i][j]==1) for j in range(56)] for i in range(56)])
labels=f.labels
results={}
for q in (1,3,5,7):
 chi=1 if q in (1,7) else -1
 perm=[]
 for c in f.curves:
  if c[0]=='h':key=('h',c[1],c[2],c[3]*q%8,c[4])
  else:key=('n',c[1]*q%4,c[2]*q%4,c[3]*chi)
  perm.append(labels[key])
 assert all(I[perm[i]][perm[j]]==I[i][j] for i in range(56) for j in range(56)),('graph automorphism',q)
 orbits=[];seen=set()
 for i in range(56):
  if i not in seen:
   orb=tuple(sorted(set([i,perm[i]])));seen.update(orb);orbits.append(orb)
 fixed=[o[0] for o in orbits if len(o)==1]
 base=fixed[0] if fixed else 0
 base_orbit=next(o for o in orbits if base in o)
 orbits=[base_orbit]+[o for o in orbits if o!=base_orbit]
 extra=not fixed
 rank=len(orbits)-1+(1 if extra else 0)
 Q=Matrix.zeros(rank,56+(1 if extra else 0))
 images={base:Matrix.zeros(rank,1)}
 if extra:
  u=Matrix.zeros(rank,1);u[rank-1]=1
  images[perm[base]]=u
 for j,o in enumerate(orbits[1:]):
  gen=Matrix.zeros(rank,1);gen[j]=1
  if len(o)==1:images[o[0]]=gen
  else:
   images[o[0]]=gen
   images[o[1]]=gen+(u if extra else Matrix.zeros(rank,1))
 for j in range(56):
  v=Matrix.zeros(rank,1)
  for i in range(56):
   if L[i,j]!=0:v+=L[i,j]*images[i]
  Q[:,j]=v
 if extra:Q[-1,56]=2
 def pval(a,p,K):
  if a==0:return K
  v=0
  while v<K and a%p==0:a//=p;v+=1
  return v
 def local_e(A,p,K):
  n=A.rows;m=A.cols;mod=p**K
  X=[[int(A[i,j])%mod for j in range(m)] for i in range(n)]
  vlist=[]
  for h in range(n):
   v,i0,j0=min((pval(X[i][j],p,K),i,j) for i in range(h,n) for j in range(h,m))
   if v>=K:raise RuntimeError(f"nonfull rank mod p^{K} at h={h}")
   X[h],X[i0]=X[i0],X[h]
   for i in range(n):X[i][h],X[i][j0]=X[i][j0],X[i][h]
   den=p**v
   un=(X[h][h]//den)%(p**(K-v));inv=pow(un,-1,p**(K-v))
   for i in range(h+1,n):
    factor=((X[i][h]//den)*inv)%(p**(K-v))
    if factor:
     for j in range(h,m):X[i][j]=(X[i][j]-factor*X[h][j])%mod
   for j in range(h+1,m):
    factor=((X[h][j]//den)*inv)%(p**(K-v))
    if factor:
     for i in range(h,n):X[i][j]=(X[i][j]-factor*X[i][h])%mod
   vlist.append(v)
  return vlist
 spectra={p:Counter(local_e(Q,p,k)) for p,k in [(2,7),(3,5),(7,3)]}
 assert all(sum(spectra[p].values())==rank for p in spectra)
 for p in [2,3,7]:assert max(spectra[p]) < {2:7,3:5,7:3}[p]
 order=math.prod(p**sum(e*n for e,n in spectra[p].items()) for p in spectra)
 results[q]={p:dict(spectra[p]) for p in spectra}
 print('q',q,'fixed vertices',len(fixed),'rank',rank,'spectra',spectra,'order',order,flush=True)


EXPECTED={
1:{2:{1:14,2:12,4:15,5:6,0:8},3:{0:34,1:14,3:7},7:{0:29,1:26}},
3:{2:{0:4,1:7,2:8,4:6,5:3},3:{0:19,1:6,3:3},7:{0:14,1:14}},
5:{2:{0:2,1:5,2:16,4:4,5:1},3:{0:23,1:4,3:1},7:{0:8,1:20}},
7:{2:{0:4,1:10,2:4,4:11,5:2},3:{0:18,1:10,3:3},7:{0:17,1:14}}
}
assert results==EXPECTED, (results,EXPECTED)
print("ARITHMETIC_FERMAT_CRITICAL_GROUP_SPECTRA_OK")
