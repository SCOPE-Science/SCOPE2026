"""Reproducible checks for an exact four-character Fourier frame erasure theorem.
No external packages are required. Exact rational enclosures certify the small orders.
"""
from fractions import Fraction as Q
from math import factorial, sin, pi, cos, sqrt, comb
from itertools import combinations


def atan_bounds(denom, terms=13):
    x=Q(1,denom)
    s=sum(((-1)**k*x**(2*k+1)/Q(2*k+1)) for k in range(terms))
    next_term=(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return min(s,s+next_term),max(s,s+next_term)

A=atan_bounds(5); B=atan_bounds(239)
PI_LOW=16*A[0]-4*B[1]
PI_HIGH=16*A[1]-4*B[0]
assert PI_LOW<Q(22,7) and PI_HIGH>Q(333,106)
assert Q(3141592653589,10**12) < PI_LOW < PI_HIGH < Q(3141592653590,10**12)


def cos_approx(x):
    return sum(((-1)**k*x**(2*k)/Q(factorial(2*k))) for k in range(11))


def cos_bounds(factor):
    # 0 <= factor <= 1, cos monotone decreasing on [0, pi]
    lo=PI_LOW*factor; hi=PI_HIGH*factor
    rem=hi**22/Q(factorial(22))
    return cos_approx(hi)-rem,cos_approx(lo)+rem


def interval_product(a,b):
    corners=[u*v for u in a for v in b]
    return min(corners),max(corners)


def r_bounds(N,d):
    d=min(d%N,(-d)%N)
    assert 1<=d<=N//2
    v=interval_product(cos_bounds(Q(d,N)),cos_bounds(Q(2*d,N)))
    return 4*v[0],4*v[1]


def square_upper(a):
    return max(a[0]*a[0],a[1]*a[1])


def upper_s(N,a,b):
    return sum(square_upper(r_bounds(N,d)) for d in [a,b,b-a])


def lower_beta_test(N,test):
    x=r_bounds(N,1); y=r_bounds(N,2)
    assert x[0]>0
    # beta is the positive root of beta^2-y*beta-2*x^2=0.
    assert test*test-y[0]*test-2*x[0]*x[0]<0


for N,beta_lower,s_upper in [(7,Q(291,100),Q(634,100)),
                              (8,Q(369,100),Q(801,100)),
                              (9,Q(434,100),Q(10,1))]:
    lower_beta_test(N,beta_lower)
    max_s=Q(0)
    for a,b in combinations(range(1,N),2):
        # If the set {0,a,b} is a cyclic triple, it is the extremizer.
        e={0,a,b}
        if any(e=={k%N,(k+1)%N,(k+2)%N} for k in range(N)):
            continue
        s=upper_s(N,a,b)
        if s>max_s:max_s=s
    assert max_s <= s_upper, (N,float(max_s))
    assert 4*s_upper/3 < beta_lower*beta_lower, (N,float(4*s_upper/3))
    print('CERTIFIED_SMALL_ORDER',N,'nonconsecutive_s_upper<',float(s_upper),
          'consecutive_beta>',float(beta_lower))

# Independent direct finite-mask calculation with cubic characteristic polynomial.
def r(N,d):
    return sin(4*pi*(d%N)/N)/sin(pi*(d%N)/N)


def top_of_zero_diagonal(x,y,z):
    s=x*x+y*y+z*z
    p=x*y*z
    # The top root of lambda^3-s lambda-2p=0 is >=sqrt(s/3).
    lo=sqrt(s/3);hi=2*max(abs(x),abs(y),abs(z))+1
    assert hi**3-s*hi-2*p>=-1e-8
    for _ in range(55):
        mid=(lo+hi)/2
        if mid**3-s*mid-2*p>=0:hi=mid
        else:lo=mid
    return hi

count=0
for N in range(7,40):
    aa=r(N,1);bb=r(N,2)
    target=4+(bb+sqrt(bb*bb+8*aa*aa))/2
    winners=[]
    for e in combinations(range(N),3):
        a,b,c=e
        w=4+top_of_zero_diagonal(r(N,b-a),r(N,c-b),r(N,c-a))
        if w>target+2e-9:raise AssertionError((N,e,w,target))
        if abs(w-target)<2e-9:winners.append(e)
        count+=1
    expected={tuple(sorted(((k+j)%N) for j in range(3))) for k in range(N)}
    assert set(winners)==expected,(N,len(winners))
print('FOUR_ROW_THREE_ERASURE_PASS exact_small_orders=3 direct_masks=',count,
      'orders=7..39')
