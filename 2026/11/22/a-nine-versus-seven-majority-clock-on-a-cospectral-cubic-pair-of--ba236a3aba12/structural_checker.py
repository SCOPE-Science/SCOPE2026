"""Exact integer checks of graph construction, switching and nonisomorphism."""
import json
from direct_checker import G_EDGES,H_EDGES

n=14

def adjacency(edges):
    A=[[0]*n for _ in range(n)]
    for a,b in edges:
        assert 0<=a<b<n and not A[a][b]
        A[a][b]=A[b][a]=1
    return A

def mm(A,B):
    N=len(A);M=len(B);K=len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(M)) for j in range(K)] for i in range(N)]

def trace(A):return sum(A[i][i] for i in range(n))

def charpoly(A):
    power=[[int(i==j) for j in range(n)] for i in range(n)]
    traces=[]
    for k in range(1,n+1):
        power=mm(power,A)
        traces.append(trace(power))
    cs=[1]
    for k in range(1,n+1):
        s=sum(cs[k-j]*traces[j-1] for j in range(1,k+1))
        assert s%k==0
        cs.append(-s//k)
    return cs

AG=adjacency(G_EDGES)
AH=adjacency(H_EDGES)
assert all(sum(r)==3 for r in AG)
assert all(sum(r)==3 for r in AH)
assert len(G_EDGES)==len(H_EDGES)==21

def connected(A):
    reached={0}
    frontier=[0]
    while frontier:
        u=frontier.pop()
        for v in range(n):
            if A[u][v] and v not in reached:
                reached.add(v);frontier.append(v)
    return len(reached)==n
assert connected(AG) and connected(AH)
B=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i<4 and j<4:B[i][j]=1-2*int(i==j)
        elif i>=4 and j>=4:B[i][j]=2*int(i==j)
assert mm(B,B)==[[4*int(i==j) for j in range(n)] for i in range(n)]
assert mm(mm(B,AG),B)==[[4*AH[i][j] for j in range(n)] for i in range(n)]

def triangles(A):
    return [tuple((a,b,c)) for a in range(n) for b in range(a+1,n)
            for c in range(b+1,n) if A[a][b] and A[b][c] and A[a][c]]
assert triangles(AG)==triangles(AH)==[(10,11,12)]

def common(A):
    ext=[]
    for t in (10,11,12):
        outside=[v for v in range(n) if A[t][v] and v not in (10,11,12)]
        assert len(outside)==1
        ext+=outside
    return [i for i in range(n) if all(A[v][i] for v in ext)]
assert common(AG)==[0]
assert common(AH)==[]
a=charpoly(AG);b=charpoly(AH)
assert a==b
print(json.dumps({'order':n,'degree':3,'edges':21,
                  'triangles':[(10,11,12)],
                  'three_external_neighbors_common_neighbor_G':[0],
                  'three_external_neighbors_common_neighbor_H':[],
                  'fourfold_matrix_conjugation':'B*A_G*B=4*A_H',
                  'charpoly_descending_coefficients':a},indent=2,sort_keys=True))
