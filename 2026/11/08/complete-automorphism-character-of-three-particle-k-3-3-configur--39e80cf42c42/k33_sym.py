import itertools,collections,sys,time
from k33_compute import *
pmod=10007
D=gen();DD=boundaries(D)
IDX=[{b:i for i,b in enumerate(rows)} for rows in D]
PERMS=list(itertools.permutations(range(3)))
AUT=[]
for swap in [0,1]:
 for p in PERMS:
  for q in PERMS:
   if not swap: g=tuple(p)+(tuple(3+x for x in q))
   else:g=tuple(3+x for x in p)+tuple(q)
   em=[]
   for a,b in E:
    aa,bb=g[a],g[b]
    if aa>bb:aa,bb=bb,aa
    em.append(E.index((aa,bb)))
   AUT.append((g,tuple(em),swap,p,q))

def act_basis(gidx,d,j):
 g,em,*_=AUT[gidx]; hs,exp=D[d][j]
 nx=[0]*len(E)
 for ii,x in enumerate(exp):nx[em[ii]]=x
 if not hs:return {IDX[d][((),tuple(nx))]:1}
 vs=tuple(g[v] for v,ch in hs)
 sgn=(-1)**sum(vs[i]>vs[j] for i in range(len(vs)) for j in range(i+1,len(vs)))
 opts=[]
 for v,ch in hs:
  vv=g[v];ee,base=H[v][ch]
  X=[]
  for e,s in ((em[ee],1),(em[base],-1)):
   if e!=neigh[vv][0]:
    X.append((neigh[vv][1:].index(e),s))
  opts.append(X)
 out=collections.defaultdict(int)
 for combo in itertools.product(*opts):
  newhs=tuple(sorted((g[v],combo[i][0]) for i,(v,ch) in enumerate(hs)))
  c=sgn
  for ch,s in combo:c*=s
  out[IDX[d][(newhs,tuple(nx))]]+=c
 return {k:v for k,v in out.items() if v}

def act_vec(gi,d,vec):
 ans=collections.defaultdict(int)
 for j,a in vec.items():
  for jj,b in act_basis(gi,d,j).items():ans[jj]=(ans[jj]+a*b)%pmod
 return {k:v for k,v in ans.items() if v}

def gauss_basis(cols):
 piv={}; arr=[]
 for col in cols:
  vec={r:v%pmod for r,v in col.items() if v%pmod}
  for r in sorted(piv):
   if r not in vec:continue
   c=vec[r]
   for rr,w in piv[r].items():
    z=(vec.get(rr,0)-c*w)%pmod
    if z:vec[rr]=z
    else:vec.pop(rr,None)
  if not vec:continue
  r=min(vec);a=pow(vec[r],-1,pmod)
  vec={rr:w*a%pmod for rr,w in vec.items()}
  piv[r]=vec;arr.append((r,vec))
 return piv,arr

def trace_action_image(gi,d,piv,arr):
 # basis elimination uses ascending pivot, each vector e_i in image
 tr=0
 for rr,vec in arr:
  tmp=act_vec(gi,d-1,vec)
  for p in sorted(piv):
   v=tmp.get(p,0)
   if not v:continue
   if p==rr:tr=(tr+v)%pmod
   for row,w in piv[p].items():
    z=(tmp.get(row,0)-v*w)%pmod
    if z:tmp[row]=z
    else:tmp.pop(row,None)
  if tmp:raise RuntimeError(f'non-image residue at {gi},{d}:{len(tmp)}')
 return tr

def chain_trace(gi,d):
 return sum(act_basis(gi,d,j).get(j,0) for j in range(len(D[d])))

def signed(x):return x-pmod if x>pmod//2 else x

def verify_all_actions_are_chain_maps():
 for gi in range(len(AUT)):
  for d in (1,2,3):
   for j,col in enumerate(DD[d-1]):
    lhs=collections.defaultdict(int)
    for r,x in col.items():
     for rr,y in act_basis(gi,d-1,r).items():lhs[rr]+=x*y
    rhs=collections.defaultdict(int)
    for u,x in act_basis(gi,d,j).items():
     for rr,y in DD[d-1][u].items():rhs[rr]+=x*y
    assert not any(lhs[k]!=rhs[k] for k in lhs.keys()|rhs.keys())
 print('all 72 automorphisms commute integrally with all three boundaries',flush=True)

if __name__=='__main__':
 t=time.monotonic()
 verify_all_actions_are_chain_maps()
 bas=[gauss_basis(cols) for cols in DD]
 print('bases',[len(a) for p,a in bas],flush=True)
 results=[]
 for gi,a in enumerate(AUT):
  tc=[chain_trace(gi,d) for d in range(4)]
  tb=[0]+[signed(trace_action_image(gi,i,*bas[i-1])) for i in (1,2,3)]+[0]
  th=[tc[i]-tb[i]-tb[i+1] for i in range(4)]
  results.append((tc,tb,th))
  if gi%12==0:print('progress',gi,tc,tb,th,flush=True)
 assert all(x[2][0]==1 and x[2][3]==0 for x in results)
 print('ID',results[0],flush=True)
 print('h1',[r[2][1] for r in results],flush=True)
 print('h2',[r[2][2] for r in results],flush=True)
 print('Trace H1 invariant',sum(r[2][1] for r in results)/72)
 print('Trace H2 invariant',sum(r[2][2] for r in results)/72)
 print('character computation completed')
 print('K33_EQUIVARIANT_CHARACTERS_PASS',flush=True)
