#!/usr/bin/env python3
"""Exact checks of the complete-tripartite two-choice hitting theorem.
All computations use Python's standard library and integer/Fraction arithmetic.
Run: python3 verify.py
"""
from fractions import Fraction


def det3(L):
    (a,b,c),(d,e,f),(g,h,i) = L
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def integer_system(a,b,c):
    L = [
        [(b+c)**2, -(b*b+2*b*c), -c*c],
        [-(a-1)**2, (a+c)**2, -(c*c+2*c*(a-1))],
        [-(a-1)**2, -(b*b+2*b*(a-1)), (a+b)**2],
    ]
    w = [(b+c)**2, (a+c)**2, (a+b)**2]
    return L,w


def column_det(L,w,j):
    return det3([[w[i] if k==j else L[i][k] for k in range(3)] for i in range(3)])


def nd_formula(a,b,c):
    return (b-c)*(b+c)**2*(2*a*(b+c+1)+2*b*c-b-c-2)


def positive_P(A,C,D):
    P0=4*(C+1)**2*(2*A+2*C+5)*(A*A+4*A*C+8*A+2*C*C+10*C+12)
    P1=2*(C+1)*(4*A**3+29*A*A*C+51*A*A+42*A*C*C+175*A*C+173*A+17*C**3+114*C*C+251*C+178)
    P2=2*A**3+26*A*A*C+37*A*A+46*A*C*C+172*A*C+146*A+22*C**3+135*C*C+270*C+169
    P3=2*(2*A*A+4*A*C+10*A+2*C*C+10*C+13)
    return P0+D*P1+D*D*P2+D**3*P3


def solve_fraction(A,b):
    n=len(b)
    M=[[Fraction(x) for x in row]+[Fraction(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if M[i][j])
        M[j],M[pivot]=M[pivot],M[j]
        q=M[j][j]
        M[j]=[x/q for x in M[j]]
        for i in range(n):
            if i==j:continue
            fac=M[i][j]
            if fac: M[i]=[x-fac*y for x,y in zip(M[i],M[j])]
    return [row[-1] for row in M]


def full_graph_test(a,b,c):
    labels = [0]*a+[1]*b+[2]*c
    n=len(labels)
    root=0
    neigh=[[j for j in range(n) if labels[j]!=labels[i]] for i in range(n)]
    L,w=integer_system(a,b,c)
    z=det3(L)
    H=[Fraction(column_det(L,w,k),z) for k in range(3)]
    assert H[0]>H[2]>=H[1]>0
    values=[Fraction(0) if i==root else H[labels[i]] for i in range(n)]
    # Full-vertex Bellman equations, enumerating all offered pairs without quotienting by part.
    checks=0
    for i in range(1,n):
        nei=neigh[i]
        avg=sum((min(values[j], values[k]) for j in nei for k in nei),Fraction(0))/len(nei)**2
        assert values[i] == 1+avg, (a,b,c,i,values[i],1+avg)
        checks+=1
    # An independent full-vertex Markov-chain solution for the stated fixed policy.
    # The finite chain's best offer is selected via class priority root,B,C,A.
    priority={0:3,1:1,2:2}
    nonroot=list(range(1,n))
    ind={v:k for k,v in enumerate(nonroot)}
    Q=[[Fraction(0) for _ in nonroot] for _ in nonroot]
    for i in nonroot:
        nei=neigh[i]; den=len(nei)**2
        for j in nei:
            for k in nei:
                chosen=min((j,k), key=lambda x:(-1 if x==root else priority[labels[x]],x))
                if chosen!=root:Q[ind[i]][ind[chosen]]+=Fraction(1,den)
    sol=solve_fraction([[Fraction(int(i==j))-Q[i][j] for j in range(len(nonroot))] for i in range(len(nonroot))],[1]*len(nonroot))
    for i in nonroot:
        assert sol[ind[i]]==values[i]
        checks+=1
    return checks


def main():
    # The two differences are polynomials of degree at most six in EACH of a,b,c:
    # every entry of L has total degree <=2, so det(L), each Cramer determinant
    # and the two displayed products have total degree <=6. Thus a polynomial
    # that vanishes at 7 values of each variable vanishes identically.
    algebra=0
    for a in range(2,9):
        for b in range(1,8):
            for c in range(1,8):
                L,w=integer_system(a,b,c)
                delta=det3(L)
                nd=column_det(L,w,2)-column_det(L,w,1)
                assert nd == nd_formula(a,b,c)
                p=delta - (b*b+2*b*c)*(b-c)*(2*a*(b+c+1)+2*b*c-b-c-2)
                assert p==positive_P(a-2,c-1,b-c)
                algebra+=2
    # Positive coefficients in P0..P3, visible directly in positive_P,
    # imply p>0 whenever a>=2, b>=c>=1.
    graphs=0; bellman=0
    for a in range(2,5):
        for b in range(1,6):
            for c in range(1,b+1):
                bellman+=full_graph_test(a,b,c)
                graphs+=1
    print(f'VERIFY_OK algebra_identities={algebra} full_graphs={graphs} exact_full_vertex_checks={bellman}')

if __name__=='__main__': main()
