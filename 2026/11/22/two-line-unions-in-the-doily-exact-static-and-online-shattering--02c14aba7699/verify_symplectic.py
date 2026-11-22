"""Independent GF(2) symplectic realization of the doily; exhaustive VC faces and online dimension."""
from itertools import combinations
from functools import lru_cache
from collections import Counter
V=range(1,16)
def pairing(x,y):
  return (((x>>0&1)*(y>>2&1))^((x>>2&1)*(y>>0&1))^((x>>1&1)*(y>>3&1))^((x>>3&1)*(y>>1&1)))
L=sorted({sum(1<<(w-1) for w in (u,v,u^v)) for u,v in combinations(V,2) if pairing(u,v)==0})
assert len(L)==15 and all(x.bit_count()==3 for x in L)
C=sorted({u|v for u,v in combinations(L,2)})
assert len(C)==105
face={k:[] for k in range(5)}
for s in range(1<<15):
 if s.bit_count()>4: continue
 if len({s&c for c in C})==1<<s.bit_count():face[s.bit_count()].append(s)
assert list(map(len,face.values()))==[1,15,105,375,495]
fac3=sum(1 for s in face[3] if not any(s&t==s for t in face[4]))
assert fac3==15
assert not any(len({s&c for c in C})==32 for s in range(1<<15) if s.bit_count()==5)
def rank(cols):
 piv={}
 for x in cols:
  while x:
   j=x.bit_length()-1
   if j in piv:x^=piv[j]
   else:piv[j]=x;break
 return len(piv)
r={}
for k in (2,3,4):
 ind={f:i for i,f in enumerate(face[k-1])}
 r[k-1]=rank([sum(1<<ind[f^(1<<i)] for i in range(15) if f>>i&1) for f in face[k]])
assert r=={1:14,2:91,3:269},r
assert [len(face[1])-1-r[1],len(face[2])-r[1]-r[2],len(face[3])-r[2]-r[3],len(face[4])-r[3]]==[0,0,15,226]
inc=[sum(1<<j for j,c in enumerate(C) if c>>i&1) for i in range(15)]
@lru_cache(None)
def depth(cset):
 d=0
 for i in inc:
  a=cset&i;b=cset^a
  if a and b:d=max(d,1+min(depth(a),depth(b)))
 return d
assert depth((1<<len(C))-1)==5
print('PASS: GF2 symplectic 15 lines, 105 concepts; face polynomial 1+15z+105z^2+375z^3+495z^4; 15 triangular facets; Betti (0,0,15,226); Ldim 5; states',depth.cache_info().currsize)
# Check a concrete complete adaptive depth-five witness, independent of the DP lower bound.
import json
from pathlib import Path
artifact=json.loads((Path(__file__).resolve().parent/'depth5_tree.json').read_text())
assert artifact['depth']==5
seen=[]
def verify_witness(node,h,d):
    if d==0:
        i=node['leaf_concept_index']
        assert h&(1<<i)
        seen.append(i)
        return
    i=node['query_point']-1
    assert 0<=i<15
    a=h&inc[i];b=h^a
    assert a and b
    verify_witness(node['zero'],b,d-1)
    verify_witness(node['one'],a,d-1)
verify_witness(artifact['tree'],(1<<len(C))-1,5)
assert len(seen)==32 and len(set(seen))==32
print('PASS: explicit depth-five tree, 31 internal nodes, 32 distinct consistent leaf hypotheses')
