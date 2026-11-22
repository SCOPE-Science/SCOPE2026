"""Exact finite-field certificate for Pascal lines on the complete conic over F_5.

Requires Python 3 standard library only. All calculations use integer residues modulo 5.
The enumerations are exhaustive over 60 hexagons, 120 projectivities and 31 lines.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import json

Q = 5

def cross(a, b):
    return ((a[1]*b[2] - a[2]*b[1]) % Q,
            (a[2]*b[0] - a[0]*b[2]) % Q,
            (a[0]*b[1] - a[1]*b[0]) % Q)

def normalized(a):
    a = tuple(z % Q for z in a)
    assert any(a), "Unexpected zero projective vector"
    s = next(z for z in a if z)
    return tuple((z * pow(s, -1, Q)) % Q for z in a)

def incidence(line, point):
    return sum(a*b for a, b in zip(line, point)) % Q == 0

# Six rational points of XZ=Y^2, with 5 denoting infinity.
points = tuple((t*t % Q, t, 1) for t in range(Q)) + ((1, 0, 0),)
assert len(set(map(normalized, points))) == 6
assert all((p[0]*p[2]-p[1]*p[1])%Q == 0 for p in points)

def chord(i, j):
    assert i != j
    return normalized(cross(points[i], points[j]))

def canonical_cycle(s):
    s = tuple(s)
    return min(w[i:] + w[:i]
               for w in (s, s[::-1]) for i in range(6))

hexagons = sorted({canonical_cycle(s) for s in permutations(range(6))})
assert len(hexagons) == 60

def pascal(h):
    a,b,c,d,e,f = h
    x = normalized(cross(chord(a,b), chord(d,e)))
    y = normalized(cross(chord(b,c), chord(e,f)))
    z = normalized(cross(chord(c,d), chord(f,a)))
    assert x != y
    line = normalized(cross(x, y))
    assert incidence(line, x) and incidence(line, y) and incidence(line, z)
    return line

images = {h:pascal(h) for h in hexagons}
fibers = defaultdict(list)
for h, l in images.items(): fibers[l].append(h)
assert len(fibers) == 10
assert Counter(map(len, fibers.values())) == {6:10}

all_lines = {normalized(s) for s in product(range(Q), repeat=3) if any(s)}
assert len(all_lines) == 31
nonsecants = {l for l in all_lines if all(not incidence(l, p) for p in points)}
assert len(nonsecants) == 10
assert set(fibers) == nonsecants
assert all(l[0] != 0 and (l[1]**2-4*l[0]*l[2])%Q in (2,3) for l in fibers)

# Independently check the projectivity-orbit proof. A map (a t+b)/(c t+d)
# is determined up to scalar with ad-bc!=0.
projectivities = set()
for a,b,c,d in product(range(Q), repeat=4):
    if (a*d-b*c)%Q == 0: continue
    def mobius(x):
        if x == 5: return 5 if c == 0 else a*pow(c,-1,Q)%Q
        den = (c*x+d)%Q
        return 5 if den == 0 else (a*x+b)*pow(den,-1,Q)%Q
    projectivities.add(tuple(mobius(x) for x in range(6)))
assert len(projectivities) == 120
pending = set(hexagons)
orbits = []
while pending:
    h = min(pending)
    o = {canonical_cycle(tuple(s[x] for x in h)) for s in projectivities}
    assert o <= pending
    orbits.append(o)
    pending -= o
assert sorted(map(len, orbits)) == [10,20,30]

orbit_data = []
for o in orbits:
    representative = min(o)
    line = images[representative]
    disc = (line[1]*line[1] - 4*line[0]*line[2])%Q
    distribution = Counter(images[h] for h in o)
    assert set(distribution) == nonsecants
    assert set(distribution.values()) == {len(o)//10}
    orbit_data.append({"representative":list(representative),
                       "orbit_size":len(o),
                       "stabilizer_size":120//len(o),
                       "pascal_line":list(line),
                       "discriminant":disc,
                       "per_line_fiber":len(o)//10})
assert [(o['orbit_size'],o['pascal_line']) for o in orbit_data] == [
    (30,[1,1,1]),(20,[1,0,3]),(10,[1,3,4])]

all_points = {normalized(v) for v in product(range(Q),repeat=3) if any(v)}
assert len(all_points) == 31
multiplicities = Counter(sum(incidence(l,P) for l in fibers) for P in all_points)
assert multiplicities == {0:6,2:15,3:10}
assert {P for P in all_points if sum(incidence(l,P) for l in fibers)==0} == set(map(normalized,points))

pair_meetings = Counter(normalized(cross(l,m)) for l,m in combinations(sorted(fibers),2))
assert len(pair_meetings) == 25
assert Counter(pair_meetings.values()) == {1:15,3:10}
assert all(sum(incidence(l,P) for l in fibers) in (2,3) for P in pair_meetings)

certificate = {
    "field":"F5", "conic":"XZ=Y^2", "point_labels":"0..4 are t in F5; 5 is infinity",
    "ordered_rational_conic_points":[list(x) for x in points],
    "hexagon_count":len(hexagons), "projectivity_count":len(projectivities),
    "projectivity_orbits":orbit_data,
    "distinct_pascal_lines":len(fibers), "per_line_multiplicity":6,
    "nonsecant_line_count":len(nonsecants),
    "normalized_nonsecant_lines":[list(l) for l in sorted(nonsecants)],
    "incidence_point_multiplicities":dict(sorted((str(k),v) for k,v in multiplicities.items())),
    "crossings":{"ordinary_double":15,"ordinary_triple":10,"other":0},
    "hexagon_images":[{"cycle":list(h),"line":list(images[h])} for h in hexagons],
    "geometric_point_count_formula":"10*(5**n)-25 for n>=1",
    "geometric_complement_point_count_formula":"(5**n)**2-9*(5**n)+26 for n>=1"
}
if __name__ == "__main__":
    print(json.dumps(certificate, ensure_ascii=False, sort_keys=True, indent=2))
