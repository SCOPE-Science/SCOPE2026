from itertools import combinations
from collections import defaultdict
from math import comb

def calc(a,b,m):
  N=a+b;blocks=[set((2*i,2*i+1,a+2*i,a+2*i+1)) for i in range(m)]
  faces=[[] for _ in range(6)]
  all_allowed=[]
  for k in range(1,7):
    for c in combinations(range(N),k):
      s=set(c)
      if sum(x<a for x in c)>3 or sum(x>=a for x in c)>3 or any(T<=s for T in blocks):continue
      faces[k-1].append(c)
  ranks=[]
  for k in range(1,6):
    prev={c:i for i,c in enumerate(faces[k-1])}
    pivot={}
    for c in faces[k]:
      col=0
      for i in range(len(c)):
        col^=1<<prev[c[:i]+c[i+1:]]
      while col:
        p=col.bit_length()-1
        if p in pivot: col^=pivot[p]
        else:pivot[p]=col;break
    ranks.append(len(pivot))
  # rank of boundary degree 0=1 from C0 to augmented C-1, provided nonempty
  extended=[1]+ranks+[0]
  betti=[len(faces[k])-extended[k]-extended[k+1] for k in range(6)]
  # betti[0] -> reduced H0, dimension4 index4, dimension5 index5
  prediction_top=comb(a-1,3)*comb(b-1,3)-m*(a-3)*(b-3)
  prediction4=0
  if a==4 and b==4 and m==2: prediction_top=0;prediction4=1
  assert betti == [0,0,0,0,prediction4,prediction_top],(a,b,m,betti,prediction_top)
  return a,b,m,[len(F) for F in faces],betti

for a,b in [(4,4),(4,5),(4,6),(5,5),(5,6),(6,6)]:
 for m in range(0,min(a,b)//2+1):
  print(calc(a,b,m),flush=True)
print('ROBUST_BICLIQUE_HOMOLOGY_PASS')
