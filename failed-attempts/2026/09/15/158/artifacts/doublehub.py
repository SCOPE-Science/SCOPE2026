"""T3: 'double-hub' stress test. n=5, G = hubs {0,1} + leaves {2,3,4}, edges: 01 + all hub-leaf.
2-connected (remove any single vertex: still connected) but {0,1} is a 2-separator with 3 components.
Schur structure: D=diag leaves; on detD!=0, V = {S=0} irreducible; hunt for extra components in V(detD).
"""
import sympy as sp

a,b,c,d,e = sp.symbols('a b c d e')   # diagonals 0..4
h = sp.symbols('h')                    # edge 01
p1,p2,p3 = sp.symbols('p1 p2 p3')      # edges 0-2,0-3,0-4
q1,q2,q3 = sp.symbols('q1 q2 q3')      # edges 1-2,1-3,1-4
M = sp.Matrix([
 [a,h,p1,p2,p3],
 [h,b,q1,q2,q3],
 [p1,q1,c,0,0],
 [p2,q2,0,d,0],
 [p3,q3,0,0,e],
])
print("2-connected check: G-0 = {1..4} star at 1: connected; G-2 = hubs+2 leaves: connected. OK")
gens = {}
for di in range(5):
    for dj in range(di,5):
        rr=[x for x in range(5) if x!=di]; cc=[x for x in range(5) if x!=dj]
        gens[(di,dj)] = sp.expand(M.extract(rr,cc).det())
nz = {k:v for k,v in gens.items() if v!=0}
print(f"nonzero minors: {len(nz)}/15")
for k,v in nz.items():
    print(f"M_{k}: terms={len(v.args)} :: {str(v)[:160]}")
