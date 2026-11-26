"""Reproduce finite checks for a random-erasure Gabor variance theorem.

Use Python >=3.9; only the standard library. The proof of the general theorem
is analytic; these tests do not establish it for all dimensions.
"""
import cmath
import itertools
import math
from fractions import Fraction


def orbit(g):
    N = len(g)
    return [[g[(j-a) % N] * cmath.exp(2j*math.pi*b*j/N)
             for j in range(N)] for a in range(N) for b in range(N)]


def weight(v, u):
    return abs(sum(x.conjugate()*y for x,y in zip(v,u)))**2


def small_orbit_test(N, g):
    v = orbit(g)
    L = N*N
    w = [[weight(a,b) for b in v] for a in v]
    Delta = sum((x-1/(N+1))**2 for x in w[0][1:])
    for k in range(2,L-1):
        vals = []
        for S in itertools.combinations(range(L), k):
            vals.append(sum(w[x][y] for x in S for y in S))
        empirical_mean = sum(vals)/len(vals)
        empirical_var = sum((x-empirical_mean)**2 for x in vals)/len(vals)
        target_mean = k+k*(k-1)/(N+1)
        target_var = (2*k*(k-1)*(L-k)*(L-k-1)
                      / ((L-1)*(L-2)*(L-3)) * Delta)
        assert abs(empirical_mean-target_mean)<1e-8
        assert abs(empirical_var-target_var)<1e-8


def alltop_weights(N):
    g = [cmath.exp(2j*math.pi*((j**3)%N)/N)/math.sqrt(N)
         for j in range(N)]
    V=orbit(g)
    ws = [weight(V[0],u) for u in V]
    assert all(abs(x)<1e-10 for x in ws[1:N])
    assert all(abs(x-1/N)<1e-10 for x in ws[N:])
    Delta = sum((x-1/(N+1))**2 for x in ws[1:])
    assert abs(Delta-(N-1)/(N*(N+1)))<1e-10


def exact_alltop_occupancy(N, k):
    # Number of subsets with k elements and squared class count s.
    dp = {(0,0):1}
    for _ in range(N):
        nx={}
        for (r,s),ways in dp.items():
            for a in range(min(N,k-r)+1):
                z=(r+a,s+a*a)
                nx[z]=nx.get(z,0)+ways*math.comb(N,a)
        dp=nx
    count=math.comb(N*N,k)
    assert sum(w for (r,s),w in dp.items() if r==k)==count
    mean=sum(Fraction(w,count)*Fraction(k*N+k*k-s,N)
             for (r,s),w in dp.items() if r==k)
    second=sum(Fraction(w,count)*Fraction(k*N+k*k-s,N)**2
               for (r,s),w in dp.items() if r==k)
    V=second-mean**2
    n=N*N
    Delta=Fraction(N-1,N*(N+1))
    target=(Fraction(2*k*(k-1)*(n-k)*(n-k-1),
                     (n-1)*(n-2)*(n-3))*Delta)
    assert mean==Fraction(k,1)+Fraction(k*(k-1),N+1)
    assert V==target


def main():
    small_orbit_test(2,[1.0,0.0])
    small_orbit_test(2,[math.sqrt(.3),1j*math.sqrt(.7)])
    small_orbit_test(3,[1.,0.,0.])
    small_orbit_test(3,[.5,.5,math.sqrt(.5)])
    for p in (5,7):
        alltop_weights(p)
    for k in (2,3,5,10,12,16):
        exact_alltop_occupancy(5,k)
    print('PASS: exact subset enumeration in dimensions 2,3;')
    print('      Alltop ambiguity in dimensions 5,7;')
    print('      exact rational occupancy variances at six sizes in dimension 5.')

if __name__=='__main__': main()
