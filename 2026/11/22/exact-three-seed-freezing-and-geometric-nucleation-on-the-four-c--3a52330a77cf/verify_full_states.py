"""Independent full-state check of exact orbit absorption probabilities on Q4.

Run: python3 verify_full_states.py q4_certificate.json
Requires Python 3, NumPy, SciPy.
"""
import json,sys,collections,math,time
from fractions import Fraction
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
T=time.monotonic()
file=sys.argv[1]
cert=json.load(open(file))
assert len(cert['orbits'])==222
# Independently derive 16-bit cube automorphism orbits by explicit maps
U=65535
base=[[i^(1<<k) for i in range(16)] for k in range(4)]
base += [[sum(((i>>j)&1)<< (j+1 if j==k else j-1 if j==k+1 else j) for j in range(4)) for i in range(16)] for k in range(3)]
def transform(v,perm):
 return sum(1<<perm[i] for i in range(16) if v&(1<<i))
group=[-1]*65536
for ix,record in enumerate(cert['orbits']):
 s=record['representative']
 assert group[s]<0,(ix,s)
 q=[s];group[s]=ix
 for m in q:
  for gen in base:
   mm=transform(m,gen)
   if group[mm]==-1:
    group[mm]=ix;q.append(mm)
  mm=m^U
  if group[mm]==-1:
   group[mm]=ix;q.append(mm)
 assert len(q)==record['orbit_size']
assert -1 not in group
prob=[Fraction(x['frozen_numerator'],x['frozen_denominator']) for x in cert['orbits']]
for ix,r in enumerate(cert['orbits']):assert r['orbit_size']>0 and 0<=prob[ix]<=1
indptr=[0];col=[]
absorbing=[]
for state in range(65536):
 choices=[]
 for v in range(16):
  color=(state>>v)&1
  disagree=0
  for k in range(4):
   w=v^(1<<k)
   disagree += ((state>>w)&1)!=color
  if disagree>=2:
   nxt=state^(1<<v)
   choices.append((nxt,2 if disagree>2 else 1))
   col.append(nxt)
 if choices:
  rs=sum(rate for nxt,rate in choices)
  lhs=rs*prob[group[state]]
  rhs=sum((rate*prob[group[nxt]] for nxt,rate in choices),Fraction(0))
  if lhs!=rhs:raise AssertionError(('recurrence-failed',state,lhs,rhs))
 else:
  absorbing.append(state)
  if prob[group[state]] != (Fraction(0) if state in (0,65535) else Fraction(1)):
   raise AssertionError(('terminal-incorrect',state))
 indptr.append(len(col))
assert len(col)<1100000
A=csr_matrix((np.ones(len(col),dtype=np.int8),np.array(col,dtype=np.int32),np.array(indptr,dtype=np.int32)),shape=(65536,65536))
n,lab=connected_components(A,directed=True,connection='strong')
edge_out=np.zeros(n,dtype=bool)
for s in range(65536):
 for j in range(indptr[s],indptr[s+1]):
  if lab[s]!=lab[col[j]]:edge_out[lab[s]]=True
closed=np.where(~edge_out)[0]
closed_states=[tuple(np.flatnonzero(lab==i).tolist()) for i in closed]
assert len(closed_states)==10 and all(len(g)==1 for g in closed_states)
assert set(x[0] for x in closed_states)==set(absorbing)
assert set(absorbing)==set(cert['absorbing_states'])
assert len(absorbing)==10
# independent source geometry enumeration, 3 sites
trip=collections.defaultdict(list)
for state in range(65536):
 if state.bit_count()!=3:continue
 verts=[j for j in range(16) if state>>j&1]
 ds=tuple(sorted((a^b).bit_count() for i,a in enumerate(verts) for b in verts[i+1:]))
 trip[ds].append(state)
assert len(trip)==6
for r in cert['three_seed_classes']:
 key=tuple(r['distances'])
 states=trip[key]
 assert len(states)==r['placements']
 assert len({prob[group[s]] for s in states})==1
 assert prob[group[states[0]]]==Fraction(r['frozen_numerator'],r['frozen_denominator'])
for state in range(65536):
 if state.bit_count()<=2:assert prob[group[state]]==0
# full uniform probability as independent readout
v=sum((prob[group[s]] for s in range(65536)),Fraction(0))/65536
bal=sum((prob[group[s]] for s in range(65536) if s.bit_count()==8),Fraction(0))/math.comb(16,8)
assert [v.numerator,v.denominator]==cert['unbiased_frozen_fraction']
assert [bal.numerator,bal.denominator]==cert['balanced_frozen_fraction']
print('PASS: 65,536 states; 222 orbit fractions; %d transition edges; 10 singleton terminal classes; 6 seed-shape classes.'%len(col))
print('unbiased frozen %.12f; balanced frozen %.12f; elapsed %.1fs'%(float(v),float(bal),time.monotonic()-T))
