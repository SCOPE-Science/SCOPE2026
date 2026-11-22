# Verify structural descriptions of all persistent four-waves on the 16-vertex four-cube.
import itertools,collections,pathlib
reps=[int(line.split()[1]) for line in pathlib.Path(__file__).with_name('results_b.txt').read_text().splitlines() if line.startswith('CYCLE')]
A=(1,2,4,8); AF=A+(15,)
def transform(p,S=A):
 E=p&65535; R=p>>16
 ne=0
 for v in range(16):
  if not ((E|R)>>v&1) and sum((E>>(v^a))&1 for a in S)>=2: ne |=1<<v
 return ne+(E<<16)
def cyc(rep,S=A):
 out=[rep]; x=transform(rep,S)
 while x!=rep and len(out)<20:out.append(x);x=transform(x,S)
 assert x==rep and len(out)==4,(rep,len(out))
 return out
def plane(S):
 if len(S)!=4:return False
 a=min(S);rel={v^a for v in S}
 return 0 in rel and all((x^y) in rel for x in rel for y in rel)
perms=list(itertools.permutations(range(4)))
permutations=[]
for perm in perms:
 for t in range(16):
  permutations.append([t ^ sum(((v>>i)&1)<<perm[i] for i in range(4)) for v in range(16)])
def perm_mask(mask,P):return sum(1<<P[v] for v in range(16) if mask>>v&1)
def spatialcanon(c):
 return min(min(tuple(perm_mask(z&65535,P)|(perm_mask(z>>16,P)<<16) for z in c[k:]+c[:k]) for k in range(4)) for P in permutations)
classes=collections.defaultdict(list)
counts={'shared':0,'alternating':0,'other':0}
cl_all=[]
for rep in reps:
 c=cyc(rep)
 phase=[{v for v in range(16) if (z&65535)>>v&1} for z in c]
 assert sorted(len(a) for a in phase)==[4]*4
 assert len(set.union(*phase))==16
 assert all(plane(S) for S in phase)
 types=[frozenset({v^min(S) for v in S}) for S in phase]
 if len(set(types))==1:kind='shared'
 elif types[0]==types[2] and types[1]==types[3] and types[0]!=types[1]:kind='alternating'
 else:kind='other'
 counts[kind]+=1
 canon=spatialcanon(c);classes[canon].append((rep,kind))
 cl_all.append(all(transform(x,AF)==transform(x,A) for x in c))
print('cycle types',counts)
print('spatial orbit classes',len(classes),[(len(v),collections.Counter(z[1] for z in v)) for v in classes.values()])
print('cycles persist under Clebsch update',sum(cl_all),'of',len(cl_all))
print('reps',reps)
print('example-cycle',cyc(reps[0]))
