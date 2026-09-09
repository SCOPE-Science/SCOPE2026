"""verify.py — independent replay from output/artifacts/polytope_table.json.
Checks, with exact integer arithmetic (no numpy/scipy):
 1. vertex integrality, full-dimensionality
 2. central symmetry about center2/2 (pairing within committed vertex set)
 3. normalized volume by merged-facet hull fan == committed normvol
 4. width attaining direction gives committed width (upper bound), and
    exhaustive primitive-direction search in box |u|_inf<=B finds same minimum
    (certificate of exact width within the recorded search bound; B=8 recorded)
 5. lattice-point count by bbox enumeration against exact facet half-spaces
    == committed npoints; every committed interior point strictly inside and
    count of strict-interior enumerated points == committed ninterior (=0)
 6. dilate counts t=0..3 == committed counts
Prints VERIFY_OK on success.
"""
import json, itertools, math, sys, os
from fractions import Fraction
_HERE = os.path.dirname(os.path.abspath(__file__))

def det3v(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0]) + a[2]*(b[0]*c[1]-b[1]*c[0]))
def sub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def hull_facets(V):
    n=len(V); pls={}
    for i,j,k in itertools.combinations(range(n),3):
        nn=cross(sub(V[j],V[i]),sub(V[k],V[i]))
        if nn==(0,0,0): continue
        d=dot(nn,V[i]); pls.setdefault((nn,d),[]).append((i,j,k))
    merged={}
    for (nn,d),tris in pls.items():
        g=math.gcd(math.gcd(abs(nn[0]),abs(nn[1])),abs(nn[2])); g=math.gcd(g,abs(d)) or 1
        q=(nn[0]//g,nn[1]//g,nn[2]//g,d//g)
        if q[0]<0 or (q[0]==0 and (q[1]<0 or (q[1]==0 and q[2]<0))):
            q=(-q[0],-q[1],-q[2],-q[3])
        s=set()
        for t in tris: s.update(t)
        merged.setdefault(q,set()).update(s)
    cx=sum(p[0] for p in V)/n; cy=sum(p[1] for p in V)/n; cz=sum(p[2] for p in V)/n
    out=[]
    for q,idxs in merged.items():
        nn=q[:3]; d=q[3]
        if nn[0]*cx+nn[1]*cy+nn[2]*cz>d: nn=(-nn[0],-nn[1],-nn[2]); d=-d
        if any(dot(nn,p)>d for p in V): continue  # cutting/non-supporting plane, not a facet
        out.append((nn,d,sorted(idxs)))
    # full-dimensionality: normals must span R^3
    M=[f[0] for f in out]
    assert any(det3v(M[i],M[j],M[k])!=0 for i in range(len(M)) for j in range(i+1,len(M)) for k in range(j+1,len(M))), "not full-dimensional"
    return out

def normvol(V,F):
    v0=V[0]; T=0
    for (nn,d,idxs) in F:
        if 0 in idxs: continue
        P=[V[i] for i in idxs]
        ax=max(range(3),key=lambda a:abs(nn[a])); others=[a for a in range(3) if a!=ax]
        c0=sum(p[others[0]] for p in P)/len(P); c1=sum(p[others[1]] for p in P)/len(P)
        ang=sorted(range(len(P)),key=lambda i:math.atan2(P[i][others[1]]-c1,P[i][others[0]]-c0))
        P=[P[i] for i in ang]
        for j in range(1,len(P)-1):
            T+=abs(det3v(sub(P[0],v0),sub(P[j],v0),sub(P[j+1],v0)))
    return T

def inside(x,F,strict=False):
    for (nn,d,_) in F:
        v=dot(nn,x)-d
        if strict:
            if v>=0: return False
        elif v>0: return False
    return True

def enum_pts(V,F,t=1):
    if t==0:
        return [(0,0,0)],[]
    W=[(t*p[0],t*p[1],t*p[2]) for p in V]
    F2=hull_facets(W)
    lo=[min(p[i] for p in W) for i in range(3)]; hi=[max(p[i] for p in W) for i in range(3)]
    pts=[(x,y,z) for x in range(lo[0],hi[0]+1) for y in range(lo[1],hi[1]+1) for z in range(lo[2],hi[2]+1) if inside((x,y,z),F2)]
    return pts,F2

def main():
    tab=json.load(open(os.path.join(_HERE, "polytope_table.json")))
    assert len(tab)==23, len(tab)
    vols=[]
    for e in tab:
        V=[tuple(p) for p in e["vertices"]]
        assert all(len(p)==3 and all(isinstance(c,int) for c in p) for p in V)
        c2=tuple(e["center2"])
        S=set(V)
        for p in V:
            assert (c2[0]-p[0],c2[1]-p[1],c2[2]-p[2]) in S, (e["name"],"sym fail")
        F=hull_facets(V)
        nv=normvol(V,F)
        assert nv==e["normvol"], (e["name"],nv,e["normvol"])
        vols.append(nv)
        u=tuple(e["width_dir"])
        vals=[dot(u,p) for p in V]
        assert max(vals)-min(vals)==e["width"]==1, e["name"]
        B=e["B"]; best=None
        R=range(-B,B+1)
        for w in itertools.product(R,R,R):
            if w==(0,0,0): continue
            if math.gcd(math.gcd(abs(w[0]),abs(w[1])),abs(w[2]))!=1: continue
            vs=[dot(w,p) for p in V]
            m=max(vs)-min(vs)
            if best is None or m<best: best=m
        assert best==e["search_width"]==1, (e["name"],best)
        pts,F2=enum_pts(V,F)
        assert len(pts)==e["npoints"], (e["name"],len(pts),e["npoints"])
        inte=[p for p in pts if inside(p,F2,strict=True)]
        assert len(inte)==e["ninterior"]==0, (e["name"],inte)
        assert e["hollow"] is True
        for t in ("0","1","2","3"):
            c,_=enum_pts(V,F,t=int(t))
            assert len(c)==e["counts"][t], (e["name"],t,len(c))
    assert sorted(vols)==list(range(4,49,2)), vols
    # width-1 => hollow lemma cross-check spot: all counts consistent
    print("VERIFY_OK: 23/23 rows (vols 4..48 even), symmetry+volume+width(B=8)+lattice/hollow+dilates all agree")
main()
