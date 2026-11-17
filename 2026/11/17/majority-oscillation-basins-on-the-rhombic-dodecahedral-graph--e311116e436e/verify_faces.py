"""Face-symbol reduction and independent dynamics on a cubic/octahedral incidence graph.

Vertices are eight 3-bit cube corners and six oriented coordinate faces.
Run: python3 verify_faces.py
"""
from collections import Counter
from itertools import product

# Input face word a: bit 2*i+b gives the color of the face x_i=b.
def corner_colors_from_faces(a):
    result=0
    for corner in range(8):
        votes=sum((a>>(2*i+((corner>>i)&1)))&1 for i in range(3))
        result |= (votes>=2)<<corner
    return result

# Faces see four corners; exact 2:2 votes retain their previous own color.
def face_colors_from_corners(c,a):
    out=0
    for axis in range(3):
        for side in range(2):
            place=2*axis+side
            votes=sum((c>>v)&1 for v in range(8) if (v>>axis)&1==side)
            bit=1 if votes>=3 else (0 if votes<=1 else (a>>place)&1)
            out|=bit<<place
    return out

def update(pair):
    c,a=pair
    return corner_colors_from_faces(a),face_colors_from_corners(c,a)

# Any temporally 2-periodic state is identified by a pair (a,b) of face words:
# c0=C(b), c1=C(a), b=R(c0,a), a=R(c1,b).
periodic=set()
for a,b in product(range(64), repeat=2):
    c0=corner_colors_from_faces(b)
    c1=corner_colors_from_faces(a)
    if face_colors_from_corners(c0,a)==b and face_colors_from_corners(c1,b)==a:
        periodic.add((c0,a))
assert len(periodic)==412
assert all(update(update(x))==x for x in periodic)
fixed={x for x in periodic if update(x)==x}
assert len(fixed)==46
assert len(periodic-fixed)==366

# A direct (not table-lookup) mixed-radix phase iteration yields basins.
ent=Counter();rootbasin=Counter()
for c,a in product(range(256),range(64)):
    x=(c,a)
    count=0
    while x not in periodic:
        x=update(x)
        count+=1
        assert count<=5
    p=1 if x in fixed else 2
    ent[count,p]+=1
    root=min(x,update(x))
    rootbasin[root]+=1
assert [ent[t,1] for t in range(6)]==[46,2122,3360,2136,1368,192]
assert [ent[t,2] for t in range(6)]==[366,4682,1536,480,96,0]
assert sum(ent.values())==16384
assert Counter(rootbasin[x] for x in fixed)==Counter({13:12,73:24,74:8,3362:2})
assert Counter(rootbasin[x] for x in rootbasin if x not in fixed)==Counter({2:16,6:12,10:6,14:48,27:48,28:12,78:24,139:16,596:1})
print('face_pairs_tested=4096 two_periodic=412 fixed=46 two_phases=366')
print('face_pair_entry_fixed='+','.join(str(ent[t,1]) for t in range(6)))
print('face_pair_entry_two='+','.join(str(ent[t,2]) for t in range(6)))
print('total=16384 longest_transient=5')
print('fixed_orbit_basin_hist='+str(sorted(Counter(rootbasin[x] for x in fixed).items())))
print('two_orbit_basin_hist='+str(sorted(Counter(rootbasin[x] for x in rootbasin if x not in fixed).items())))
