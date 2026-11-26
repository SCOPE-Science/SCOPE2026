"""Independent Burnside count of barycentric orbit cells, standard library only."""
from itertools import permutations
from collections import Counter

vertices = [(i,j) for i in range(4) for j in range(4) if j != i]
vid={v:k for k,v in enumerate(vertices)}
# Bit-mask independent set test, separate from face-combinations implementation.
adj=[0]*12
for i,(a,b) in enumerate(vertices):
 for j,(c,d) in enumerate(vertices):
  if i != j and (a==c or (a==d and b==c)):
   adj[i]|=1<<j
faces=[]
for mask in range(1,1<<12):
 if all(not(mask & adj[i]) for i in range(12) if mask&(1<<i)):
  faces.append(mask)
assert len(faces)==162
fcounts=Counter()
for p in permutations(range(4)):
    g=[vid[(p[a],p[b])] for a,b in vertices]
    def move(mask):
      return sum(1<<g[i] for i in range(12) if mask&(1<<i))
    fixed=sorted((f for f in faces if move(f)==f), key=lambda m:m.bit_count())
    # all flags ending at face f; count by length, dynamic programming
    partial={}
    for face in fixed:
      v=[0]*4;v[0]=1
      for smaller in fixed:
        if smaller==face:break
        if smaller&face==smaller:
          for l,c in enumerate(partial[smaller]):
            if l+1<4:v[l+1]+=c
      partial[face]=v
      for l,n in enumerate(v):fcounts[l]+=n
q={l:count//24 for l,count in fcounts.items()}
assert all(n%24==0 for n in fcounts.values())
assert q=={0:11,1:42,2:63,3:30},q
print('BURNSIDE_ORBIT_COUNTS', [q[i] for i in range(4)])
print('BURNSIDE_EULER',sum((-1)**i*q[i] for i in range(4)))
print('BURNSIDE_OK')
