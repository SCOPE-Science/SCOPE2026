"""Independent cyclic-orbit certificate of the eleven-cycle mobility result."""
from itertools import combinations
from collections import Counter,deque
import json
N=11
U=frozenset(range(N))
def rot(z,t):return frozenset((i+t)%N for i in z)
def is_independent_step3(z):return all((i+3)%N not in z for i in z)
def triple_free(z):return all(not {i,(i+1)%N,(i+2)%N}.issubset(z) for i in range(N))
def key(z):return ''.join('1' if i in z else '0' for i in range(N))
# Work with the omitted vertices, not closed-neighborhood signatures.
raw=[frozenset(z) for z in combinations(range(N),4) if is_independent_step3(z)]
assert len(raw)==55
classes={};unseen=set(raw)
while unseen:
 z=next(iter(unseen));orbit={rot(z,t) for t in range(N)}
 assert orbit<=unseen;unseen-=orbit
 classes[min(map(key,orbit))]=orbit
assert sorted(classes)==['00001000111','00001010101','00001100011','00001110001','00010100011']
valid={x:all(triple_free(z) for z in orbit) for x,orbit in classes.items()}
assert sum(valid.values())==3 and len(set().union(*(orb for rep,orb in classes.items() if valid[rep])))==33

# Any six-vertex code would omit a size-five independent set in the step-three cycle.
ind5=[frozenset(z) for z in combinations(range(N),5) if is_independent_step3(z)]
assert len(ind5)==11
assert all(not triple_free(z) for z in ind5)

A='00001010101';B='00001100011';C='00010100011'
def parse(s):return frozenset(i for i,c in enumerate(s) if c=='1')
assert all(valid[x] for x in (A,B,C))
def name(z):
 for label,rep in [('A',A),('B',B),('C',C)]:
  base=parse(rep)
  for t in range(N):
   if rot(base,t)==z:return label,t
 raise ValueError('nonoptimal state')

valid_omissions=set().union(*(orb for rep,orb in classes.items() if valid[rep]))
def neighborhood(z,slide):
 code=U-z
 result=set()
 for i in code:
  for j in z:
   if slide and (j-i)%N not in (1,N-1):continue
   newz=(z-{j})|{i}
   if newz in valid_omissions:result.add(name(frozenset(newz)))
 return sorted(result)
sl={lab:neighborhood(parse(rep),True) for lab,rep in [('A',A),('B',B),('C',C)]}
ju={lab:neighborhood(parse(rep),False) for lab,rep in [('A',A),('B',B),('C',C)]}
assert sl=={'A':[],'B':[('C',0),('C',6)],'C':[('B',0),('B',5)]}
assert ju=={'A':[('A',2),('A',9),('C',1),('C',5)],
 'B':[('B',5),('B',6),('C',0),('C',6)],
 'C':[('A',6),('A',10),('B',0),('B',5)]}
# Rotations reproduce the 11 fixed A-states, and the B,C component is a 22-cycle.
# In the jump graph, A rotations are linked by step 2, B rotations by step 5;
# C attaches to both, proving connectedness without BFS.
assert 2%11 and 5%11
report={
 'candidate_size7_omissions':len(raw),
 'step3_independent_size5_omissions':len(ind5),
 'candidate_rotation_orbits':[{ 'zeros':rep,'size':len(orb),'domination_valid':valid[rep] } for rep,orb in sorted(classes.items())],
 'valid_code_count':len(valid_omissions),
 'slide_neighbors_by_orbit_representative':sl,
 'jump_neighbors_by_orbit_representative':ju,
 'deduced_slide_structure':'11 isolated vertices plus one cycle of length 22',
 'deduced_jump_structure':'connected 4-regular graph on 33 vertices'
}
print(json.dumps(report,sort_keys=True,indent=2))
