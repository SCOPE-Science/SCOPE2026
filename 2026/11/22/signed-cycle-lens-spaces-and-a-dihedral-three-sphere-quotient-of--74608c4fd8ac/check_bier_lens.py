#!/usr/bin/env python3
"""Exact cellular check for a five-label balanced Bier sphere C10 orbit."""
from itertools import combinations
from collections import Counter
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
N=5

def action(v,k):
    i,sign=v%N, v//N
    return (i+k)%N+N*((sign+k)%2)

def g_face(f,k):
    return tuple(sorted(action(v,k) for v in f))

def parity(vals):
    return (-1)**sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))

def sign_to_sorted(f,k):
    arr=[action(v,k) for v in f]
    return parity(arr)

faces_by_dim=[]
for k in range(1,5):
    fs=[]
    for f in combinations(range(10),k):
        plus={v for v in f if v<5}
        minus={v-5 for v in f if v>=5}
        if len(plus)<=2 and len(minus)<=2 and not(plus & minus): fs.append(f)
    faces_by_dim.append(fs)

reps=[]
rep_of=[]
for dim,faces in enumerate(faces_by_dim):
    ro={}; reprs=[]
    for f in faces:
        orbit=[g_face(f,j) for j in range(10)]
        rr=min(orbit)
        if rr not in reprs: reprs.append(rr)
        j=next(j for j in range(10) if g_face(rr,j)==f)
        assert all(g_face(rr,l)!=f for l in range(j+1,10))
        ro[f]=(rr,sign_to_sorted(rr,j))
        assert len(set(orbit))==10, (dim,f)
    reprs.sort()
    reps.append(reprs); rep_of.append(ro)

boundaries=[]
for dim in range(1,4):
    froms=reps[dim]; tos=reps[dim-1]; tid={f:i for i,f in enumerate(tos)}
    d=Matrix.zeros(len(tos),len(froms))
    for j,f in enumerate(froms):
        for i in range(len(f)):
            sub=f[:i]+f[i+1:]
            rr,sgn=rep_of[dim-1][sub]
            d[tid[rr],j]+=(-1)**i * sgn
    boundaries.append(d)
for i in (0,1): assert boundaries[i]*boundaries[i+1]==Matrix.zeros(boundaries[i].rows,boundaries[i+1].cols)
assert [len(s) for s in faces_by_dim] == [10,40,60,30]
assert [len(s) for s in reps] == [1,4,6,3]
assert boundaries[0] == Matrix.zeros(1,4)
assert boundaries[1].rank()==4
assert boundaries[2].rank()==2
S=smith_normal_form(boundaries[1],domain=ZZ)
assert [abs(S[i,i]) for i in range(min(S.rows,S.cols))] == [1,1,1,10]
# For the dimension-three chain map every nontrivial power is fixed-point-free.
assert all(all(g_face(f,k)!=f for f in sum(faces_by_dim,[]) ) for k in range(1,10))
# Characteristic polynomial of rotation in the real standard representation of C5.
# The generator is -rotation; eigen-weights (5+2k) on two Fourier planes k=1,2.
weights=[7,9]
assert all(__import__('math').gcd(w,10)==1 for w in weights)
print('BIER5_LENS10_EXACT_OK')
print('faces', [len(s) for s in faces_by_dim], 'orbits', [len(s) for s in reps], 'smith_d2', [int(S[i,i]) for i in range(4)], 'weights',weights)
print('d2:')
print(boundaries[1])
print('3-cells',reps[3])
# Exact determinant and fixed-space checks for the generators in dimension four.
import sympy as sp
E=sp.eye(N)
B=sp.Matrix.hstack(*[E[:,i]-E[:,N-1] for i in range(N-1)])
R=sp.zeros(N); J=sp.zeros(N)
for i in range(N):
    R[(i+1)%N,i]=1
    J[(-i)%N,i]=1

def restrict(M):
    return sp.Matrix.hstack(*[B.gauss_jordan_solve(M*B[:,i])[0] for i in range(N-1)])
rg=restrict(-R); s=restrict(J); gs=restrict(-R*J)
assert rg.det()==s.det()==gs.det()==1
assert (s-sp.eye(4)).rank()==(gs-sp.eye(4)).rank()==2
assert rg**10==sp.eye(4)
assert all((rg**j-sp.eye(4)).rank()==4 for j in range(1,10))
assert s*s==sp.eye(4) and s*rg*s==rg.inv()
print('BIER5_DIHEDRAL_REFLECTION_FIXED_CIRCLES_OK')
