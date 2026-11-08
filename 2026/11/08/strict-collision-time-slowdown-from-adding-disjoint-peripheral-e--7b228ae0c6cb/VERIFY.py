"""Independent exact collision-time checks for a hub with matched peripheral edges.

Standard library only. Uses the full unordered two-walker Markov chain, rather than
its symmetry quotient, and rational Gaussian elimination.
"""
from fractions import Fraction
from itertools import combinations

def closed(n, k):
    num = (10*n**3+8*n**2-18*n+27*k*n**2-66*k*n-9*k
           +8*k*k*n+10*k*k-4*k**3)
    den = (n-1)*(5*n*n+14*n+9+8*k)
    return Fraction(num,den)

def exact_pair_generator(n,k):
    neighbors = [set(range(1,n+1))] + [{0} for _ in range(n)]
    for i in range(k):
        a,b=2*i+1,2*i+2
        neighbors[a].add(b)
        neighbors[b].add(a)
    states=list(combinations(range(n+1),2))
    ix={st:i for i,st in enumerate(states)}
    mat=[[Fraction(0) for _ in states] for _ in states]
    ans=[Fraction(1) for _ in states]
    for row,(a,b) in enumerate(states):
        mat[row][row]=Fraction(2)
        for v,w in ((a,b),(b,a)):
            for t in neighbors[v]:
                if t != w:
                    mat[row][ix[tuple(sorted((t,w)))]]-=Fraction(1,len(neighbors[v]))
    N=len(states)
    for col in range(N):
        pivot=next(i for i in range(col,N) if mat[i][col])
        if pivot!=col:
            mat[col],mat[pivot]=mat[pivot],mat[col]
            ans[col],ans[pivot]=ans[pivot],ans[col]
        scale=mat[col][col]
        for j in range(col,N): mat[col][j]/=scale
        ans[col]/=scale
        for i in range(col+1,N):
            fac=mat[i][col]
            if fac:
                for j in range(col,N): mat[i][j]-=fac*mat[col][j]
                ans[i]-=fac*ans[col]
    x=[Fraction(0) for _ in states]
    for i in range(N-1,-1,-1):
        x[i]=ans[i]-sum(mat[i][j]*x[j] for j in range(i+1,N))
    return sum(x[ix[(i,j)]] for i in range(1,n+1) for j in range(i+1,n+1))/Fraction(n*(n-1),2)

def poly(n,k):
    # numerator of M(n,k+1)-M(n,k) with u=n-2(k+1)
    u=n-2*(k+1)
    return (2560*k**4+5040*k**3*u+10928*k**3
       +3660*k*k*u*u+15688*k*k*u+14660*k*k
       +1160*k*u**3+7272*k*u*u+12896*k*u+5264*k
       +135*u**4+1088*u**3+2640*u*u+1404*u-1235)

def run():
    cases=0
    for n in range(3,11):
        for k in range(0,n//2+1):
            got=exact_pair_generator(n,k)
            want=closed(n,k)
            assert got==want,(n,k,got,want)
            cases+=1
    # All admissible adjacent increments including n even, final k=n/2-1.
    diffs=0
    for n in range(3,150):
        for k in range(n//2):
            d=5*n*n+14*n+9+8*k
            assert closed(n,k+1)-closed(n,k)==Fraction(poly(n,k),(n-1)*d*(d+8)),(n,k)
            assert poly(n,k)>0,(n,k)
            diffs+=1
        assert closed(n,0)==Fraction(2*n,n+1)
        if n%2==0:
            m=n//2
            assert closed(n,m)==Fraction(5*m*(4*m-3),(2*m-1)*(2*m+3))
    print(f'PASS exact full generator: {cases} (n,k) cases, 3<=n<=10')
    print(f'PASS exact adjacent increments and positivity: {diffs} cases, 3<=n<150')
    print('PASS endpoint identities for 3<=n<150')

if __name__=='__main__':
    run()
