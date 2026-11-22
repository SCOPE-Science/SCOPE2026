"""Independent exact Smith and spectral cross-check; requires sympy >=1.10."""
from itertools import combinations
from sympy import Matrix, zeros, ZZ, Symbol, expand
from sympy.matrices.normalforms import smith_normal_form
pairs=list(combinations(range(6),2))
triples=list(combinations(range(6),3))
B=Matrix([[int(set(a).issubset(t)) for t in triples] for a in pairs])
assert expand((B*B.T).charpoly().as_expr()-(Symbol('lambda')-12)*(Symbol('lambda')-6)**5*(Symbol('lambda')-2)**9)==0
L=zeros(35,35)
for i in range(15):
 for j in range(20):
  if B[i,j]:
   k=15+j
   L[i,i]+=1;L[k,k]+=1;L[i,k]-=1;L[k,i]-=1
x=Symbol('lambda')
assert expand(L.charpoly(x).as_expr() - x*(x-7)*(x-6)**5*(x-5)**9*(x-3)**5*(x-2)**9*(x-1)**5)==0
expected=[1]*24+[2]*2+[10]*2+[30]*2+[180]*4
for deleted in (0,15):
 ids=[i for i in range(35) if i!=deleted]
 A=L.extract(ids,ids)
 S=smith_normal_form(A,domain=ZZ)
 got=[abs(int(S[i,i])) for i in range(34)]
 assert got==expected,(deleted,got)
print('STEINER_PLUCKER_SYMPY_CROSSCHECK_OK')
