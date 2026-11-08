#!/usr/bin/env python3
"""Exact F_4/F_16 incidence and cohomological input for a quartic K3.

Field: F_2[a]/(a^4+a^3+a^2+a+1), with a represented by 2.
No packages beyond the Python standard library are needed.
"""
from itertools import permutations, product
from collections import Counter

MOD = 0b11111

def mul(a, b):
    out = 0
    while b:
        if b & 1: out ^= a
        b >>= 1
        a <<= 1
        if a & 16: a ^= MOD
    return out

def power(a, n):
    out = 1
    while n:
        if n & 1: out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out

INV = {x: power(x, 14) for x in range(1, 16)}

def xor(xs):
    out = 0
    for a in xs: out ^= a
    return out

def rref(rows):
    mat = [list(row) for row in rows]
    if not mat: return ()
    row = 0
    for col in range(len(mat[0])):
        pivot = next((r for r in range(row, len(mat)) if mat[r][col]), None)
        if pivot is None: continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        d = INV[mat[row][col]]
        mat[row] = [mul(d, z) for z in mat[row]]
        for r in range(len(mat)):
            if r != row and mat[r][col]:
                d = mat[r][col]
                mat[r] = [a ^ mul(d, b) for a, b in zip(mat[r], mat[row])]
        row += 1
        if row == len(mat): break
    return tuple(tuple(r) for r in mat[:row])

def rank(rows): return len(rref(rows))

def rank_prime(mat, prime=101):
    mat = [list(map(lambda x: x % prime, r)) for r in mat]
    if not mat: return 0
    h, w = len(mat), len(mat[0])
    r = 0
    for j in range(w):
        piv = next((i for i in range(r, h) if mat[i][j]), None)
        if piv is None: continue
        mat[r], mat[piv] = mat[piv], mat[r]
        d = pow(mat[r][j], -1, prime)
        mat[r] = [(d*x)%prime for x in mat[r]]
        for i in range(r+1, h):
            if mat[i][j]:
                d = mat[i][j]
                mat[i] = [(a-d*b)%prime for a,b in zip(mat[i],mat[r])]
        r += 1
        if r == h: break
    return r

def e2(x):
    return xor(mul(x[i],x[j]) for i in range(5) for j in range(i+1,5))

def e4(x):
    from itertools import combinations
    terms = []
    for ids in combinations(range(5),4):
        z=1
        for i in ids: z=mul(z,x[i])
        terms.append(z)
    return xor(terms)

ALPHA=2
A = power(ALPHA,3) ^ ALPHA ^ 1
B = power(ALPHA,3) ^ power(ALPHA,2) ^ ALPHA ^ 1
MU = 1 ^ power(ALPHA,2) ^ power(ALPHA,3)
assert power(ALPHA,5) == 1 and ALPHA != 1
assert power(MU,3)==1 and MU!=1 and power(MU,4)==MU

# x_1=u,x_2=v,x_3=v+A*u,x_4=B*v+alpha*u,x_0=x_1+x_2+x_3+x_4.
U = (power(ALPHA,3),1,0,A,ALPHA)
V = (B,0,1,1,B)

def on_surface(x):
    return xor(x)==0 and e4(x)==mul(MU,mul(e2(x),e2(x)))

def point_norm(x):
    a=next(z for z in x if z)
    return tuple(mul(z, INV[a]) for z in x)

def line_points(L):
    u,v = L
    return [point_norm(v)] + [point_norm([u[k]^mul(z,v[k]) for k in range(5)]) for z in range(16)]

assert all(on_surface(x) for x in line_points((U,V)))
line_set={rref([[vec[p[i]] for i in range(5)] for vec in (U,V)]) for p in permutations(range(5))}
assert len(line_set)==60
lines=sorted(line_set)
index={L:i for i,L in enumerate(lines)}
assert all(len(set(line_points(L)))==17 for L in lines)
assert all(all(on_surface(x) for x in line_points(L)) for L in lines)

frobenius=lambda x:power(x,4)
perm=[index[rref([[frobenius(x) for x in row] for row in L])] for L in lines]
assert all(perm[perm[i]]==i for i in range(60))
fixed=[i for i in range(60) if perm[i]==i]
pairs=[(i,perm[i]) for i in range(60) if i < perm[i]]
assert len(fixed)==0 and len(pairs)==30
assert all(rank(lines[i]+lines[j])==4 for i,j in pairs)

incidence=[[0]*60 for _ in range(60)]
for i in range(60):
    incidence[i][i]=-2
    for j in range(i):
        r=rank(lines[i]+lines[j])
        assert r in (3,4)
        incidence[i][j]=incidence[j][i]=int(r==3)
assert all(sum(incidence[i][j] for j in range(60) if j!=i)==17 for i in range(60))

# On a K3 surface, line self-intersection is -2; distinct lines
# have intersection 1 when meeting, otherwise 0.
base_rank=rank_prime(incidence)
plus=[[incidence[i][j]+incidence[i][k] for j,k in pairs] for i in range(60)]
minus=[[incidence[i][j]-incidence[i][k] for j,k in pairs] for i in range(60)]
rplus=rank_prime(plus)
rminus=rank_prime(minus)
assert (base_rank,rplus,rminus)==(20,10,10)
# Published result: these 60 classes span a rank-20 Neron-Severi
# group. Modular ranks 10 + 10 then determine the rational eigenspaces.

line_support={}
for i,L in enumerate(lines):
    for pt in line_points(L):
        line_support.setdefault(pt,[]).append(i)
mult=Counter(len(v) for v in line_support.values())
assert mult==Counter({2:510})
assert all(any(i!=j for i,j in [indices]) for indices in line_support.values())
assert all(any(frobenius(x)!=x for x in pt) for pt in line_support)

F4 = [x for x in range(16) if power(x,4)==x]
assert F4 == [0,1,12,13]

def surface_count(field):
    # A point in s1=0 has unique coordinates
    # (y0,y1,y2,y3,y0+y1+y2+y3), with first nonzero y normalized to 1.
    count=0
    for j in range(4):
        for tail in product(field, repeat=3-j):
            y=(0,)*j + (1,) + tuple(tail)
            x=y+(xor(y),)
            if on_surface(x): count+=1
    return count

N4=surface_count(F4)
N16=surface_count(list(range(16)))
assert (N4,N16)==(20,554)
assert len(line_support)==510
# The 60 lines have no F4 points because conjugate pairs are skew.
# Over every odd extension degree their union has no rational point.
# Over every even degree m it has 60*(4**m+1)-510 points.
s1=N4-1-4**2-4*(rplus-rminus)
s2=N16-1-16**2-16*(rplus+rminus)
product_trans=(s1*s1-s2)//2
assert (s1,s2,product_trans)==(3,-23,16)

print('FIELD_POLY=x^4+x^3+x^2+x+1; ALPHA=2; MU=',MU)
print('LINE_ORBIT=60; FROBENIUS_CYCLES=30_PAIRS; CONJUGATE_PAIRS_SKEW')
print('INCIDENCE_VALENCY=17; LINE_INTERSECTION_MULTIPLICITIES=',dict(mult))
print('GRAM_RANK_MOD101=',base_rank,'; NS_FROB_PLUS_MINUS=',(rplus,rminus))
print('SURFACE_POINTS_F4_F16=',(N4,N16))
print('LINE_UNION_POINTS_F4_F16=',(0,len(line_support)))
print('COMPLEMENT_POINTS_F4_F16=',(N4,N16-len(line_support)))
print('TRANS_FROB_TRACE_AND_DET=',(s1,product_trans))
print('ZETA_S_DEN=(1-T)(1-16T)(1-16T^2)^10(1-3T+16T^2)')
print('ZETA_U=(1-16T^2)^20/((1-T)(1-16T)(1-T^2)^225(1-3T+16T^2))')
print('VERIFY_OK')
