"""Reproducibility checks for exact moments of the radius-one limited permutation channel."""
from itertools import product
from fractions import Fraction
from math import comb


def direct_ball(word):
    """Channel images from all disjoint adjacent swaps; independent of DP count."""
    n=len(word)
    images=set()
    def walk(i, out):
        if i>=n:
            images.add(tuple(out)); return
        walk(i+1,out+(word[i],))
        if i+1<n:
            walk(i+2,out+(word[i+1],word[i]))
    walk(0,())
    return len(images)


def ball_dp(word):
    """Independent-set recurrence on effective edges, constant-memory."""
    a,b=1,1
    for i in range(len(word)-1):
        a,b=a+(word[i]!=word[i+1])*b,a
    return a


def moments(q,n):
    p=Fraction(q-1,q)
    N=n-1
    mean0,mean1=Fraction(1),Fraction(1)+p
    if N==0: mean=mean0
    elif N==1: mean=mean1
    else:
        for _ in range(2,N+1):mean0,mean1=mean1,mean1+p*mean0
        mean=mean1
    a,b,c=Fraction(1),Fraction(0),Fraction(0)
    for _ in range(N):
        a,b,c=a+2*b+c,p*(a+b),p*a
    return mean,a+2*b+c


def run():
    tests=0
    for q,nmax in [(2,12),(3,9),(4,7)]:
        for n in range(1,nmax+1):
            total=0; total_sq=0
            for word in product(range(q),repeat=n):
                b=direct_ball(word)
                assert b==ball_dp(word),(q,n,word,b,ball_dp(word))
                total+=b;total_sq+=b*b;tests+=1
            e1,e2=moments(q,n)
            assert Fraction(total,q**n)==e1,(q,n,'first',total,e1)
            assert Fraction(total_sq,q**n)==e2,(q,n,'second',total_sq,e2)
    print('PASS: independent channel enumeration, exact matching recurrence, and two annealed moments')
    print('source instances:',tests)
    for q in [2,3,5]:
        for n in [15,25,50]:
            a,b=moments(q,n)
            assert b>a*a
    print('PASS: strict positive variances and finite rational matrix recurrences')

if __name__=='__main__': run()
