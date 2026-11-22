#!/usr/bin/env python3
"""Exact Q(sqrt(5)) audit of four-point volumes in the regular icosidodecahedron.

All coordinates are represented in Z[phi], phi^2=phi+1, by pairs (a,b).
The icosahedron has edge length 2; its edge midpoints form the unit-edge
icosidodecahedron. Four-point determinants are calculated in doubled-midpoint
coordinates and converted to physical tetrahedron volume by dividing by 48.
Only the Python standard library is needed.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from functools import cmp_to_key

ZERO=(0,0)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def summ(xs):
 out=ZERO
 for x in xs:out=add(out,x)
 return out
def sign(x):
 # Exact: a+b*phi has the sign of a+b*(1+sqrt(5))/2.
 a,b=x; A=2*a+b
 if b==0:return (a>0)-(a<0)
 if A==0:return (b>0)-(b<0)
 if A>0 and b>0:return 1
 if A<0 and b<0:return -1
 z=A*A-5*b*b
 if z==0:raise AssertionError('irrational root unexpectedly rational')
 return (z>0)-(z<0) if A>0 else (z<0)-(z>0)
def absq(x):return x if sign(x)>=0 else neg(x)
def dot(v,w):return summ(mul(x,y) for x,y in zip(v,w))
def minus(v,w):return tuple(sub(x,y) for x,y in zip(v,w))
def sqdist(v,w):return dot(minus(v,w),minus(v,w))
def cross(v,w):return (sub(mul(v[1],w[2]),mul(v[2],w[1])),sub(mul(v[2],w[0]),mul(v[0],w[2])),sub(mul(v[0],w[1]),mul(v[1],w[0])))
def determinant(a,b,c):return dot(a,cross(b,c))
def determinant_alt(a,b,c):
 # Independently expanded Leibniz formula.
 ix=(0,1,2)
 d=ZERO
 for p in permutations(ix):
  inversions=sum(p[i]>p[j] for i in ix for j in ix if i<j)
  term=mul(mul(a[p[0]],b[p[1]]),c[p[2]])
  d=add(d,term if inversions%2==0 else neg(term))
 return d

def main():
 ico=[]
 for k in range(3):
  for s,t in product((-1,1),repeat=2):
   p=[ZERO]*3
   p[(k+1)%3]=(s,0)
   p[(k+2)%3]=(0,t)
   ico.append(tuple(p))
 assert len(ico)==len(set(ico))==12
 edges=[(i,j) for i,j in combinations(range(12),2) if sqdist(ico[i],ico[j])==(4,0)]
 assert len(edges)==30
 pts=[tuple(add(x,y) for x,y in zip(ico[i],ico[j])) for i,j in edges]
 assert len(pts)==len(set(pts))==30
 assert len({dot(p,p) for p in pts})==1
 assert next(iter({dot(p,p) for p in pts}))==(4,4)  # doubled midpoint radius squared 4 phi^2
 face_triples=[tuple(sorted((i,j,k))) for i,j,k in combinations(range(12),3)
               if all(tuple(sorted(e)) in edges for e in ((i,j),(i,k),(j,k)))]
 assert len(face_triples)==20
 spectra=Counter()
 members=defaultdict(list)
 maximal_candidates=[]
 for indices in combinations(range(30),4):
  p,q,r,s=[pts[i] for i in indices]
  a,b,c=minus(q,p),minus(r,p),minus(s,p)
  d=determinant(a,b,c)
  assert d==determinant_alt(a,b,c)
  val=absq(d)
  spectra[val]+=1
  members[val].append(indices)
 assert sum(spectra.values())==27405
 levels=sorted(spectra,key=cmp_to_key(lambda x,y: -sign(sub(x,y))))
 assert len(levels)==27
 assert (levels[0],spectra[levels[0]])==((28,44),60)
 assert (levels[1],spectra[levels[1]])==((24,40),240)
 assert sub(levels[0],levels[1])==(4,4)
 assert spectra[(0,0)]>0
 maximal=members[levels[0]]
 # For a maximal vertex-supported tetrahedron, inspect all possible
 # replacements of one vertex while fixing the other three.
 options={}
 for ind in maximal:
  nonunique=[]
  for omit in ind:
   anchor=tuple(sorted(i for i in ind if i!=omit))
   a,b,c=[pts[j] for j in anchor]
   high=[]
   for j,p in enumerate(pts):
    d=determinant(minus(b,a),minus(c,a),minus(p,a))
    if absq(d)==levels[0]:high.append(j)
   options[(ind,omit)]=tuple(high)
   if len(high)>1:nonunique.append((omit,tuple(high)))
  assert len(nonunique)==1
  assert len(nonunique[0][1])==3
 # Unique anchor triples indexed by 20 triangular faces; no other anchors
 # have multiple maximizing fourth vertices.
 fam={}
 for ind in maximal:
  for omit in ind:
   choices=options[(ind,omit)]
   if len(choices)==3:
    anchor=tuple(sorted(i for i in ind if i!=omit))
    fam[anchor]=choices
 assert len(fam)==20
 face_edge_sets={tuple(sorted(next(i for i,e in enumerate(edges) if e==tuple(sorted(edge)))
                                  for edge in combinations(face,2))) for face in face_triples}
 assert {tuple(sorted(v)) for v in fam.values()}==face_edge_sets
 # Each maximal tetrahedron is in exactly one three-vertex moving family.
 assert set(maximal)=={tuple(sorted((*anchors,j))) for anchors,tri in fam.items() for j in tri}
 # Build all 120 exact symmetries from ordered oriented icosahedral faces.
 base=face_triples[0]
 base_pts=tuple(ico[i] for i in base)
 def key(v,basis):return tuple(dot(v,w) for w in basis)
 ref_keys=[key(v,base_pts) for v in ico]
 assert len(set(ref_keys))==12
 perms=[]
 for face in face_triples:
  for image_basis in permutations(face):
   basis=tuple(ico[j] for j in image_basis)
   reverse={key(v,basis):i for i,v in enumerate(ico)}
   assert len(reverse)==12
   perm=tuple(reverse[k] for k in ref_keys)
   assert all(sqdist(ico[i],ico[j])==sqdist(ico[perm[i]],ico[perm[j]])
              for i,j in combinations(range(12),2))
   perms.append(perm)
 assert len(set(perms))==120
 edge_index={e:i for i,e in enumerate(edges)}
 orbit=set()
 for pi in perms:
  induced=tuple(edge_index[tuple(sorted((pi[i],pi[j])))] for i,j in edges)
  orbit.add(tuple(sorted(induced[x] for x in maximal[0])))
 assert orbit==set(maximal)
 # The signature of the fixed triangle and moving triangle is constant.
 def sig(inds):return tuple(sorted((sqdist(pts[i],pts[j]) for i,j in combinations(inds,2)),key=cmp_to_key(lambda x,y:sign(sub(x,y)))))
 anchor_sigs={sig(anchor) for anchor in fam}
 free_sigs={sig(tri) for tri in fam.values()}
 assert len(anchor_sigs)==len(free_sigs)==1
 assert free_sigs=={((4,0),(4,0),(4,0))}
 # Exclude any accidental second-level coincidences via exact order.
 assert sign(sub(levels[1],levels[2]))>0
 print('ICOSIDODECAHEDRON_TETRAHEDRA_EXACT_PASS vertices=30 quadruples=27405')
 print('distance_levels=27 maximal_vertex_tetrahedra=60 second_level_tetrahedra=240')
 print('continuous_maximum_families=20 symmetry_order=120 maximal_orbit=60')
 print('top_determinant_doubled=(28,44) second=(24,40) denominator=48')
 print('anchor_squared_distances_doubled', next(iter(anchor_sigs)))
 print('spectrum_a_plus_b_phi_doubled_determinants')
 for v in levels:print(v[0],v[1],spectra[v])
 print('sample_anchor',next(iter(fam.items())))
 return levels,spectra,fam

if __name__=='__main__':main()
