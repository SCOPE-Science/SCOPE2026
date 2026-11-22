from fractions import Fraction as Q
from math import gcd

def f(a,x):
    y=a*x
    y-=y.numerator//y.denominator
    return min(y,1-y)

def exact_cov(A,B):
    pts=sorted(set([Q(k,2*A) for k in range(2*A+1)]+[Q(k,2*B) for k in range(2*B+1)]))
    out=Q(0)
    for left,right in zip(pts,pts[1:]):
        mid=(left+right)/2
        def h(x):return (f(A,x)-Q(1,4))*(f(B,x)-Q(1,4))
        out+=(right-left)*(h(left)+4*h(mid)+h(right))/6
    return out

def formula(A,B):
    g=gcd(A,B)
    if (A//g)%2==0 or (B//g)%2==0:return Q(0)
    return Q(g**4,48*A*A*B*B)

count=0
for A in range(1,29):
    for B in range(1,29):
        got=exact_cov(A,B); target=formula(A,B)
        assert got==target,(A,B,got,target)
        count+=1
print('exact rational identity validated for',count,'ordered pairs A,B<=28')
for m,n in [(2,3),(2,4),(3,9),(3,5),(6,12),(4,8),(9,27)]:
    for N in [5,10,20]:
        val=sum((formula(m**j,n**k) for j in range(N) for k in range(N)),Q(0))
        print((m,n,N),float(val), 'normalized',float(val/N))
