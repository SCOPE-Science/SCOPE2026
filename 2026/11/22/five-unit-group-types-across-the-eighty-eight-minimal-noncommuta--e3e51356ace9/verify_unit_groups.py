"""Independent finite verification of the abstract unit-group census.

Parameter representatives are transcribed from Tables 1--3 and Propositions
4.1--4.2 of Abyzov--Lyubimtsev--Tuganbaev, arXiv:2611.16086v1.
No external Python modules or source files are required.
"""
from itertools import product
from collections import Counter, defaultdict

W, S1, S2 = 1, 2, 4

def dim(vectors):
    span={0}
    for v in vectors:
        span |= {s^v for s in list(span)}
    return (len(span).bit_length()-1)

def square(u,v,x):
    return ((u if x&1 else 0) ^ (v if x&2 else 0) ^ (W if x==3 else 0))

# This classifying signature is independent of the orbit calculation:
# (number of involutions, dimension of the Frattini subgroup).
def signature(u,v):
    return (8*sum(square(u,v,x)==0 for x in range(4)),dim((u,v,W)))

expected_signatures={(24,1):'H1',(16,2):'H2',(8,1):'H3',(8,2):'H4',(8,3):'H5'}

# Independently determine orbits of quadratic maps under GL(V) x GL(E)_W.
linear_GL2=[(a,b) for a in (1,2,3) for b in (1,2,3) if a!=b]
linear_GL3=[]
for c1,c2 in product(range(8),repeat=2):
    if dim((W,c1,c2))==3:
        linear_GL3.append(tuple((W if i&1 else 0)^(c1 if i&2 else 0)^(c2 if i&4 else 0) for i in range(8)))
assert len(linear_GL3)==24 and len(linear_GL2)==6

def orbit_rep(u,v):
    return min((f[square(u,v,a)],f[square(u,v,b)])
               for a,b in linear_GL2 for f in linear_GL3)

orbits=defaultdict(list)
for u,v in product(range(8),repeat=2):
    orbits[orbit_rep(u,v)].append((u,v))
assert len(orbits)==5 and sorted(map(len,orbits.values()))==[1,3,18,18,24]
for v in orbits.values():
    assert len({signature(*x) for x in v})==1
assert set(signature(u,v) for u,v in product(range(8),repeat=2))==set(expected_signatures)
assert all(len({orbit_rep(u,v) for u,v in product(range(8),repeat=2) if signature(u,v)==sig})==1 for sig in expected_signatures)

# All distinct ring class representatives. Each pair means squares A^2,B^2 in E.
family_one=[(0,2),(0,3),(1,0),(1,1),(0,0),(1,2),(2,0),(2,1),(2,2),(2,3)]
family_two_three=[(0,0),(1,1),(2,0),(2,1),(4,0),(4,1),(4,2),(6,2),(6,4)]
rows=[]
def include(label,char,u,v):
    rows.append((label,char,u,v,expected_signatures[signature(u,v)]))

for i,(u,v) in enumerate(family_one,1):include('F2_R1.'+str(i),2,u,v)
for i,(u,v) in enumerate(family_two_three,1):include('F2_R23.'+str(i),2,u,v)
for i,(u,v) in enumerate(family_one,1):include('F4_R1.'+str(i)+'_twounitcomm',4,u,v)
for i,(u,v) in enumerate(family_two_three,1):include('F4_R23.'+str(i)+'_twounitann',4,u,v)
for u,v in product(range(4),repeat=2):include('F4_e0=s2_'+str(u)+str(v),4,u,v)
for i,(u,v) in enumerate(family_one,1):include('F4_e0=c_R1.'+str(i),4,u^W,v^S1)

# In the remaining family c1=2*1, 2a=w, 2b=0. The source's Table 3.
table_three=[
 ((0,0,0,0),((0,0),(0,1),(1,1))),
 ((1,0,0,0),((0,0),(0,1),(1,1))),
 ((0,1,1,0),((0,0),(0,1))),
 ((1,1,1,0),((0,0),(0,1))),
 ((0,1,0,0),((0,0),(0,1))),
 ((0,0,1,0),((0,0),(1,0),(0,1),(1,1))),
 ((0,0,0,1),((0,0),(1,0))),
 ((1,0,0,1),((0,0),(1,0))),
 ((0,1,0,1),((0,0),(0,1))),
 ((1,0,1,1),((0,0),(1,0)))
]
for i,((l1,l2,l3,l4),choices) in enumerate(table_three):
    for alpha,beta in choices:
        u=(S1 if l1 else 0)^(S2 if l2 else 0)^alpha^W
        v=(S1 if l3 else 0)^(S2 if l4 else 0)^beta
        include('F4_e0=c1_'+str(i)+'_'+str(alpha)+str(beta),4,u,v)

assert len(rows)==88 and len({r[0] for r in rows})==88
assert Counter(c for _,c,*_ in rows)=={2:19,4:69}
counts=Counter(group for *_,group in rows)
assert counts=={'H1':13,'H2':28,'H3':7,'H4':26,'H5':14},counts
assert Counter((c,h) for _,c,_,_,h in rows)=={
(2,'H1'):3,(2,'H2'):6,(2,'H3'):2,(2,'H4'):5,(2,'H5'):3,
(4,'H1'):10,(4,'H2'):22,(4,'H3'):5,(4,'H4'):21,(4,'H5'):11}

# Multiplication of the 32-element central extension, not a ring-structure check.
def multiply(a,b,u,v):
    z,x,y=a; t,r,s=b
    return (z^t^(u if x and r else 0)^(v if y and s else 0)^(W if y and r else 0),x^r,y^s)
elements=list(product(range(8),(0,1),(0,1)))
identity=(0,0,0)
for u,v in ((0,0),(0,S1),(W,W),(W,S1),(S1,S2)):
    assert all(multiply(a,identity,u,v)==a==multiply(identity,a,u,v) for a in elements)
    assert all(multiply(multiply(a,b,u,v),c,u,v)==multiply(a,multiply(b,c,u,v),u,v)
               for a in elements for b in elements for c in elements)
    central=[a for a in elements if all(multiply(a,b,u,v)==multiply(b,a,u,v) for b in elements)]
    involutions=[a for a in elements if multiply(a,a,u,v)==identity]
    assert len(central)==8 and len(involutions)==signature(u,v)[0]
    assert all(multiply(a,multiply(a,multiply(a,a,u,v),u,v),u,v)==identity for a in elements)
print('CENTRALLY_ESSENTIAL_UNIT_GROUP_CENSUS_OK')
print('signature  group  char2  char4  total')
for sig,group in sorted(expected_signatures.items(),key=lambda kv:kv[1]):
    print(sig,group,sum(c==2 and h==group for _,c,_,_,h in rows),
          sum(c==4 and h==group for _,c,_,_,h in rows),counts[group])
