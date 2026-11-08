import itertools, time
MOD=3
n=18
lcf=(5,7,-7,7,-7,-5)*3
edges={tuple(sorted((i,(i+1)%n))) for i in range(n)}|{tuple(sorted((i,(i+d)%n))) for i,d in enumerate(lcf)}
faces={k:[] for k in (4,5,6)}
for k in faces:
 for x in itertools.combinations(range(n),k):
  if not any(a in x and b in x for a,b in edges):faces[k].append(x)
print('faces',[(k,len(v)) for k,v in faces.items()],flush=True)
indexes={k:{v:i for i,v in enumerate(faces[k])} for k in faces}
def trim(d):return {k:v%3 for k,v in d.items() if v%3}
def sadd(a,b,c):
 for i,v in b.items():
  nv=(a.get(i,0)+c*v)%3
  if nv:a[i]=nv
  elif i in a:del a[i]
def bdy(x):
 out={}; k=len(x)
 for j in range(k):out[indexes[k-1][x[:j]+x[j+1:]]]=1 if j%2==0 else 2
 return out
# simultaneous column reduction: record dependent boundary cycles in C4 for d4: C4 (5vertices) -> C3 (4vertices).
piv_d4={}; reps_d4={}; cycles=[]
for j,x in enumerate(faces[5]):
 v=bdy(x);comb={j:1}
 while v:
  p=max(v)
  if p not in piv_d4:
   factor=1 if v[p]==1 else 2
   if factor==2:
    v={i:factor*w%3 for i,w in v.items()};comb={i:factor*w%3 for i,w in comb.items()}
   piv_d4[p]=v;reps_d4[p]=comb;break
  c=-v[p]
  sadd(v,piv_d4[p],c);sadd(comb,reps_d4[p],c)
 if not v:cycles.append(comb)
print('d4 rank',len(piv_d4),'cycles',len(cycles),flush=True)
assert len(piv_d4)==472 and len(cycles)==284
# Reduce 5-boundaries (d5: C5 -> C4) and augment with homology cycles
piv_4={};rep_4={};b_rank=0

def add(v,hom=None):
 v=v.copy(); comb={} if hom is None else hom.copy()
 while v:
  p=max(v)
  if p not in piv_4:
   factor=1 if v[p]==1 else 2
   if factor==2:
    v={i:factor*w%3 for i,w in v.items()};comb={i:factor*w%3 for i,w in comb.items()}
   piv_4[p]=v;rep_4[p]=comb;return True,comb
  c=-v[p]
  sadd(v,piv_4[p],c);sadd(comb,rep_4[p],c)
 return False,comb
for j,x in enumerate(faces[6]):
 inserted,_=add(bdy(x))
 if inserted:b_rank+=1
print('d5 rank',b_rank,flush=True)
assert b_rank==274
H=[]
for v in cycles:
 inserted,_=add(v,hom={len(H):1})
 if inserted:H.append(v)
print('homology',len(H),flush=True)
assert len(H)==10
# get coordinates in modulo3 homology by reduction over all d5 and H pivots
def coords(v):
 v=v.copy();coeff={}
 while v:
  p=max(v);assert p in piv_4,p
  c=v[p];sadd(v,piv_4[p],-c);sadd(coeff,rep_4[p],c)
 return [coeff.get(j,0)%3 for j in range(10)]
def chain_transform(v,p):
 w={}
 for idx,coef in v.items():
  x=faces[5][idx]; img=[p[i] for i in x]
  s=(-1)**sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))
  j=indexes[5][tuple(sorted(img))]
  nv=(w.get(j,0)+coef*s)%3
  if nv:w[j]=nv
  elif j in w:del w[j]
 return w

def rank(A):
 p={}
 for row in A:
  r={j:v%3 for j,v in enumerate(row) if v%3}
  while r:
   a=max(r)
   if a not in p:
    if r[a]==2:r={j:2*v%3 for j,v in r.items()}
    p[a]=r;break
   sadd(r,p[a],-r[a])
 return len(p)
def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(10))%3 for j in range(10)] for i in range(10)]
G_mats={}
for shift in (6,12):
 g=tuple((i+shift)%n for i in range(n))
 assert all(tuple(sorted((g[a],g[b]))) in edges for a,b in edges)
 cols=[]
 for v in H:
  t=chain_transform(v,g)
  cols.append(coords(t))
 G=[[cols[j][i] for j in range(10)] for i in range(10)]
 G_mats[shift]=G
 N=[[(G[i][j]-(i==j))%3 for j in range(10)] for i in range(10)]
 N2=matmul(N,N);N3=matmul(N2,N)
 assert not any(any(a for a in row) for row in N3)
 r1,r2=rank(N),rank(N2)
 js=(10-2*r1+r2,r1-2*r2,r2)
 print('translation',shift,'rN',r1,'rN2',r2,'Jordan sizes1 2 3',js,flush=True)
 print('matrix rows',G,flush=True)

assert matmul(G_mats[6],G_mats[6])==G_mats[12]
assert matmul(G_mats[6],G_mats[12])==[[int(i==j) for j in range(10)] for i in range(10)]
print('CONSISTENCY: second generator matrix is square; third power identity')
