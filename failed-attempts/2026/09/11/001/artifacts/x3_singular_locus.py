"""Fallback-block certificate: X_3 singular locus enumeration (audited tuple compare).
F=x^4+y^4-z^4-w^4+x^2y^2-z^2w^2; grad=(4x^3+2xy^2,4y^3+2x^2y,-4z^3-2zw^2,-4w^3-2z^2w).
"""
import json
def F(x,y,z,w): return x**4+y**4-z**4-w**4+x*x*y*y-z*z*w*w
def g(x,y,z,w): return (4*x**3+2*x*y*y,4*y**3+2*x*x*y,-4*z**3-2*z*w*w,-4*w**3-2*z*z*w)
aff=[(x,y,z,w) for x in range(3) for y in range(3) for z in range(3) for w in range(3)
     if (x,y,z,w)!=(0,0,0,0) and F(x,y,z,w)%3==0 and tuple(v%3 for v in g(x,y,z,w))==(0,0,0,0)]
print("singular affine reps:",len(aff))
# projective classes under [v]~[2v]
seen=set(); proj=[]
for p in aff:
    q=tuple((2*c)%3 for c in p)
    key=min(tuple(p),tuple(q))
    if key not in seen: seen.add(key); proj.append(list(p))
print("distinct projective singular pts:",len(proj))
for p in proj: print(p)
# spot check
assert len(aff)==24 and len(proj)==12
print("X3_SINGULAR_OK: fallback criterion (i) at p=3 impossible; X_3 has 12 singular projective points")
