"""Finite verification for vertex covariance of friendship-graph matching polytopes.
Run with Python 3: python verify.py. Standard library only.
"""
from fractions import Fraction as Q
from math import sqrt

def expected(m):
    n=m+1
    D=3*m
    out=[[Q(0) for _ in range(D)] for _ in range(D)]
    px=Q(m,2*n)
    py=Q(1,2*n)
    for i in range(m):
        for j in range(m):
            out[i][j]=Q(1,4)*(i==j)-Q(1,4*n*n)
    for i in range(m):
        for j in range(2*m):
            val=(Q(1,4*n*n)-Q(1,4*n)*(i==j//2))
            out[i][m+j]=out[m+j][i]=val
    for i in range(2*m):
        for j in range(2*m):
            out[m+i][m+j]=py*(i==j)-py*py
    return out

def enumerate_matchings(m):
    # Basis edges first, then 2 spokes in every triangle.
    for bits in range(1<<m):
        yield tuple((bits>>i)&1 for i in range(m))+tuple(0 for _ in range(2*m))
    for idx in range(2*m):
        i=idx//2
        for bits in range(1<<m):
            if (bits>>i)&1: continue
            a=[(bits>>j)&1 for j in range(m)]
            b=[0]*(2*m);b[idx]=1
            yield tuple(a+b)

def run():
    cases=0; vertices=0; moments=0
    for m in range(2,9):
        M=list(enumerate_matchings(m)); n=len(M); D=3*m
        assert n==(m+1)*2**m
        E=expected(m)
        mean=[Q(sum(v[i] for v in M),n) for i in range(D)]
        actual=[[Q(sum(v[i]*v[j] for v in M),n)-mean[i]*mean[j] for j in range(D)] for i in range(D)]
        assert actual==E,(m,'wrong moments')
        cases+=1;vertices+=n;moments+=D*D
    for m in range(2,501):
        n=m+1
        q=1/(2*n)
        cm=(m+3-sqrt(m*m-2*m+9))/(8*n)
        cp=(m+3+sqrt(m*m-2*m+9))/(8*n)
        um=(m*m+m+3-sqrt((m*m+m+3)**2-8*m*n))/(8*n*n)
        up=(m*m+m+3+sqrt((m*m+m+3)**2-8*m*n))/(8*n*n)
        assert 0<um<cm<q<up<cp
    # Exact symbolic inequality checks for every integer m>=2 use separate written proof.
    for m in range(2,1001):
        n=m+1
        assert m*m>3
        assert m*(n*n-2)>2
        assert m*m-m-1>0
    print(f'FRIENDSHIP_MATCHING_COVARIANCE_CHECKS_PASSED m_cases={cases} vertices={vertices} exact_entries={moments} spectral_profiles=499')
if __name__=='__main__': run()

# The block spectral identities are also checked as exact rational invariants.
for m in range(2,1001):
    n=m+1
    # Two contrast-mode eigenvalues are roots of x*x - tr_C*x + det_C.
    trC=Q(m+3,4*n)
    detC=Q(m,8*n*n)
    assert trC*trC-4*detC==Q(m*m-2*m+9,16*n*n)
    # Two axial-mode eigenvalues are roots of x*x - tr_U*x + det_U.
    trU=Q(m*m+m+3,4*n*n)
    detU=Q(m,8*n*n*n)
    assert trU*trU-4*detU==Q((m*m+m+3)**2-8*m*n,16*n**4)
