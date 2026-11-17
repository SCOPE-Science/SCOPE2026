from itertools import product
from collections import Counter, defaultdict
from functools import lru_cache

q=4
V=list(product(range(q),repeat=3));idx={a:i for i,a in enumerate(V)}; N=len(V)
adj=[0]*N
for i,a in enumerate(V):
 for j,b in enumerate(V):
  if i!=j and all(x!=y for x,y in zip(a,b)): adj[i]|=1<<j

def quotient_graph(t):
 perm=[idx[tuple((a[k]+t[k])%4 for k in range(3))] for a in V]
 visited=set();orbs=[]
 for i in range(N):
  if i in visited:continue
  o=[];j=i
  while j not in visited:visited.add(j);o.append(j);j=perm[j]
  orbs.append(o)
 good=[]
 for o in orbs:
  if all(not ((adj[a]>>b)&1) for i,a in enumerate(o) for b in o[i+1:]):good.append(o)
 ne=[0]*len(good)
 for i,o in enumerate(good):
  for j,z in enumerate(good[:i]):
   if any((adj[a]>>b)&1 for a in o for b in z):
    ne[i]|=1<<j;ne[j]|=1<<i
 return ne,len(orbs),len(good)

def Iminus1(ne):
 @lru_cache(None)
 def f(mask):
  if not mask:return 1
  verts=[j for j in range(len(ne)) if mask>>j&1]
  v=max(verts,key=lambda j: (ne[j]&mask).bit_count())
  return f(mask^(1<<v))-f(mask&~((1<<v)|ne[v]))
 return f((1<<len(ne))-1),f.cache_info().currsize

rows=[]
for s in product(range(4),repeat=3):
 ne,o,g=quotient_graph(s)
 val,c=Iminus1(ne)
 rows.append((s,val,o,g,c))
bytype=defaultdict(list)
for s,val,*other in rows:
 tt=tuple(sorted(0 if a==0 else 2 if a==2 else 1 for a in s))
 bytype[tt].append(val)
print('TRANSLATION TRACE TYPES')
for t,v in sorted(bytype.items()):print(t,len(v),set(v))
print('total trace',sum(r[1] for r in rows),'invariant dim',sum(r[1] for r in rows)//64)

# exact gaussian integer in Z[i]
def power_I(exp):return [(1,0),(0,1),(-1,0),(0,-1)][exp%4]
mult={}
for k in product(range(4),repeat=3):
 re=im=0
 for s,tr,*_ in rows:
  r,i=power_I(-sum(a*b for a,b in zip(k,s)))
  re+=tr*r;im+=tr*i
 assert im==0 and re%64==0,(k,re,im)
 mult[k]=re//64
byctype=defaultdict(list)
for k,m in mult.items():
 tt=tuple(sorted(0 if a==0 else 2 if a==2 else 1 for a in k))
 byctype[tt].append(m)
print('CHARACTER MULTIPLICITY TYPES')
for t,v in sorted(byctype.items()):print(t,len(v),set(v))
assert sum(mult.values())==405
assert all(m>=0 for m in mult.values())
print('SUM MULT',sum(mult.values()),'MIN',min(mult.values()),'MAX',max(mult.values()))
print('COUNTER',dict(sorted(Counter(mult.values()).items())))
print('DONE')

# The subgroup of coordinate half-turns has eight elements.
b_trace=sum(tr for s,tr,*_ in rows if all(z in (0,2) for z in s))
assert b_trace==568
print('HALF_TURN_SUBGROUP_INVARIANTS',b_trace//8)
assert sum(tr for _,tr,*_ in rows)==576 and mult[(0,0,0)]==9
want_tr={(0,0,0):405,(0,0,1):9,(0,0,2):9,(0,1,1):-3,(0,1,2):-3,(0,2,2):45,(1,1,1):1,(1,1,2):1,(1,2,2):1,(2,2,2):1}
want_mul={(0,0,0):9,(0,0,1):6,(0,0,2):9,(0,1,1):6,(0,1,2):6,(0,2,2):9,(1,1,1):8,(1,1,2):5,(1,2,2):5,(2,2,2):8}
assert all(next(iter(set(v)))==want_tr[t] for t,v in bytype.items())
assert all(next(iter(set(v)))==want_mul[t] for t,v in byctype.items())
print('QUATERNARY_TRANSLATION_CHARACTER_PASS')
if __name__=='__main__':
 import csv
 with open('translation_character.csv','w',newline='',encoding='utf8') as fw:
  w=csv.writer(fw);w.writerow(['a0','a1','a2','trace_on_H3','chi_a0','chi_a1','chi_a2','multiplicity'])
  for a,tr,*_ in rows:w.writerow([*a,tr,*a,mult[a]])
