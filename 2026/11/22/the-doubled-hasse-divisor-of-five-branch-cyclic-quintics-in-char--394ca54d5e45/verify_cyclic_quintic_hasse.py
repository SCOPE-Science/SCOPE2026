#!/usr/bin/env python3
"""Exact Hasse and finite-field checks for a five-branch cyclic quintic family.

Requires sympy 1.14 or compatible. All arithmetic is exact in characteristic 11.
Run: python verify_cyclic_quintic_hasse.py
"""
import itertools
from collections import Counter
import sympy as sp

p = 11
s, t = sp.symbols('s t')
R = lambda f: sp.Poly(f, s, t, modulus=p)
zero, one = R(0), R(1)
f = [zero, R(-t), R(s+t), R(-s-1), one]  # x(x-1)(x^2-sx+t)
coefficient_powers = {0: [one]}
for n in range(1, 9):
    old = coefficient_powers[n-1]
    nxt = [zero] * (len(old) + 4)
    for i, c in enumerate(old):
        for j, v in enumerate(f):
            nxt[i+j] += c*v
    coefficient_powers[n] = nxt

def determinant(mat):
    n = len(mat)
    return sum(((-1)**sum(i>j for k, i in enumerate(perm) for j in perm[k+1:]))
               * sp.prod(mat[k][perm[k]] for k in range(n))
               for perm in itertools.permutations(range(n)))

blocks = {}
for j in (2, 3, 4):
    d = j-1
    v = coefficient_powers[2*j]
    blocks[j] = [[v[11*k+10-i] for i in range(d)] for k in range(d)]

H = R(-5*s**4+5*s**3*t+5*s**3-5*s**2*t**2-5*s**2*t-5*s**2
      +4*s*t**2+4*s*t+4*t**3+3*t**2+4*t)
Delta = R(t*(t-s+1)*(s*s-4*t))
assert sp.gcd(H, H.diff(s)) == one  # reduced Hasse support
assert {-1 % p, 2}.isdisjoint({(z*z)%p for z in range(p)})
assert determinant(blocks[2]) == H
assert determinant(blocks[3]) == R(-t*t*(t-s+1)**2*(s*s-4*t))*H
assert determinant(blocks[4]) == R(t**6*(t-s+1)**6*(s*s-4*t)**3)
# In particular det of the six-dimensional Cartier matrix is a unit
# times H^2 on the smooth parameter space Delta != 0.

# On Delta != 0 the 2x2 block cannot vanish identically.
u = sp.symbols('u')
rank_one_ideal = [v.as_expr() for row in blocks[3] for v in row]
rank_one_ideal.append(u*Delta.as_expr()-1)
assert sp.groebner(rank_one_ideal, u, s, t, modulus=p,
                   order='lex').polys == [sp.Poly(1, u, s, t, modulus=p)]

# GF(121) = F_11[i]/(i^2+1), encode a+11*b*i.
q = 121
add = [[((x%p+y%p)%p) + p*((x//p+y//p)%p) for y in range(q)]
       for x in range(q)]
mul = [[((x%p*y%p-(x//p)*(y//p))%p)
        +p*((x%p*(y//p)+(x//p)*(y%p))%p) for y in range(q)]
       for x in range(q)]
neg = [((-x)%p)+p*((-(x//p))%p) for x in range(q)]
inv = [0]*q
for x in range(1, q):
    inv[x] = next(y for y in range(1, q) if mul[x][y]==1)
assert all(mul[x][inv[x]]==1 for x in range(1,q))

def field_poly_mul(a, b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]=add[c[i+j]][mul[x][y]]
    return c

def field_blocks(a,b):
    ff=field_poly_mul(field_poly_mul([0,1],[neg[1],1]),
                      field_poly_mul([neg[a],1],[neg[b],1]))
    pw=[[1]]
    for n in range(1,9):pw.append(field_poly_mul(pw[-1],ff))
    return {j:[[pw[2*j][11*k+10-i] for i in range(j-1)]
               for k in range(j-1)] for j in (2,3,4)}

def rank(A):
    A=[r[:] for r in A];n=len(A);r=0
    for k in range(n):
        pivot=next((i for i in range(r,n) if A[i][k]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        v=inv[A[r][k]]
        A[r]=[mul[v][x] for x in A[r]]
        for i in range(n):
            if i!=r and A[i][k]:
                v=A[i][k]
                A[i]=[add[x][neg[mul[v][y]]] for x,y in zip(A[i],A[r])]
        r+=1
    return r

def det2(A):
    return add[mul[A[0][0]][A[1][1]]][neg[mul[A[0][1]][A[1][0]]]]

def pow_field(x,n):
    y=1
    while n:
        if n&1:y=mul[y][x]
        x=mul[x][x];n//=2
    return y

frob=[pow_field(z,11) for z in range(q)]

def compose_rank(B):
    bf=[[frob[x] for x in row] for row in B]
    C=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j]=add[C[i][j]][mul[B[i][k]][bf[k][j]]]
    assert add[C[0][0]][C[1][1]] != 0, "nilpotent semilinear block"
    return rank(C)

# Independent evaluation of H using its stored polynomial terms.
terms = [(int(coeff)%11, power[0],power[1]) for power,coeff in H.terms()]
def eval_h(a,b):
    ss=add[a][b];tt=mul[a][b]
    powers_s=[1]; powers_t=[1]
    for i in range(4):
        powers_s.append(mul[powers_s[-1]][ss])
        powers_t.append(mul[powers_t[-1]][tt])
    z=0
    for c,i,j in terms:
        z=add[z][mul[c][mul[powers_s[i]][powers_t[j]]]]
    return z

rank_hist=Counter();exceptions=set()
for a in range(q):
    if a in (0,1):continue
    for b in range(q):
        if b in (0,1,a):continue
        B=field_blocks(a,b)
        profile=tuple(rank(B[j]) for j in (2,3,4))
        h_zero=eval_h(a,b)==0
        assert h_zero == (profile!=(1,2,3))
        if h_zero:
            assert profile==(0,1,3)
            assert compose_rank(B[3])==1
            exceptions.add((a,b))
        rank_hist[profile]+=1
assert rank_hist=={(1,2,3):13832,(0,1,3):210}
assert not any(a<11 and b<11 for a,b in exceptions)

# The five branch points are infinity,0,1,a,b. PGL2 changes of
# coordinates are given exactly by projective cross ratios.
def detproj(A,B):
    return add[mul[A[0]][B[1]]][neg[mul[A[1]][B[0]]]]

def cross_ratio_orbit(a,b):
    P=[(1,0),(0,1),(1,1),(a,1),(b,1)]
    E=set()
    for i,j,k in itertools.permutations(range(5),3):
        A=detproj(P[k],P[i]);B=detproj(P[k],P[j])
        left=[m for m in range(5) if m not in (i,j,k)]
        images=[]
        for m in left:
            num=mul[detproj(P[m],P[j])][A]
            den=mul[detproj(P[m],P[i])][B]
            assert den!=0
            images.append(mul[num][inv[den]])
        E.add(tuple(images));E.add(tuple(reversed(images)))
    return E

orb=[]
while exceptions:
    a,b=min(exceptions)
    O=cross_ratio_orbit(a,b)
    assert O<=exceptions
    orb.append((len(O),min(O)))
    exceptions-=O
assert sorted(x[0] for x in orb)==[30,60,120]
assert sorted(x[1] for x in orb)==[(2,12),(3,27),(33,35)]
# Second field presentation: F_11[u]/(u^2-2) independently counts H=0.
mul_alt = [[((x%p*y%p+2*(x//p)*(y//p))%p)
            +p*((x%p*(y//p)+(x//p)*(y%p))%p) for y in range(q)]
           for x in range(q)]
zero_alt=0
for a in range(2,q):
    for b in range(2,q):
        if a==b: continue
        ss=add[a][b];tt=mul_alt[a][b]
        spowers=[1];tpowers=[1]
        for k in range(4):
            spowers.append(mul_alt[spowers[-1]][ss])
            tpowers.append(mul_alt[tpowers[-1]][tt])
        y=0
        for c,i,j in terms:
            y=add[y][mul_alt[c][mul_alt[spowers[i]][tpowers[j]]]]
        if y==0:zero_alt+=1
assert zero_alt==210

print('CYCLIC_QUINTIC_F11_HASSE_VERIFIED '
      'rank11=(72,0) rank121=(13832,210) '
      'nonordinary_Cartier=(0,1,3) p_rank=4 a_number=2 '
      'branch_orbits=(30,60,120)')
