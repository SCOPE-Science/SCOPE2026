from itertools import combinations
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
E=list(combinations(range(7),2)); ix={e:i for i,e in enumerate(E)}
F0=[(i,) for i in range(21)]
F1=[(i,j) for i,j in combinations(range(21),2) if len(set(E[i]+E[j]))==4]
F2=[t for t in combinations(range(21),3) if len(set(E[t[0]]+E[t[1]]+E[t[2]]))==6]
F=F0+F1+F2
FI={t:i for i,t in enumerate(F)}
def move(f,k):return tuple(sorted(ix[tuple(sorted(((v+k)%7) for v in E[e]))] for e in f))
def act(i,k):return FI[move(F[i],k)]
def canon(chain):return min(tuple(act(i,k) for i in chain) for k in range(7))
chains0=[(i,) for i in range(len(F))]
chains1=[(i,j) for i in range(len(F)) for j in range(len(F)) if len(F[i])<len(F[j]) and set(F[i])<set(F[j])]
chains2=[(i,j,k) for i in range(len(F)) for j in range(len(F)) for k in range(len(F)) if len(F[i])==1 and len(F[j])==2 and len(F[k])==3 and set(F[i])<set(F[j])<set(F[k])]
RS=[sorted({canon(c) for c in arr}) for arr in [chains0,chains1,chains2]]
print('quotient barycentric counts',list(map(len,RS)))
MAP=[{canon(c):i for i,c in enumerate(R)} for R in RS]
N0,N1,N2=map(len,RS)
bd1=Matrix.zeros(N0,N1);bd2=Matrix.zeros(N1,N2)
for j,(a,b) in enumerate(RS[1]):
 bd1[MAP[0][canon((b,))],j]+=1
 bd1[MAP[0][canon((a,))],j]-=1
for j,(a,b,c) in enumerate(RS[2]):
 for f,sgn in [((b,c),1),((a,c),-1),((a,b),1)]:
  bd2[MAP[1][canon(f)],j]+=sgn
assert bd1*bd2==Matrix.zeros(N0,N2)
print('d1 rank',bd1.rank())
# choose tree and create cokernel in cycle basis using pivot edges
parent=list(range(N0));
def root(a):
 while parent[a]!=a:a=parent[a]
 return a
TREE=[]
for j,(a,b) in enumerate(RS[1]):
 a,b=MAP[0][canon((a,))],MAP[0][canon((b,))]
 if root(a)!=root(b):parent[root(a)]=root(b);TREE.append(j)
assert len(TREE)==N0-1
rest=[i for i in range(N1) if i not in TREE]
Z=bd2.extract(rest,list(range(N2)))
print('cycle matrix',Z.shape,'rank',Z.rank())
snf=smith_normal_form(Z,domain=ZZ)
diag=[abs(int(snf[i,i])) for i in range(min(snf.rows,snf.cols)) if snf[i,i]!=0]
print('SNF nonunit',sorted(x for x in diag if x!=1),'rank',len(diag),'H2_rank',N2-len(diag))
assert sorted(x for x in diag if x!=1)==[21]
assert N2-len(diag)==2
print('BARYCENTRIC_INDEPENDENT_CHECK_OK')
