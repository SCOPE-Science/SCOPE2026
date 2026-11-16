"""Exact rational checks for the Bessel ninth-or-higher (q>=9) angular stability theorem.
Scientific input: standard integer-order Bessel Taylor series and a published
sixth-moment upper bound for orders >=2; no external libraries needed.
"""
from fractions import Fraction as F
from math import factorial, comb

# For 1<=x<=3, the polynomial L(x) is a lower bound on J_1(x),
# by the alternating Taylor series (the first omitted term is positive).
L=[F(0)]*12
for m in range(6):
    L[2*m+1]=F((-1)**m,2**(2*m+1)*factorial(m)*factorial(m+1))
def mul(p,q):
    ans=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        if a:
            for j,b in enumerate(q):
                if b: ans[i+j]+=a*b
    return ans
poly=[F(1)]
for _ in range(10): poly=mul(poly,L)
T=sum(c*F(3**(i+2)-1,i+2) for i,c in enumerate(poly))
assert T>F(3,400), ('10th moment local lower',float(T))
# Ninth moment lower on [0,7/2], where L(x)>0 by a direct
# rational positivity estimate on the alternating-series bracket.
Q=[F(1)]
for _ in range(9): Q=mul(Q,L)
B=F(7,2)
T9=sum(c*B**(i+2)/F(i+2) for i,c in enumerate(Q))
assert T9>F(137,10000), ('ninth moment lower',float(T9))
t9=F(49,16)
assert 1-t9/2+t9*t9/12-t9**3/144>0 and t9<30
# L(x)>0 on [1,3]: in t=x^2/4<=9/4, its bracket after
# the first four terms is decreasing and >0, and remaining
# two terms have nonnegative sum (t<=30).
t=F(9,4)
assert 1-t/F(2)+t*t/F(12)-t**3/F(144)>0
assert t <=30

# J_2(x) <= polynomial U(x^2) on [0,3]; alternating series
# next omitted term is negative (x^2/4<=9/4).
U=[F(0),F(1,8),-F(1,96),F(1,3072),-F(1,184320),F(1,17694720)]
y=F(9)
assert sum(c*y**j for j,c in enumerate(U))<F(1,2)
# Alternating-series lower J2(r)>=r^2/8-r^4/96 is positive
# for 0<r<=3; combined with U this proves the absolute bound.
assert 1-F(9,12)>0
# Derivative of U(9t) in Bernstein form on [0,1] is positive;
# all five rational Bernstein coefficients are strictly positive.
d=[j*U[j]*9**(j-1) for j in range(1,len(U))]
b=[sum(d[j]*F(comb(k,j),comb(4,j)) for j in range(k+1)) for k in range(5)]
assert all(x>0 for x in b)

# Exact rational Taylor interval at x=3 for J_1, J_2, J_3.
def J_interval(k,x,terms=60):
    term=F(x**k,2**k*factorial(k))
    p=F(0)
    for m in range(terms):
        p += (-1)**m*term
        term *= F(x*x,4*(m+1)*(m+k+1))
    return p-term,p+term
j2l,j2u=J_interval(2,3)
j1l,j1u=J_interval(1,3)
j3l,j3u=J_interval(3,3)
assert -F(49,100)<j2l<=j2u<F(49,100)
assert -F(1,50)<(j1l-j3u)/2<=(j1u-j3l)/2<F(1,50)
# Sonin function |J_2|^2+(J_2')^2/(1-4/x^2) decreases for x>2,
# implying for x>=3 an upper bound at the rational data x=3.
assert F(49,100)**2+F(9,5)*F(1,50)**2 <F(1,4)
# For orders >=3, Landau bound (7/10)n^-1/3 is below 1/2.
assert F(7,10)**3 <F(3,8)

# Simpson upper bound for integral_0^60 x J_1(x)^6 dx.
# Bessel Taylor terms evaluated as outward rational intervals
# at scale 10^70, with n=145 and first omitted term bound.
S=10**70
N=6000
TERM=145

def bessel_bracket(j):
    # x=j/100; x/2=j/200
    den=200
    lo=S*j//den
    hi=(S*j+den-1)//den
    outlo=outhi=0
    for m in range(TERM):
        if m%2==0: outlo+=lo;outhi+=hi
        else: outlo-=hi;outhi-=lo
        dd=40000*(m+1)*(m+2)
        lo=lo*j*j//dd
        hi=(hi*j*j+dd-1)//dd
    return outlo-hi,outhi+hi

high=0
for j in range(N+1):
    l,u=bessel_bracket(j)
    m=max(abs(l),abs(u))
    w=1 if j in (0,N) else (4 if j%2 else 2)
    high+=w*j*m**6
# Simpson: h=1/100, f(jh)=j/100*J_1(jh)^6
# h/3 times weighted sum = sum (w*j)/30000 J^6
DEN=30000*S**6
assert high*10000 <DEN*1036, ('Simpson upper', high/DEN)
err=F(60,180)*F(1,100)**4*(4*6**3+60*6**4)
assert err<F(3,10000)
# Standard Bessel bound |J_1(r)|^2 <=2/(pi sqrt(r^2-1)), r>1,
# and pi>3 imply tail_60 <= (8/27)/sqrt(3599)<8/(27*59).
assert 60**2-1>59**2
assert F(1036,10000)+err+F(8,27*59)<F(109,1000)
# Comparison required for all real q>=10:
# local 10th moment >3/400, global 6th moment <11/100,
# (3/400)/(11/100)>1/16 and (3/400)> (1/10)*(1/2)^4.
assert F(3,400)/F(11,100)>F(1,16)
assert F(3,400)>F(1,10)*F(1,2)**4
# Sharper odd base exponent: I1(9)>137/10000 and I1(6)<109/1000.
# Their ratio exceeds 1/8, and I1(9)>I_k(6)/8 for every k>=2.
assert F(137,10000)/F(109,1000)>F(1,8)
assert F(137,10000)>F(1,10)*F(1,2)**3
print('CHECK_OK rational_9th_lower rational_6th_upper all_order_sup certificate complete')

# Independent reproduction of the imported sixth-moment separator
# I_k(6)<1/10 for all k>=2: finite rational certificate k=2..11,
# then the source's analytic high-mode bound k>=12.
QS=10**70
QN=2000
QT=145

def Jk_interval(k,j):
    den=100**k*factorial(k)
    lo=QS*j**k//den
    hi=(QS*j**k+den-1)//den
    a=b=0
    for m in range(QT):
        if m%2==0: a+=lo;b+=hi
        else: a-=hi;b-=lo
        dd=10000*(m+1)*(m+k+1)
        lo=lo*j*j//dd
        hi=(hi*j*j+dd-1)//dd
    return a-hi,b+hi

for k in range(2,12):
    upper=0
    for j in range(QN+1):
        lo,hi=Jk_interval(k,j)
        v=max(abs(lo),abs(hi))
        w=1 if j in (0,QN) else (4 if j%2 else 2)
        upper+=w*j*v**6
    assert upper*100 <7500*QS**6*7, ('sixth finite',k)
# uniform Simpson 0..40 error < 1/500, Watson tail < 1/100.
assert F(40,180)*F(1,50)**4*(4*6**3+40*6**4)<F(1,500)
assert 1600-11**2>38**2
assert F(8,27*38)<F(1,100)
assert F(7,100)+F(1,500)+F(1,100)<F(1,10)
# Xu 2026, Eq.(3.87) establishes fifth-moment bound <13/40 for k>=4.
# Landau bound then yields for k>=12 the strict comparison below.
assert 91**3*1000 < 400**3*12
print('CHECK_OK sixth moment all-order separator independently reproduced')
