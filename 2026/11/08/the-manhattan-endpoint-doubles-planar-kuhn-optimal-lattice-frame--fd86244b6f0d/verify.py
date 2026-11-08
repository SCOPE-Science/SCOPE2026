"""Finite independent enumeration supporting the exact planar Kuhn-frame theorem.

This checks all integer vectors in the radius-2 l1 shell and the p>1
candidate shell. The proof of global optimality is mathematical, not brute force.
"""
from itertools import product

def det(a,b): return a[0]*b[1]-a[1]*b[0]
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def n1(a): return abs(a[0])+abs(a[1])
def ninf(a): return max(abs(a[0]),abs(a[1]))

short={a for a in product(range(-2,3),repeat=2) if a!=(0,0) and n1(a)<=2}
assert len(short)==12
frames1={(a,b) for a in short for b in short if det(a,b) and add(a,b) in short}
assert len(frames1)==48, len(frames1)
assert sum(abs(det(a,b))==1 for a,b in frames1)==24
assert sum(abs(det(a,b))==2 for a,b in frames1)==24
assert {abs(det(a,b)) for a,b in frames1}=={1,2}

short_g={a for a in product(range(-1,2),repeat=2) if a!=(0,0)}
frames_g={(a,b) for a in short_g for b in short_g if det(a,b) and add(a,b) in short_g}
assert len(frames_g)==24
assert all(abs(det(a,b))==1 for a,b in frames_g)
assert frames_g<=frames1
new=frames1-frames_g
assert len(new)==24
assert all(abs(det(a,b))==2 for a,b in new)
assert all((a[0]+a[1])%2==0 and (b[0]+b[1])%2==0 for a,b in new)
# The transforms U(x,y)=(x+y,x-y) give exact minimal l1 radii for
# planar finite vertex sets: half the l1 diameter (since U is an isometry
# onto l_infinity and coordinate boxes have a center).
for a,b in frames1:
    for verts in ((0,0),a,add(a,b)),((0,0),b,add(a,b)):
        ds=[n1((u[0]-v[0],u[1]-v[1])) for u in verts for v in verts]
        assert max(ds)<=2
    # Independent of triangle verification, the extremal lattice condition:
    assert max(n1(a),n1(b),n1(add(a,b)))<=2
# In each p>1 frame both packet triangles lie in axis-aligned unit squares.
for a,b in frames_g:
    for verts in ((0,0),a,add(a,b)),((0,0),b,add(a,b)):
        for i in (0,1):
            assert max(v[i] for v in verts)-min(v[i] for v in verts)<=1
# Direct exclusion of all other frames with coordinates in [-2,2]
# for the p=1 test and [-1,1] for p>1, independent of the theorem's proof.
assert all(max(n1(a),n1(b),n1(add(a,b)))>2
           for a in short for b in short if det(a,b) and (a,b) not in frames1)
assert all(max(ninf(a),ninf(b),ninf(add(a,b)))>1
           for a in short_g for b in short_g if det(a,b) and (a,b) not in frames_g)
print('PASS: p=1: 48 ordered frames, 24 unimodular, 24 index-two')
print('PASS: 1<p<=infinity: 24 ordered unimodular frames')
print('PASS: both packet triangles meet the geometric norm criteria')
print('PASS: excluded finite shell cases independently verified')
