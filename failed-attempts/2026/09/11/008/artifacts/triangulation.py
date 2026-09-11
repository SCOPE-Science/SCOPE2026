# Substep 2: fix smooth triangulation of 4*Delta2 + regularity check (stdlib only).
import itertools
# Lattice points of 4Delta2
pts=[(i,j) for i in range(5) for j in range(5-i)]
print("n pts:", len(pts))
# Heights: strictly convex quadratic h=i^2+j^2+i*j (generic convex)
def h(p): i,j=p; return i*i+j*j+i*j
for p in pts: print(p, h(p))
# Candidate standard triangulation: slice by x=k,y=k,x+y=k lines.
# Small triangles: unit right triangles of legs 1. Enumerate explicitly:
tris=set()
for i in range(4):
    for j in range(4-i):
        # unit square-ish cell at (i,j): points (i,j),(i+1,j),(i,j+1),(i+1,j+1)/(i+2..) careful at boundary
        pass
# Build triangulation as all minimal triangles with vertices in pts, area 1/2,
# consistent with diagonal direction x+y=c? Let's instead compute regular triangulation
# induced by h via brute force: triangle (a,b,c) is a face of lower hull iff exists affine
# function l agreeing with h at a,b,c and strictly below h elsewhere.
import math
def area2(a,b,c): return abs((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1]))
cand=[]
for a,b,c in itertools.combinations(pts,3):
    if area2(a,b,c)!=1: continue
    # solve l(x,y)=ux+vy+w through h at a,b,c
    import fractions
    # linear solve 3x3 over rationals
    M=[[a[0],a[1],1],[b[0],b[1],1],[c[0],c[1],1]]; rhs=[h(a),h(b),h(c)]
    # Cramer/det
    def det3(M):
        return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    d=det3(M)
    if d==0: continue
    def repl(M,col,rhs):
        N=[r[:] for r in M]
        for k in range(3): N[k][col]=rhs[k]
        return det3(N)
    u=repl(M,0,rhs)/d; v=repl(M,1,rhs)/d; w=repl(M,2,rhs)/d
    ok=all(abs(u*x+v*y+w-h((x,y)))<1e-9 or (u*x+v*y+w<=h((x,y))-1e-9) for (x,y) in pts)
    tight=sum(1 for (x,y) in pts if abs(u*x+v*y+w-h((x,y)))<1e-9)
    if ok and tight==3:
        cand.append((a,b,c))
print("lower-hull unimodular faces:", len(cand))
for t in sorted(cand): print(t)
# check they tile 4Delta2 (area sum = 16/2=8)
print("total area:", sum(area2(*t) for t in cand)/2, "(expect 8)")
