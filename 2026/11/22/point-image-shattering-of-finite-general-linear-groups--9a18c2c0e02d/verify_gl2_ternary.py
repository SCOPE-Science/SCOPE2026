"""Independent enumeration of point-image traces for GL_2 over F_3."""
from itertools import combinations, product
q=3
V=[(a,b) for a,b in product(range(q),repeat=2) if (a,b)!=(0,0)]
def det(a,b):return (a[0]*b[1]-a[1]*b[0])%q
maps=[]
for a,b in product(V,repeat=2):
    if det(a,b)==0:continue
    maps.append({x:tuple((x[0]*a[j]+x[1]*b[j])%q for j in range(2)) for x in V})
assert len(maps)==48
cells=list(product(V,V));counts=[1,0,0]
for k in (1,2):
    for subset in combinations(range(len(cells)),k):
        pairs=[cells[i] for i in subset]
        row=[p[0] for p in pairs]; col=[p[1] for p in pairs]
        independently=(k==1 or (det(*row)!=0 and det(*col)!=0))
        traces={sum(1<<j for j,(x,y) in enumerate(pairs) if g[x]==y) for g in maps}
        shat=len(traces)==(1<<k)
        assert shat==independently,subset
        counts[k]+=shat
assert counts==[1,64,1152],counts
print('GL2_TERNARY_SHATTER_PASS',counts)
