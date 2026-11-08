"""Exact plane-quartic and tangent-line incidence over GF(8). Pure Python."""
from collections import Counter

def mul(a,b):
    v=0
    while b:
        if b&1:v^=a
        b>>=1;a<<=1
        if a&8:a^=11
    return v

def power(a,n):
    v=1
    for _ in range(n): v=mul(v,a)
    return v

def dot(a,b): return mul(a[0],b[0])^mul(a[1],b[1])^mul(a[2],b[2])

def project(v):
    i=next(i for i,x in enumerate(v) if x)
    inv=power(v[i],6)
    return tuple(mul(inv,x) for x in v)

points=sorted({project((x,y,z)) for x in range(8) for y in range(8) for z in range(8) if x|y|z})
lines=points[:]
assert len(points)==len(lines)==73

def curve(p):
    x,y,z=p
    return mul(power(x,3),y)^mul(power(y,3),z)^mul(power(z,3),x)

def gradient(p):
    x,y,z=p
    return (mul(power(x,2),y)^power(z,3),power(x,3)^mul(power(y,2),z),power(y,3)^mul(power(z,2),x))

C={p for p in points if curve(p)==0}
U={p for p in points if gradient(p)==(0,0,0)}
assert len(C)==24 and len(U)==7 and C.isdisjoint(U)
formula_U={project((1,t,power(t,5))) for t in range(1,8)}
assert U==formula_U
assert all(curve(p)!=0 for p in U)
tangents=[project(gradient(p)) for p in C]
assert len(set(tangents))==24
U_hits=Counter(sum(dot(l,p)==0 for p in U) for l in lines)
assert U_hits=={0:24,1:42,3:7},U_hits
assert set(tangents)=={l for l in lines if all(dot(l,p)!=0 for p in U)}
fano_secants=[l for l in lines if sum(dot(l,p)==0 for p in U)==3]
assert len(fano_secants)==7
assert all(all(dot(l,p)!=0 for l in fano_secants) for p in C)
incidence={p:sum(dot(l,p)==0 for l in tangents) for p in points}
assert Counter(incidence.values())=={0:7,2:24,4:42}
assert {p for p,n in incidence.items() if n==0}==U
assert {p for p,n in incidence.items() if n==2}==C
assert all(sum(dot(l,p)==0 for p in C)==2 for l in tangents)
print('KLEIN_GF8_EXACT_TANGENT_PASS',len(points),len(C),len(set(tangents)),len(U))
print('FANO_LINE_INTERSECTIONS_PASS',dict(sorted(U_hits.items())))
print('TANGENT_INCIDENCE_SPECTRUM_PASS',dict(sorted(Counter(incidence.values()).items())))
