#!/usr/bin/env python3
"""Reproducible finite checks for critical cyclic Vietoris--Rips fixed spaces.
Scientific theorem and normalization are documented in RESULT.md.
"""
from itertools import combinations
from math import gcd

def dist(u,v,n):
    return min((u-v)%n,(v-u)%n)

def full_orbit_partition(n,perm):
    remaining=set(range(n)); orbits=[]
    while remaining:
        x=min(remaining); orbit={x}; y=perm(x)
        while y not in orbit:
            orbit.add(y); y=perm(y)
        assert y==x
        remaining-=orbit;orbits.append(frozenset(orbit))
    return orbits

def fixed_orbit_graph(n,r,perm):
    orbits=full_orbit_partition(n,perm)
    allowed=[o for o in orbits if all(dist(a,b,n)<=r for a,b in combinations(o,2))]
    edge=set()
    for i,j in combinations(range(len(allowed)),2):
        if all(dist(u,v,n)<=r for u in allowed[i] for v in allowed[j]):edge.add(frozenset((allowed[i],allowed[j])))
    return set(allowed),edge

def predicted_reflection_graph(r,a):
    n=3*r;h=r//2
    if r%2:
        assert a==0
        A=[frozenset([i,(-i)%n]) for i in range(h+1)]
        B=[frozenset([3*h+1-j,3*h+2+j]) for j in range(h+1)]
        cross={(A[0],B[h])}
    elif a==0:
        A=[frozenset([i,(-i)%n]) for i in range(h+1)]
        B=[frozenset([3*h-j,3*h+j]) for j in range(h+1)]
        cross={(A[0],B[h]),(A[h],B[0])}
    else:
        assert a==1
        A=[frozenset([(-i)%n,1+i]) for i in range(h)]
        B=[frozenset([3*h-j,3*h+1+j]) for j in range(h)]
        cross=set()
    verts=set(A+B)
    edges={frozenset((u,v)) for group in (A,B) for u,v in combinations(group,2)}
    edges|={frozenset(t) for t in cross}
    return verts,edges

def ranks_mod_two(vertices,edges):
    verts=sorted(vertices,key=lambda x:(min(x),len(x)))
    idmap={v:i for i,v in enumerate(verts)}
    E={frozenset((idmap[u],idmap[v])) for u,v in (tuple(edge) for edge in edges)}
    simplices=[]
    for k in range(1,len(verts)+1):
        layer=[t for t in combinations(range(len(verts)),k) if all(frozenset((i,j)) in E for i,j in combinations(t,2))]
        if not layer:break
        simplices.append(layer)
    rk=[]
    for k in range(1,len(simplices)):
        faces={face:i for i,face in enumerate(simplices[k-1])}; piv={}
        for face in simplices[k]:
            vec=0
            for i in range(k+1):vec^=(1<<faces[face[:i]+face[i+1:]])
            while vec:
                p=vec.bit_length()-1
                if p in piv:vec^=piv[p]
                else:piv[p]=vec;break
        rk.append(len(piv))
    result=[]
    for k,layer in enumerate(simplices):
        betti=len(layer)-(rk[k-1] if k else 0)-(rk[k] if k<len(rk) else 0)-(1 if k==0 else 0)
        result.append(betti)
    return result

def main():
    rotations=reflections=graphs=faces=0
    for r in range(2,25):
        n=3*r
        for k in range(1,n):
            actual,_=fixed_orbit_graph(n,r,lambda x,k=k:(x+k)%n)
            if k in (r,2*r):
                assert len(actual)==r
                assert all(len(o)==3 for o in actual)
                _,ed=fixed_orbit_graph(n,r,lambda x,k=k:(x+k)%n)
                assert not ed
            else:assert not actual,(r,k,actual)
            rotations+=1
        for a in range(n):
            actual=fixed_orbit_graph(n,r,lambda x,a=a:(a-x)%n)
            canonical= a%2 if r%2==0 else 0
            expected=predicted_reflection_graph(r,canonical)
            # Translating coordinates by t conjugates reflection a to canonical.
            t=((a-canonical)//2) if n%2==0 else ((a*pow(2,-1,n))%n)
            transformed=(set(frozenset((v+t)%n for v in o) for o in expected[0]),
                         set(frozenset(frozenset((v+t)%n for v in o) for o in edge) for edge in expected[1]))
            assert actual==transformed,(r,a,actual,transformed)
            reflections+=1
        for a in ([0,1] if r%2==0 else [0]):
            vs,es=fixed_orbit_graph(n,r,lambda x,a=a:(a-x)%n)
            if r<=12:
                got=ranks_mod_two(vs,es)
                if r%2:want=[0]
                elif a==0:want=[0,1]
                else:want=[1]
                assert got[:len(want)]==want and not any(got[len(want):]),(r,a,got,want)
                faces+=sum(got)
            graphs+=1
    print('ALL_CRITICAL_DIHEDRAL_CHECKS_OK')
    print('critical_parameters=23 rotation_elements=%d reflection_elements=%d orbit_graphs=%d homology_witness_sum=%d'%(rotations,reflections,graphs,faces))
    print('verified critical orbit-graph identities exactly for 2<=r<=24 and every dihedral element')
    print('verified reduced F2 homology for canonical reflections 2<=r<=12')
if __name__=='__main__':main()
