from fractions import Fraction as F
from itertools import product

def mul(U,V):
    return [[sum((U[i][k]*V[k][j] for k in range(len(V))),F(0)) for j in range(len(V[0]))] for i in range(len(U))]

def check(S,x,r):
    n=len(x)
    assert max(sum(S[i][j] for i in range(n)) for j in range(n))<=1
    lhs=sum((abs((F(i==j))-S[i][j])*x[j] for i in range(n) for j in range(n)),F(0))
    rhs=sum(sorted(x,reverse=True)[r:],F(0))
    assert lhs>=rhs,(S,x,r,lhs,rhs)
    return lhs

count=0
for n in (2,3,4):
    for r in (0,1,2):
        if r>=n:continue
        # positive rank <= r via U V, contractive column normalization
        for k in range(200):
            if r==0:S=[[F(0)]*n for _ in range(n)]
            else:
                U=[[F((3*i+7*j+5*k*k+11*k+2)%7,7) for j in range(r)] for i in range(n)]
                V=[[F((2*i+5*j+7*k*k+3*k+1)%7,7) for j in range(n)] for i in range(r)]
                S=mul(U,V)
                colmax=max(sum(S[i][j] for i in range(n)) for j in range(n))
                if colmax:S=[[entry/colmax for entry in row] for row in S]
            x=[F((i*i+3*i+k)%11+1,11) for i in range(n)]
            check(S,x,r)
            # match by top r-coordinate projection
            top=sorted(range(n),key=lambda i:(-x[i],i))[:r]
            P=[[F(i==j and i in top) for j in range(n)] for i in range(n)]
            assert check(P,x,r)==sum(sorted(x,reverse=True)[r:],F(0))
            count+=2
print('RANK_MODULUS_ATOMIC_EXACT_CHECK_OK',count)
