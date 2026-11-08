#!/usr/bin/env python3
"""Exact F_719 stabilizer check for a 20-point branch configuration."""
from itertools import permutations
p=719
parameters=(2,3,4,5,6)
roots=tuple(t for t in range(p) if any((((t*t+1)**2-4*a*t*t)%p)==0 for a in parameters))
expected=(9,22,58,62,80,98,313,317,323,325,394,396,402,406,621,639,657,661,697,710)
assert roots==expected and len(set(roots))==20

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%p

def projectivity(xys):
    rows=[[x,1,-x*y,-y] for x,y in xys]
    v=tuple(((-1)**j*det3([[r[i] for i in range(4) if i!=j] for r in rows]))%p for j in range(4))
    if (v[0]*v[3]-v[1]*v[2])%p==0:return None
    factor=pow(next(z for z in v if z),-1,p)
    return tuple(z*factor%p for z in v)

def maps_set(m):
    a,b,c,d=m
    s=set(roots)
    for t in roots:
        den=(c*t+d)%p
        if not den:return False
        if ((a*t+b)*pow(den,-1,p))%p not in s:return False
    return True

x0,x1,x2=roots[:3]
accepted=set()
triples=0
for y0,y1,y2 in permutations(roots,3):
    triples+=1
    z=projectivity(((x0,y0),(x1,y1),(x2,y2)))
    if z and maps_set(z):accepted.add(z)
assert triples==6840
expected_maps={(1,0,0,1),(1,0,0,p-1),(0,1,1,0),(0,1,p-1,0)}
assert accepted==expected_maps,(accepted,expected_maps)
print('BRANCH_ROOTS',len(roots),'ORDERED_TRIPLES',triples,'REDUCED_GROUP_ORDER',len(accepted))
print('CERTIFICATE_OK')
