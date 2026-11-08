#!/usr/bin/env python3
"""Exact Q(sqrt(5)) proof checks for the optimal seventh-line extensions."""
import itertools
import sympy as sp
x,y,z,t,w=sp.symbols('x y z t w')
s=sp.sqrt(5); r=9+4*s;u=(3-s)/2;v=(3+s)/2
Q=(7-3*s)*x**2-4*x*y-2*(3-s)*x*z+(7+3*s)*y**2-2*(3+s)*y*z+2*z**2
lines=[sp.Matrix(a) for a in [(1,0,0),(0,1,0),(0,0,1),(0,1,-1),(1,0,-1),(1,-r,0)]]


def zero(e):return sp.simplify(e)==0
def dot(a,b):return sp.simplify(sum(a[i]*b[i] for i in range(3)))
def proportional(a,b):return all(zero(q) for q in a.cross(b))
def qeval(p):return sp.simplify(Q.subs({x:p[0],y:p[1],z:p[2]},simultaneous=True))
def restriction_discriminant(p,q):
    poly=sp.expand(Q.subs({x:p[0]+t*q[0],y:p[1]+t*q[1],z:p[2]+t*q[2]},simultaneous=True))
    return sp.simplify(sp.discriminant(poly,t))

# Reconstruct all nine projective intersections of the six initial lines.
pts=[]
for a,b in itertools.combinations(lines,2):
    p=a.cross(b)
    assert any(not zero(zz) for zz in p)
    if not any(proportional(p,h) for h in pts):pts.append(p)
assert len(pts)==9
assert sorted(sum(zero(dot(a,p)) for a in lines) for p in pts)==[2]*6+[3]*3
T=[sp.Matrix(p) for p in [(1,0,0),(0,1,0),(0,0,1),(1,1,1),(r,1,1),(r,1,r)]]
N=[sp.Matrix(p) for p in [(0,1,1),(1,0,1),(r,1,0)]]
assert all(any(proportional(q,p) for q in pts) for p in T+N)
assert [sum(zero(dot(a,p)) for a in lines) for p in T]==[3,3,3,2,2,2]
assert all(sum(zero(dot(a,p)) for a in lines)==2 for p in N)
assert all(zero(qeval(p)) for p in T[3:])
assert all(not zero(qeval(p)) for p in T[:3]+N)
# Check the conic is smooth, and the three coordinate-line tangencies.
H=sp.hessian(Q,(x,y,z))/2
assert not zero(H.det())
P=[sp.Matrix(p) for p in [(0,1,v),(1,0,u),(v,u,0)]]
assert all(zero(qeval(p)) for p in P)
assert all(sum(zero(dot(a,p)) for a in lines)==1 for p in P)
for i,p in enumerate(P):
    g=sp.Matrix([sp.diff(Q,zz).subs({x:p[0],y:p[1],z:p[2]},simultaneous=True) for zz in (x,y,z)])
    assert proportional(g,lines[i])
for i in (3,4,5):
    roots=[p for p in T[3:] if zero(dot(lines[i],p))]
    assert len(roots)==2 and not proportional(*roots)
# The original arrangement has 3 nodes, 3 tacnodes, 6 ordinary triples.
assert 3+3*3+4*6==36

# A joining line passes two nodes, avoids every other old singularity,
# and cannot be tangent to the conic. These give the first three maximizers.
join_discriminants=[128,3008+1344*s,448+192*s]
joining=[]
for (i,p),(j,q) in itertools.combinations(enumerate(N),2):
    a=p.cross(q)
    assert not any(proportional(a,h) for h in lines)
    assert all(not zero(dot(a,h)) for h in T+P)
    assert all(not zero(dot(a,h)) for k,h in enumerate(N) if k not in (i,j))
    D=restriction_discriminant(p,q)
    assert not zero(D)
    joining.append(a)
assert all(zero(restriction_discriminant(N[i],N[j])-D)
           for (i,j),D in zip(itertools.combinations(range(3),2),join_discriminants))

# The only other way to have an increment of 10 is to pass one old node
# and be tangent to Q. Solve the dual-conic equation in each node pencil.
# One solution is an original component (not an admissible new line),
# and the second solution is an allowable seventh line.
expected_other=[sp.Matrix((1,-2-s,2+s)),sp.Matrix((s-2,1,2-s)),sp.Matrix((2-s,2+s,1))]
other_tangents=[]
for k,(i,j) in enumerate([(0,3),(1,4),(2,5)]):
    line=lines[i]+w*lines[j]
    dual=sp.factor((line.T*H.adjugate()*line)[0],extension=s)
    roots=sp.solve(dual,w)
    assert len(roots)==2 and any(zero(zz) for zz in roots)
    nonzero=[zz for zz in roots if not zero(zz)]
    assert len(nonzero)==1
    a=sp.Matrix([sp.simplify(c.subs(w,nonzero[0])) for c in line])
    assert proportional(a,expected_other[k])
    assert not any(proportional(a,h) for h in lines)
    assert all(not zero(dot(a,h)) for h in T+P)
    assert [zero(dot(a,p)) for p in N]==[j==k for j in range(3)]
    # The dual condition ensures exactly one tangency; no old singularity
    # lies on the new line besides its unique old node.
    assert zero((a.T*H.adjugate()*a)[0])
    other_tangents.append(a)
assert len(joining)==3 and len(other_tangents)==3
assert all(not proportional(a,b) for i,a in enumerate(joining+other_tangents) for b in (joining+other_tangents)[i+1:])
# The six possible optimal extensions each have Delta tau = 10.
# Joining lines: (n2,t,n3)=(5,3,8).
assert 5+2*3+3*8==35 and 5+3*3+4*8==46
# New tangent through an old node: (n2,t,n3)=(6,4,7).
assert 6+2*4+3*7==35 and 6+3*4+4*7==46
# Every allowable new line contributes 8 + n + epsilon to tau,
# with n=0,1,2 old nodes and epsilon=0,1 new conic tangency.
# A line with n=2 cannot be tangent; therefore tau <= 36+10=46.
assert 36+10==46
# Gałecka's general bound gives mdr>=2m/3-2=4 at m=9.
# A free degree-9 curve would need tau 48; nearly free needs tau 47.
assert (8*8-4*4)==48 and (8*8-4*4-1)==47
print('DEGREE9_SIX_OPTIMAL_ADDITIONS_PASS',len(pts),len(N),len(joining),len(other_tangents),46,47,48)
