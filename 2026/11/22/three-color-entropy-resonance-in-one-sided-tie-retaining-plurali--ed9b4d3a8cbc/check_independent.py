"""Independent specification check: direct plurality ballot and exhaustive recurrent DAG."""
from itertools import product
from collections import Counter

def ballot(x):
    n=len(x);z=[]
    for i in range(n):
        a,b,c=x[i],x[(i+1)%n],x[(i+2)%n]
        tally=Counter((a,b,c))
        top=max(tally.values()); winners=[v for v,k in tally.items() if k==top]
        z.append(winners[0] if len(winners)==1 else a)
    return tuple(z)

def form(x):
    n=len(x)
    return tuple(x[(i+1)%n] if x[(i+1)%n]==x[(i+2)%n] else x[i] for i in range(n))

C=0
for q,ns in [(2,range(3,11)),(3,range(3,11)),(4,range(3,8)),(5,range(3,7))]:
    for n in ns:
        for x in product(range(q),repeat=n):
            assert ballot(x)==form(x),(q,n,x)
            C+=1
print('PASS direct three-ballot implementation matches algebraic local rule on',C,'complete configurations')

# A 3-color trajectory with one doubled color and a singleton string
for n in range(3,30):
    x=(0,0)+tuple(1+(i%2) for i in range(n-2))
    for t in range(n-2):
        assert len(set(x))>1 and x!=ballot(x)
        x=ballot(x)
    assert x==(0,)*n
print('PASS sharp transient witness for every n=3,...,29')
