# Substep 3 (bounded): dual tropical curve from triangulation + grid search for bitangent vertex.
from fractions import Fraction as Q
pts=[(i,j) for i in range(5) for j in range(5-i)]
def h(p): i,j=p; return i*i+j*j+i*j
tris=[((0,0),(0,1),(1,0)),((0,1),(0,2),(1,1)),((0,1),(1,0),(1,1)),((0,2),(0,3),(1,2)),
((0,2),(1,1),(1,2)),((0,3),(0,4),(1,3)),((0,3),(1,2),(1,3)),((1,0),(1,1),(2,0)),
((1,1),(1,2),(2,1)),((1,1),(2,0),(2,1)),((1,2),(1,3),(2,2)),((1,2),(2,1),(2,2)),
((2,0),(2,1),(3,0)),((2,1),(2,2),(3,1)),((2,1),(3,0),(3,1)),((3,0),(3,1),(4,0))]
# dual vertex of triangle = solution to l=h at its 3 pts
def dual_vertex(t):
    (a,b,c)=t
    import sympy as sp
    u,v,w=sp.symbols('u v w')
    sol=sp.solve([u*a[0]+v*a[1]+w-h(a),u*b[0]+v*b[1]+w-h(b),u*c[0]+v*c[1]+w-h(c)],[u,v,w])
    return (sol[u],sol[v])
verts={t:(float(dual_vertex(t)[0]),float(dual_vertex(t)[1])) for t in tris}
for t in sorted(verts): print(t, verts[t])
# edges: pairs of triangles sharing an edge -> segment between dual vertices
def edges_of(t):
    a,b,c=t; return [tuple(sorted(e)) for e in [(a,b),(b,c),(a,c)]]
from collections import defaultdict
emap=defaultdict(list)
for t in tris:
    for e in edges_of(t): emap[e].append(t)
print("interior edges:", sum(1 for e,v in emap.items() if len(v)==2))
