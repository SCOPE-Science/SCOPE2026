"""Exact rational checks for high-order Whittaker smoothing in path variation."""
from fractions import Fraction
from math import comb


def inv(a):
    n=len(a)
    b=[[Fraction(x) for x in row]+[Fraction(i==j) for j in range(n)] for i,row in enumerate(a)]
    for i in range(n):
        t=next(j for j in range(i,n) if b[j][i])
        b[i],b[t]=b[t],b[i]
        c=b[i][i]
        b[i]=[z/c for z in b[i]]
        for j in range(n):
            if j!=i:
                c=b[j][i]
                b[j]=[b[j][k]-c*b[i][k] for k in range(2*n)]
    return [row[n:] for row in b]


def theorem(p,lmbd):
    C=comb(2*p,p)
    M=max(comb(p-1,j)*(2**(p+1)-2-2*comb(p+1,j+1)) for j in range(p))
    return Fraction(1)+Fraction(lmbd,1+lmbd*C)*M, C, M


def direct(p,lmbd):
    n=p+1
    d=[(-1)**(p-j)*comb(p,j) for j in range(n)]
    A=[[Fraction(int(i==j))+lmbd*d[i]*d[j] for j in range(n)] for i in range(n)]
    S=inv(A)
    # D sends vectors to successive differences; the jth basis vector of difference coordinates
    # comes from a step vector with zeros up to j and ones from j+1 onward.
    vals=[]
    for j in range(p):
        step=[Fraction(int(k>j)) for k in range(n)]
        y=[sum(S[i][k]*step[k] for k in range(n)) for i in range(n)]
        vals.append(sum(abs(y[i+1]-y[i]) for i in range(p)))
    return max(vals), vals


def main():
    for p in range(1,13):
        for lam in [Fraction(1,23),Fraction(2,3),Fraction(9,2)]:
            t,_,_=theorem(p,lam)
            actual,vals=direct(p,lam)
            assert actual==t,(p,lam,t,actual)
            assert all(v<=t for v in vals)
    print('EXACT_RANK_ONE_AND_ALL_STEP_CUTS_PASS p=1..12, lambda=1/23,2/3,9/2')
    expected={1:-2,2:0,3:6,4:30,5:132}
    assert all(theorem(p,Fraction(1,1))[2]==m for p,m in expected.items())
    print('SHARP_FIRST_ORDERS_TRICHOTOMY_PASS')
    for p in [50,100,200,500,1000]:
        c=comb(2*p,p)
        m=theorem(p,Fraction(1))[2]
        ratio=m/c
        assert 0<ratio<2
        print('HIGH_ORDER_RATIO',p,format(ratio,'.10f'))
    print('ALL_WHITTAKER_PATH_VARIATION_CHECKS_PASS')

if __name__=='__main__': main()
