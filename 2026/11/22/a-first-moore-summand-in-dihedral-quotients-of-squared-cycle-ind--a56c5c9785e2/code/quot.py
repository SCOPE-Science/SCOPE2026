import itertools,collections,sys,time

def qcomplex(n,verbose=False):
 def faces():
  arr=[]
  for b in range(1,1<<n):
   ids=[i for i in range(n) if (b>>i)&1]
   if all(min((j-i)%n,(i-j)%n)>2 for i,j in itertools.combinations(ids,2)):arr.append(b)
  return arr
 faces=faces(); face_set=set(faces)
 gmaps=[]
 for eps in (1,-1):
  for k in range(n):gmaps.append([ (eps*i+k)%n for i in range(n) ])
 maps=[]
 for mp in gmaps:
  maps.append({f:sum(1<<mp[i] for i in range(n) if f>>i&1) for f in faces})
 def can(flag): return min(tuple(m[f] for f in flag) for m in maps)
 # distinct flags made as subchains in arbitrary faces
 orbits=[set() for _ in range(max(f.bit_count() for f in faces))]
 for f in faces:
  subs=[s for s in faces if s & f==s]
  bysize=collections.defaultdict(list)
  for s in subs:bysize[s.bit_count()].append(s)
  for r in range(1,len(bysize)+1):
   for sizes in itertools.combinations(sorted(bysize),r):
    for flag in itertools.product(*(bysize[s] for s in sizes)):
     if flag[-1]!=f or any((a&b)!=a for a,b in zip(flag,flag[1:])):continue
     orbits[r-1].add(can(flag))
 basis=[sorted(s) for s in orbits]
 inds=[{f:i for i,f in enumerate(b)} for b in basis]
 boundaries=[]
 for d in range(1,len(basis)):
  cols=[]
  for flag in basis[d]:
   col=collections.Counter()
   for i in range(d+1):
    targ=can(flag[:i]+flag[i+1:]);col[inds[d-1][targ]]+=(-1)**i
   cols.append({j:v for j,v in col.items() if v})
  boundaries.append(cols)
 if verbose:print('n',n,'faces',len(faces),'orbit cells',list(map(len,basis)), 'boundaries',list(map(len,boundaries)),flush=True)
 return basis,boundaries

def modrank(cols,p):
 pivots={};rank=0
 for vec in cols:
  a={i:v%p for i,v in vec.items() if v%p}
  while a:
   i=min(a)
   if i in pivots:
    b=pivots[i];mul=a[i]
    for j,v in b.items():
     r=(a.get(j,0)-mul*v)%p
     if r:a[j]=r
     else:a.pop(j,None)
   else:
    inv=pow(a[i],-1,p)
    pivots[i]={j:v*inv%p for j,v in a.items()};rank+=1;break
 return rank

if __name__=='__main__':
 for n in range(int(sys.argv[1]),int(sys.argv[2])+1):
  start=time.time(); b,d=qcomplex(n,True)
  rr=[modrank(m, 32003) for m in d]
  bet=[len(x) -(rr[i-1] if i else 0)-(rr[i] if i<len(rr) else 0) for i,x in enumerate(b)]
  print(n,rr,bet, 'seconds',time.time()-start,flush=True)
