"""Independent full physical Ising-energy census for small cyclic prisms."""
from itertools import product
from collections import Counter
from fractions import Fraction

def compute(n):
    # Base-graph vertices: 0..n-1 upper rail, n..2n-1 lower rail.
    edges=[]
    for rail in range(2):
        for j in range(n):edges.append((rail*n+j,rail*n+(j+1)%n))
    for j in range(n):edges.append((j,n+j))
    # Every pair of incident original edges is a physical Ising bond.
    bonds=[(i,j) for i,(a,b) in enumerate(edges) for j,(c,d) in enumerate(edges)
           if i<j and bool({a,b}&{c,d})]
    assert len(edges)==3*n and len(bonds)==6*n
    hist=Counter(); Emin=None
    for spins in product((-1,1),repeat=3*n):
        E=sum(spins[i]*spins[j] for i,j in bonds)
        if Emin is None or E<Emin:
            Emin=E; hist.clear()
        if E==Emin:hist[sum(spins)]+=1
    assert Emin==-2*n
    return hist

expect={
  3:{-3:4,-1:39,1:39,3:4},
  4:{-4:9,-2:108,0:216,2:108,4:9},
  5:{-5:11,-3:220,-1:740,1:740,3:220,5:11},
  6:{-6:20,-4:462,-2:2235,0:3640,2:2235,4:462,6:20},
}
# Test complete state-space counts from independently obtained transfer cases.
counts={3:86,4:450,5:1942,6:9074}
for n,total in counts.items():
    h=compute(n)
    assert sum(h.values())==total,(n,h)
    assert sum(k*v for k,v in h.items())==0
    if n in expect:
       # Magnetization support is checked independently of the transfer matrix.
       assert dict(h)==expect[n],(n,h)
    print(n, 'energy minimum',-2*n,'ground count',total,'M²',sum(k*k*v for k,v in h.items()))
print('FULL PHYSICAL ENERGY ENUMERATION: PASS')
