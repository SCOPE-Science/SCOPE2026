import itertools, sys
sys.path.insert(0,'output/artifacts')
from flipsearch import check_valid, strand_of_facets
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

def cyc(n,off=0): return [(off+i,off+(i+1)%n) for i in range(n)]
def join(E1,E2): return [frozenset((a,b,c,d)) for (a,b) in E1 for (c,d) in E2]
def susp(facets,a,b): return [F|{a} for F in facets]+[F|{b} for F in facets]

tests=[]
# k=4,n=16: stacked chain of 3
from flipsearch import stacked_chain
tests.append(('stacked k=4',stacked_chain(4,3)))
J=join(cyc(8),cyc(8,8)); col=[v%2 for v in range(8)]+[2+((v-8)%2) for v in range(8,16)]
tests.append(('join C8*C8', (J,col,16)))
J2=join(cyc(6),cyc(10,6)); col2=[v%2 for v in range(6)]+[2+((v-6)%2) for v in range(6,16)]
tests.append(('join C6*C10',(J2,col2,16)))
s2=susp(susp([frozenset((i,(i+1)%10)) for i in range(10)],10,11),12,13)
col3={}
for v in range(10): col3[v]=v%2
col3[10]=2;col3[11]=2;col3[12]=3;col3[13]=3
tests.append(('2-susp C10',(s2,[col3[v] for v in range(14)],14)))
for name,(fac,col,n) in tests:
    if n!=16: print(name,'n=',n,'skip formula'); beta=strand_of_facets(fac,n); print('  strand',beta); continue
    print(name,'valid',check_valid(fac,4,col))
    beta=strand_of_facets(fac,n)
    print('  strand',beta)
    print('  excess',[b-formula(4,4,i) for i,b in enumerate(beta)])
# k=2: only cross-polytope (proved). d=5,k=2: cross-polytope boundary (10 verts): strand [0,5,0...]; any other? partition forced (2,2,2,2,2) by counting (sum nj=10, nj>=2 -> all 2). Same rigidity. k=2 PROVED for all d.
# d=5,k=3 (n=15): stacked chain of 2 (5-dim? d=5 summands are 4-dim cross-polytope boundaries, 10 verts each, glue facet 5 verts -> n=15). strand cost 2^15=32768 ok.
from flipsearch import stacked_chain as sc
fac5,col5,n5=sc(5,2)
print('d=5 stacked k=3 valid',check_valid(fac5,5,col5))
beta5=strand_of_facets(fac5,n5)
print('  strand',beta5)
print('  formula',[formula(5,3,i) for i in range(n5+1)])
