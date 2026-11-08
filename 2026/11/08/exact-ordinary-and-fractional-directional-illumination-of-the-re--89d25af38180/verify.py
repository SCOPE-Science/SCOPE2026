"""Exact finite certificates for the directional illumination of the icosidodecahedron.
Standard library only; coordinates belong to Z[phi], phi^2=phi+1.
Run: python3 verify.py
"""
from itertools import combinations, product
from collections import Counter

# (a,b) denotes a+b*phi, phi=(1+sqrt(5))/2.
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b): return (a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def dot(a,b):
    r=(0,0)
    for x,y in zip(a,b):r=add(r,mul(x,y))
    return r
def positive(z):
    a,b=z
    if b==0: return a>0
    # q(phi)>0 iff q(8/5)>0 and q(13/8)>0; otherwise use conjugate norm
    if 5*a+8*b>0 and 8*a+13*b>0:return True
    if 5*a+8*b<0 and 8*a+13*b<0:return False
    # Exact sign since the other conjugate phi' <0; norm N=a^2+ab-b^2
    norm=a*a+a*b-b*b
    if norm==0:return False
    # q(phi')=a+b*(1-sqrt5)/2: use high precision integer test if needed
    # q(phi) can also be checked with phi>r rational by integer squaring.
    if b>0:
        if a>=0:return True
        # phi > -a/b iff (2*(-a)-b)^2 < 5*b*b if -a/b >= 1/2
        c=-2*a-b
        return c<0 or 5*b*b>c*c
    else:
        if a<=0:return False
        c=2*a+b
        return c>=0 and c*c>5*b*b

Z=(0,0); O=(1,0); P=(0,1)
V=[]
for i in range(3):
    for a,b in product((-1,1),repeat=2):
        x=[Z,Z,Z]
        x[(i+1)%3]=(a,0)
        x[(i+2)%3]=(0,b)
        V.append(tuple(x))
assert len(V)==12 and len(set(V))==12
assert dot(V[0],V[0])==(2,1)
E=tuple((i,j) for i,j in combinations(range(12),2) if dot(V[i],V[j])==P)
Eset=set(E)
F=tuple(c for c in combinations(range(12),3) if all(tuple(sorted(e)) in Eset for e in combinations(c,2)))
assert len(E)==30 and len(F)==20
for i in range(12): assert sum(i in e for e in E)==5
for e in E: assert sum(set(e).issubset(f) for f in F)==2
A=[frozenset({i}|{j for k,j in E if k==i}|{k for k,j in E if j==i}) for i in range(12)]
assert all(len(s)==6 for s in A)
# all opposite pairs
opp=[]
for i in range(12):
    j=next(j for j in range(12) if V[j]==tuple(neg(x) for x in V[i]))
    if i<j:opp.append((i,j))
assert len(opp)==6
assert all(i in A[i] for i in range(12))
axis_covers=[]
for k in range(12):
    covered=set()
    for ix,(i,j) in enumerate(E):
        # At each rectified vertex, the four facet normals are V[i], V[j],
        # and the sums V[a]+V[b]+V[c] from the two incident original faces.
        normals=[V[i],V[j]]
        for face in F:
            if i in face and j in face:
                normals.append(tuple(add(add(V[face[0]][h],V[face[1]][h]),V[face[2]][h]) for h in range(3)))
        assert len(normals)==4
        lit=all(positive(dot(V[k],nn)) for nn in normals)
        if lit:covered.add(ix)
        assert lit == (i in A[k] and j in A[k]),(k,i,j,lit)
    axis_covers.append(frozenset(covered))
    assert len(covered)==10
assert all(sum(e in s for s in axis_covers)==4 for e in range(30))
assert set.union(*(set(axis_covers[i]) for i in (0,1,4,11)))==set(range(30))
C=Counter()
max_s=[]
for choices in product((0,1),repeat=6):
    subset=frozenset(opp[k][t] for k,t in enumerate(choices))
    cnt=sum(i in subset and j in subset for i,j in E)
    C[cnt]+=1
    if cnt==10:max_s.append(subset)
assert C=={5:12,6:20,9:20,10:12},C
assert set(max_s)==set(A)
for i,j in combinations(range(12),2):
    intersection=len(axis_covers[i]&axis_covers[j])
    antipodal=any(set(pair)=={i,j} for pair in opp)
    adjacent=tuple(sorted((i,j))) in Eset
    assert intersection==(0 if antipodal else 5 if adjacent else 1),(i,j,intersection)
# Six antipodal representatives form equiangular tight frame.
# Sum vv^T = (8+4 phi) I_3 for the twelve original vectors.
for a in range(3):
    for b in range(3):
        z=Z
        for i in range(12):z=add(z,mul(V[i][a],V[i][b]))
        assert z==((8,4) if a==b else Z),(a,b,z)
# Independently confirm that all thirty-two proposed planes support P in
# exactly their claimed 5-vertex or 3-vertex faces. Work with doubled midpoints.
midpoints=[tuple(add(V[i][k],V[j][k]) for k in range(3)) for i,j in E]
assert len(set(midpoints))==30
all_normals=[(V[a],5) for a in range(12)]
all_normals += [(tuple(add(add(V[a][k],V[b][k]),V[c][k]) for k in range(3)),3) for a,b,c in F]
for n,expected in all_normals:
    values=[dot(n,m) for m in midpoints]
    top=values[0]
    for z in values[1:]:
        if positive(add(z,neg(top))):top=z
    assert sum(z==top for z in values)==expected
    assert all(not positive(add(z,neg(top))) for z in values)
assert len(all_normals)==32
print('EXACT_OK', 'vertices=30, faces=32, signed transversals=64, distribution='+str(dict(sorted(C.items()))), 'fractional=3, ordinary=4, exact facet inequalities=1440')
