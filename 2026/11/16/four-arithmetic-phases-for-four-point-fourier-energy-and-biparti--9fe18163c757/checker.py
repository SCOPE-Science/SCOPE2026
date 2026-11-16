"""Exact checks for four-frequency additive-energy and graph-collision identities."""
from itertools import combinations
from math import comb, gcd
import cmath


def energy(N, A):
    r=[0]*N
    for a in A:
        for b in A:
            r[(a-b)%N]+=1
    return sum(v*v for v in r)


def predicted(N):
    if N%4==0: return 64
    if N%5==0: return 52
    if N%2==0: return 48
    return 44


def equality_shape(N, A):
    A=set(A)
    # First three classifications are exact finite group-coset predicates.
    if N%4==0:
        h=N//4
        return A=={(a+j*h)%N for j in range(4) for a in [min(A)]}
    if N%5==0:
        h=N//5
        return any(A.issubset({(a+j*h)%N for j in range(5)}) for a in A)
    if N%2==0:
        h=N//2
        return all((a+h)%N in A for a in A)
    return any({(a+j*d)%N for j in range(4)}==A for a in A for d in range(1,N))


def direct_graph_energy(N,A):
    A=set(A)
    edges={(x,y) for x in range(N) for y in range(N) if (x in A)!=(y in A)}
    vals={}
    for x,y in edges:
        for s,t in edges:
            z=((x-s)%N,(y-t)%N)
            vals[z]=vals.get(z,0)+1
    return sum(v*v for v in vals.values())


def graph_energy_formula(N,E):
    t=N*E-4**4
    b=2*4*(N-4)
    numerator=b**4+2*(N-8)**4*t+16*t*t
    assert numerator%(N*N)==0
    return numerator//(N*N)


def run():
    n_cases=0; optimal=0
    for N in range(8,34):
        observed=0; sets=[]
        for A in combinations(range(N),4):
            x=energy(N,A)
            assert x<=predicted(N),(N,A,x,predicted(N))
            assert (x==predicted(N))==equality_shape(N,A),(N,A,x,predicted(N))
            if x==predicted(N): optimal+=1
            observed=max(observed,x)
            n_cases+=1
        assert observed==predicted(N),(N,observed,predicted(N))
    count_graph=0
    for N in range(8,14):
        for A in combinations(range(N),4):
            # Direct pair-difference counting over the directed edge set;
            # slow quadratic only on small samples, still independent of Fourier formula.
            if count_graph>=60: break
            assert graph_energy_formula(N,energy(N,A))==direct_graph_energy(N,A)
            count_graph+=1
    print('PASS',n_cases,'four-point sets,',optimal,'sharp-equality cases,',count_graph,'independent graph comparisons')

if __name__=='__main__': run()
