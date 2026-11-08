"""Exact finite replay of peak probabilities in record-weighted permutations."""
from fractions import Fraction
from itertools import permutations
from math import factorial

def expected_peak(i, theta):
    return Fraction(1,3)-theta*(theta-1)*(theta-2)/(3*(theta+i-2)*(theta+i-1)*(theta+i))

def test():
    checks=0
    for n in range(3,9):
        for theta in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(3)):
            weights=Fraction(0)
            counts=[Fraction(0) for _ in range(n+1)]
            for p in permutations(range(1,n+1)):
                mx=0; rec=0
                for value in p:
                    if value>mx:
                        mx=value; rec+=1
                wt=theta**rec
                weights+=wt
                for i in range(2,n):
                    if p[i-2]<p[i-1]>p[i]:counts[i]+=wt
            expected_weight=Fraction(1)
            for j in range(n):expected_weight*=theta+j
            assert weights==expected_weight,(n,theta,weights,expected_weight)
            checks+=1
            total=Fraction(0)
            for i in range(2,n):
                actual=counts[i]/weights
                expected=expected_peak(i,theta)
                assert actual==expected,(n,theta,i,actual,expected)
                total+=actual
                checks+=1
                if theta in (1,2): assert actual==Fraction(1,3)
                elif theta in (Fraction(1,2),Fraction(3)): assert actual<Fraction(1,3)
                else: assert actual>Fraction(1,3)
                checks+=1
            rhs=Fraction(n-2,3)-(theta-1)*(theta-2)/6*(1/(theta+1)-theta/((theta+n-2)*(theta+n-1)))
            assert total==rhs,(n,theta,total,rhs)
            checks+=1
    print('VERIFY_OK',checks,'exact assertions')
if __name__=='__main__':test()
