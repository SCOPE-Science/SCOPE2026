"""Exact incidence and topological-arithmetic checks for a normal nonic model.

This checker is supplementary to the geometric proof; it does not certify
that a resolution is minimal or that the global Euler arguments apply.
"""
from itertools import combinations
from collections import Counter

P = 13
ZETA = 3
assert pow(ZETA, 3, P) == 1 and ZETA != 1

def normalize(v):
    v = tuple(i % P for i in v)
    for x in v:
        if x:
            inv = pow(x, -1, P)
            return tuple((t * inv) % P for t in v)
    raise AssertionError('zero vector')

def cross(a, b):
    return normalize((a[1]*b[2]-a[2]*b[1],
                      a[2]*b[0]-a[0]*b[2],
                      a[0]*b[1]-a[1]*b[0]))

def scalar(a, b):
    return sum(i*j for i,j in zip(a,b)) % P

roots = [pow(ZETA, i, P) for i in range(3)]
lines = ([(1, (-z)%P, 0) for z in roots]
         + [(0, 1, (-z)%P) for z in roots]
         + [((-z)%P, 0, 1) for z in roots])
assert len(set(map(normalize, lines))) == 9
points = Counter(cross(a,b) for a,b in combinations(lines,2))
assert len(points) == 12 and all(v == 3 for v in points.values())
assert sum(points.values()) == 36
assert all(sum(scalar(line,p)==0 for line in lines)==3 for p in points)

# A concrete characteristic-zero conic is validated by a good reduction.
# All conditions below are polynomial nonvanishing conditions with integer data.
def Q(pt):
    x,y,z = pt
    return (x*x+2*y*y+3*z*z) % P
assert (1*2*3) % P != 0
assert all(Q(pt) for pt in points)
assert len(points) == 12
# The nine restrictions are diagonal binary quadratics, each with both
# coefficients nonzero, hence have two simple geometric roots.
for z in roots:
    assert (z*z+2) % P and 3 % P
    assert (2*z*z+3) % P and 1 % P
    assert (1+3*z*z) % P and 2 % P

branch_lines = 9
triple_points = 12
branch_intersection = 18
base_euler = 3
branch_euler = 2*branch_lines - 2*triple_points
conic_euler = 2
complement_euler = base_euler - (branch_euler+conic_euler-branch_intersection)
surface_euler = 3*complement_euler + (branch_euler-branch_intersection) + branch_intersection + 1
assert (branch_euler, complement_euler, surface_euler) == (-6,25,70)

# The exceptional curve is a degree-three cover of a conic with 18 totally
# ramified points.  The source divisor square is 12, with 18 blowups.
degree = 3
ramified = 18
r_h = degree*(-2) + ramified*(degree-1)
genus = (r_h+2)//2
self_intersection = degree*2*2 - ramified
assert (genus,self_intersection) == (16,-6)

smooth_nonic_euler = 9*(9*9-4*9+6)
mu_at_twelve_cubic_cones = 12*(3-1)**3
mu_vertex = smooth_nonic_euler - surface_euler - mu_at_twelve_cubic_cones
assert (smooth_nonic_euler,mu_at_twelve_cubic_cones,mu_vertex) == (459,96,293)

# Independent Euler route through the weighted cyclic triple-plane model.
cyclic_plane_euler = 3*(base_euler-branch_euler) + branch_euler
minimal_cyclic_resolution_euler = cyclic_plane_euler - triple_points
blown_up_resolution_euler = minimal_cyclic_resolution_euler + ramified
resolution_to_surface_euler_change = triple_points*(0-1) + ((2-2*genus)-1)
assert (cyclic_plane_euler,minimal_cyclic_resolution_euler,blown_up_resolution_euler) == (21,9,27)
assert blown_up_resolution_euler-resolution_to_surface_euler_change == surface_euler

# Splitting of the cyclic cover and the normal-line-bundle cohomology.
def h1_on_P1(n):
    return max(0,-n-1)
normal_grades = [h1_on_P1(2*k)+h1_on_P1(2*k-6)+h1_on_P1(2*k-12) for k in range(7)]
assert normal_grades == [16,12,8,5,3,1,0]
assert sum(normal_grades) == 45

print('PASS: twelve triple points and nondegenerate conic witness over F13')
print('PASS: degree-three ramification, genus 16, self-intersection -6')
print('PASS: e(S)=70, total Milnor sum 389, vertex Milnor number 293')
print('PASS: independent resolution Euler calculation')
print('PASS: normal-bundle cohomology dimensions 16,12,8,5,3,1')
