import itertools, sys
sys.path.insert(0,'output/artifacts')
from flipsearch import stacked_chain, check_valid, strand_of_facets
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)
def fvec(facets,n):
    E=set(); T=set()
    for F in facets:
        for e in itertools.combinations(sorted(F),2): E.add(e)
        for t in itertools.combinations(sorted(F),3): T.add(t)
    return (n,len(E),len(T),len(facets))
def cyc(n,off=0): return [(off+i,off+(i+1)%n) for i in range(n)]
def join(E1,E2): return [frozenset((a,b,c,d)) for (a,b) in E1 for (c,d) in E2]
def susp(facets,a,b): return [F|{a} for F in facets]+[F|{b} for F in facets]

cands={}
cands['Gamma stacked'] = stacked_chain(4,2)
J=join(cyc(6),cyc(6,6)); col=[v%2 for v in range(6)]+[2+((v-6)%2) for v in range(6,12)]
cands['join C6*C6']=(J,col,12)
s2=susp(susp([frozenset((i,(i+1)%8)) for i in range(8)],8,9),10,11)
col2={}; 
for v in range(8): col2[v]=v%2
col2[8]=2;col2[9]=2;col2[10]=3;col2[11]=3
cands['2-susp C8']=(s2,[col2[v] for v in range(12)],12)
# stacked chain of 2 but different glue? same. cyclic handle from bimon:
sys.path.insert(0,'.')
import importlib
for name,(fac,col,n) in cands.items():
    print(f'== {name}: fvec={fvec(fac,n)} valid={check_valid(fac,n,4 if False else 4,col) if False else check_valid(fac,4,col)}')
    beta=strand_of_facets(fac,n)
    print('   strand',beta,'excess',[b-formula(4,3,i) for i,b in enumerate(beta)])
