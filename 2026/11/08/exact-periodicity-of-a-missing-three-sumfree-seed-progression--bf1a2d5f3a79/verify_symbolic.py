"""An exact affine-interval proof checker for the strict 3-sumfree family.
All comparisons quantify over EVERY integer k >= 2, not a sample.
"""
from itertools import combinations_with_replacement, product

K0=2

def add(a,b):return (a[0]+b[0], a[1]+b[1])
def sub(a,b):return (a[0]-b[0], a[1]-b[1])
def mul(n,a):return (n*a[0],n*a[1])
def c(x):return (0,x)
def ev(x,k):return x[0]*k+x[1]
def ge0(f):return f[0]>=0 and ev(f,K0)>=0
def le0(f):return f[0]<=0 and ev(f,K0)<=0

def union(intervals):
 intervals=sorted(intervals,key=lambda x:(ev(x[0],K0),ev(x[1],K0),x[0][0]))
 for I in intervals:
  assert ge0(sub(I[1],I[0])), ('bad interval',I)
 out=[]
 for L,U in intervals:
  if not out:out.append((L,U));continue
  assert ge0(sub(L,out[-1][0])), ('order switch',out[-1],(L,U))
  # if overlap/adjacency universally, merge; else if disjoint universally, append
  delta=sub(add(out[-1][1],c(1)),L)
  if ge0(delta):
   old=out[-1][1]
   if ge0(sub(U,old)):out[-1]=(out[-1][0],U)
   elif ge0(sub(old,U)):pass
   else:raise AssertionError(('upper switch',old,U))
  elif le0(add(delta,c(1))):out.append((L,U)) # delta<=-1 all k
  else:raise AssertionError(('overlap switch',delta,(L,U)))
 return out

# r, lower u(k), upper u(k)
C=[(1,c(0),c(0)), (2,c(0),c(0)),
   (5,(1,0),(2,1)),(0,(1,1),(2,1)),(1,(1,1),(2,1)),(4,(2,2),(2,2))]
B=[(5,(6,5),(7,5)),(0,(6,5),(7,5)),(1,(6,4),(7,4))]
R=[(5,(1,1),(2,1)),(0,(1,1),(2,1)),(1,(1,0),(2,0))]

def sums(groups, multiplicity=3, distinct=True):
 """Exact sums of distinct entries (within each class) when distinct=True."""
 out={r:[] for r in range(6)}
 for ids in combinations_with_replacement(range(len(groups)),multiplicity):
  counts={i:ids.count(i) for i in set(ids)}
  lo=c(0);hi=c(0)
  for i,q in counts.items():
   _,L,U=groups[i]
   if distinct:
    width=sub(sub(U,L),c(q-1))
    if not ge0(width):
     assert le0(add(width,c(1))), ("parameter-dependent group admissibility",i,q,width)
     lo=c(1);hi=c(0);break
   lo=add(lo,add(mul(q,L),c(q*(q-1)//2 if distinct else 0)))
   hi=add(hi,sub(mul(q,U),c(q*(q-1)//2 if distinct else 0)))
  if not ge0(sub(hi,lo)):continue
  rr=sum(groups[i][0] for i in ids)
  carry=rr//6;r=rr%6
  out[r].append((add(lo,c(carry)),add(hi,c(carry))))
 return {r:union(v) for r,v in out.items()}

def mixed(groups1,num1,distinct1,groups2,num2,distinct2):
 x=sums(groups1,num1,distinct1); y=sums(groups2,num2,distinct2)
 out={r:[] for r in range(6)}
 for r in range(6):
  for s in range(6):
   for a,b in x[r]:
    for cc,dd in y[s]:
     rr=r+s;carry=rr//6
     out[rr%6].append((add(add(a,cc),c(carry)),add(add(b,dd),c(carry))))
 return {r:union(v) for r,v in out.items()}

def iv(a,b): return ((a[0],a[1]),(b[0],b[1]))

def expected():
 # Each pair denotes affine endpoints (slope, intercept), exact for every k>=2.
 return {
  "3C":{
   0:[iv((2,2),(6,4))], 1:[iv((2,2),(6,3))],
   2:[iv((1,1),(6,5))], 3:[iv((1,1),(6,5))],
   4:[iv((1,1),(2,1)),iv((2,3),(6,5))],
   5:[iv((2,2),(6,4))]},
  "2C+B":{
   0:[iv((7,6),(11,8))],1:[iv((7,5),(11,7))],
   2:[iv((6,6),(11,10))],3:[iv((6,5),(11,9))],
   4:[iv((6,4),(11,9))],5:[iv((7,6),(11,8))]},
  "2C+R":{
   0:[iv((2,2),(6,4))],1:[iv((2,1),(6,3))],
   2:[iv((1,2),(6,6))],3:[iv((1,1),(6,5))],
   4:[iv((1,0),(6,5))],5:[iv((2,2),(6,4))]},
  "C+2R":{
   0:[iv((2,3),(6,4))],1:[iv((2,2),(6,3))],
   2:[iv((2,1),(6,6))],3:[iv((2,0),(6,5))],
   4:[iv((2,0),(6,4))],5:[iv((2,3),(6,4))]},
  "3R":{
   0:[iv((3,3),(6,3))],1:[iv((3,2),(6,2))],
   2:[iv((3,1),(6,1))],3:[iv((3,0),(6,5))],
   4:[iv((3,4),(6,4))],5:[iv((3,3),(6,3))]}
 }

def check():
 e=expected()
 d={"3C":sums(C,3,True), "2C+B":mixed(C,2,True,B,1,True),
    "2C+R":mixed(C,2,True,R,1,False),
    "C+2R":mixed(C,1,True,R,2,False),"3R":sums(R,3,False)}
 for name in e:
  assert d[name]==e[name], (name,d[name],e[name])
 print('AFFINE_SUMSET_IDENTITIES_OK 5 tables x 6 residues; all integers k>=2')
 # The only tail residues modulo 6M are r=0,1,5, with M=5k+4.
 # At those residues the possible 2C+R,C+2R,3R sums fall
 # strictly between the original R interval and its shift by M.
 M=(5,4)
 for name in ('2C+R','C+2R','3R'):
  for r,L,U in [(0,(1,1),(2,1)),(1,(1,0),(2,0)),(5,(1,1),(2,1))]:
   for A,Bb in d[name][r]:
    assert ge0(sub(A,add(U,c(1)))), (name,r,'lower')
    assert ge0(sub(sub(add(M,L),c(1)),Bb)),(name,r,'upper')
 print('MODULAR_NONCOLLISION_OK 3 classes of triples; all k>=2')
 # The three-residue slices of S in (h,11h+3] and their complements.
 A={
  0:[iv((1,1),(2,1)),iv((6,5),(7,5)),iv((11,9),(11,9))],
  1:[iv((1,1),(2,1)),iv((6,4),(7,4)),iv((11,8),(11,9))],
  2:[],3:[],4:[iv((2,2),(2,2))],
  5:[iv((1,1),(2,1)),iv((6,5),(7,5))]}
 lower=(1,1)
 for r in range(6):
  upper=(11,8) if r==5 else (11,9)
  # Exact triple sums from C, or from distinct C pairs and B0.
  E=union([*d['3C'][r],*d['2C+B'][r]])
  # The part of 2C+B exceeding 11h+3 is excluded. All other
  # terms in these two lists lie above h and at or below that bound.
  clipped=[]
  for lo,hi in E:
   if ge0(sub(lo,add(upper,c(1)))):continue
   if ge0(sub(upper,hi)):
    clipped.append((lo,hi))
   else:
    assert ge0(sub(hi,upper))
    clipped.append((lo,upper))
  # Ascending A/E intervals must EXACTLY partition the full interval.
  tagged=sorted([(lo,hi,'A') for lo,hi in A[r]]+[(lo,hi,'T') for lo,hi in clipped],key=lambda z:ev(z[0],K0))
  assert tagged[0][0]==lower,(r,'start',tagged)
  assert tagged[-1][1]==upper,(r,'end',tagged)
  for x,y in zip(tagged,tagged[1:]):
   assert add(x[1],c(1))==y[0],(r,'adjacency',x,y)
 print('BASE_PARTITION_IDENTITY_OK (h,11h+3] for every k>=2')
 print('SYMBOLIC_PROOF_CHECK_OK finite-interval arithmetic, no finite-k cutoff')

if __name__=='__main__':check()
