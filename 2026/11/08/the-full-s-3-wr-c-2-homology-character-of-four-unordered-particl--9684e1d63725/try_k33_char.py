import itertools,collections,time,json
from try_k33_4 import bases,indices,incident,E,differential
P=101

def perm_sign(seq):
 return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def addmul(d,k,v,p=P):
 for r,c in v.items():
  z=(d.get(r,0)+k*c)%p
  if z:d[r]=z
  else:d.pop(r,None)

def build_basis(vecs):
 piv={};dependent=[]
 for i,vec in enumerate(vecs):
  d={r:v%P for r,v in vec.items() if v%P}
  while d:
   r=min(d)
   if r in piv:addmul(d,-d[r],piv[r]);continue
   k=pow(d[r],-1,P)
   piv[r]={r2:(v*k)%P for r2,v in d.items()};break
  if not d:dependent.append(i)
 return piv,dependent

def kernel_gen(columns):
 piv={};rels=[]
 for j,vec in enumerate(columns):
  d={r:v%P for r,v in vec.items() if v%P};c={j:1}
  while d:
   r=min(d)
   if r in piv:
    v,rep=piv[r];factor=d[r]
    addmul(d,-factor,v);addmul(c,-factor,rep)
   else:
    k=pow(d[r],-1,P)
    piv[r]=({q:(z*k)%P for q,z in d.items()}, {q:(z*k)%P for q,z in c.items()})
    break
  if not d:rels.append(c)
 return piv,rels

def allG():
 S=list(itertools.permutations(range(3)))
 for a in S:
  for b in S:
   yield tuple(list(a)+[3+x for x in b])
   yield tuple([3+x for x in a]+list(b))
G=list(allG());assert len(G)==72 and len(set(G))==72

def act_basis(deg,j,g,mod=P):
 vv,exp=bases[deg][j]
 eperm={e:E.index(tuple(sorted((g[a],g[b])))) for e,(a,b) in enumerate(E)}
 out_exp=[0]*9
 for e,z in enumerate(exp):out_exp[eperm[e]]=z
 gvv=[g[v] for v,d in vv]
 order=sorted(range(deg),key=lambda i:gvv[i]);sgn=perm_sign(order)
 local=[]
 for v,d in vv:
  newv=g[v]
  enew_d=eperm[incident[v][d]]
  enew_ref=eperm[incident[v][0]]
  posd=incident[newv].index(enew_d);posr=incident[newv].index(enew_ref)
  mapping=collections.defaultdict(int)
  if posd:mapping[posd]+=1
  if posr:mapping[posr]-=1
  local.append([(x,y) for x,y in mapping.items() if y])
 result=collections.defaultdict(int)
 for combo in itertools.product(*local):
  newvv=tuple((gvv[i],combo[i][0]) for i in order)
  jj=indices[deg][(newvv,tuple(out_exp))]
  result[jj]+=sgn*mathprod(x[1] for x in combo)
 return {j:z%mod for j,z in result.items() if z%mod}

def mathprod(it):
 z=1
 for a in it:z*=a
 return z

def trace_chains(g):
 trs=[]
 for k,bb in enumerate(bases):
  trace=0
  for j in range(len(bb)):
   v=act_basis(k,j,g).get(j,0)
   if v>P//2:v-=P
   trace+=v
  trs.append(trace)
 return trs

def rank3generator():
 ds3=differential(3);ds4=differential(4)
 img,dep=build_basis(ds4)
 assert len(img)==240
 piv,rels=kernel_gen(ds3)
 print('rank d3',len(piv),'nullity',len(rels),flush=True)
 assert len(rels)==241
 zz=None
 for k,v in enumerate(rels):
  d=dict(v)
  while d:
   r=min(d)
   if r in img:addmul(d,-d[r],img[r]);continue
   break
  if d:
   zz=v;print('H3 nonboundary relation index',k,'sparsity',len(v),flush=True);break
 assert zz
 # insert z after image
 newimg=dict(img)
 d=dict(zz)
 while d:
  r=min(d)
  if r in newimg:addmul(d,-d[r],newimg[r]);continue
  newr=r;newcoef=d[r]
  inv=pow(newcoef,-1,P)
  newimg[r]={q:x*inv%P for q,x in d.items()};break
 return zz,img,newr,newcoef

def action_vec(k,vec,g):
 dest={}
 for j,c in vec.items():addmul(dest,c,act_basis(k,j,g))
 return dest

def h3character(zz,img,newr,newcoef,g):
 d=action_vec(3,zz,g)
 while d:
  r=min(d)
  if r in img:addmul(d,-d[r],img[r]);continue
  assert r==newr,(r,newr)
  c=d[r]*pow(newcoef,-1,P)%P
  addmul(d,-c,{q:v for q,v in _ZRED.items()})
  while d:
   rr=min(d)
   assert rr in img,(rr,len(d))
   addmul(d,-d[rr],img[rr])
  assert not d,len(d)
  assert c in (1,P-1),c
  return 1 if c==1 else -1

# need _ZRED = residual normalized? uses residual unnormalized of zz
if __name__=='__main__':
 z,img,newr,newcoef=rank3generator()
 red=dict(z)
 while red:
  r=min(red)
  if r in img:addmul(red,-red[r],img[r]);continue
  break
 _ZRED=red
 print('residual length',len(red),'coef',newcoef,flush=True)
 chars=[]
 for i,g in enumerate(G):
  tr=trace_chains(g)
  l=sum((-1)**k*tr[k] for k in range(5))
  h1=(sum((1 if {g[E[e][0]],g[E[e][1]]}==set(E[e]) else 0) * (1 if set(g[:3])==set(range(3)) else -1) for e in range(9)) -sum(g[v]==v for v in range(6))+1)
  c3=h3character(z,img,newr,newcoef,g)
  h2=l-1+h1+c3
  chars.append(dict(g=g,tr=tr,L=l,h1=h1,h2=h2,h3=c3))
  if i%12==0:print('g',i,g,'L',l,'h1',h1,'h2',h2,'h3',c3,flush=True)
 print('identity',chars[0],flush=True)
 with open('k33four_chars.json','w') as f:json.dump(chars,f,indent=2)
