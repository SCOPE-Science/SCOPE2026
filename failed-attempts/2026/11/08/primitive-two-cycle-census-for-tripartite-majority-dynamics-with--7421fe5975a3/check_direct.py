"""Label-level direct dynamics; does not use occupancy transitions."""
from itertools import combinations_with_replacement
from math import comb

def formula(a,b,c):
 d=[a,b,c]
 v=int(d.count(max(d))==1)
 for i in range(3):
  for j in range(i+1,3):
   if d[i]==d[j]:
    c=d[3-i-j]
    v+=sum(comb(c,h) for h in range(c+1) if abs(2*h-c)<d[i])
 return v

def pairs(a,b,c):
 sizes=(a,b,c);N=sum(sizes)
 shores=[0]*a+[1]*b+[2]*c
 other_masks=[]
 for i in range(N):
  bitmask=0
  for j in range(N):
   if shores[j]!=shores[i]:bitmask|=1<<j
  other_masks.append(bitmask)
 result=0
 for state in range(1<<N):
  new=0
  for i in range(N):
   ones=(state&other_masks[i]).bit_count();deg=other_masks[i].bit_count()
   if 2*ones>deg or (2*ones==deg and ((state>>i)&1)):new|=1<<i
  if new==state:continue
  again=0
  for i in range(N):
   ones=(new&other_masks[i]).bit_count();deg=other_masks[i].bit_count()
   if 2*ones>deg or (2*ones==deg and ((new>>i)&1)):again|=1<<i
  if again==state:result+=1
 assert result%2==0
 return result//2
cases=0
states=0
for n in combinations_with_replacement(range(1,9),3):
 if sum(n)>15:continue
 x=pairs(*n)
 if x!=formula(*n):raise AssertionError((n,x,formula(*n)))
 cases+=1;states+=1<<sum(n)
print(f'PASS direct labelled bit configurations: {cases} unordered shore profiles, {states} states, all period-two orbits match formula.')
