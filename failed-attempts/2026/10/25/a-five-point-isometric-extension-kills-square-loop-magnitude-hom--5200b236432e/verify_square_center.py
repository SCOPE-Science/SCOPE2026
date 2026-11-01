from itertools import product

# Exact Euclidean distances are represented as a + b*sqrt(2).
# Corners of a side-2 square and its center.
P = {
    'A': (1, 1),
    'B': (-1, 1),
    'C': (-1, -1),
    'D': (1, -1),
    'O': (0, 0),
}
X = ('A', 'B', 'C', 'D')
Y = ('A', 'B', 'C', 'D', 'O')
TARGET = (0, 4)  # 4*sqrt(2)

def dist(u, v):
    x1, y1 = P[u]; x2, y2 = P[v]
    s = (x1-x2)**2 + (y1-y2)**2
    return {0:(0,0), 2:(0,1), 4:(2,0), 8:(0,2)}[s]

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def length(seq):
    out=(0,0)
    for u,v in zip(seq,seq[1:]): out=add(out,dist(u,v))
    return out

def chains(vertices, k):
    return [t for t in product(vertices, repeat=k+1)
            if all(t[i] != t[i+1] for i in range(k)) and length(t)==TARGET]

def smooth(a,b,c): return dist(a,c)==add(dist(a,b),dist(b,c))

def boundary3(t):
    out=[]
    # Only internal deletions can preserve total length.
    for i in (1,2):
        if smooth(t[i-1],t[i],t[i+1]):
            out.append(((-1)**i, t[:i]+t[i+1:]))
    return out

C2X=chains(X,2); C3X=chains(X,3)
C2Y=chains(Y,2); C3Y=chains(Y,3)
assert len(C2X)==4 and len(C3X)==0, (C2X,C3X)
assert len(C2Y)==4, C2Y
assert set(C2X)==set(C2Y)
assert all(t[0]==t[2] for t in C2Y)
assert all(not smooth(t[0],t[1],t[2]) for t in C2Y)
for t in C2Y:
    A=t[0]; B=t[1]
    tau=(A,'O',B,A)
    assert tau in C3Y, (tau, C3Y)
    bd=boundary3(tau)
    assert bd==[(-1,t)], (tau,bd,t)
print('PASS: X has 4 degree-2 chains at weight 4sqrt(2), no degree-3 chains.')
print('PASS: Y has the same 4 degree-2 chains; each is a boundary of (A,O,opposite(A),A).')
print('PASS: MH_2,4sqrt(2)(X) = Z^4 and MH_2,4sqrt(2)(Y) = 0; inclusion map is zero.')
