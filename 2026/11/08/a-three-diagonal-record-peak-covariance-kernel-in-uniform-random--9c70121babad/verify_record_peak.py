"""Independent finite exact checks of the record-peak covariance kernel.
Run with Python 3: python verify_record_peak.py
The all-order proof is in RESULT.md; finite tests are auxiliary.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

def kernel(i,j):
    if i == j-1:
        return Fraction(2-j,3*(j-1)*(j+1))
    if i == j:
        return Fraction(2*j-1,3*j*(j+1))
    if i == j+1:
        return Fraction(-1,3*(j+1))
    return Fraction(0)

def test(n):
    N=factorial(n)
    sumr=[0]*n
    sump=[0]*n
    both=[[0]*n for _ in range(n)]
    for v in permutations(range(1,n+1)):
        rec=[]
        mx=0
        for x in v:
            rec.append(int(x>mx));mx=max(mx,x)
        peak=[0]*n
        for j in range(1,n-1):
            peak[j]=int(v[j-1]<v[j]>v[j+1])
        for i in range(n):
            sumr[i]+=rec[i]
            for j in range(1,n-1):
                both[i][j]+=rec[i]*peak[j]
        for j in range(1,n-1):
            sump[j]+=peak[j]
    assertions=0
    for j in range(2,n):
        for i in range(1,n+1):
            found=Fraction(both[i-1][j-1],N)-Fraction(sumr[i-1]*sump[j-1],N*N)
            assert found == kernel(i,j),(n,i,j,found,kernel(i,j))
            assertions+=1
        found=sum(Fraction(both[i-1][j-1],N)-Fraction(sumr[i-1]*sump[j-1],N*N) for i in range(1,n+1))
        assert found == Fraction(1,3*j*(j-1)*(j+1))
        assertions+=1
    found=sum(Fraction(both[i-1][j-1],N)-Fraction(sumr[i-1]*sump[j-1],N*N) for j in range(2,n) for i in range(1,n+1))
    assert found == Fraction((n-2)*(n+1),12*n*(n-1))
    assertions+=1
    return assertions

if __name__=='__main__':
    total=sum(test(n) for n in range(3,9))
    print(f'PASS: {total} exact rational assertions, exhaustive n=3,...,8')
