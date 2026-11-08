"""Exact finite verification of a triangular-ladder maximal hard-core transfer theorem.

Run with python3 verify.py (Python standard library only).
This is a finite diagnostic, not a proof of the infinite statements.
"""

STATES=['00','0A','0B','A0','AB','B0']
NEXT={'0':'0AB','A':'0B','B':'0'}
def admissible(a,b,c):
    if c not in NEXT[b]: return False
    if b!='0': return True
    return (a!='0' or c=='A') and (a=='B' or c!='0')
EDGES=[]
for i,ab in enumerate(STATES):
    for j,bc in enumerate(STATES):
        if ab[1]==bc[0] and admissible(ab[0],ab[1],bc[1]):
            EDGES.append((i,j,int(bc[1]!='0')))
assert len(EDGES)==10, (EDGES,len(EDGES))
LOW=[-4,-1,0,-3,0,-2]
HIGH=[0,-1,-1,0,-2,0]
for i,j,w in EDGES:
    assert 5*w-2+LOW[i]-LOW[j]>=0
    assert 2-3*w+HIGH[i]-HIGH[j]>=0
# Characteristic identity by Cayley-Hamilton with integer z specializations.
def matrix_at(z):
    t=[[0]*6 for _ in range(6)]
    for i,j,w in EDGES:t[i][j]=z if w else 1
    return t
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(6)) for j in range(6)] for i in range(6)]
def madd(a,b):return [[a[i][j]+b[i][j] for j in range(6)]for i in range(6)]
def scalar(a,c):return [[c*x for x in row] for row in a]
ID=[[int(i==j) for j in range(6)]for i in range(6)]
for z in [1,2,3,5]:
    t=matrix_at(z); pw=[ID]
    for n in range(6):pw.append(mm(pw[-1],t))
    expr=madd(madd(pw[6],scalar(pw[4],-2*z)),madd(scalar(pw[3],-z*z),madd(scalar(pw[2],-z*z),scalar(pw[1],-z*z))))
    assert all(v==0 for row in expr for v in row)

def brute(n):
    # order: U0,L0,U1,L1,...
    edges=set()
    for i in range(n):
        u,l=2*i,2*i+1
        for a,b in [(u,l),(u,2*((i+1)%n)),(l,2*((i+1)%n)+1),(l,2*((i+1)%n))]:
            if a>b:a,b=b,a
            edges.add((a,b))
    neighbors=[0]*(2*n)
    for i,j in edges:
        neighbors[i]|=1<<j;neighbors[j]|=1<<i
    out=[0]*(n+1)
    for mask in range(1<<(2*n)):
        if any(((mask>>i)&1) and (mask&neighbors[i]) for i in range(2*n)):continue
        if any(not((mask>>i)&1) and not(mask&neighbors[i]) for i in range(2*n)):continue
        out[mask.bit_count()]+=1
    return out

def transfer(n):
    # integer polynomial via DP, closed paths over 6 states
    out=[0]*(n+1)
    for start in range(6):
        data={(start,0):1}
        for _ in range(n):
            nextdata={}
            for (i,k),v in data.items():
                for a,b,w in EDGES:
                    if a==i:nextdata[b,k+w]=nextdata.get((b,k+w),0)+v
            data=nextdata
        for (end,k),v in data.items():
            if end==start:out[k]+=v
    return out
for n in range(4,9):
    b,t=brute(n),transfer(n)
    assert b==t,(n,b,t)
    assert min(k for k,c in enumerate(b) if c)==(2*n+4)//5
    assert max(k for k,c in enumerate(b) if c)==2*n//3
    if n%5==0:assert b[2*n//5]==5
    if n%3==0:assert b[2*n//3]==3
    print(f'n={n}: independent domination polynomial coefficients {b}')
print('Verified finite transfer/brute-force comparisons, potential inequalities, and matrix characteristic identity at four activities.')
