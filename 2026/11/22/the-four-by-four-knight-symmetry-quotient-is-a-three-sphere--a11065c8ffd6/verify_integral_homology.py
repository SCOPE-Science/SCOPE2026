from collections import Counter
f=open('quotient_reduced.txt');dim=int(next(f));sizes=[int(next(f)) for _ in range(dim)]
B=[{} for _ in range(dim)]
for d in range(1,dim):
 for c in range(sizes[d]):
  a=list(map(int,next(f).split()))
  B[d][c]={a[j+1]:a[j+2] for j in range(0,2*a[0],2)}
active=[set(range(n)) for n in sizes]
print('sizes',sizes,flush=True)
for d in range(1,dim-1):
 for c, col in B[d+1].items():
  dd=Counter()
  for r,coeff in col.items():
   for s,v in B[d][r].items():dd[s]+=coeff*v
  assert all(v==0 for v in dd.values()), (d,c,dd)
print('all boundary compositions zero')
def check():
 for d in range(1,dim-1):
  for c,col in B[d+1].items():
   dd=Counter()
   for r,coeff in col.items():
    for s,v in B[d][r].items():dd[s]+=coeff*v
   assert all(v==0 for v in dd.values()),(d,c,dd)
count=Counter()
for d in range(1,dim):
 while True:
  pivot=next(((r,c,v) for c,col in B[d].items() for r,v in col.items() if abs(v)==1),None)
  if not pivot:break
  r,c,p=pivot
  pc=B[d].pop(c)
  for cc, col in B[d].items():
   v=col.pop(r,0)
   if v:
    for row,w in pc.items():
     if row==r:continue
     col[row]=col.get(row,0)-p*v*w
     if col[row]==0:del col[row]
  active[d-1].remove(r);active[d].remove(c)
  if d+1<dim:
   for col in B[d+1].values():col.pop(c,None)
  if d-1>=1:B[d-1].pop(r)
  count[d]+=1
 print('after',d,'cancel',count[d], 'surv',list(map(len,active)),flush=True)
 check()
print('final remaining sizes',list(map(len,active)), 'unit cancellations',count)
assert list(map(len,active))==[1,0,0,1,0,0,0,0]
assert dict(count)=={1:21,2:81,3:79}
assert all(not col for d in range(1,dim) for col in B[d].values())
print('KNIGHT4_D4_INTEGRAL_HOMOLOGY_OK',dict(count))
