"""Exact checks for the age-resolved recursive-tree degree-leaf covariance law."""
from itertools import product
from fractions import Fraction

def harmonic(m):
    return sum((Fraction(1,k) for k in range(1,m+1)),Fraction(0))

def predicted(n,i):
    if i == 1:
        return Fraction(n-2,2*(n-1))
    if i == n:
        return Fraction(0)
    return Fraction(n-i,2*(n-1))-Fraction(i-1,n-1)*(harmonic(n-2)-harmonic(i-2))

def exhaustive(n):
    count=0
    sum_leaves=0
    sum_degree=[0]*(n+1)
    sum_product=[0]*(n+1)
    for choices in product(*(range(1,j) for j in range(2,n+1))):
        count+=1
        children=[0]*(n+1)
        for j,p in enumerate(choices,2):
            children[p]+=1
        leaves=sum(children[i]==0 for i in range(1,n+1))
        sum_leaves+=leaves
        for i in range(1,n+1):
            sum_degree[i]+=children[i]
            sum_product[i]+=children[i]*leaves
    for i in range(1,n+1):
        actual=Fraction(sum_product[i],count)-Fraction(sum_degree[i]*sum_leaves,count*count)
        assert actual==predicted(n,i),(n,i,actual,predicted(n,i))
    return n

def analytic(n,i):
    if i==n:return Fraction(0)
    result=Fraction(0)
    for j in range(i+1,n+1):
        if i==1:
            if j>2:result+=Fraction(1,2*(n-1))
        else:
            result+=Fraction(1,2*(n-1))-Fraction(i-1,(n-1)*(j-2))
    return result

if __name__=='__main__':
    checks=0
    for n in range(2,9):
        exhaustive(n)
        checks+=n
    for n in range(2,121):
        for i in range(1,n+1):
            assert analytic(n,i)==predicted(n,i),(n,i)
            checks+=1
    for n in range(7,121):
        a=[predicted(n,i) for i in range(2,n)]
        assert a[0]>0 and a[-1]<0
        s=[1 if x>0 else (-1 if x<0 else 0) for x in a]
        assert not any(s[j]==-1 and s[k]==1 for j in range(len(s)) for k in range(j+1,len(s)))
        checks+=1
    print('PASS:',checks,'exact comparisons; full tree enumeration n=2..8, analytic identities n=2..120, sign ordering n=7..120')
