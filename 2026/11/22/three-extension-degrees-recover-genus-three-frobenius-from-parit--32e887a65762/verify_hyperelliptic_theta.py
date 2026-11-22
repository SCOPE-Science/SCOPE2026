import itertools, collections

def partitions(n,maxv=None):
 if n==0: yield ();return
 if maxv is None:maxv=n
 for k in range(min(n,maxv),1-1,-1):
  for tail in partitions(n-k,k):yield (k,)+tail

def perm(part):
 p=list(range(8));k=0
 for n in part:
  for j in range(n): p[k+j]=k+(j+1)%n
  k+=n
 return p
pairs=list(itertools.combinations(range(8),2))
quads=sorted(set(min(tuple(C),tuple(i for i in range(8) if i not in C)) for C in itertools.combinations(range(8),4)))
assert len(quads)==35

def cycs(objects,convert,p):
 ix={x:i for i,x in enumerate(objects)}; seen=set();out=[]
 for u in objects:
  if u in seen:continue
  v=u;m=0
  while v not in seen:
   seen.add(v);m+=1
   v=convert(tuple(sorted(p[i] for i in v)))
  assert v==u
  out.append(m)
 return sorted(out)

def counts(cc,n):return sum(i for i in cc if n%i==0)
records=[]
for pt in partitions(8):
 p=perm(pt)
 odd=cycs(pairs,lambda c:c,p)
 even=[1]+cycs(quads,lambda c:min(c,tuple(i for i in range(8) if i not in c)),p)
 sig=tuple((counts(odd,n),counts(even,n)) for n in range(1,4))
 records.append((pt,odd,even,sig))
print('PARTS',len(records))
for n in range(1,4):
 dd=collections.defaultdict(list)
 for part,o,e,sig in records:dd[sig[:n]].append(part)
 print('DEGREE',n,'distinct',len(dd),'collisions',[x for x in dd.values() if len(x)>1])
for part,o,e,sig in records:print(part,sig)
