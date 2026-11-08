# Independent simplicial chain ranks, using direct row sparse elimination modulo two primes.
# The generator enumerates faces from the edge disjointness condition, not from any Morse data.
from collections import Counter
E=sorted({tuple(sorted((a,b))) for j in range(6) for a,b in ((j,(j+1)%6),(j,6+j),(6+j,6+(j+2)%6))})
by_dim={i:[] for i in range(6)}
for mask in range(1,1<<18):
 occupied=0;valid=True
 for i,(a,b) in enumerate(E):
  if (mask>>i)&1:
   if (occupied>>a)&1 or (occupied>>b)&1:valid=False;break
   occupied|=(1<<a)|(1<<b)
 if valid:by_dim[mask.bit_count()-1].append(mask)
assert tuple(map(lambda d:len(by_dim[d]),range(6)))==(18,117,334,402,156,10)

def rank(cols, prime):
 pivots={}
 for C in cols:
  col={row:c%prime for row,c in C.items() if c%prime}
  while col:
   k=min(col)
   if k not in pivots:
    ck=col[k]
    inv=pow(ck,-1,prime)
    pivots[k]={j:(v*inv)%prime for j,v in col.items()}
    break
   a=col[k]
   for j,v in pivots[k].items():
    u=(col.get(j,0)-a*v)%prime
    if u:col[j]=u
    else:col.pop(j,None)
 return len(pivots)
for p in (2,3,5):
 rr=[]
 for k in range(1,6):
  ids={mask:i for i,mask in enumerate(by_dim[k-1])}
  cols=[]
  for mask in by_dim[k]:
   col={}
   j=0
   for i in range(18):
    if (mask>>i)&1:
     col[ids[mask^(1<<i)]]=(-1)**j
     j+=1
   cols.append(col)
  rr.append(rank(cols,p))
 assert rr==[17,100,234,146,10],(p,rr)
 print('mod',p,'boundary_ranks',rr,'betti', [1,0,0,22,0,0])
print('DURER_INDEPENDENT_MODULAR_RANKS_PASS')
