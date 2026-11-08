"""Independent small-rank enumeration and coefficient checks for a central Fourier projector."""
from itertools import permutations
from math import factorial
from fractions import Fraction
from decimal import Decimal, getcontext

def cycles_12(perm):
    n=len(perm);seen=[False]*n;X1=X2=0
    for i in range(n):
        if seen[i]:continue
        j=i;k=0
        while not seen[j]:
            seen[j]=True;j=perm[j];k+=1
        X1+=k==1;X2+=k==2
    return X1,X2

def a_values(N):
    # Every permutation has its cycle containing 0 of size j>=3.
    a=[0]*(N+1);a[0]=1
    from math import comb
    for n in range(1,N+1):
        a[n]=sum(comb(n-1,j-1)*factorial(j-1)*a[n-j] for j in range(3,n+1))
    return a

a=a_values(12)
for n in range(4,9):
    neg=0;sumabs=0;sumchi=0
    for p in permutations(range(n)):
        x1,x2=cycles_12(p)
        chi=x1*(x1-1)//2+x2-x1
        sumabs+=abs(chi);sumchi+=chi
        if chi<0:
            assert chi==-1 and x1 in (1,2) and x2==0
            neg+=1
    assert sumchi==0
    q=Fraction(a[n-1],factorial(n-1))+Fraction(a[n-2],2*factorial(n-2))
    assert q==Fraction(neg,factorial(n))
    d=n*(n-3)//2
    norm=d*Fraction(sumabs,factorial(n))
    assert norm==n*(n-3)*q
    print('n',n,'neg_count',neg,'q',str(q),'norm',str(norm))
# Distinct coefficient computation: exp(-z-z²/2) recurrence n*c[n]=-c[n-1]-c[n-2].
c=[Fraction(0)]*13;c[0]=Fraction(1)
for n in range(1,13):c[n]=-(c[n-1]+(c[n-2] if n>=2 else 0))/n
for n in range(4,12):
    f1=sum(c[:n]);f2=sum(c[:n-1]);q=f1+f2/2
    assert q==Fraction(a[n-1],factorial(n-1))+Fraction(a[n-2],2*factorial(n-2))
getcontext().prec=25
limit=Decimal(3)/2*(-Decimal(3)/2).exp()
print('asymptotic normalized limit',limit)
# Additional independent finite regular-representation convolution check.
for n in (4,5):
    perms=list(permutations(range(n)))
    idp=tuple(range(n))
    def inv(p):
        r=[0]*len(p)
        for i,j in enumerate(p):r[j]=i
        return tuple(r)
    def compose(a,b):return tuple(a[b[i]] for i in range(len(a)))
    ch={p: (lambda x,y:x*(x-1)//2+y-x)(*cycles_12(p)) for p in perms}
    d=n*(n-3)//2
    for g in perms:
        v=sum(ch[h]*ch[compose(inv(h),g)] for h in perms)
        assert d*v==factorial(n)*ch[g]
    print('exact central idempotence verified',n,'group elements',len(perms))
print('PAIR_CHARACTER_PROJECTOR_CHECKS_PASS')
