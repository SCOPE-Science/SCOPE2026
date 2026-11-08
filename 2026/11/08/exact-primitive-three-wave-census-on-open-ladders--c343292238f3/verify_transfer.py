"""Exact 27-state finite-transfer certificate for primitive three-cycles on open ladders.
Run: python3 verify_transfer.py (Python standard library only)."""
from itertools import product

Z = range(3)
STATES = list(product(Z, repeat=3))
POS = {s:i for i,s in enumerate(STATES)}

def valid(center, left=None, right=None):
    for row in (0,1):
        wanted = (center[row] + 1) % 3
        neighbors = [center[1-row]]
        if left is not None: neighbors.append(left[row])
        if right is not None: neighbors.append(right[row])
        if wanted not in neighbors: return False
    return True

M = [[0]*27 for _ in range(27)]
a = [0]*27
b = [0]*27
for i, (e,p,q) in enumerate(STATES):
    left = (e,(e+p)%3)
    center = (0,q)
    a[i] = int(valid(left,None,center))
    b[i] = int(valid(center,left,None))
    for x,d in product(Z,repeat=2):
        right=(x,(x+d)%3)
        if valid(center,left,right):
            M[i][POS[((-x)%3,q,d)]] += 1

def mv(v):
    return [sum(M[i][j]*v[j] for j in range(27)) for i in range(27)]

b1=mv(b)
b2=mv(b1)
b3=mv(b2)
assert all(b3[i]-4*b2[i]+b1[i]+2*b[i] == 0 for i in range(27))
values=[3*sum(a[i]*v[i] for i in range(27)) for v in (b,b1,b2,b3)]
assert values == [0,6,24,90]
assert all(x in (0,1) for x in a+b)
# Verify a full independent recurrence calculation using the transfer, not sequence fitting.
seq=[]
v=b
for n in range(2,71):
    seq.append(3*sum(a[i]*v[i] for i in range(27)))
    v=mv(v)
for i in range(3,len(seq)):
    assert seq[i]==4*seq[i-1]-seq[i-2]-2*seq[i-3], (i,seq[i])
assert seq[:10] == [0,6,24,90,324,1158,4128,14706,52380,186558]
print('TRANSFER_OK states=27 componentwise_cubic_identity=27 recurrence_n=5..71')
print('N2..N11=' + ','.join(map(str,seq[:10])))
