"""Reproducible exact-arithmetic checks for the cone mixing transfer principle.
Requires Python 3.9+ standard library only. No external data.
"""
from fractions import Fraction as F
from itertools import combinations

checks = 0

def chk(condition):
    global checks
    assert condition
    checks += 1

def matmul(A,B):
    return [[sum((a*b for a,b in zip(row,col)), F(0)) for col in zip(*B)] for row in A]

def ident(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def trace(A):
    return sum((A[i][i] for i in range(len(A))), F(0))

def cp(A):
    """Characteristic polynomial high-to-low via Faddeev-LeVerrier."""
    n=len(A); M=ident(n); out=[F(1)]
    for k in range(1,n+1):
        M=matmul(A,M)
        c=-trace(M)/k
        out.append(c)
        for i in range(n): M[i][i]+=c
    return out

def conv(a,b):
    o=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return o

def graph_q(m,edges,t):
    Q=ident(m)
    for i,j in edges:
        Q[i][j]+=t;Q[j][i]+=t
        Q[i][i]-=t;Q[j][j]-=t
    chk(all(v>=0 for row in Q for v in row))
    chk(all(sum(row)==1 for row in Q))
    chk(all(Q[i][j]==Q[j][i] for i in range(m) for j in range(m)))
    return Q

def cone_P(Q,b):
    m=len(Q)
    P=[[F(0) for _ in range(m+1)] for _ in range(m+1)]
    P[m][m]=1-m*b
    for i in range(m):
        P[i][m]=P[m][i]=b
        for j in range(m):P[i][j]=(1-b)*Q[i][j]
    chk(all(x>=0 for row in P for x in row))
    chk(all(sum(row)==1 for row in P))
    return P

def test_pair(m,edges,t,bs):
    Q=graph_q(m,edges,t)
    for b in bs:
        P=cone_P(Q,b)
        TQ=ident(m);TP=ident(m+1)
        for k in range(1,m+3):
            TQ=matmul(TQ,Q);TP=matmul(TP,P)
            left=trace(TP)
            right=F(1)+(1-(m+1)*b)**k+(1-b)**k*(trace(TQ)-1)
            chk(left==right)
    return Q

# Five different vertex-transitive graph families and selected spoke rates.
for m in range(3,11):
    edges=[(i,(i+1)%m) for i in range(m)]
    t=F(1,4)
    test_pair(m,edges,t,[F(0),F(1,2*m),F(1,m)])
for m in range(2,9):
    es=list(combinations(range(m),2))
    test_pair(m,es,F(1,m),[F(0),F(1,2*m),F(1,m)])
for m in range(2,9):
    test_pair(m,[],F(0),[F(0),F(1,2*m),F(1,m)])
for d in range(2,5):
    m=2**d
    es=[(x,x^(1<<i)) for x in range(m) for i in range(d) if x<(x^(1<<i))]
    test_pair(m,es,F(1,d+1),[F(1,2*m),F(1,m)])
for m in [4,6,8,10]:
    es=[(i,j) for i,j in combinations(range(m),2) if j!=i+m//2 and i!=j+m//2]
    test_pair(m,es,F(1,m),[F(1,2*m),F(1,m)])

# A nonvertex-transitive core: path on four vertices.
# This rational five-state stochastic matrix is supported on K1 join P4.
P=[[F(3,10),F(3,10),F(0),F(0),F(2,5)],
   [F(3,10),F(1,5),F(9,20),F(0),F(1,20)],
   [F(0),F(9,20),F(1,5),F(3,10),F(1,20)],
   [F(0),F(0),F(3,10),F(3,10),F(2,5)],
   [F(2,5),F(1,20),F(1,20),F(2,5),F(1,10)]]
chk(all(sum(row)==1 for row in P))
chk(all(P[i][j]==P[j][i] for i in range(5) for j in range(5)))
chk(all(v>=0 for row in P for v in row))
M=[[P[i][j]-F(1,5) for j in range(5)] for i in range(5)]
expected=conv(conv([F(1),F(0)],[F(1),F(-1,20),F(-7,40)]),[F(1),F(-1,20),F(-33,200)])
chk(cp(M)==expected)
# Top absolute eigenvalue = (1+sqrt(281))/40 < 1/2 < 3sqrt(2)/8.
chk(281<19*19) # gives upper bound < 1/2
chk(F(1,2)**2 < F(3,8)**2*2)

# Nonedge witness in a four-cycle, exactly saturating the bound 1/(m-1).
Q=graph_q(4,[(0,1),(1,2),(2,3),(3,0)],F(1,3))
# Spectrum of Q is 1,1/3,1/3,-1/3; check polynomial directly.
chk(cp(Q)==conv(conv([F(1),F(-1)],[F(1),F(-1,3)]),conv([F(1),F(-1,3)],[F(1),F(1,3)])))

print('VERIFY_OK exact_rational_checks=', checks)
