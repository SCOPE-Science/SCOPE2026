"""Independent incidence-hitting check of optimal Shrikhande identifying codes.

Uses constraints N[v] and symmetric differences N[u] Delta N[v] instead of
checking signature collisions. Verifies all templates and exchanges directly.
"""
from itertools import combinations
from collections import Counter
V = range(16)
STEPS = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
def to_i(p): return 4*(p[0]%4)+(p[1]%4)
def to_p(i):return divmod(i,4)
def nmask(i):
    x,y=to_p(i)
    return sum(1<<to_i((x+dx,y+dy)) for dx,dy in STEPS) | (1<<i)
N=[nmask(i) for i in V]
CSTR = N + [N[i]^N[j] for i,j in combinations(V,2)]
assert len(CSTR)==136

def valid(m):return all(m&t for t in CSTR)

all4=[sum(1<<x for x in s) for s in combinations(V,4)]
assert not any(valid(m) for m in all4)
all5={sum(1<<x for x in s) for s in combinations(V,5) if valid(sum(1<<x for x in s))}
assert len(all5)==96

def parity_coset(x):
 a,b=to_p(x)
 return {to_i((a+2*i,b+2*j)) for i in (0,1) for j in (0,1)}

def neighbors(x):return {v for v in V if v!=x and (N[x]>>v)&1}

def connected(a,b):return bool((N[a]>>b)&1) and a!=b

families={}
for x in V:
 core=parity_coset(x)-{x}
 nn=neighbors(x)
 edges=[(a,b) for a,b in combinations(sorted(nn),2) if connected(a,b)]
 assert len(edges)==6
 local_deg=Counter(v for a,b in edges for v in (a,b))
 assert set(local_deg)==nn and set(local_deg.values())=={2}
 fam={sum(1<<v for v in (core|{a,b})) for a,b in edges}
 assert len(fam)==6
 assert all(valid(m) for m in fam)
 families[x]=fam
assert len(set.union(*families.values()))==96
assert set.union(*families.values())==all5
for x,codes in families.items():
 for m in codes:
  # The only one-token neighbors belong to the same six-code component.
  candidates={k for k in all5 if (m^k).bit_count()==2}
  expected={k for k in codes if k!=m and (m^k).bit_count()==2}
  assert candidates==expected and len(candidates)==2
 assert sum((a^b).bit_count()==2 for a,b in combinations(codes,2))==6
# Characteristic root 0 sample set for manual replay.
x=0; c=sorted(families[x]); print('CHECK_STRUCTURAL_OK')
print('hitting_constraints',len(CSTR),'four_checked',len(all4),'five_checked',4368)
print('accepted',len(all5),'families',len(families),'each_family_size',len(c))
print('component_root_0_core',sorted(parity_coset(0)-{0}))
print('component_root_0_codes', [sorted(v for v in V if m>>v&1) for m in c])
print('exchange_graph','16*C6', 'code_count',len(all5),'edge_count',96)
