"""Exact arithmetic regression tests for a fixed-core-edge constrained mixing frontier.
Run with Python 3's standard library: python verify.py.
"""
from fractions import Fraction as F
from itertools import product


def lower_bound(s, m, t):
    t = F(t)
    return max(
        F(m, m + 2*s),
        (F(m-s) + s*s*t)/F(m+s),
        1 - F(s, m)*(1-(s-1)*t),
        F(s, 2*m+s)*(1-(m+s)*t),
        1 - F(m, s) - s*t,
        s*t - 1,
        F(0),
    )


def positive_intervals(s,m,t,mu):
    return (max(F(0),(1-mu)/s,(1-mu-s*t)/m),
            min(F(1,s),(1-(s-1)*t)/m,(1+mu)/(m+s),(1+mu-s*t)/m))


def eigen_objective(s,m,t,a):
    return max(abs(1-s*a),abs(1-m*a-s*t),abs(1-(m+s)*a))


def independent_vertex_minimax(s,m,t):
    """Independent minimization of three absolute affine eigenvalue expressions.

    Their maximum is piecewise linear; a minimizer is at an endpoint
    or an intersection of two signed eigenvalue lines.
    """
    u=min(F(1,s),(1-(s-1)*t)/m)
    affine=[(F(1),F(-s)), (F(-1),F(s)),
            (1-s*t,F(-m)),(-1+s*t,F(m)),
            (F(1),F(-m-s)),(F(-1),F(m+s))]
    candidates={F(0),u}
    for i in range(len(affine)):
        for j in range(i):
            k1,v1=affine[i];k2,v2=affine[j]
            if v1!=v2:
                a=(k2-k1)/(v1-v2)
                if 0<=a<=u:candidates.add(a)
    return min(eigen_objective(s,m,t,a) for a in candidates)


def direct_matrix(s,m,t,a):
    n=s+m
    P=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(s):
        for j in range(s):
            if i!=j:P[i][j]=t
        for j in range(s,n):
            P[i][j]=P[j][i]=a
        P[i][i]=1-(s-1)*t-m*a
    for i in range(s,n):P[i][i]=1-s*a
    return P


def matvec(P,v):
    return [sum((x*y for x,y in zip(row,v)),F(0)) for row in P]

checks=0
matrix_checks=0
for s in range(2,16):
    for m in range(2,16):
        for j in range(17):
            t=F(j,16*(s-1))
            v=lower_bound(s,m,t)
            assert 0<=v<=1
            assert v==independent_vertex_minimax(s,m,t)
            lo,hi=positive_intervals(s,m,t,v)
            assert 0<=lo<=hi
            a=lo
            assert eigen_objective(s,m,t,a)==v
            checks+=1
            if s<=7 and m<=7 and j%4==0:
                P=direct_matrix(s,m,t,a)
                n=s+m
                assert all(all(x>=0 for x in row) and sum(row)==1 for row in P)
                ones=[F(1)]*n
                assert matvec(P,ones)==ones
                leaf=[F(0)]*n;leaf[s]=1;leaf[s+1]=-1
                core=[F(0)]*n;core[0]=1;core[1]=-1
                quot=[F(m)]*s+[F(-s)]*m
                for z,L in ((leaf,1-s*a),(core,1-m*a-s*t),(quot,1-(m+s)*a)):
                    assert matvec(P,z)==[L*e for e in z]
                matrix_checks+=1

# Four distinct active regimes, exact boundaries, and continuity.
def example(t):
    if t<=F(1,25):return F(3,5)-5*t
    if t<=F(1,10):return F(5,9)-F(35,9)*t
    if t<=F(1,6):return F(1,6)
    return 10*t-F(3,2)
for j in range(3001):
    t=F(j,12000)
    assert lower_bound(5,2,t)==example(t)
print('PASS:',checks,'exact LP vertex comparisons,',matrix_checks,'full matrix spectral checks, 3001 four-regime tests')
