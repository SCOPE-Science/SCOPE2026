"""Exact reproducible Ehrhart count for the explicitly listed 8-polytope.
Python 3 standard library only. No external data or packages needed.
"""
from collections import Counter
from itertools import combinations
from math import comb, gcd
from functools import reduce

VERTICES = [
(6,-6,0),(4,0,-2),(3,1,-2),(3,0,0),(3,0,-3),
(2,1,-1),(2,-2,2),(1,1,-1),(1,0,1),(1,-1,2),
(0,0,-3),(0,-1,2),(0,-3,3),(0,-6,0),(0,-6,-6),
(-1,0,0),(-1,0,-1),(-1,-2,2),(-2,-1,-1),(-2,-2,-2),(-3,-3,0),
]


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))

def facets_from_all_triples():
    facets=set()
    for a,b,c in combinations(VERTICES,3):
        u=cross(minus(b,a),minus(c,a))
        g=reduce(gcd,u,0)
        if not g:continue
        u=tuple(t//g for t in u)
        h=dot(u,a)
        vals=[dot(u,v) for v in VERTICES]
        if min(vals)<h<max(vals): continue
        if min(vals)==h and max(vals)>h:
            u=tuple(-t for t in u);h=-h
            vals=[-t for t in vals]
        assert max(vals)==h and h>0
        facets.add((*u,h))
    return sorted(facets)

def oriented_ccw_hull(points):
    # Return planar convex hull vertices, dropping collinear boundary points.
    pts=sorted(set(points))
    def o(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[]
    for p in pts:
        while len(lower)>=2 and o(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    upper=[]
    for p in pts[::-1]:
        while len(upper)>=2 and o(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def exact_normalized_volume(facets):
    vol=0
    for f in facets:
        u=f[:3];h=f[3]
        members=[v for v in VERTICES if dot(u,v)==h]
        # Project to coordinate pair not containing a nonzero normal component.
        drop=next(i for i,x in enumerate(u) if x)
        rem=[j for j in range(3) if j!=drop]
        xy={tuple(v[j] for j in rem):v for v in members}
        poly=oriented_ccw_hull(xy)
        assert len(poly)>=3
        a=xy[poly[0]]
        for i in range(1,len(poly)-1):
            vol+=abs(det(a,xy[poly[i]],xy[poly[i+1]]))
    return vol

def shells(facets,max_k=8):
    # All lattice points of max_k Q lie in its coordinate bounding box.
    vmin=[min(v[i] for v in VERTICES)*max_k for i in range(3)]
    vmax=[max(v[i] for v in VERTICES)*max_k for i in range(3)]
    S=Counter()
    for x in range(vmin[0],vmax[0]+1):
        for y in range(vmin[1],vmax[1]+1):
            for z in range(vmin[2],vmax[2]+1):
                # Every height divides 6; the gauge times 6 is integral.
                ell=max((6*(a*x+b*y+c*z))//h for a,b,c,h in facets)
                if 0<=ell<=6*max_k:S[ell]+=1
    return [S[i] for i in range(6*max_k+1)]

def ehrhart_counts(s):
    max_l=len(s)-1
    conv=[0]*(2*max_l+1)
    for i,a in enumerate(s):
        for j,b in enumerate(s):conv[i+j]+=a*b
    cumulative=[];total=0
    for val in conv:
        total+=val;cumulative.append(total)
    ans=[]
    for k in range(9):
        count=0
        for m in range(3*k+1):
            for n in range(2*k+1):
                t=6*k-2*m-3*n
                if t>=0:count+=cumulative[t]
        ans.append(count)
    return ans

def run():
    F=facets_from_all_triples()
    assert len(F)==37
    assert {h for *u,h in F}=={1,3,6}
    assert len(VERTICES)==21
    assert exact_normalized_volume(F)==1071
    for v in VERTICES:
        normals=[u for *u,h in F if dot(u,v)==h]
        assert any(det(*t)!=0 for t in combinations(normals,3))
    s=shells(F)
    assert sum(s)==94577
    L=ehrhart_counts(s)
    expect_L=[1,4206,254471,3793683,28466361,142125171,541690094,1703589231,4639992475]
    assert L==expect_L,(L,expect_L)
    hstar=[sum((-1)**j*comb(9,j)*L[i-j] for j in range(i+1)) for i in range(9)]
    expect=[1,4197,216653,1654776,3130992,1654776,216653,4197,1]
    assert hstar==expect,(hstar,expect)
    assert hstar==hstar[::-1]
    assert sum(hstar)==6*1071**2==6882246
    # Palindromic reciprocal substitution yields quartic q(x).
    def q(x):return x**4+4197*x**3+216649*x**2+1642185*x+2697688
    endpoints=[(-5000,-4000),(-50,-40),(-7,-6),(-3,-2)]
    assert all(q(a)*q(b)<0 and b<=-2 for a,b in endpoints)
    gamma=[1,4189,191491,825921,246354]
    polys=[[comb(8-2*j,k-j) if 0<=k-j<=8-2*j else 0 for k in range(9)] for j in range(5)]
    assert [sum(gamma[j]*polys[j][k] for j in range(5)) for k in range(9)]==hstar
    print('PASS: 37 exact facets, 21 extreme vertices, volume(Q3)=1071')
    print('PASS: exact lattice shells',s)
    print('PASS: L_P8(k), k=0,...,8',L)
    print('PASS: hstar',hstar,'normalized volume',sum(hstar))
    print('PASS: quartic signs',[(a,q(a),b,q(b)) for a,b in endpoints])
    print('PASS: eight simple negative roots and gamma vector',gamma)

if __name__=='__main__': run()
