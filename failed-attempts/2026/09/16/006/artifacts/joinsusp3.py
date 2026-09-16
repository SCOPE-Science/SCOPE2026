import itertools
from flipsearch import check_valid, strand_of_facets
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

def cycle_edges(n,off):
    return [(off+i,off+(i+1)%n) for i in range(n)]

def join_complex(E1,n1,E2):
    # E2 verts already offset; facets = quads
    return [frozenset((a,b,c,d)) for (a,b) in E1 for (c,d) in E2]

for (m,n_) in [(6,6),(8,8),(6,10)]:
    E1=cycle_edges(m,0); E2=cycle_edges(n_,m)
    J=join_complex(E1,m,E2)
    N=m+n_
    col=[0]*N
    for v in range(m): col[v]=v%2
    for v in range(m,N): col[v]=2+((v-m)%2)
    print(f'join C{m}*C{n_}: n={N} nfacets={len(J)} valid={check_valid(J,4,col)}')
    beta=strand_of_facets(J,N)
    k=N//4
    print('  strand',beta)
    print('  formula',[formula(4,k,i) for i in range(N+1)])
    print('  excess',[b-formula(4,k,i) for i,b in enumerate(beta)])
