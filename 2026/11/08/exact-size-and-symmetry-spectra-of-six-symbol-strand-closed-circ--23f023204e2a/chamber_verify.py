"""Independent signed-order extension enumeration and Burnside orbit census.
Run: python3 chamber_verify.py
"""
from itertools import permutations,product
from collections import Counter

def run(m, orbit_census=True):
 q=2*m
 c=lambda x:x^1
 full=(1<<q)-1
 chambers=[]
 for perm in permutations(range(m)):
  for flips in product((0,1),repeat=m):
   first=[2*perm[i]+flips[i] for i in range(m)]
   chambers.append(first+[c(v) for v in reversed(first)])
 assert len(chambers)==2**m*__import__('math').factorial(m)
 code_masks=set()
 for order in chambers:
  ranks={v:i for i,v in enumerate(order)}
  arcs={(u,v) for u in range(q) for v in range(q) if ranks[u]<ranks[v]}
  groups=[]
  used=set()
  for e in sorted(arcs):
   if e in used:continue
   mate=(c(e[1]),c(e[0]))
   assert mate in arcs
   group={e,mate};used.update(group)
   groups.append(sum(1<<(q*u+v) for u,v in group))
  assert len(groups)==m*m
  for bits in range(1<<len(groups)):
   mask=0
   for k,group in enumerate(groups):
    if bits>>k&1:mask|=group
   code_masks.add(mask)
 def weight(z):return z.bit_count()
 hist=Counter(map(weight,code_masks))
 if orbit_census:
  # Burnside, not a canonicalization-orbit traversal.
  group_perms=[]
  for perm in permutations(range(m)):
   for flips in product((0,1),repeat=m):
    group_perms.append([2*perm[u//2]+((u%2)^flips[u//2]) for u in range(q)])
  fixed_sum=Counter()
  for g in group_perms:
   moved=[]
   for u in range(q):
    for v in range(q):
     moved.append((1<<(q*u+v),1<<(q*g[u]+g[v])))
   for mask in code_masks:
    mapped=0
    for source,dest in moved:
     if mask & source:mapped|=dest
    if mapped==mask:fixed_sum[weight(mask)]+=1
  orbits={k:fixed_sum[k]//len(group_perms) for k in hist}
  assert all(fixed_sum[k]%len(group_perms)==0 for k in hist)
  print('CHAMBER_BURNSIDE_VERIFY_OK',m,len(code_masks),sum(orbits.values()))
  print('HIST', [hist[k] for k in range(q*(q-1)//2+1)])
  print('ORBIT', [orbits.get(k,0) for k in range(q*(q-1)//2+1)])
 else:print('CHAMBER_VERIFY_OK',m,len(code_masks),list(sorted(hist.items())))

run(1,False)
run(2,False)
run(3,True)
