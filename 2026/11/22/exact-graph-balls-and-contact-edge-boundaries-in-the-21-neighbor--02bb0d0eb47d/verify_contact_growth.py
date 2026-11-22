"""Exact combinatorial and rational-coordinate checks for a central triangular subdivision.

Run: python3 verify_contact_growth.py
Uses only the Python standard library. These finite checks corroborate, but do not
replace, the all-radius geometric and counting proof.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations

STEP = ((1, 0), (0, 1), (1, -1))
STEPS = STEP + tuple((-x, -y) for x, y in STEP)


def dist(u, v):
    x, y = u[0] - v[0], u[1] - v[1]
    return max(abs(x), abs(y), abs(x + y))


def add(u, w):
    return u[0] + w[0], u[1] + w[1]


def edge(u, v):
    return tuple(sorted((u, v)))


def outer_edges(S):
    return {edge(v, add(v, w)) for v in S for w in STEPS}


def exact_ball(r):
    k = r - 1
    S = {(x, y) for x in range(-k-1, k+3)
         for y in range(-k-1, k+2)
         if min(dist((x, y), (0, 0)), dist((x, y), (1, 0))) <= k}
    return S, outer_edges(S)


def det(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def onsegment(p, a, b):
    return det(a, b, p) == 0 and all(min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1))


def intersects_segment(a, b, c, d):
    x1, x2, y1, y2 = det(a, b, c), det(a, b, d), det(c, d, a), det(c, d, b)
    if x1 == x2 == 0:
        return any(onsegment(p, c, d) for p in (a, b)) or any(onsegment(p, a, b) for p in (c, d))
    return x1*x2 <= 0 and y1*y2 <= 0


def inside_triangle(p, tri):
    signed = [det(tri[i], tri[(i+1)%3], p) for i in range(3)]
    return min(signed) >= 0 or max(signed) <= 0


def triangles_intersect(A, B):
    return (any(inside_triangle(p, B) for p in A)
            or any(inside_triangle(p, A) for p in B)
            or any(intersects_segment(A[i], A[(i+1)%3], B[j], B[(j+1)%3])
                   for i in range(3) for j in range(3)))


def face_tiles(a, b, c):
    center = tuple((Fraction(a[i])+Fraction(b[i])+Fraction(c[i]))/3 for i in range(2))
    return [(edge(u, v), tuple((tuple(map(Fraction, u)), tuple(map(Fraction, v)), center)))
            for u, v in ((a,b), (b,c), (c,a))]


def geometry_check():
    tiles=[]
    for x in range(-2, 3):
        for y in range(-2, 3):
            a=(x,y); b=(x+1,y); c=(x,y+1); d=(x+1,y+1)
            tiles.extend(face_tiles(a,b,c))
            tiles.extend(face_tiles(b,c,d))
    pairs=0
    for (e,A),(f,B) in combinations(tiles,2):
        geo=triangles_intersect(A,B)
        inc=bool(set(e).intersection(f))
        assert geo == inc,(e,f,geo,inc)
        pairs+=1
    return len(tiles),pairs


def graph_check():
    # For two copies per lattice edge, adjacency is sharing a lattice endpoint.
    # Independent breadth-first search on the finite induced ball of surrounding edges.
    R=12
    S={(x,y) for x in range(-R,R+2) for y in range(-R,R+2)}
    edges=outer_edges(S)
    incid={v:[] for e in edges for v in e}
    for e in edges:
        for v in e: incid[v].append(e)
    root=edge((0,0),(1,0))
    start=(root,0)
    visited={start:0}; q=deque([start])
    while q:
        e,s=q.popleft(); d=visited[(e,s)]
        if d>=8: continue
        adjacent=set(incid[e[0]]+incid[e[1]])
        for f in adjacent:
            for t in (0,1):
                p=(f,t)
                if p == (e,s) or p in visited:continue
                visited[p]=d+1
                q.append(p)
    for r in range(1,9):
        b=sum(d<=r for d in visited.values())
        assert b==18*r*r+6*r-2,(r,b)
    for r in range(1,8):
        inside={p for p,d in visited.items() if d<=r}
        cut=0
        for e,s in inside:
            adjacent=set(incid[e[0]]+incid[e[1]])
            cut+=sum((f,t) not in inside for f in adjacent for t in (0,1) if (f,t)!=(e,s))
        assert cut==192*r-8,(r,cut)
    return len(visited)


def arithmetic_check():
    for k in range(0,61):
        S,E=exact_ball(k+1)
        assert len(S)==3*k*k+5*k+2,(k,len(S))
        assert len(E)==9*k*k+21*k+11,(k,len(E))
        polygon={(x,y) for x in range(-k-1,k+3) for y in range(-k-1,k+2)
                 if -k<=x<=k+1 and -k<=y<=k and -k<=x+y<=k+1}
        assert polygon==S,k
    return 61


if __name__=='__main__':
    n,p=geometry_check()
    m=arithmetic_check()
    v=graph_check()
    print('PASS: exact triangle-intersection/contact checks:',n,'tiles,',p,'pairs')
    print('PASS: exact lattice-ball and incident-edge counts:',m,'radii')
    print('PASS: independently enumerated contact-graph BFS:',v,'visited vertices')
