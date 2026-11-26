from itertools import permutations, combinations
from fractions import Fraction
from math import factorial


def cycle_count(p):
    n=len(p)
    seen=[False]*n
    c=0
    for i in range(n):
        if not seen[i]:
            c += 1
            j=i
            while not seen[j]:
                seen[j]=True
                j=p[j]-1
    return c


def H(k):
    return sum((Fraction(1,j) for j in range(1,k+1)), Fraction(0))

partial_checks=0
for n in range(2,8):
    ps=list(permutations(range(1,n+1)))
    denom=factorial(n-2)
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            groups={}
            for p in ps:
                key=(p[a-1],p[b-1])
                s,count=groups.get(key,(0,0))
                groups[key]=(s+cycle_count(p),count+1)
            for x in range(1,n+1):
                for y in range(1,n+1):
                    if x==y: continue
                    s,count=groups[(x,y)]
                    assert count==denom
                    c0=(1 if x==a else 0)+(1 if y==b else 0)+(1 if (x==b and y==a) else 0)
                    assert Fraction(s,count)==H(n-2)+c0
                    partial_checks += 1

local_checks=0
global_checks=0
permutation_states=0
for n in range(2,10):
    M=factorial(n)
    sumC=0
    sumInv=0
    sumCInv=0
    sumCI={(a,b):0 for a in range(n) for b in range(a+1,n)}
    for p in permutations(range(1,n+1)):
        c=cycle_count(p)
        inv=0
        sumC += c
        for a in range(n):
            pa=p[a]
            for b in range(a+1,n):
                I=1 if pa>p[b] else 0
                inv += I
                if I:
                    sumCI[(a,b)] += c
        sumInv += inv
        sumCInv += c*inv
        permutation_states += 1
    EC=Fraction(sumC,M)
    EInv=Fraction(sumInv,M)
    cov_global=Fraction(sumCInv,M)-EC*EInv
    assert EC==H(n)
    assert EInv==Fraction(n*(n-1),4)
    assert cov_global == -Fraction(2*n-1,12)
    global_checks += 1
    for (a,b),sci in sumCI.items():
        ECI=Fraction(sci,M)
        cov=ECI-EC*Fraction(1,2)
        d=b-a
        expected=-Fraction(2*d-1,2*n*(n-1))
        assert cov==expected
        cond=Fraction(sci, M//2)
        assert cond == H(n)-Fraction(2*d-1,n*(n-1))
        local_checks += 2

print('PASS')
print('partial_completion_checks=',partial_checks)
print('local_covariance_and_conditional_checks=',local_checks)
print('global_covariance_checks=',global_checks)
print('enumerated_permutation_states=',permutation_states)
