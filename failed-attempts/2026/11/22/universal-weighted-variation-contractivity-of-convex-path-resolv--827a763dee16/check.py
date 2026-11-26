"""Exact rational checks for weighted path convex-edge proximal variation theorem.
No external libraries; self contained. Random tests are supplementary to proof.
"""
from fractions import Fraction as Q
from random import Random

R = Random(384091)

def diff(x): return [x[i+1]-x[i] for i in range(len(x)-1)]
def matmul(A, B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))), Q(0)) for j in range(len(B[0]))] for i in range(len(A))]
def dot(a, b): return sum((x*y for x,y in zip(a,b)), Q(0))
def inverse(A):
    n=len(A); C=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if C[k][j]); C[j],C[k]=C[k],C[j]
        t=C[j][j];C[j]=[v/t for v in C[j]]
        for i in range(n):
            if i!=j:
                t=C[i][j];C[i]=[a-t*b for a,b in zip(C[i],C[j])]
    return [row[n:] for row in C]
def Bmatrix(m):
    n=len(m); r=n-1
    return [[(1/m[i]+1/m[i+1] if i==j else -1/m[max(i,j)] if abs(i-j)==1 else Q(0)) for j in range(r)] for i in range(r)]
def weights(m):
    B=Bmatrix(m); Rb=inverse(B)
    return [sum(row,Q(0)) for row in Rb]
def var(x,w):return dot([abs(t) for t in diff(x)],w)
def edge_potential_data(u, m, coeff):
    z=diff(u); q=[a*t**3 for a,t in zip(coeff,z)]
    v=[Q(0)]*len(u)
    for i,qi in enumerate(q):v[i]-=qi;v[i+1]+=qi
    return [ui+vi/mi for ui,vi,mi in zip(u,v,m)]

count_matrix=count_nonlinear=0
for n in range(2,9):
    for test in range(18):
        m=[Q(R.randint(1,5),R.randint(1,5)) for _ in range(n)]
        B=Bmatrix(m);w=weights(m)
        assert all(v>0 for v in w)
        assert all(dot(w,[B[i][j] for i in range(n-1)])==1 for j in range(n-1))
        a=[Q(R.randrange(0,5),R.randrange(1,5)) for _ in range(n-1)]
        G=[[Q(i==j)+B[i][j]*a[j] for j in range(n-1)] for i in range(n-1)]
        inv=inverse(G)
        assert all(t>=0 for row in inv for t in row)
        assert all(dot(w,[inv[i][j] for i in range(n-1)])<=w[j] for j in range(n-1))
        count_matrix+=1
        for _ in range(4):
            u=[Q(R.randrange(-3,4),R.randrange(1,4)) for _ in range(n)]
            v=[Q(R.randrange(-3,4),R.randrange(1,4)) for _ in range(n)]
            f=edge_potential_data(u,m,a)
            g=edge_potential_data(v,m,a)
            assert var([x-y for x,y in zip(u,v)],w)<=var([x-y for x,y in zip(f,g)],w)
            count_nonlinear+=1
print('RATIONAL_INVERSE_POSITIVITY_AND_WEIGHTED_COLUMN_TESTS_PASS',count_matrix)
print('EXACT_NONLINEAR_QUARTIC_PROXIMAL_TWO_INPUT_TESTS_PASS',count_nonlinear)

m=[Q(1)]*4;w=[Q(1),Q(1,2),Q(1)];B=Bmatrix(m);j=1;t=Q(1)
d=[Q(i==j) for i in range(3)]
G=[[Q(i==k)+(t if k==j else Q(0))*B[i][k] for k in range(3)] for i in range(3)]
Rinv=inverse(G); z=[sum((Rinv[i][k]*d[k] for k in range(3)),Q(0)) for i in range(3)]
assert z==[Q(1,3),Q(1,3),Q(1,3)]
assert dot(w,z)==Q(5,6)>w[j]==Q(1,2)
print('EXACT_SHARP_FAILURE_WITNESS_PASS',str(dot(w,z)),str(w[j]))
print('ALL_CONVEX_PATH_VARIATION_CERTIFICATES_PASS')
