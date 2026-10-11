#!/usr/bin/env python3
import math
import cmath

def mm(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][q]*B[q][j] for q in range(k)) for j in range(m)] for i in range(n)]

def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

def ueff(N):
    s=math.sqrt(max(0,N-2))
    return [
        [1-2/N, -2/N,  2*s/N],
        [-2/N, 1-2/N, 2*s/N],
        [-2*s/N, -2*s/N, 1-4/N],
    ]

def fidelity_formula(N,t):
    w=math.acos((N-4)/N)
    return math.sin(w*t/2)**4

def fidelity_matrix(N,t):
    v=[1+0j,0j,0j]
    U=ueff(N)
    for _ in range(t):
        v=mv(U,v)
    return abs(v[1])**2

def main():
    comparisons=0
    for N in range(2,81):
        U=ueff(N)
        # numerical unitarity
        for i in range(3):
            for j in range(3):
                x=sum(U[k][i]*U[k][j] for k in range(3))
                assert abs(x-(1 if i==j else 0)) < 3e-12
        for t in range(0,61):
            a=fidelity_matrix(N,t)
            b=fidelity_formula(N,t)
            assert abs(a-b)<3e-11,(N,t,a,b)
            comparisons+=1

    exact={2:1,4:2,8:3}  # effective t; physical time is 2t
    for N,t in exact.items():
        assert abs(fidelity_formula(N,t)-1.0)<1e-14

    # Rational-angle algebraic-integer candidates: 2 cos(omega) must be in {-2,-1,0,1,2}.
    candidates=[]
    for N in range(2,10001):
        x=2-8/N
        if any(abs(x-j)<1e-15 for j in (-2,-1,0,1,2)):
            candidates.append(N)
    assert candidates==[2,4,8],candidates

    # Representative PGST witnesses: finite evidence only.
    pgst_witnesses={}
    for N in (3,5,6,7,9,10,11,25,100):
        best=(-1.0,None)
        for t in range(1,250000):
            f=fidelity_formula(N,t)
            if f>best[0]:
                best=(f,t)
            if f>0.999999:
                break
        assert best[0]>0.9999,(N,best)
        pgst_witnesses[N]=(best[0],2*best[1])

    # Source N=100 first local maximum at 22 physical steps is not exact.
    f100=fidelity_formula(100,11)
    assert 0.999 < f100 < 1.0

    print("VERIFY_OK")
    print("matrix_formula_comparisons =",comparisons)
    print("exact_sizes = 2,4,8")
    print("first_physical_times = 2,4,6")
    print("N100_fidelity_at_22 =",format(f100,".15f"))
    for N,(f,T) in pgst_witnesses.items():
        print("pgst_witness",N,"physical_time",T,"fidelity",format(f,".12f"))

if __name__=="__main__":
    main()
