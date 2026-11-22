"""Independent exhaustive dynamic programming on pentagon + pentagram + spokes."""
from itertools import product,combinations
from collections import defaultdict,Counter
from fractions import Fraction
from json import dumps
N=10
edge=set()
for k in range(5):
 for i,j in [(k,(k+1)%5),(5+k,5+(k+2)%5),(k,5+k)]:
  edge.add(tuple(sorted((i,j))))
E=sorted(edge)
assert len(E)==15
# use 10-tuples rather than base-three integer encodings
states=list(product(range(3),repeat=N))
match=lambda a: sum(a[i]==a[j] for i,j in E)
by_score=defaultdict(list)
for a in states:by_score[match(a)].append(a)
labels=[(10,),(5,5),(5,3,2),(4,3,3)]
P={}; num=Counter()
for score in range(15,-1,-1):
 for state in by_score[score]:
  moves=[]
  for i in range(N):
   for c in range(3):
    if c==state[i]:continue
    b=state[:i]+(c,)+state[i+1:]
    if match(b)>score:moves.append(b)
  if moves:
   P[state]=tuple(sum((P[m][k] for m in moves),Fraction())/len(moves) for k in range(4))
  else:
   pop=tuple(sorted(Counter(state).values(),reverse=True))
   assert pop in labels,(state,pop,score)
   index=labels.index(pop)
   num[str(pop)]+=1
   P[state]=tuple(Fraction(int(k==index)) for k in range(4))
assert len(P)==3**10
agg=[sum((P[s][k] for s in states),Fraction())/len(states) for k in range(4)]
# Relabel vertices, but geometry counts are invariant under isomorphism
NBR=[set() for i in range(N)]
for i,j in E:NBR[i].add(j);NBR[j].add(i)
geom=defaultdict(list)
for i,j in combinations(range(N),2):
 for w in range(N):
  if w==i or w==j:continue
  c=[0]*N;c[i]=c[j]=1;c[w]=2
  typ=(int(j in NBR[i]),int(i in NBR[w])+int(j in NBR[w]))
  geom[typ].append(1-P[tuple(c)][0])
assert all(len(set(v))==1 for v in geom.values())
assert (len(geom[(0,1)]),geom[(0,1)][0])==(120,Fraction(11,270))
assert all(v[0]==0 for k,v in geom.items() if k!=(0,1))
out={'method':'GP(5,2), all states via descending bond count, full energy comparisons',
     'terminal_counts':dict(num),'states':len(states),
     'uniform_initial_absorption':{str(t):str(z) for t,z in zip(labels,agg)},
     'three_seed_geometry':{str(k):{'count':len(vals),'p':str(vals[0])} for k,vals in sorted(geom.items())},
     'three_seed_721_freeze_mean':str(sum((x for v in geom.values() for x in v),Fraction())/360),
     'all_freezing':str(1-agg[0])}
print(dumps(out,sort_keys=True,indent=2))
