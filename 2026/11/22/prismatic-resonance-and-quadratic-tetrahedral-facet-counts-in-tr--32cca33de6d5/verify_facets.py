"""Finite floating-point cross-check of the two-edge contacts and cap face structure."""
from cmath import exp
from math import cos, pi

EPS = 1e-8
OMEGA = exp(2j*pi/3)


def caps(n):
    triangles = [tuple(exp(2j*pi*(k/3 + t/n)) for k in range(3)) for t in range(2)]
    faces = {frozenset((t,k) for k in range(3)) for t in range(2)}
    for triangle in triangles:
        for j in range(3):
            # Outward unit normal to the edge between consecutive triangle vertices.
            normal = triangle[j] + triangle[(j+1)%3]
            face = set()
            for t, tri in enumerate(triangles):
                values = [(normal.conjugate()*v).real for v in tri]
                h = max(values)
                face.update((t,k) for k, v in enumerate(values) if abs(h-v)<EPS)
            faces.add(frozenset(face))
    neighbors = {(t,k):set() for t in range(2) for k in range(3)}
    # Each edge is the two-vertex intersection of two distinct faces.
    for f in faces:
        for g in faces:
            if f != g and len(f & g)==2:
                u,v = f & g
                neighbors[u].add(v)
                neighbors[v].add(u)
    return sorted(map(len, faces)), sorted(map(len, neighbors.values()))


def check(n):
    roots = [exp(2j*pi*k/n) for k in range(n)]
    normals = [exp(-1j*(2*k+1)*pi/n) for k in range(n)]
    height = cos(pi/n)
    contacts = [0,0,0]
    for w0 in normals:
        for w1 in normals:
            w2 = -OMEGA*w0 - OMEGA**2*w1
            dots = [(w2*z).real for z in roots]
            if max(dots) <= height+EPS:
                hits = sum(abs(v-height)<EPS for v in dots)
                assert hits < 3
                contacts[hits] += 1
    assert contacts == [n*((n-1)//3), 0, n*(1+(n%3==0))], (n,contacts)
    face_sizes, degrees = caps(n)
    if n==3:
        assert face_sizes == [3,3,4,4,4] and degrees == [3]*6
        shape = 'prism'
    else:
        assert face_sizes == [3]*8 and degrees == [4]*6
        shape = 'octahedron'
    print(n, 'two-edge tetrahedra', 3*contacts[0], shape, contacts[2])


for n in range(3,81):
    check(n)
print('PASS 3 <= n <= 80')
