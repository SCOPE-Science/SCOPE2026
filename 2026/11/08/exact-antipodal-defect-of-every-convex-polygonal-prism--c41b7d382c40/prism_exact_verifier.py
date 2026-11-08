"""Exact rational/integer validation for antipodal vertex/edge-midpoint counts of polygonal prisms.
Run with Python 3. No third-party packages required.
"""
from itertools import combinations
import random


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def convex_hull(points):
    ps=sorted(set(points))
    if len(ps)<3:
        return []
    lower=[]
    for q in ps:
        while len(lower)>=2 and cross(lower[-2],lower[-1],q)<=0:
            lower.pop()
        lower.append(q)
    upper=[]
    for q in reversed(ps):
        while len(upper)>=2 and cross(upper[-2],upper[-1],q)<=0:
            upper.pop()
        upper.append(q)
    return lower[:-1]+upper[:-1]


def boundary(hull, d):
    # For a point known to be in a CCW polygon, it is on its boundary iff
    # at least one exact supporting-edge determinant vanishes.
    ds=[cross(hull[i],hull[(i+1)%len(hull)],d) for i in range(len(hull))]
    assert all(z>=0 for z in ds), (hull,d,ds)
    return any(z==0 for z in ds)


def pair_count(points, dhull):
    return sum(boundary(dhull, (u[0]-v[0],u[1]-v[1])) or abs(u[2]-v[2])==4
               for u,v in combinations(points,2))


def test(Q):
    n=len(Q)
    assert n>=3
    assert convex_hull(Q)==Q, Q  # Counterclockwise, no superfluous vertices.
    edges=[(Q[(i+1)%n][0]-Q[i][0],Q[(i+1)%n][1]-Q[i][1]) for i in range(n)]
    p=sum(e[0]*f[1]-e[1]*f[0]==0 for e,f in combinations(edges,2))
    D=convex_hull([(2*(a[0]-b[0]),2*(a[1]-b[1])) for a in Q for b in Q])
    verts=[(2*x,2*y,z) for z in (-2,2) for x,y in Q]
    mids=[]
    for z in (-2,2):
        for i in range(n):
            a,b=Q[i],Q[(i+1)%n]
            mids.append((a[0]+b[0],a[1]+b[1],z))
    mids += [(2*x,2*y,0) for x,y in Q]
    assert len(mids)==3*n
    A=pair_count(verts,D)
    B=pair_count(mids,D)
    assert (A,B)==(n*n+2*n+2*p,n*n+3*n+7*p),(n,p,A,B)
    assert 2*n-1-A+B==3*n-1+5*p
    return n,p,A,B,3*n-1+5*p


def main():
    cases=[
       [(0,0),(4,0),(0,5)],
       [(0,0),(4,0),(4,5),(0,5)],
       [(0,0),(5,0),(4,3),(1,3)],
       [(0,0),(5,0),(4,3),(0,4)],
       [(0,0),(5,0),(6,3),(4,6),(1,5)],
       [(-2,-1),(0,-2),(2,-1),(2,1),(0,2),(-2,1)],
       [(-3,-1),(-1,-3),(1,-3),(3,-1),(3,1),(1,3),(-1,3),(-3,1)],
    ]
    seen=set()
    for q in cases:
        outcome=test(q);seen.add((outcome[0],outcome[1]))
    rng=random.Random(17831)
    checks=len(cases)
    for _ in range(180):
        points=[(rng.randint(-25,25),rng.randint(-25,25)) for i in range(rng.randint(6,35))]
        q=convex_hull(points)
        if len(q)<3:continue
        outcome=test(q)
        seen.add((outcome[0],outcome[1]));checks+=1
    print('PRISM_ANTIPODAL_EXACT_OK',checks,'distinct (n,p)',sorted(seen))


if __name__=='__main__':main()
