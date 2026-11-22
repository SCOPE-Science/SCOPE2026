#!/usr/bin/env python3
"""Finite independently recomputed relative faces and sequential toggle matching."""
from itertools import combinations
from collections import Counter

def new_faces(n,i):
    a,b=i,n+i+1
    edges={tuple(sorted(x)) for x in ([(j,j+n) for j in range(n)]+[(j,j+1) for j in range(n-1)]+[(j+n,j+n+1) for j in range(n-1)]+[(a,b)])}
    adjacent=lambda x,y:tuple(sorted((x,y))) in edges
    vertices=[v for v in range(2*n) if v not in (a,b)]
    old_neighbors={a,b}
    forbidden=[v for v in vertices if not adjacent(v,a) and not adjacent(v,b)]
    result=set()
    for r in (1,2,3):
        for w in combinations(vertices,r):
            if not any(v in forbidden for v in w): continue
            face=(a,b)+w
            if any(not (adjacent(x,y) or adjacent(x,z) or adjacent(y,z)) for x,y,z in combinations(face,3)): continue
            result.add(sum(1<<v for v in face))
    return result

def check(n,i):
    faces=new_faces(n,i); allfaces=set(faces)
    a,b=i,n+i+1
    verts=[v for v in range(2*n) if v not in (a,b)]
    # All positions: process the nearer core vertices first, breaking ties rightward.
    distance=lambda v:min(abs(v%n-i),abs(v%n-i-1))
    for v in sorted(verts,key=lambda v:(distance(v),-(v%n),v//n)):
        for f in sorted(tuple(faces)):
            g=f|(1<<v)
            if not (f>>v&1) and g in faces:
                faces.remove(f);faces.remove(g)
    actual=Counter(f.bit_count()-1 for f in faces)
    assert actual=={4:n-2},(n,i,actual)
    return len(allfaces),len(faces)

def main():
    count=0; maxfaces=0
    for n in range(3,13):
        for i in range(n-1):
            total,critical=check(n,i); count+=1; maxfaces=max(total,maxfaces)
        print(f"n={n}: {n-1} diagonal positions, relative critical 4-cells={n-2}, pass")
    print(f"checked={count}; maximum_relative_faces={maxfaces}; status=PASS")

if __name__=='__main__': main()
