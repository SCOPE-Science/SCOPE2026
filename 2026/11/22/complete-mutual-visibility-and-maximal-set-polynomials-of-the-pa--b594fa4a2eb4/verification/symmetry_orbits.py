from collections import Counter

# Vertices: 0..8 are points P(x,y); 9..17 are lines L(m,b), all over F_3.
facets = [int(s) for s in open('maximal_sets.txt', encoding='utf-8')]
affine=[]
for a in (1,2):
 for c in (1,2):
  for b in range(3):
   for d in range(3):
    for e in range(3):
     p=[0]*18
     for x in range(3):
      for y in range(3):p[3*x+y]=3*((a*x+b)%3)+(c*y+d*x+e)%3
     for m in range(3):
      for t in range(3):
       mp=((c*m+d)*a)%3
       tp=(c*t+e-mp*b)%3
       p[9+3*m+t]=9+3*mp+tp
     affine.append(tuple(p))
assert len(set(affine))==108
# Incidence-reversing polarity: P(x,y) <-> L(x,-y).
dual=[0]*18
for x in range(3):
 for y in range(3): dual[3*x+y]=9+3*x+(-y)%3
for m in range(3):
 for t in range(3):dual[9+3*m+t]=3*m+(-t)%3
perms=set(affine)|{tuple(dual[p[i]] for i in range(18)) for p in affine}
assert len(perms)==216
# Directly certify all transformations preserve the graph edge relation.
edges={(i,j) for x in range(3) for y in range(3) for m in range(3) for t in range(3) if y==(m*x+t)%3 for i,j in [(3*x+y,9+3*m+t)]}
for p in perms:
 assert {tuple(sorted((p[i],p[j]))) for i,j in edges}==edges

def act(s,p):
 out=0
 while s:
  b=s&-s;s-=b;out|=1<<p[b.bit_length()-1]
 return out
print('automorphisms',len(perms),'facet_count',len(facets))
for k in (6,7,8):
 remaining={s for s in facets if s.bit_count()==k}
 orbits=[]
 while remaining:
  rep=min(remaining);orbit={act(rep,p) for p in perms}
  assert orbit<=remaining,(k,rep,len(orbit))
  remaining-=orbit
  orbits.append((len(orbit),rep))
 print('facet',k,'orbits',len(orbits),'sizes',dict(sorted(Counter(x[0] for x in orbits).items())))
 if k in (6,8):
  for sz,rep in sorted(orbits):
   names=['P%d%d'%(i//3,i%3) if i<9 else 'L%d%d'%((i-9)//3,(i-9)%3) for i in range(18) if rep>>i&1]
   print(' representative',k,sz,rep,names)
