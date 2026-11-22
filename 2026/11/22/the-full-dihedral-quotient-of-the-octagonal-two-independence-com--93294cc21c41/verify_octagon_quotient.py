import time,collections

def make(n,k,dihedral=True):
 groups=[[((e*i+a)%n) for i in range(n)] for a in range(n) for e in ([1,-1] if dihedral else [1])]
 faces=[m for m in range(1,1<<n) if all((m & sum(1<<((i+j)%n) for j in range(k)))!=sum(1<<((i+j)%n) for j in range(k)) for i in range(n))]
 acts={m:tuple(sum(1<<g[i] for i in range(n) if m>>i&1) for g in groups) for m in faces}
 def canon(ch):return min(tuple(acts[m][g] for m in ch) for g in range(len(groups)))
 cells=[sorted({canon((m,)) for m in faces})]
 for d in range(1,max(m.bit_count() for m in faces)):
  new=set()
  for ch in cells[-1]:
   tip=ch[-1]
   for m in faces:
    if m!=tip and tip&m==tip:new.add(canon(ch+(m,)))
  if not new:break
  cells.append(sorted(new))
 ix=[{c:(d,i) for i,c in enumerate(level)} for d,level in enumerate(cells)]
 bd={}
 for d in range(1,len(cells)):
  for ch in cells[d]:
   dic=collections.defaultdict(int)
   for j in range(d+1):dic[ix[d-1][canon(ch[:j]+ch[j+1:])]]+=(-1)**j
   bd[ix[d][ch]]={k:v for k,v in dic.items() if v}
 return cells,bd

def cancel(cells,bd):
 alive=[{(d,i) for i in range(len(level))} for d,level in enumerate(cells)]
 steps=[]; t=time.monotonic()
 while True:
  pivot=None
  # prefer unique incident row
  for d in range(len(cells)-1,0,-1):
   lower=collections.defaultdict(list)
   for x in alive[d]:
    for y,a in bd.get(x,{}).items():
     if abs(a)==1:lower[y].append(x)
   for y,upp in lower.items():
    if len(upp)==1:
     pivot=(upp[0],y);break
   if pivot:break
  if not pivot:
   for d in range(len(cells)-1,0,-1):
    for x in alive[d]:
     for y,a in bd.get(x,{}).items():
      if abs(a)==1:pivot=(x,y);break
     if pivot:break
    if pivot:break
  if not pivot:break
  x,y=pivot; d=x[0];p=bd[x][y];dict_x=bd[x].copy()
  for z in alive[d]-{x}:
   q=bd.get(z,{}).get(y,0)
   if not q:continue
   for a,v in dict_x.items():
    val=bd[z].get(a,0)-q//p*v
    if val:bd[z][a]=val
    else:bd[z].pop(a,None)
  alive[d].remove(x);alive[d-1].remove(y);bd.pop(x,None);bd.pop(y,None)
  if d+1<len(cells):
   for w in alive[d+1]:bd[w].pop(x,None)
  steps.append((x,y,p))
  if len(steps)%100==0:print('cancelled',len(steps),'alive',[len(a) for a in alive],'sec',round(time.monotonic()-t,2),flush=True)
 print('DONE steps',len(steps),'alive',[len(a) for a in alive],'sec',round(time.monotonic()-t,2))
 for d in range(1,len(cells)):
  for x in alive[d]:
   if bd.get(x):print('NONZERO',x,bd[x])
 return alive,steps,bd

def verify():
 cells,bd=make(8,3,True)
 assert [len(level) for level in cells]==[15,81,183,177,60]
 for x,terms in bd.items():
  for y,a in terms.items():
   if y[0]:
    for z,b in bd[y].items():
     pass
  comp=collections.defaultdict(int)
  for y,a in terms.items():
   for z,b in bd.get(y,{}).items(): comp[z]+=a*b
  assert not any(comp.values()),('boundary_squared',x)
 alive,steps,reduced=cancel(cells,bd)
 assert len(steps)==257
 assert [len(a) for a in alive]==[1,0,0,1,0]
 assert all(not reduced.get(x) for level in alive for x in level)
 print('OCTAGON_DIHEDRAL_QUOTIENT_INTEGRAL_HOMOLOGY_OK')

if __name__=='__main__':verify()
