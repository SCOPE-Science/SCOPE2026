"""Exact dual-Hesse conic and numerical consistency checks over Q(zeta)."""
from itertools import combinations

zero, one, zeta = (0,0), (1,0), (0,1)


def add(p,q):
    return (p[0]+q[0],p[1]+q[1])


def sub(p,q):
    return (p[0]-q[0],p[1]-q[1])


def mul(p,q):
    a,b=p; c,d=q
    return (a*c-b*d,a*d+b*c-b*d)


def cross(p,q):
    return tuple(sub(mul(p[(i+1)%3],q[(i+2)%3]),
                     mul(p[(i+2)%3],q[(i+1)%3])) for i in range(3))


def conic(x,y,z):
    return add(add(mul(x,x),mul((2,0),mul(y,y))),mul((3,0),mul(z,z)))


R=[one,zeta,mul(zeta,zeta)]
assert len(set(R))==3 and all(mul(t,mul(t,t))==one for t in R)
lines=[]
for t in R:
    nt=sub(zero,t)
    lines.extend([(one,nt,zero),(zero,one,nt),(nt,zero,one)])
    t2=mul(t,t)
    # Diagonal quadratic coefficients other than 3, 1, 2, respectively.
    assert all(c!=zero for c in [add(t2,(2,0)),add(mul((2,0),t2),(3,0)),
                                 add(one,mul((3,0),t2))])

points=[]; counts=[]
for l,k in combinations(lines,2):
    p=cross(l,k)
    assert any(c!=zero for c in p) and conic(*p)!=zero
    i=next((i for i,q in enumerate(points) if cross(p,q)==(zero,)*3),len(points))
    if i==len(points):
        points.append(p); counts.append(0)
    counts[i]+=1
assert len(points)==12 and counts==[3]*12

B=2*len(lines)-2*len(points); C=2; r=2*len(lines)
genus=1+(3*(-2)+2*r)//2
square=3*2**2-r
grades=[sum(max(0,-1-(2*k-i)) for i in (0,6,12)) for k in range(7)]
assert (genus,square,grades)==(16,-6,[16,12,8,5,3,1,0])
e=1+3*(3-(B+C-r))+B-r+r
e_cover=3*(3-B)+B
e_res=e_cover-len(points)+r
assert e==e_res-(-len(points)+(2-2*genus-1))==70
milnor=9*(9**2-4*9+6)-e-len(points)*8
assert milnor==341+3*C-3*r==293
print('36 line pairs, 12 triple points, 18 transverse branch intersections')
print('genus, square, normal-bundle h1:',genus,square,grades)
print('Euler and vertex Milnor consistency:',e,milnor)
