"""Exact integer certificate for primitive-three GHM waves on open three-row grid strips.

Pure Python 3.9+ stdlib, no external packages, no stored tables.
"""
from itertools import product
from math import isqrt

K = range(3)
columns = tuple(product(K, repeat=3))
states = tuple((p,u,v) for p in columns for u in K for v in K)
index = {s: i for i,s in enumerate(states)}
assert len(states) == 243

def sees_successor(center, left=None, right=None):
    for row in range(3):
        candidates = []
        if left is not None:
            candidates.append(left[row])
        if right is not None:
            candidates.append(right[row])
        if row:
            candidates.append(center[row-1])
        if row < 2:
            candidates.append(center[row+1])
        if (center[row] + 1) % 3 not in candidates:
            return False
    return True

left_boundary = []
right_boundary = []
transitions = []
for i,(left, c1,c2) in enumerate(states):
    center=(0,c1,c2)
    left_boundary.append(int(sees_successor(left, right=center)))
    right_boundary.append(int(sees_successor(center, left=left)))
    for right in columns:
        if sees_successor(center,left=left,right=right):
            x=right[0]
            normalized=(tuple((z-x)%3 for z in center), (right[1]-x)%3, (right[2]-x)%3)
            transitions.append((i,index[normalized]))
assert len(transitions)==2465

def multiply_row(v):
    w = [0]*243
    for i,j in transitions:
        w[j]+=v[i]
    return w

def evaluate(v):
    return 3*sum(v[i]*right_boundary[i] for i in range(243))

# Q(z) = z^10 - 11z^9 + 18z^8 + 22z^7 + 6z^6
#        - 162z^5 + 29z^4 + 105z^3 + 62z^2 + 22z + 4.
q = (4,22,62,105,29,-162,6,22,18,-11,1)
expected=(6,84,774,6954,59988,519126,4486806,38771652,
          335039910,2895154566)
v = left_boundary[:]
sequence=[]
for k in range(254):
    sequence.append(evaluate(v))
    v=multiply_row(v)
assert tuple(sequence[:10])==expected
# 243 exact identities; CH on a 243-dimensional matrix gives all further k.
for k in range(243):
    assert sum(q[j]*sequence[k+j] for j in range(11))==0, (k,sequence[k:k+11])
# Reconstruct generating numerator from initial counts and denominator.
d=(1,-11,18,22,6,-162,29,105,62,22,4)
numerator=tuple(sum(d[j]*expected[k-j] for j in range(k+1)) for k in range(10))
assert numerator==(6,18,-42,84,-690,990,402,192,36,0)
# Rouché on |z|=8: z^9(z-11) dominates the degree <= 8 terms.
assert sum(abs(q[j])*8**j for j in range(9))==355185204
assert 355185204 < 3*8**9==402653184
# Q(8)<0<Q(9), and only one root of Q can have |z|>8.
def poly(v,x):
    return sum(a*x**i for i,a in enumerate(v))
assert poly(q,8)==-58084812 and poly(q,9)==99120064
# Show numerator and denominator are coprime over Q by gcd=1 modulo 7.
# D has unit constant term and nonzero mod 7 leading coefficient.
def trim(p):
    while p and p[-1]%7==0:p.pop()
    return p

def rem(f,g):
    f=trim([x%7 for x in f]);g=trim([x%7 for x in g])
    assert g
    while len(f)>=len(g):
        c=f[-1]*pow(g[-1],-1,7)%7
        for i in range(len(g)):
            f[len(f)-len(g)+i]=(f[len(f)-len(g)+i]-c*g[i])%7
        trim(f)
    return f
u=trim([x%7 for x in d]); w=trim([x%7 for x in numerator])
assert u and w
while w:
    u,w=w,rem(u,w)
assert len(u)==1, u
print('PASS: normalized matrix size 243, transition arcs',len(transitions))
print('PASS: all 243 Cayley-Hamilton base identities and exact 10-term generating function')
print('PASS: Rouché and mod-7 noncancellation checks')
print('N_2 through N_11:',*expected)
print('D:',d)
print('numerator:',numerator)
