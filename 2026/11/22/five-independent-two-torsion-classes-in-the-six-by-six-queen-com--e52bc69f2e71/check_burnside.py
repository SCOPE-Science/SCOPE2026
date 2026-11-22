#!/usr/bin/env python3
"""Independent enumeration/Burnside consistency test for a square-board queen complex."""
from collections import Counter
from itertools import combinations,permutations
N=6
faces=set()
for q in range(1,N+1):
 for rows in combinations(range(N),q):
  for columns in permutations(range(N),q):
   if len({r-c for r,c in zip(rows,columns)})<q:continue
   if len({r+c for r,c in zip(rows,columns)})<q:continue
   faces.add(sum(1<<(N*r+c) for r,c in zip(rows,columns)))
assert len(faces)==2634
by_size=Counter(f.bit_count() for f in faces)
assert [by_size[k] for k in range(1,7)]==[36,340,1024,982,248,4]
# D4 acts independently on all face masks.
squares=[(i,j) for i in range(N) for j in range(N)]
actions=[]
for transpose in [False,True]:
 for k in range(4):
  def g(i,j):
   if transpose:i,j=j,i
   for _ in range(k):i,j=j,N-1-i
   return i,j
  actions.append(tuple(squares.index(g(*p)) for p in squares))
assert len(set(actions))==8
fixed=[]
for a in actions:
 F=set()
 for f in faces:
  v=sum(1<<a[k] for k in range(36) if f>>k&1)
  if v==f:F.add(f)
 fixed.append(F)
# A flag fixed by an action iff every constituent face is fixed.
# Count all fixed flags recursively by strictly extending a chain.
counts=[]
for face_set in fixed:
 sup={f:[] for f in face_set}
 for x in face_set:
  sup[x]=[y for y in face_set if x!=y and (x&y)==x]
 levels=Counter()
 def explore(f,depth):
  levels[depth]+=1
  for y in sup[f]:explore(y,depth+1)
 for x in face_set:explore(x,1)
 counts.append(levels)
quot=[sum(c[k] for c in counts)//8 for k in range(1,7)]
assert all(sum(c[k] for c in counts)%8==0 for k in range(1,7))
assert quot==[337,3541,10110,11166,4620,360]
print('BURNSIDE_QUEENS6_D4_OK')
print('fixed face counts:',[len(x) for x in fixed])
print('fixed flag counts:',[[c[k] for k in range(1,7)] for c in counts])
print('quotient cell counts:',quot)
