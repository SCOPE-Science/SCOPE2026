#!/usr/bin/env python3
"""Exact, self-contained verification of a finite cut-complex homotopy equivalence.

Only Python standard library; bitmask enumeration, discrete Morse, integer signed boundary.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque
N=12
EDGES=[(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
ORDER=[1,11,6,10,8,3,4,0,9,2,5,7]
ALL=(1<<N)-1
adj=[0]*N
for a,b in EDGES:adj[a]|=1<<b;adj[b]|=1<<a
assert all(a.bit_count()==4 for a in adj)

def connected(s):
 if s==0:return True
 reached=s&-s
 while True:
  nxt=reached
  for v in range(N):
   if (reached>>v)&1:nxt|=adj[v]&s
  if nxt==reached:return nxt==s
  reached=nxt

def all_faces():
 # Test disconnected vertex triples, then downward-close their complements.
 facets={ALL^sum(1<<i for i in t) for t in combinations(range(N),3) if not connected(sum(1<<i for i in t))}
 complex_faces=set()
 for f in facets:
  s=f
  while s:
   complex_faces.add(s)
   s=(s-1)&f
 # Independent face criterion: a set is a face iff its complement contains a disconnected triple.
 for s in range(1,1<<N):
  complement=ALL^s
  isface=any(not connected(sum(1<<i for i in t)) for t in combinations([i for i in range(N) if complement>>i&1],3))
  assert (s in complex_faces)==isface,('criterion',s)
 return complex_faces,facets

def matching(faces):
 alive=set(faces)|{0};matched={}
 for v in ORDER:
  b=1<<v
  for x in list(alive):
   if not x&b and x|b in alive:
    alive.remove(x);alive.remove(x|b);matched[x]=x|b
 # Convert the empty-face match to one vertex-critical ordinary Morse matching.
 root=matched.pop(0)
 assert root.bit_count()==1
 # empty face omitted, hence root becomes critical.
 return matched,alive|{root}

def oriented_hasse(faces,matched):
 indeg={x:0 for x in faces};success={x:[] for x in faces};m=len(faces);e=0
 for upper in faces:
  t=upper
  while t:
   bit=t&-t;t-=bit;lower=upper^bit
   if lower==0:continue
   if matched.get(lower)==upper:
    src,dst=lower,upper
   else:
    src,dst=upper,lower
   success[src].append(dst);indeg[dst]+=1;e+=1
 queue=deque(x for x in faces if indeg[x]==0);seen=0
 while queue:
  x=queue.popleft();seen+=1
  for y in success[x]:
   indeg[y]-=1
   if indeg[y]==0:queue.append(y)
 assert seen==m,('cycle',seen,m)
 return e

def sign(upper,bit):
 return -1 if (upper & (bit-1)).bit_count()%2 else 1

def boundary(upper):
 out={};t=upper
 while t:
  bit=t&-t;t-=bit
  out[upper^bit]=sign(upper,bit)
 return out

def morse_coefficient(faces,matched,critical):
 crit7=[x for x in critical if x.bit_count()==8]
 crit8=[x for x in critical if x.bit_count()==9]
 assert len(crit7)==len(crit8)==1
 c7,c8=crit7[0],crit8[0]
 down_7_to_8={l:u for l,u in matched.items() if l.bit_count()==8}
 # Acyclic matching ensures a well-founded recursion in 7-face -> other 7-faces transitions.
 memo={};active=set();calls=[0]
 def project(face):
  calls[0]+=1
  if face==c7:return 1
  if face not in down_7_to_8:
   # It is paired upward from a 6-face, so gives zero in the remaining 7-cell basis.
   return 0
  if face in memo:return memo[face]
  assert face not in active,('closed_gradient_path',face)
  active.add(face)
  upper=down_7_to_8[face]
  eps=boundary(upper)[face]
  z=-eps*sum(coef*project(other) for other,coef in boundary(upper).items() if other!=face)
  active.remove(face);memo[face]=z
  return z
 d=sum(coef*project(face) for face,coef in boundary(c8).items())
 assert abs(d)==2,('integer_Morse_differential',d)
 return d,c7,c8,calls[0]

def independent_betti_mod2(faces):
 dims=Counter(s.bit_count()-1 for s in faces)
 bydim={d:sorted(s for s in faces if s.bit_count()-1==d) for d in dims}
 rank={0:0}
 for d in sorted(bydim):
  if d==0:continue
  idx={s:i for i,s in enumerate(bydim[d-1])}
  piv={};r=0
  for upper in bydim[d]:
   vec=0;t=upper
   while t:
    b=t&-t;t-=b;vec^=1<<idx[upper^b]
   while vec:
    p=vec.bit_length()-1
    if p in piv:vec ^= piv[p]
    else:piv[p]=vec;r+=1;break
  rank[d]=r
 bet={d:dims[d]-rank[d]-rank.get(d+1,0) for d in dims}
 assert all(bet[d]==(1 if d in (0,7,8) else 0) for d in dims)
 return bet


def boundary_rank_prime(faces, d, prime):
    upper=sorted(s for s in faces if s.bit_count()==d+1)
    lower=sorted(s for s in faces if s.bit_count()==d)
    idx={s:i for i,s in enumerate(lower)}
    pivots={}
    for s in upper:
        vec={idx[t]:c%prime for t,c in boundary(s).items()}
        while vec:
            p=max(vec)
            if p not in pivots:
                inverse=pow(vec[p],-1,prime)
                pivots[p]={i:(x*inverse)%prime for i,x in vec.items()}
                break
            factor=vec[p]
            for i,x in pivots[p].items():
                r=(vec.get(i,0)-factor*x)%prime
                if r:vec[i]=r
                elif i in vec:del vec[i]
    return len(pivots)


def graph_properties():
    assert all((adj[u] & adj[v])==0 for u,v in EDGES), 'triangle found'
    def k_colorable(k):
        colors=[-1]*N
        order=sorted(range(N), key=lambda v: -adj[v].bit_count())
        def solve(j):
            if j==N:return True
            v=order[j]
            used={colors[u] for u in range(N) if (adj[v]>>u)&1}
            for c in range(k):
                if c not in used:
                    colors[v]=c
                    if solve(j+1):return True
            colors[v]=-1
            return False
        return solve(0)
    assert not k_colorable(3) and k_colorable(4), 'chromatic number != 4'
    squares=set()
    for v in range(N):
        for w in range(v+1,N):
            common=[i for i in range(N) if (adj[v]>>i)&1 and (adj[w]>>i)&1]
            for a,b in combinations(common,2):
                edges=frozenset(tuple(sorted(e)) for e in [(v,a),(a,w),(w,b),(b,v)])
                squares.add(edges)
    assert len(squares)==17
    assert any(len(a&b)>0 for a,b in combinations(squares,2))
    return len(squares)

def independent_top_pivots(faces,matched,critical):
    # Perform integer elementary column cancellations of all 7->8 matched pairs.
    # The critical-7 row is never pivoted; its residual entry is the Morse degree.
    columns={u:boundary(u) for u in faces if u.bit_count()==9}
    pivots=[(l,u) for l,u in matched.items() if l.bit_count()==8]
    assert len(pivots)==147
    for lower,upper in pivots:
        v=columns[upper]
        epsilon=v.get(lower,0)
        assert epsilon in (-1,1)
        for other,col in columns.items():
            if other==upper:continue
            multiple=col.get(lower,0)*epsilon
            if multiple:
                for row,coeff in v.items():
                    z=col.get(row,0)-multiple*coeff
                    if z: col[row]=z
                    else:col.pop(row,None)
        del columns[upper]
    assert len(columns)==1
    remaining=next(iter(columns.values()))
    c7=next(x for x in critical if x.bit_count()==8)
    other_upper_sevens={u for l,u in matched.items() if l.bit_count()==7}
    assert all(x==c7 or x in other_upper_sevens for x in remaining)
    assert remaining[c7]==2,('independent_top_pivots',remaining[c7])
    return remaining[c7], len(remaining)

def main():
 squares=graph_properties()
 faces,facets=all_faces()
 match,critical=matching(faces)
 assert len(facets)==148
 assert len(faces)==3927
 assert len(match)*2+len(critical)==len(faces)
 counts=Counter(s.bit_count()-1 for s in faces)
 assert counts=={0:12,1:66,2:220,3:495,4:792,5:924,6:792,7:478,8:148}
 missing_eight={sum(1<<i for i in vs) for vs in combinations(range(N),8) if sum(1<<i for i in vs) not in faces}
 square_complements=set()
 for v in range(N):
  for w in range(v+1,N):
   common=[i for i in range(N) if adj[v]>>i&1 and adj[w]>>i&1]
   for a,b in combinations(common,2):
    square_complements.add(ALL ^ sum(1<<i for i in (v,w,a,b)))
 assert len(missing_eight)==17 and missing_eight==square_complements

 crit=Counter(s.bit_count()-1 for s in critical)
 assert crit=={0:1,7:1,8:1},crit
 edges=oriented_hasse(faces,match)
 assert edges>0
 coeff,c7,c8,numcalls=morse_coefficient(faces,match,critical)
 second_degree,remaining_rows=independent_top_pivots(faces,match,critical)
 assert second_degree==coeff
 bet=independent_betti_mod2(faces)
 rk7=boundary_rank_prime(faces,7,3)
 rk8=boundary_rank_prime(faces,8,3)
 assert (rk7,rk8)==(330,148),(rk7,rk8)
 print('CHVATAL_CUT3_VERIFIED')
 print('vertices',N,'edges',len(EDGES),'girth_four_squares',squares,'disconnected_triple_facets',len(facets))
 print('nonempty_faces',len(faces),'f_vector',dict(sorted(counts.items())))
 print('missing_dimension_seven_faces_equal_square_complements',len(missing_eight))
 print('morse_pairs',len(match),'critical_cells',dict(sorted(crit.items())))
 print('critical_masks',{'dimension_0':next(x for x in critical if x.bit_count()==1), 'dimension_7':c7,'dimension_8':c8})
 print('hasse_incidences',edges,'acyclic',True)
 print('integer_Morse_attaching_degree',coeff,'projection_calls',numcalls)
 print('independent_integer_pivot_degree',second_degree,'residual_top_column_rows',remaining_rows)
 print('mod2_unreduced_betti',dict(sorted(bet.items())))
 print('mod3_boundary_ranks_d7_d8',rk7,rk8)
 print('homotopy_type','Moore(Z/2,7)')
if __name__=='__main__':main()
