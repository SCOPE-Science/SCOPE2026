#!/usr/bin/env python3
"""Exact integer transfer verification for parallel diffusion with a triangle core."""
from itertools import product

SIGNS = (-1, 0, 1)
PAIRS = tuple(product(SIGNS, repeat=2))

def sign(x):
    return (x > 0) - (x < 0)

def weight(a,b,c):
    if b == 0:
        return int(a == -c)
    return max(1-b*(a+c), 0)

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def matadd(A,B,coef=1):
    return [[x+coef*y for x,y in zip(row,srow)] for row,srow in zip(A,B)]

def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def matpower(M,n):
    X=identity(len(M))
    for _ in range(n):X=matmul(X,M)
    return X

# The 9-state path-edge transfer. An edge sign b has two adjacent signs a,c.
M = [[weight(a,b,d) if c == b else 0
      for c,d in PAIRS] for a,b in PAIRS]
beta = [[weight(a,b,0)] for a,b in PAIRS]
alpha = [0]*len(PAIRS)
zero_root_core = []
for x,y in product(range(-4,5), repeat=2):
    old = (0,x,y)
    core_b = (sign(-x)+sign(-y), sign(x)+sign(x-y), sign(y)+sign(y-x))
    for s1 in SIGNS:
        b=(core_b[0]-s1, core_b[1], core_b[2])
        new=tuple(old[i]-b[i] for i in range(3))
        if any(sign(new[i]-new[j]) != -sign(old[i]-old[j])
               for i,j in ((0,1),(0,2),(1,2))):
            continue
        if s1 == 0 and b[0] == 0:
            zero_root_core.append((x,y))
        for s2 in SIGNS:
            alpha[PAIRS.index((s1,s2))] += weight(core_b[0],s1,s2)
assert sorted(zero_root_core) == [(-1,1),(0,0),(1,-1)]
assert alpha == [14,21,28,4,3,4,28,21,14]

# Even-sign subspace contains a 4x4 transfer block plus the all-flat eigenline.
reps=((-1,-1),(-1,0),(-1,1),(0,-1),(0,0))
E=[[int((a,b)==r or (a,b)==(-r[0],-r[1])) for r in reps] for a,b in PAIRS]
B4=[[0,0,1,0],[0,0,0,1],[1,2,3,0],[0,1,2,0]]
BE=[list(row)+[0] for row in B4]+[[0,0,0,0,1]]
assert matmul(M,E) == matmul(E,BE)
# P(B4)=B4^4-3B4^3-2B4^2-B4+I=0, proving the quartic recurrence.
P=matadd(matpower(B4,4),matpower(B4,3),-3)
P=matadd(P,matpower(B4,2),-2)
P=matadd(P,B4,-1)
P=matadd(P,identity(4))
assert P == [[0]*4 for _ in range(4)]
assert alpha[4] == 3  # all-flat path eigenline multiplicity Z(K3,r)

expected={2:123,3:469,4:1675,5:6029,6:21771,7:78565,
          8:283579,9:1023597,10:3694731,11:13336389,12:48138635}
count={k:matmul([alpha],matmul(matpower(M,k-2),beta))[0][0]
       for k in range(2,13)}
assert count == expected
for k in range(2,9):
    T=lambda t:count[t]-1
    assert T(k+4)-3*T(k+3)-2*T(k+2)-T(k+1)+T(k)==-8
# The path-core specialization must reproduce the published path sequence.
alpha_path = [[weight(0,a,b) for a,b in PAIRS]]
assert [matmul(alpha_path,matmul(matpower(M,k-2),beta))[0][0]-1
        for k in range(2,7)] == [8,26,96,346,1248]
print('core_zero_drift', sorted(zero_root_core))
print('alpha', [alpha[i:i+3] for i in range(0,9,3)])
print('even_block', BE)
print('quartic_matrix_identity', True)
print('triangle_tail_N', count)
print('fourth_order_residual', -8, 'for every checked k=2..8')
print('path_specialization', [8,26,96,346,1248])
print('TRANSFER_PASS')
