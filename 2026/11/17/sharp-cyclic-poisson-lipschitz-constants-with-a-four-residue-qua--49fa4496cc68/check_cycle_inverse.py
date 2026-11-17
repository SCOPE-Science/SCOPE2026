from fractions import Fraction as F
from itertools import product

def green(n,j):
    return F(n*n-1,12*n)-F((j%n)*(n-j%n),2*n)

def explicit(n):
    r=n%4
    if r==0:return F(n*n,32)
    if r==1:return (F(n*n+1)-F(2,n))/32
    if r==2:return F(n*n+4,32)
    return (F(n*n+1)+F(2,n))/32

def norm(n):
    v=[green(n,j) for j in range(n)]
    middle=sorted(v)
    med=middle[n//2]
    return sum(abs(x-med) for x in v)

checks=0
for n in range(3,200):
    assert norm(n)==explicit(n),(n,norm(n),explicit(n))
    checks+=1
print('ALL_FOUR_RESIDUE_FORMULAS_PASSED',checks)

lap_checks=0
for n in range(3,23):
    g=[green(n,j) for j in range(n)]
    assert sum(g)==0
    for j in range(n):
        assert 2*g[j]-g[(j-1)%n]-g[(j+1)%n]==F(int(j==0))-F(1,n)
        lap_checks+=1
print('INDEPENDENT_DISCRETE_GREEN_RESIDUALS_PASSED',lap_checks)

# Enumerate every vertex of the zero-sum cube: for even n all balanced signed vertices;
# for odd n choose one zero, balance rest. Then evaluate true linear Green functional.
vertex_checks=0
for n in range(3,13):
    g=[green(n,j) for j in range(n)]
    best=F(0)
    for s in product((-1,1),repeat=n):
        if sum(s)==0:
            value=abs(sum(g[j]*s[j] for j in range(n)))
            best=max(best,value)
            vertex_checks+=1
    if n%2:
        for missing in range(n):
            for sub in product((-1,1),repeat=n-1):
                if sum(sub)==0:
                    s=list(sub);s.insert(missing,0)
                    value=abs(sum(g[j]*s[j] for j in range(n)))
                    best=max(best,value)
                    vertex_checks+=1
    assert best==explicit(n),(n,best,explicit(n))
print('EXHAUSTIVE_ZERO_SUM_CUBE_VERTEX_EVALUATIONS_PASSED',vertex_checks)
print('ALL_CYCLE_LIPSCHITZ_POISSON_CHECKS_PASSED')
