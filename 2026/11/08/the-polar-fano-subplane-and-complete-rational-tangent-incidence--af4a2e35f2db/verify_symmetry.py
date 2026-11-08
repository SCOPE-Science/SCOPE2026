"""Independent GF(8) presentation: group orbits, flexes, and polar Fano plane."""
from itertools import combinations

def m(a,b):
    # Distinct irreducible polynomial z^3+z^2+1, represented by 0b1101.
    r=0
    for i in range(3):
        for j in range(3):
            if (a>>i)&(b>>j)&1: r^=1<<(i+j)
    for i in (4,3):
        if r&(1<<i):r^=13<<(i-3)
    return r

def e(a,n):
    z=1
    for i in range(n):z=m(z,a)
    return z

def norm(v):
    k=next(a for a in v if a)
    return tuple(m(a,e(k,6)) for a in v)

def f(p):
    x,y,z=p
    return m(e(x,3),y)^m(e(y,3),z)^m(e(z,3),x)

def g(p):
    x,y,z=p
    return (m(e(x,2),y)^e(z,3), e(x,3)^m(e(y,2),z),e(y,3)^m(e(z,2),x))

def dot(l,p):return m(l[0],p[0])^m(l[1],p[1])^m(l[2],p[2])

def cross(p,q):
    return (m(p[1],q[2])^m(p[2],q[1]),m(p[2],q[0])^m(p[0],q[2]),m(p[0],q[1])^m(p[1],q[0]))

alpha=next(a for a in range(2,8) if e(a,3)^a^1==0)
assert alpha>1
P=(1,1,alpha)
assert f(P)==0
h=lambda p:(p[0],m(alpha,p[1]),m(e(alpha,5),p[2]))
sigma=lambda p:(p[1],p[2],p[0])
orbit={norm(P)}
queue=[norm(P)]
while queue:
    p=queue.pop()
    for op in (h,sigma):
        q=norm(op(p))
        if q not in orbit: orbit.add(q);queue.append(q)
assert len(orbit)==21 and all(f(p)==0 for p in orbit)
vertices={(1,0,0),(0,1,0),(0,0,1)}
C=orbit|vertices
assert len(C)==24
U={norm((u,e(u,4),e(u,2))) for u in range(1,8)}
assert len(U)==7 and U.isdisjoint(C)
assert all(g(p)==(0,0,0) for p in U)
# Seven U-points produce exactly seven different joining lines with P.
join={norm(cross(P,u)) for u in U}
assert len(join)==7
assert all(dot(g(P),u)!=0 for u in U)
assert all(dot(g((1,0,0)),u)!=0 for u in U)
# Check P flex contact: affine tangent parametrized Y=1+s, Z=alpha+delta*s.
delta=m(g(P)[1],e(g(P)[2],6))
assert delta!=0
assert all(f((1,1^t,alpha^m(delta,t)))==m(e(alpha,3),e(t,3))^m(e(alpha,4),e(t,4)) for t in range(8))
# At least threefold contact and not fourfold by exact coefficient extraction.
# For F(1,1+t,alpha+delta*t), constant and linear/quadratic coefficients vanish.
# Cubic coefficient is alpha^3 and quartic coefficient alpha^4, both nonzero.
assert delta==e(alpha,4)
# Any two U-points determine a Fano secant containing a third U-point.
secants={norm(cross(p,q)) for p,q in combinations(U,2)}
assert len(secants)==7 and all(sum(dot(l,u)==0 for u in U)==3 for l in secants)
assert not any(dot(l,P)==0 for l in secants)
assert not any(dot(l,(1,0,0))==0 for l in secants)
print('KLEIN_ALT_GF8_ORBIT_FLEX_PASS',alpha,len(C),len(orbit))
print('POLAR_FANO_AND_SECANT_TEST_PASS',len(U),len(secants),len(join))
