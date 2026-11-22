#!/usr/bin/env python3
"""Reproducible exact rational cohomology character for a graph-derived 2-step CE complex."""
import itertools
from collections import defaultdict
from sympy import Matrix
V=4
E=((0,1),(0,2),(0,3),(1,2),(1,3))
N=V+len(E)
S=[tuple(c) for k in range(N+1) for c in itertools.combinations(range(N),k)]
Sby={k:[c for c in S if len(c)==k] for k in range(N+1)}

# d y_ij = x_i wedge x_j; d x_i = 0.
def differential(tup):
 out=defaultdict(int)
 for pos,g in enumerate(tup):
  if g<V:continue
  u,v=E[g-V]
  a=tup[:pos]+(u,v)+tup[pos+1:]
  if len(set(a))!=len(a):continue
  inv=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
  key=tuple(sorted(a))
  out[key]+=(-1)**(pos+inv)
 return {s:c for s,c in out.items() if c}

def dg_matrix(k):
 a=Sby[k]; b=Sby[k+1]; row={x:i for i,x in enumerate(b)}
 M=Matrix.zeros(len(b),len(a))
 for j,x in enumerate(a):
  for y,z in differential(x).items():M[row[y],j]=z
 return M

def weight(t):
 w=[0]*V
 for g in t:
  if g<V:w[g]+=1
  else:
   u,v=E[g-V];w[u]+=1;w[v]+=1
 return tuple(w)

def rational_rank_by_weight(mat,k):
 bydom=defaultdict(list);byran=defaultdict(list)
 for j,t in enumerate(Sby[k]):bydom[weight(t)].append(j)
 for i,t in enumerate(Sby[k+1]):byran[weight(t)].append(i)
 return sum(mat.extract(byran[w],I).rank() for w,I in bydom.items() if w in byran)

def sign_and_permute(t,perm):
 ans=[];sign=1
 for g in t:
  if g<V:ans.append(perm[g]);continue
  a,b=E[g-V];a=perm[a];b=perm[b]
  if a>b: a,b=b,a;sign*=-1
  ans.append(V+E.index((a,b)))
 sign*=(-1)**sum(ans[i]>ans[j] for i in range(len(ans)) for j in range(i+1,len(ans)))
 return tuple(sorted(ans)),sign

def action_matrix(k,perm):
 B=Sby[k];ii={x:i for i,x in enumerate(B)};A=Matrix.zeros(len(B),len(B))
 for j,t in enumerate(B):
  x,sgn=sign_and_permute(t,perm);A[ii[x],j]=sgn
 return A

def eigenspace_image_rank(k,perm,eps):
 # Images under d of signed (+) or (-) eigenspace basis of g in degree k
 B=Sby[k];index={x:i for i,x in enumerate(B)};done=set();columns=[]
 for i,t in enumerate(B):
  if i in done:continue
  x,s=sign_and_permute(t,perm);j=index[x]
  done.add(i);done.add(j)
  if i==j:
   if s==eps:columns.append({i:1})
  else:columns.append({i:1,j:eps*s})
 # Project differential; group by g-permuted weights of degree k for exact small block ranks
 d={t:differential(t) for t in B}
 groups=defaultdict(list)
 for col in columns:
  wt=weight(B[next(iter(col))]);
  wp=tuple(wt[perm.index(j)] for j in range(V))
  groups[min(wt,wp)].append(col)
 total=0
 for I,cols in groups.items():
  target=set()
  vecs=[]
  for col in cols:
   v=defaultdict(int)
   for j,c in col.items():
    for t,z in d[B[j]].items():v[t]+=c*z
   vecs.append({t:a for t,a in v.items() if a})
   target.update(vecs[-1])
  target=sorted(target)
  mat=Matrix([[v.get(t,0) for v in vecs] for t in target])
  if mat.rows and mat.cols:total+=mat.rank()
 return total

def main():
 dmat=[dg_matrix(k) for k in range(N)]
 for k in range(N-1):assert dmat[k+1]*dmat[k]==Matrix.zeros(len(Sby[k+2]),len(Sby[k]))
 ranks=[rational_rank_by_weight(dmat[k],k) for k in range(N)]
 dims=[len(Sby[k]) for k in range(N+1)]
 betti=[dims[k]-(ranks[k-1] if k else 0)-(ranks[k] if k<N else 0) for k in range(N+1)]
 print('dimensions',dims,'ranks',ranks,'betti',betti,'total',sum(betti))
 autos={
 'identity':(0,1,2,3),
 'hub_swap':(1,0,2,3),
 'tip_swap':(0,1,3,2),
 'both':(1,0,3,2)}
 character={}
 for name,perm in autos.items():
  traces_chain=[];trace_image=[]
  for k in range(N+1):
   M=action_matrix(k,perm);assert M*M==Matrix.eye(dims[k]);
   traces_chain.append(M.trace())
   if k<N:assert action_matrix(k+1,perm)*dmat[k]==dmat[k]*M
  if name=='identity':trace_image=ranks
  else:
   for k in range(N):
    rp=eigenspace_image_rank(k,perm,1)
    rm=eigenspace_image_rank(k,perm,-1)
    assert rp+rm==ranks[k],(k,name,rp,rm,ranks[k])
    trace_image.append(rp-rm)
  trace_h=[traces_chain[k]-(trace_image[k-1] if k else 0)-(trace_image[k] if k<N else 0) for k in range(N+1)]
  if name=='identity':assert trace_h==betti
  print(name,'chains',traces_chain,'imageTr',trace_image,'cohomTr',trace_h)
  character[name]=trace_h
 print('invariant multiplicities')
 # Fourier inversion for V4 characters label eigenvalues of hub and tip swaps
 for epsh in (+1,-1):
  for epst in (+1,-1):
   mult=[(character['identity'][k]+epsh*character['hub_swap'][k]+epst*character['tip_swap'][k]+epsh*epst*character['both'][k])//4 for k in range(N+1)]
   assert all(m>=0 for m in mult)
   print(epsh,epst,mult,sum(mult))

if __name__=='__main__':main()
