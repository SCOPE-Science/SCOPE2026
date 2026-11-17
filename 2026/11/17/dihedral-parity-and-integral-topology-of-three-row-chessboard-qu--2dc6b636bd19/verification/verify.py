#!/usr/bin/env python3
"""Reconstructs the ordinary orbit CW chain complex of a 3-by-n chessboard.
Requires Python 3 and sympy; no network or external data.
"""
from itertools import combinations, permutations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def independent_faces(n):
    # Canonical ordering is by row, so no orbit action reverses orientation.
    all_faces=[[] for _ in range(3)]
    for k in range(1,4):
        for rows in combinations(range(3),k):
            for cols in permutations(range(n),k):
                all_faces[k-1].append(tuple(zip(rows,cols)))
    return all_faces

def image(face,n,shift,sign):
    return tuple((r,(sign*c+shift)%n) for r,c in face)

def build(n):
    original=independent_faces(n)
    group=[(shift,sign) for sign in (1,-1) for shift in range(n)]
    orbitmaps=[];reps=[]
    for faces in original:
        seen={};orbit_reps=[]
        for face in faces:
            if face in seen:continue
            orbit={image(face,n,*g) for g in group}
            rep=min(orbit)
            ix=len(orbit_reps)
            orbit_reps.append(rep)
            for x in orbit: seen[x]=ix
        reps.append(orbit_reps);orbitmaps.append(seen)
    d1=Matrix.zeros(len(reps[0]),len(reps[1]))
    d2=Matrix.zeros(len(reps[1]),len(reps[2]))
    for j,edge in enumerate(reps[1]):
        for a in range(2):
            face=edge[:a]+edge[a+1:]
            d1[orbitmaps[0][face],j]+=(-1)**a
    for j,tri in enumerate(reps[2]):
        for a in range(3):
            face=tri[:a]+tri[a+1:]
            d2[orbitmaps[1][face],j]+=(-1)**a
    assert d1*d2==Matrix.zeros(*((len(reps[0]),len(reps[2]))))
    diag=smith_normal_form(d2,domain=ZZ)
    pivots=[abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i]]
    assert len(pivots)==len(reps[1])-2
    assert sorted(x for x in pivots if x>1)==([] if n%2 else [2])
    assert len(reps)==3
    f=[len(x) for x in reps]
    F=n*n-6*n+8
    h2=f[2]-len(pivots)
    expected_h2=((n-3)**2//2) if n%2 else (n*n-6*n+6)//2
    assert h2==expected_h2
    assert f==[3,3*((n-1)//2 if n%2 else n//2),(n-1)*(n-2)//2]
    assert f[0]-f[1]+f[2]==((F+3)//2 if n%2 else F//2)
    return n,f, sorted(x for x in pivots if x>1),h2

if __name__=='__main__':
    for n in range(5,13):
        n,f,torsion,h2=build(n)
        print('n=%d orbit_cells=%s H1_torsion=%s H2_rank=%d' % (n,f,torsion,h2))
    print('THREE_ROW_CHESSBOARD_DIHEDRAL_QUOTIENT_PASS n=5..12')
