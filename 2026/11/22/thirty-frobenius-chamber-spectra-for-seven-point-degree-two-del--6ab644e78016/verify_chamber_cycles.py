from itertools import combinations
from collections import Counter
import json
from pathlib import Path
V=[]
for i in range(7): V.append((0,tuple(-int(j==i) for j in range(7))))
for z in combinations(range(7),2):V.append((1,tuple(int(j in z) for j in range(7))))
for z in combinations(range(7),5):V.append((2,tuple(int(j in z) for j in range(7))))
for i in range(7):V.append((3,tuple(2 if j==i else 1 for j in range(7))))
I={v:i for i,v in enumerate(V)}
J=[I[(3-d,tuple(1-x for x in m))] for d,m in V]
adj=[0]*56
for i,(d,m) in enumerate(V):
 for j,(e,n) in enumerate(V):
  if i!=j and d*e-sum(x*y for x,y in zip(m,n))==0:adj[i]|=1<<j
sets=[0]
def dfs(mask,tail):
 while tail:
  bit=tail&-tail;tail^=bit
  s=mask|bit;sets.append(s)
  dfs(s,tail&adj[bit.bit_length()-1])
dfs(0,(1<<56)-1)
assert len(sets)==33645

def partitions(n,upper=None):
 if not n:yield ()
 else:
  for x in range(min(n,upper or n),0,-1):
   for p in partitions(n-x,x):yield (x,)+p

def get_sigma(p):
 s=list(range(7));start=0
 for n in p:
  for k in range(n):s[start+k]=start+(k+1)%n
  start+=n
 return s

def curve_perm(p,twist):
 s=get_sigma(p)
 perm=[]
 for d,m in V:
  n=[0]*7
  for i,v in enumerate(m):n[s[i]]=v
  t=I[(d,tuple(n))]
  perm.append(J[t] if twist else t)
 return perm

def act(mask,perm):
 y=0
 while mask:
  b=mask&-mask;mask^=b
  y|=1<<perm[b.bit_length()-1]
 return y

def spectra(p,twist):
 pi=curve_perm(p,twist)
 visited=set();cycle=Counter();poly=Counter()
 for S in sets:
  if S in visited:continue
  T=S;length=0
  while T not in visited:
   visited.add(T);length+=1;T=act(T,pi)
  assert T==S
  cycle[length]+=1
  if length==1:poly[S.bit_count()]+=1
 assert sum(k*v for k,v in cycle.items())==33645
 return (dict(sorted(cycle.items())),[poly[i] for i in range(8)])

out={}
for p in partitions(7):
 key=','.join(map(str,p));out[key]={}
 for twist in (0,1):
  cyc,poly=spectra(p,twist)
  out[key]['geiser' if twist else 'ordinary']={'fixed':sum(poly),'support_by_size':poly,'cycle_spectrum':cyc}
  print(key,twist,'fixed=',sum(poly),'cycles=',cyc,'poly=',poly,flush=True)
expected=json.loads(Path(__file__).with_name('CHAMBER_SPECTRA.json').read_text(encoding='utf-8'))
for label,types in out.items():
    for twist_name,data in types.items():
        assert data=={ 'fixed':expected[label][twist_name]['fixed'],
                       'support_by_size':expected[label][twist_name]['support_by_size'],
                       'cycle_spectrum':{int(k):n for k,n in expected[label][twist_name]['cycle_spectrum'].items()} }
print('DIRECT_33645_SUPPORT_PERMUTATION_30_CASES_OK')
