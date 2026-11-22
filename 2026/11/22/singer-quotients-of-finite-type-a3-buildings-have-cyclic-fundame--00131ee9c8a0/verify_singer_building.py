import itertools, math, sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def fm(a,b,p,mod):
 c=[0]*7
 for i in range(4):
  for j in range(4):c[i+j]+=a[i]*b[j]
 for t in range(6,3,-1):
  v=c[t]%p
  for j in range(4):c[t-4+j]-=v*mod[j]
 return tuple(x%p for x in c[:4])
def fp(a,n,p,mod):
 r=(1,0,0,0)
 while n:
  if n&1:r=fm(r,a,p,mod)
  a=fm(a,a,p,mod);n//=2
 return r

def findpoly(p):
 x=(0,1,0,0); target=p**4-1
 fs=sp.factorint(target)
 for co in itertools.product(range(p),repeat=4):
  if co[0]==0:continue
  if fp(x,target,p,co)==(1,0,0,0) and all(fp(x,target//z,p,co)!=(1,0,0,0) for z in fs):
   return co
 raise Exception('no primitive')

def rref(vs,p):
 a=[list(v) for v in vs];k=0
 for j in range(4):
  pi=next((i for i in range(k,len(a)) if a[i][j]%p),None)
  if pi is None:continue
  a[k],a[pi]=a[pi],a[k];inv=pow(int(a[k][j]),-1,p)
  a[k]=[(v*inv)%p for v in a[k]]
  for i in range(len(a)):
   if i!=k and a[i][j]:
    c=a[i][j];a[i]=[(v-c*w)%p for v,w in zip(a[i],a[k])]
  k+=1
  if k==len(a):break
 return tuple(tuple(x) for x in a[:k])

def allspaces(p,dim):
 # enumerate unique rowspaces by bases with canonical rref, every pivot pattern and free entries
 out=[]
 for piv in itertools.combinations(range(4),dim):
  loc=[(i,j) for i in range(dim) for j in range(piv[i]+1,4) if j not in piv]
  for vals in itertools.product(range(p),repeat=len(loc)):
   rows=[[int(j==piv[i]) for j in range(4)] for i in range(dim)]
   for (i,j),val in zip(loc,vals):rows[i][j]=val
   out.append(tuple(tuple(row) for row in rows))
 return out

def vspan(a,b,p):return len(rref(a+b,p))==len(b)
def cells(p):
 mod=findpoly(p); x=(0,1,0,0); N=(p**4-1)//(p-1)
 print('p',p,'primitive',mod,'group',N)
 spaces={d:allspaces(p,d) for d in (1,2,3)}
 for d in spaces:print('subspaces',d,len(spaces[d]))
 v=[(d,rows) for d in (1,2,3) for rows in spaces[d]]
 lookup={cell:i for i,cell in enumerate(v)}
 xs=[fp(x,k,p,mod) for k in range(N)]
 def act(v0,k):
  d,vs=v0
  return (d,rref(tuple(fm(w,xs[k],p,mod) for w in vs),p))
 permutation=[lookup[act(w,1)] for w in v]
 # face orbits via repeated one-step permutation
 def orbit(rep):
  cur=rep;arr=[]
  while cur not in arr:
   arr.append(cur);cur=tuple(permutation[u] for u in cur)
  assert cur==rep
  return arr
 edges=[];tris=[]
 for i,(d,s) in enumerate(v):
  for j,(e,t) in enumerate(v):
   if d<e and vspan(s,t,p):edges.append((i,j))
 for a,b in edges:
  if v[a][0]!=1 or v[b][0]!=2:continue
  for c in range(len(v)):
   if v[c][0]==3 and vspan(v[b][1],v[c][1],p):tris.append((a,b,c))
 bydim=[[(i,) for i in range(len(v))],edges,tris]
 ids=[];orbits=[]
 for ff in bydim:
  mapx={}; reps=[]
  for face in ff:
   if face in mapx:continue
   j=len(reps); reps.append(face)
   for z in orbit(face):mapx[z]=j
  ids.append(mapx);orbits.append(reps)
 print('quotient f-vector',[len(r) for r in orbits])
 d1=sp.zeros(len(orbits[0]),len(orbits[1]));d2=sp.zeros(len(orbits[1]),len(orbits[2]))
 for j,(a,b) in enumerate(orbits[1]):d1[ids[0][(b,)],j]+=1;d1[ids[0][(a,)],j]-=1
 for j,(a,b,c) in enumerate(orbits[2]):
  for t,e in ((1,(b,c)),(-1,(a,c)),(1,(a,b))):d2[ids[1][e],j]+=t
 assert d1*d2==sp.zeros(*((d1*d2).shape))
 print('ranks',d1.rank(),d2.rank(), 'chi',len(orbits[0])-len(orbits[1])+len(orbits[2]))
 # eliminate graph tree: relation in free rank E-V+1
 edgeends=[(ids[0][(a,)],ids[0][(b,)]) for a,b in orbits[1]]
 parent=list(range(len(orbits[0])))
 def root(a):
  while parent[a]!=a:a=parent[a]
  return a
 tree=[]
 for j,(a,b) in enumerate(edgeends):
  ra,rb=root(a),root(b)
  if ra!=rb:tree.append(j);parent[ra]=rb
 assert len(tree)==len(orbits[0])-1
 rest=[j for j in range(len(orbits[1])) if j not in tree]
 rel=d2.extract(rest,list(range(d2.cols)))
 sd=smith_normal_form(rel,domain=ZZ)
 nonzero=[abs(int(sd[i,i])) for i in range(min(sd.shape)) if sd[i,i]]
 tors=[x for x in nonzero if x>1]
 print('H1 elementary factors',tors, 'H1 free rank',len(rest)-len(nonzero), 'H2 rank',d2.cols-len(nonzero))
 return [len(r) for r in orbits],tors,d2.cols-len(nonzero)

if __name__=='__main__':
 for p in [2,3]:
  f,tors,h2=cells(p)
  assert f==[p+3,3*(p*p+p+1),(p+1)*(p*p+p+1)]
  assert tors==[p*p+1] and h2==p*p*(p-1)
 print('SINGER_BUILDING_QUOTIENT_CHECKS_OK')
