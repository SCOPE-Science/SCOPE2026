import itertools, sys
sys.path.insert(0,'output/artifacts')
from flipsearch import strand_of_facets
from litcheck import chain
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)
for branch in (False,True):
    f,c,N=chain(4,4,branch)
    beta=strand_of_facets(f,N)
    print('star' if branch else 'chain',beta)
    print('formula',[formula(4,5,i) for i in range(N+1)])
