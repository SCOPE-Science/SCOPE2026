import sympy as s
from collections import Counter
e=[s.eye(4)[:,i] for i in range(4)]
roots=[e[1]-e[2],e[2]-e[3],e[3],(e[0]-e[1]-e[2]-e[3])/2]
roots=[s.Matrix(x) for x in roots]
def refl(a):return s.eye(4)-2*a*a.T/(a.dot(a))
gens=[refl(a) for a in roots]

def key(A): return tuple(int(2*x) for x in A)
I=s.eye(4); W=[I]; keys={key(I):0}; words=[()]; head=0
while head < len(W):
 A=W[head]
 for j,B in enumerate(gens):
  M=A*B; k=key(M)
  if k not in keys:
   keys[k]=len(W);W.append(M);words.append(words[head]+(j,))
 head+=1
print("group_order",len(W))
assert len(W)==1152
c=gens[0]*gens[1]*gens[2]*gens[3]; inv_c=c.T;print('coxeter_order',next(i for i in range(1,101) if c**i==I));assert c**6 == -I
print('half_turn_is_central_minus_identity')
# rank over rationals using minor determinants rank4 via trace etc
ranks=[(A-I).rank() for A in W]; print('reflection_codimension_histogram',sorted(Counter(ranks).items()))
# Check Carter's rank formula independently by shortest reflection words.
reflections=[A for i,A in enumerate(W) if ranks[i]==1]
assert len(reflections)==24
shortest={0:0}; frontier=[0]
while frontier:
  nxt=[]
  for i in frontier:
    for R in reflections:
      j=keys[key(W[i]*R)]
      if j not in shortest:
        shortest[j]=shortest[i]+1; nxt.append(j)
  frontier=nxt
assert len(shortest)==1152
assert all(shortest[i]==ranks[i] for i in range(1152))
print('reflection_word_length_equals_fixed_codimension_ALL_1152')
ci=keys[key(c)]; cn=keys[key(c.T)]
# conjugation maps
cc=[keys[key(c*A*inv_c)] for A in W]
N=[]; nr=[]
for i,A in enumerate(W):
 B=A.T*c  # inverses orthogonal
 if ranks[i]+ranks[keys[key(B)]]==4:
  N.append(i);nr.append(ranks[i])
print('NC_total_and_ranks',len(N),sorted(Counter(nr).items()))
assert len(N)==105
rank={i:ranks[i] for i in N}; ncset=set(N)
assert all(cc[i] in ncset for i in N)
# partial order a <= b iff lt(a)+lt(a^-1 b)=lt(b)
# map all w indices maybe N comparisons
less={i:set() for i in N}
for i in N:
 for j in N:
  if rank[i]<rank[j]:
   ij=keys[key(W[i].T*W[j])]
   if rank[i]+ranks[ij]==rank[j]:less[i].add(j)
P=[i for i in N if 0<rank[i]<4]
V=sorted(P)
E=[(a,b) for a in V for b in less[a] if b in P]
FACES=[(a,b,c0) for a,b in E for c0 in less[b] if c0 in P]
print('proper_order_complex_simplex_counts',len(V),len(E),len(FACES))
# orbits of rank ordered simplices under conjugation
simplices=[V,E,FACES]
reps=[];maps=[]
for ss in simplices:
 index={}; orbs=[]
 for x in ss:
  if x in index:continue
  oid=len(orbs); y=x; orb=[]
  while y not in index:
   index[y]=oid;orb.append(y)
   y=tuple(cc[a] for a in y) if isinstance(y,tuple) else cc[y]
  assert index[y]==oid
  orbs.append(orb)
 reps.append(orbs);maps.append(index)
print('quotient_cell_counts',*[len(a) for a in reps]);print('vertex_orbit_sizes',sorted(Counter(map(len,reps[0])).items()))
fixed_counts=[]
for k in range(6):
 fixed=[]
 for ss in simplices:
  num=0
  for a in ss:
   y=a
   for _ in range(k):y=tuple(cc[z] for z in y) if isinstance(y,tuple) else cc[y]
   if y==a:num+=1
  fixed.append(num)
 fixed_counts.append(fixed)
 print('fixed_by_rotation_power',k,*fixed)
# Cross-check Burnside's orbit counts independently of orbit construction.
assert [sum(row[d] for row in fixed_counts)//6 for d in range(3)] == [len(oo) for oo in reps]
# orientation by rank; d1 columns -a+b; d2 columns +(b,c)-(a,c)+(a,b)
D1=s.zeros(len(reps[0]),len(reps[1]));D2=s.zeros(len(reps[1]),len(reps[2]))
for col,orb in enumerate(reps[1]):
 a,b=orb[0]; D1[maps[0][a],col]-=1; D1[maps[0][b],col]+=1
for col,orb in enumerate(reps[2]):
 a,b,d=orb[0];D2[maps[1][(b,d)],col]+=1;D2[maps[1][(a,d)],col]-=1;D2[maps[1][(a,b)],col]+=1
assert D1*D2==s.zeros(D1.rows,D2.cols)
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
for nam,M in [('d1',D1),('d2',D2)]:
 S=smith_normal_form(M,domain=ZZ);diag=[abs(int(S[i,i])) for i in range(min(M.shape)) if S[i,i]!=0]; print(nam,'shape',M.shape,'rank',len(diag),'nonunit',Counter(d for d in diag if d>1),flush=True)
print('Euler',D1.rows-D1.cols+D2.cols); assert [len(a) for a in reps]==[19,78,72]

assert all(len(orb) in (2,3,6) for orb in reps[0]); assert any(len(orb)==2 for orb in reps[0]); assert any(len(orb)==3 for orb in reps[0])
print('F4_COXETER_QUOTIENT_PASS')
