import itertools,collections,math,time,sys
w=4
V=6
E=[(i,3+j) for i in range(3) for j in range(3)]
incident=[[q for q,(a,b) in enumerate(E) if v in (a,b)] for v in range(V)]
assert all(len(x)==3 for x in incident)

def weak_composition(n,k):
 if k==1:
  yield (n,);return
 for x in range(n+1):
  for y in weak_composition(n-x,k-1):yield (x,)+y

bases=[];indices=[]
for deg in range(w+1):
 items=[]
 for verts in itertools.combinations(range(V),deg):
  for dirs in itertools.product([1,2],repeat=deg):
   vv=tuple((v,d) for v,d in zip(verts,dirs))
   for exp in weak_composition(w-deg,len(E)):
    items.append((vv,exp))
 bases.append(items);indices.append({x:i for i,x in enumerate(items)})
print('CH', [len(x) for x in bases],flush=True)

def differential(k):
 # [(rowindex, integer coefficient) per column]
 cols=[]
 for vv,exp in bases[k]:
  c=collections.defaultdict(int)
  for i,(v,d) in enumerate(vv):
   vnew=vv[:i]+vv[i+1:]
   for e,sgn in ((incident[v][d],(-1)**i),(incident[v][0],-(-1)**i)):
    enew=list(exp);enew[e]+=1
    c[indices[k-1][(vnew,tuple(enew))]]+=sgn
  cols.append({x:y for x,y in c.items() if y})
 return cols

def rank_mod(cols,p,limit=None):
 pivot={}; processed=0;t=time.time();maxfill=0
 for j,c in enumerate(cols):
  d={i:v%p for i,v in c.items() if v%p}
  while d:
   i=min(d); coeff=d[i];base=pivot.get(i)
   if base is None:
    inv=pow(coeff,-1,p);d={r:val*inv%p for r,val in d.items() if val%p};pivot[i]=d;maxfill=max(maxfill,len(d));break
   factor=coeff
   for r,val in base.items():
    new=(d.get(r,0)-factor*val)%p
    if new:d[r]=new
    elif r in d:del d[r]
  processed+=1
  if j%300==299: print('progress',p,processed,len(pivot),round(time.time()-t,2),'maxfill',maxfill,flush=True)
  if limit is not None and time.time()-t>limit:
   print('timeout',flush=True);return None
 return len(pivot)

if __name__=='__main__':
 ds=[None]+[differential(k) for k in range(1,5)]
 for k in range(2,5):
  count=0
  for c in ds[k]:
   res=collections.defaultdict(int)
   for i,sgn in c.items():
    for j,v in ds[k-1][i].items():res[j]+=sgn*v
   if any(res.values()):count+=1
  print('square',k,count,flush=True)
 for p in (2,3,101):
  ranks=[]
  for k in range(1,5):ranks.append(rank_mod(ds[k],p,100));print('rank',p,k,ranks[-1],flush=True)
  if any(q is None for q in ranks):break
  b=[len(bases[i])-(ranks[i-1] if i>0 else 0)-(ranks[i] if i<4 else 0) for i in range(5)]
  print('BETTI',p,b,flush=True)
