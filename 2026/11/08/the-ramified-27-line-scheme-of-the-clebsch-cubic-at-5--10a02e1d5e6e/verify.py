#!/usr/bin/env python3
"""Exact arithmetic checks for the integral Clebsch cubic line calculation.
Only Python's standard library is required. Finite enumeration is used solely
for explicit identities and a rational-field cross-check, not geometric exhaustiveness.
"""
from itertools import product, combinations, permutations

P = 5

def normalize(v):
    v = tuple(a % P for a in v)
    assert any(v)
    scale = pow(next(a for a in v if a), -1, P)
    return tuple((scale*a) % P for a in v)

def wedge(u,v):
    return normalize([u[i]*v[j]-u[j]*v[i] for i in range(5) for j in range(i+1,5)])

def is_line(u,v):
    return all(sum((u[i]**(3-j)*v[i]**j) for i in range(5)) % P == 0
               for j in range(4))

# R[t]/(t^2+t-1) represented as (constant,t coefficient).
def mul(x,y):
    a,b=x; c,d=y
    return (a*c+b*d, a*d+b*c-b*d)
def cube(x):
    return mul(mul(x,x),x)
def add(*args):
    return tuple(sum(z[i] for z in args) for i in (0,1))
def scale(a,x):
    return (a*x[0], a*x[1])

t=(0,1)
s=[(2,0),t,(-1,-1),(-1,-1),t]
a=[(0,0),(1,0),t,(0,-1),(-1,0)]
assert add(*s)==(0,0) and add(*a)==(0,0)
# Four coefficients of the cubic restriction
assert add(*(cube(x) for x in s))==(0,0)
assert add(*(scale(3,mul(mul(s[i],s[i]),a[i])) for i in range(5)))==(0,0)
assert add(*(scale(3,mul(s[i],mul(a[i],a[i]))) for i in range(5)))==(0,0)
assert add(*(cube(x) for x in a))==(0,0)
# Pluecker coordinates p_01=2, p_02=2*t identify the full ramified order.
def minor(i,j): return add(mul(s[i],a[j]),scale(-1,mul(s[j],a[i])))
assert minor(0,1)==(2,0) and minor(0,2)==(0,2)
# The 120 coordinate permutations yield twelve generic lines over K.
def pluecker_over_K(a1,b1):
    return tuple(add(mul(a1[i],b1[j]),scale(-1,mul(a1[j],b1[i])))
                 for i in range(5) for j in range(i+1,5))
def same_line_in_K(v,w):
    j=next(i for i in range(len(v)) if v[i]!=(0,0))
    return all(mul(v[i],w[j])==mul(w[i],v[j]) for i in range(len(v)))
unique_K=[]
for perm in permutations(range(5)):
    pp=pluecker_over_K([s[i] for i in perm],[a[i] for i in perm])
    if not any(same_line_in_K(pp,z) for z in unique_K): unique_K.append(pp)
assert len(unique_K)==12
from collections import Counter
specialization = Counter(normalize([(x[0]+2*x[1])%P for x in z]) for z in unique_K)
assert len(specialization)==6 and set(specialization.values())=={2}
print('twelve_generic_lines_specialize_two_to_each_of_six_lines_OK')
print('generic_line_on_cubic_and_pluecker_generator_OK')

# Six basepoints of the characteristic-five nodal projection.
def q(a,b,c):
    d=(-a-b-c)%P
    return (a*a+b*b+c*c+d*d)%P
def cubic(a,b,c):
    d=(-a-b-c)%P
    return (a**3+b**3+c**3+d**3)%P
points=set()
for u in product(range(P),repeat=3):
    if any(u):
        v=normalize(u)
        if q(*v)==0 and cubic(*v)==0: points.add(v)
assert len(points)==6
assert all((u[0]+u[1])*(u[0]+u[2])*(u[1]+u[2])%P==0 for u in points)
for line_pts in combinations(points,3):
    v1,v2,v3=line_pts
    determinant=(v1[0]*(v2[1]*v3[2]-v2[2]*v3[1])-v1[1]*(v2[0]*v3[2]-v2[2]*v3[0])+v1[2]*(v2[0]*v3[1]-v2[1]*v3[0]))%P
    assert determinant!=0
print('six_reduced_rational_conic_basepoints_no_three_collinear_OK', sorted(points))

unit=(1,1,1,1,1)
base=(0,1,2,3,4)
new={wedge(unit,pi) for pi in set(permutations(base))}
assert len(new)==6
assert all(is_line(unit,pi) for pi in set(permutations(base)))
old=set()
for k in range(5):
    remain=[i for i in range(5) if i!=k]
    for first in combinations(remain,2):
        other=[i for i in remain if i not in first]
        u=[0]*5;v=[0]*5
        u[first[0]]=1;u[first[1]]=-1
        v[other[0]]=1;v[other[1]]=-1
        old.add(wedge(u,v))
        assert is_line(u,v)
assert len(old)==15 and not(old&new)
print('old_15_new_6_distinct_rational_lines_OK')

# Independent exhaustive rational Grassmannian check (806 F_5 lines).
projective_points=set()
for z in product(range(P),repeat=4):
    if any(z): projective_points.add(normalize(tuple(z)+((-sum(z))%P,)))
assert len(projective_points)==156
seen={}; on_surface=set()
for u,v in combinations(sorted(projective_points),2):
    key=wedge(u,v)
    if key not in seen:
        seen[key]=(u,v)
        if is_line(u,v): on_surface.add(key)
assert len(seen)==806
assert on_surface==old|new
print('enumeration_806_F5_lines_exactly_21_on_surface_OK')

# The ring of integers R[t]/(t^2+t-1) has special fibre F_5[e]/e^2, e=t-2.
assert (2*2+2-1)%P == 0 and (2*2+1)%P==0
print('six_ramified_quadratic_branches_each_reduce_to_dual_numbers_OK')
print('CHECK_OK')
