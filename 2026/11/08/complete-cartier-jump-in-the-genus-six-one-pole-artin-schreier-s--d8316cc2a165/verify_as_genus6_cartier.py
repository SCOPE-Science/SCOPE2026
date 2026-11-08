#!/usr/bin/env python3
"""Exact finite-field replay for a genus-six Artin--Schreier Cartier stratification.
Only finite checks are performed here; the accompanying proof handles algebraic closures.
"""
from itertools import product

# F_9 = F_3[t]/(t^2+1); represent a+bt by a+3b.
def add(u,v):
    return ((u%3+v%3)%3)+3*((u//3+v//3)%3)
def neg(u):
    return ((-u%3)%3)+3*((-u//3)%3)
def mul(u,v):
    a,b=u%3,u//3
    c,d=v%3,v//3
    return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)
def pow9(u,n):
    r=1
    while n:
        if n&1:r=mul(r,u)
        u=mul(u,u);n//=2
    return r
def inv(u):
    assert u!=0
    return pow9(u,7)
def root(u):
    return pow9(u,3)

def rank(M):
    M=[list(row) for row in M]
    rows=len(M); cols=len(M[0]); pivot=0
    for j in range(cols):
        r=next((i for i in range(pivot,rows) if M[i][j]),None)
        if r is None:continue
        M[pivot],M[r]=M[r],M[pivot]
        z=inv(M[pivot][j]);M[pivot]=[mul(z,x) for x in M[pivot]]
        for i in range(rows):
            if i!=pivot and M[i][j]:
                factor=M[i][j]
                M[i]=[add(x,neg(mul(factor,y))) for x,y in zip(M[i],M[pivot])]
        pivot+=1
    return pivot

def matmul(A,B):
    return [[sum9([mul(A[i][k],B[k][j]) for k in range(6)]) for j in range(6)] for i in range(6)]
def sum9(vals):
    v=0
    for x in vals:v=add(v,x)
    return v

def direct_cartier(a,b,c):
    # Basis monomials x^i y^j dx for (i,j)=(0,0),(1,0),(2,0),(3,0),(0,1),(1,1).
    # Rewrite y=y^3-f(x), use C(g^3*omega)=g*C(omega), and select x^(3m+2)dx.
    f={7:1,5:a,4:b,2:c}
    cols=[]
    for i,j in ((0,0),(1,0),(2,0),(3,0),(0,1),(1,1)):
        v=[0]*6
        if j==0:
            if i%3==2:
                v[(i-2)//3]=1
        else:
            # y^3 term dies because C(x^i dx)=0 for i=0,1.
            for exponent,coefficient in f.items():
                t=exponent+i
                if coefficient and t%3==2:
                    m=(t-2)//3
                    v[m]=add(v[m],neg(root(coefficient)))
        cols.append(v)
    return [[cols[j][i] for j in range(6)] for i in range(6)]

def predicted_cartier(a,b,c):
    # Written independently using the six displayed images.
    M=[[0]*6 for _ in range(6)]
    M[0][2]=1
    M[0][4]=neg(root(c)); M[1][4]=neg(root(a))
    M[1][5]=neg(root(b)); M[2][5]=neg(1)
    return M

def ranks_of_iterates(M):
    P=[[int(i==j) for j in range(6)] for i in range(6)]
    out=[rank(P)]
    N=[r[:] for r in M]
    for _ in range(3):
        P=matmul(P,N)
        out.append(rank(P))
        # σ is inverse Frobenius: a ↦ a^3 on F_9.
        N=[[root(x) for x in row] for row in N]
    return out

def main():
    assert all(mul(x,inv(x))==1 for x in range(1,9))
    counts={(6,2,1,0):0,(6,3,1,0):0}
    for a,b,c in product(range(9),repeat=3):
        M=direct_cartier(a,b,c)
        assert M==predicted_cartier(a,b,c),(a,b,c,M)
        ranks=tuple(ranks_of_iterates(M))
        expected=(6,3 if a else 2,1,0)
        assert ranks==expected,(a,b,c,ranks)
        counts[ranks]+=1
    assert counts==( {(6,2,1,0):81,(6,3,1,0):648} )
    print('AS_GENUS6_CH3_CARTIER_REPLAY_PASS',counts,'F9_parameters=729')

if __name__=='__main__':main()
