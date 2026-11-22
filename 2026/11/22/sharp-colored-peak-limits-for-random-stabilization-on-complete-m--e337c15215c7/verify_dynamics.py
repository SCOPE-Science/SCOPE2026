from fractions import Fraction
from itertools import product,permutations
from functools import lru_cache
from collections import defaultdict

def run(parts,colors_count):
 N=sum(parts); part_of=sum(([i]*a for i,a in enumerate(parts)),[]); adj=[[u for u in range(N) if part_of[u]!=part_of[v]] for v in range(N)]
 q=max(colors_count,max(map(len,adj))+1)
 @lru_cache(None)
 def solve(initial,state,changed):
  enabled=[v for v in range(N) if any(state[v]==state[u] for u in adj[v])]
  if not enabled:
   return {tuple(sum(1 for v in range(N) if initial[v]==c and not changed[v]) for c in range(colors_count)):Fraction(1)}
  out=defaultdict(Fraction)
  for v in enabled:
   free=min(c for c in range(q) if c not in {state[u] for u in adj[v]})
   newstate=state[:v]+(free,)+state[v+1:]
   newchanged=changed[:v]+(True,)+changed[v+1:]
   for x,p in solve(initial,newstate,newchanged).items():out[x]+=p/len(enabled)
  return dict(out)
 initial_law=defaultdict(Fraction)
 for initial in product(range(colors_count),repeat=N):
  x=solve(initial,initial,(False,)*N)
  for k,p in x.items(): initial_law[k]+=p/Fraction(colors_count**N)
 peak_law=defaultdict(Fraction)
 for initial in product(range(colors_count),repeat=N):
  for perm in permutations(range(N)):
   rank={v:i for i,v in enumerate(perm)}
   x=tuple(sum(1 for v in range(N) if initial[v]==c and all(initial[u]!=c or rank[v]>rank[u] for u in adj[v])) for c in range(colors_count))
   peak_law[x]+=Fraction(1,colors_count**N * __import__('math').factorial(N))
 assert dict(initial_law)==dict(peak_law),(parts,initial_law,peak_law)
 print('DIRECT_ACTIVATION_VS_PEAK_REDUCTION_PASS',parts,colors_count,'states',solve.cache_info())
for p,k in [((1,1,1),2),((2,1,1),2),((1,1,1,1),2),((2,1,1),3)]:run(p,k)
