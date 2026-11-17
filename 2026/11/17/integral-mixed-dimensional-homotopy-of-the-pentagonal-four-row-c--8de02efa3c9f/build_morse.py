import json,collections,functools,time
from pathlib import Path
p=Path('complex.txt');f=p.open(); hdr=f.readline().strip(); E=int(hdr.split()[5]); edges=[tuple(map(int,f.readline().split())) for _ in range(E)];assert f.readline().strip()=='critical';crit_counts={};
while 1:
 s=f.readline().strip()
 if s=='masks':break
 d,n=map(int,s.split());crit_counts[d]=n
crit=[]
while 1:
 s=f.readline().strip()
 if s=='pairs':break
 crit.append(int(s))
pairs=[];lower={};upper=set()
for s in f:
 a,b=map(int,s.split());pairs.append((a,b));lower[a]=b;upper.add(b)
f.close();crit_by_dim=collections.defaultdict(list)
for s in crit:crit_by_dim[s.bit_count()-1].append(s)
for d in crit_by_dim:crit_by_dim[d].sort()
print('counts',len(pairs),[(d,len(v)) for d,v in crit_by_dim.items()]);

def boundary(s):
 bits=[];temp=s
 while temp:
  low=temp&-temp;temp-=low;bits.append(low)
 return [(s^low,(-1 if j%2 else 1)) for j,low in enumerate(bits)]

@functools.lru_cache(maxsize=None)
def projection(face):
 if face in critical_set:return {face:1}
 if face in upper:return {}
 if face in lower:
  coface=lower[face]
  missing=coface^face
  j=(coface & (missing-1)).bit_count();sgn=(-1 if j%2 else 1)
  result=collections.defaultdict(int)
  for f,eps in boundary(coface):
   if f==face:continue
   for k,v in projection(f).items():result[k]-=sgn*eps*v
  return {k:v for k,v in result.items() if v}
 raise Exception('unknown face '+str(face))

out={};
for d in [6,7]:
 t=time.monotonic();critical_set=set(crit_by_dim[d-1]);projection.cache_clear();matrix=[]
 for face in crit_by_dim[d]:
  acc=collections.defaultdict(int)
  for sub,eps in boundary(face):
   for k,v in projection(sub).items():acc[k]+=eps*v
  matrix.append([acc.get(sub,0) for sub in crit_by_dim[d-1]])
 print('boundary',d,'shape',len(matrix),len(matrix[0]),'nonzero',sum(bool(x) for row in matrix for x in row),'max coeff',max(abs(x) for row in matrix for x in row),'cache',projection.cache_info(), 'time',time.monotonic()-t, flush=True)
 out[str(d)]={'from':crit_by_dim[d],'to':crit_by_dim[d-1],'rows':matrix}
Path('morse_matrices.json').write_text(json.dumps(out))
