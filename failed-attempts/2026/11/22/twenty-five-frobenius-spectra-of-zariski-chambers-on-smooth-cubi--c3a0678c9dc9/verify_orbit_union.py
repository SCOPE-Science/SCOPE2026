"""Independent orbit-union/Burnside verification of Weyl-action chamber data."""
import json, itertools, collections
from pathlib import Path
p=Path(__file__).with_name('e6_spectra.json')
results=json.loads(p.read_text(encoding='utf-8'))['classes']
L=[]
for i in range(6):
 m=[0]*6;m[i]=-1;L.append((0,*m))
for i,j in itertools.combinations(range(6),2):
 m=[0]*6;m[i]=m[j]=1;L.append((1,*m))
for absent in range(6):
 m=[int(i!=absent) for i in range(6)];L.append((2,*m))

def inc(a,b):return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))
def cycles(p):
 seen=set();orbs=[]
 for i in range(27):
  if i in seen:continue
  v=[];j=i
  while j not in seen:
   seen.add(j);v.append(j);j=p[j]
  orbs.append(v)
 return orbs

def fixed(p):
 orbs=cycles(p)
 ok=[i for i,v in enumerate(orbs) if all(inc(L[x],L[y])==0 for x,y in itertools.combinations(v,2))]
 graph={i:[j for j in ok if j>i and all(inc(L[x],L[y])==0 for x in orbs[i] for y in orbs[j])] for i in ok}
 counts=collections.Counter({0:1})
 def enumerate_sets(chosen,candidates,total):
  for pos,i in enumerate(candidates):
   n=total+len(orbs[i]);counts[n]+=1
   enumerate_sets(chosen+[i],[j for j in candidates[pos+1:] if j in graph[i]],n)
 enumerate_sets([],ok,0)
 return sum(counts.values()),dict(counts)

def power(p,d):
 q=tuple(range(27))
 for _ in range(d):q=tuple(p[q[i]] for i in range(27))
 return q
for r in results:
 p=bytes.fromhex(r['rep']);m=r['order'];c={int(k):v for k,v in r['chamber_cycles'].items()}
 for d in range(1,m+1):
  f,weights=fixed(power(p,d));expected=sum(l*v for l,v in c.items() if d%l==0)
  assert f==expected,(m,d,f,expected)
 assert fixed(p)[0]==r['fixed']
print('INDEPENDENT_FIXED_ORBIT_UNION_CHECK_PASS', len(results),'classes; all powers checked')
print('BURNSIDE_PASS', sum(r['class_size']*r['fixed'] for r in results), 'equals',8*51840)
assert sum(r['class_size']*r['fixed'] for r in results)==8*51840
print('W_E6_ORBIT_UNION_INDEPENDENT_CHECK_OK')
