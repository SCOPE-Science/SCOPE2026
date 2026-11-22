"""Exact finite-sample checks for circular Fourier energies; no external data."""
from itertools import combinations, product
from fractions import Fraction
from math import comb, sqrt

def central_moment_direct(n, freqs):
    """Expand each centered energy into edge characters and integrate exactly."""
    es=list(combinations(range(n),2))
    total=0
    for choices in product(es, repeat=len(freqs)):
        for signs in product((-1,1), repeat=len(freqs)):
            balance=[0]*n
            for (u,v),k,sgn in zip(choices, freqs, signs):
                balance[u]+=k*sgn
                balance[v]-=k*sgn
            total+=all(x==0 for x in balance)
    return Fraction(total,n**len(freqs))

def resonance(a,b,c):
    return int(a+b==c or a+c==b or b+c==a)

def predicted_mixed3(n,a,b,c):
    return Fraction(n-1,n*n)*resonance(a,b,c)+Fraction(2*(n-1)*(n-2),n*n)*int(a==b==c)

def predicted_var(n,a,b):
    return Fraction(n-1,n)*int(a==b)

checks=0
for n in range(2,6):
    for a,b in product(range(1,5),repeat=2):
        v=central_moment_direct(n,[a,b]); expect=predicted_var(n,a,b)
        assert v==expect,(n,a,b,v,expect)
        checks+=1
    for a,b,c in product(range(1,5),repeat=3):
        v=central_moment_direct(n,[a,b,c]); expect=predicted_mixed3(n,a,b,c)
        assert v==expect,(n,a,b,c,v,expect)
        checks+=1

for n in range(2,6):
    for M in range(1,7):
        x=sum((central_moment_direct(n,[a,b,c]) for a,b,c in product(range(1,M+1),repeat=3)),Fraction())
        y=Fraction((n-1)*(2*M*(n-2)+3*M*(M-1)//2),n*n)
        assert x==y,(n,M,x,y)
        checks+=1

for n in range(2,50):
    b=4*n-11
    # Check that discrete difference's sign agrees with the exact threshold.
    for M in range(1,70):
        lhs=(3*M+b)/sqrt(M)
        rhs=(3*(M+1)+b)/sqrt(M+1)
        predicted=(b*b - 9*M*(M+1)) if b>=0 else -1
        # difference negative if 3sqrt(M(M+1))<b
        should_decrease = b>0 and 9*M*(M+1)<b*b
        assert (rhs<lhs)==should_decrease,(n,M,lhs,rhs,should_decrease)
        checks+=1


# Independent weighted-cubic reconstruction from all mixed moments.
for n in range(2,6):
    for weights in ([0,1,0,2,3], [1,2,0,0,4], [2,0,1,0,0], [1,1,1,1,1], [0,0,0,0,0]):
        M=len(weights)
        direct=sum((weights[a-1]*weights[b-1]*weights[c-1]*central_moment_direct(n,[a,b,c])
                    for a,b,c in product(range(1,M+1),repeat=3)),Fraction())
        diagonal=2*(n-2)*sum(w**3 for w in weights)
        conv=3*sum(weights[a-1]*weights[b-1]*weights[a+b-1]
                   for a in range(1,M+1) for b in range(1,M+1) if a+b<=M)
        predicted=Fraction(n-1,n*n)*(diagonal+conv)
        assert direct==predicted,(n,weights,direct,predicted)
        checks+=1

# Strictly unique minimizing cutoff: algebraic threshold and no integer tie.
for n in range(3,101):
    b=4*n-11
    m=next(M for M in range(1,4*n) if 9*M*(M+1)>b*b)
    assert m==1 or 9*(m-1)*m<b*b
    assert 9*m*(m+1)>b*b
    for M in range(1,min(3*n,120)):
        assert 9*M*(M+1)!=b*b
        checks+=1
print('PASS',checks,'exact/moment and monotonicity checks')
print('examples')
for n in [2,3,4,5,10,30,100]:
    b=4*n-11
    if b>0:
        mins=[M for M in range(1,4*n+10) if not (b>0 and 9*M*(M+1)<b*b)]
        minimizer=mins[0]
    else:minimizer=1
    print(n,minimizer,(3*minimizer+b)/(2*sqrt(n*(n-1)*minimizer)))
