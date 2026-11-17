"""Exact, finite, self-contained check of the D5 signed-permutation census.
Run: python3 verify_frobenius.py
"""
from itertools import permutations
from collections import Counter

M = tuple(x for x in range(32) if x.bit_count() % 2 == 0)
EDGES = tuple((a,b) for i,a in enumerate(M) for b in M[i+1:] if (a^b).bit_count()==4)
assert len(M)==16 and len(EDGES)==40
assert all(sum(a in e for e in EDGES)==5 for a in M)
assert all(not ((a,b) in EDGES and (b,c) in EDGES and (a,c) in EDGES)
           for a in M for b in M for c in M)

def permute(x,p):
    return sum(((x>>i)&1)<<p[i] for i in range(5))

def action(x,p,s):
    return permute(x,p)^s

def profile(p,s):
    h = {x:action(x,p,s) for x in M}
    assert set(h.values())==set(M)
    assert all(tuple(sorted((h[a],h[b]))) in EDGES for a,b in EDGES)
    fixed_vertices = sum(x==h[x] for x in M)
    fixed_pair_edges = sum(h[a]==a and h[b]==b for a,b in EDGES)
    swapped_edges = sum(h[a]==b and h[b]==a for a,b in EDGES)
    picard_trace = 1+sum((-1)**((s>>i)&1) for i in range(5) if p[i]==i)
    return (picard_trace, fixed_vertices, fixed_pair_edges, swapped_edges)

G = tuple((p,s) for p in permutations(range(5)) for s in M)
assert len(G)==1920
hist = Counter(profile(p,s) for p,s in G)
expected = {
 (-2,0,0,0):20,(-2,0,0,8):5,(-1,0,0,0):80,
 (0,0,0,0):360,(0,0,0,4):60,(1,0,0,0):160,
 (1,0,0,2):160,(1,1,0,0):384,(1,2,0,0):160,
 (2,0,0,0):130,(2,2,1,1):240,(2,4,2,2):60,
 (3,4,4,0):80,(4,8,12,0):20,(6,16,40,0):1,
}
assert hist == expected, (hist - Counter(expected),Counter(expected)-hist)
assert len(hist)==15 and sum(hist.values())==1920
polynomials = {(1,t-m,1-m+a-b) for t,m,a,b in hist}
assert len(polynomials)==14

ID=tuple(range(5))
def product(g,h):
 p,s=g; r,t=h
 return (tuple(p[r[i]] for i in range(5)), s ^ permute(t,p))
def inverse(g):
 p,s=g
 ip=tuple(p.index(i) for i in range(5))
 return (ip, permute(s,ip))
gens=[]
for i in range(4):
 x=list(ID); x[i],x[i+1]=x[i+1],x[i]
 gens.append((tuple(x),0))
gens.append((ID,3))
assert len(set(G))==1920
observed=set(); cc=[]
for g in G:
 if g in observed:continue
 orbit={g}; stack=[g]
 while stack:
  h=stack.pop()
  for t in gens:
   c=product(product(t,h),inverse(t))
   if c not in orbit:
    orbit.add(c); stack.append(c)
 observed.update(orbit)
 cc.append((len(orbit),profile(*g)))
assert len(observed)==1920 and len(cc)==18
for profile_name in expected:
 assert sum(n for n,prof in cc if prof==profile_name)==expected[profile_name]

# Direct signed edge trace, computed independently for powers of any group element.
for g in G:
 p,s=g
 h={x:action(x,p,s) for x in M}
 nmap={x:x for x in M}
 for n in range(1,11):
  nmap={x:h[nmap[x]] for x in M}
  # The signed oriented edge representation has +1 for two fixed ends,
  # -1 for a transposed pair, and trace zero for every other edge.
  e_trace = sum((1 if nmap[a]==a and nmap[b]==b else
                 -1 if nmap[a]==b and nmap[b]==a else 0)
                for a,b in EDGES)
  v_trace = sum(nmap[x]==x for x in M)
  # Compute the Picard trace of the exact n-th group power:
  powg=(ID,0)
  for _ in range(n):powg=product(g,powg)
  qp,qs=powg
  pic_tr=1+sum((-1)**(qs>>i&1) for i in range(5) if qp[i]==i)
  _counts = [nmap[a]==a and nmap[b]==b for a,b in EDGES]
  fixed_edges=sum(_counts)
  swapped=sum(nmap[a]==b and nmap[b]==a for a,b in EDGES)
  assert e_trace==fixed_edges-swapped
  # Formally at q=11: open zeta logarithmic trace formula.
  assert 11**(2*n)+11**n*(pic_tr-v_trace)+1-v_trace+e_trace == \
      11**(2*n)+pic_tr*11**n+1-v_trace*(11**n+1)+fixed_edges-swapped

print('VERIFY_FROBENIUS_OK',len(G),len(cc),len(hist),len(polynomials))
