from itertools import combinations
from collections import Counter
N=49
def mul(x,y):
 a,b=x%7,x//7;c,d=y%7,y//7
 return ((a*c-b*d)%7)+7*((a*d+b*c)%7)
def sub(x,y):return ((x%7-y%7)%7)+7*((x//7-y//7)%7)
def add(x,y):return ((x%7+y%7)%7)+7*((x//7+y//7)%7)
# Independent field-norm square criterion: Norm(a+bi)=a*a+b*b (mod 7).
def is_square(x):
 a,b=x%7,x//7
 return x!=0 and (a*a+b*b)%7 in {1,2,4}
sq={i for i in range(1,N) if is_square(i)}
adj=[[int(is_square(sub(a,b))) for b in range(N)]for a in range(N)]
assert len(sq)==24
assert all(sum(row)==24 for row in adj)
def shattered(s):
 k=len(s); seen=set()
 for c in range(N):
  seen.add(sum(adj[c][x]<<j for j,x in enumerate(s)))
  if len(seen)==1<<k:return True
 return False
anchors={s for tail in combinations(range(1,N),4) if shattered(s:=(0,)+tail)}
print('anchored',len(anchors))
def transforms(s):
 for conj in (False,True):
  v=[x%7+7*((-(x//7))%7) if conj else x for x in s]
  for m in sq:
   w=[mul(m,x) for x in v]
   for x in w:
    yield tuple(sorted(sub(y,x) for y in w))
unseen=set(anchors);classes=[]
while unseen:
 r=min(unseen)
 orbit=set(transforms(r))
 assert orbit<=anchors, (len(orbit),len(orbit-anchors))
 classes.append((r,len(orbit),49*len(orbit)//5))
 unseen-=orbit
print('classes',classes,'total',sum(t[2] for t in classes))
# counts of five-extension degrees of anchored 4 supports:
a4={s for tail in combinations(range(1,N),3) if shattered(s:=(0,)+tail)}
print('a4',len(a4))
# for each anchored 4-support, candidate fifth among all vertices
mult=Counter();shat4=[]
for s in a4:
 degree=sum(shattered(tuple(sorted(s+(x,)))) for x in range(49) if x not in s)
 mult[degree]+=1
 if degree>0:shat4.append(s)
print('4extensiondegree',sorted(mult.items()))
print('4facet_total',49*mult[0]//4)

assert len(anchors)==480
assert sorted([v[1] for v in classes])==[240,240]
assert sum(v[2] for v in classes)==4704
assert sorted(mult.items())==[(0,15360),(2,960)]
print("INDEPENDENT_NORM_ORBIT_CHECKS_PASS")
