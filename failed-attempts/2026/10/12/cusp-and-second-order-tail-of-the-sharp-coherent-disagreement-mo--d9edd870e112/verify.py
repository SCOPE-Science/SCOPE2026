from fractions import Fraction as Q
import math

def mul(a,b,n):
    out=[Q(0) for _ in range(n+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=n: out[i+j]+=x*y
    return out

def inv(a,n):
    assert a[0] != 0
    out=[Q(0) for _ in range(n+1)]
    out[0]=1/a[0]
    for k in range(1,n+1):
        out[k]=-sum(a[j]*out[k-j] for j in range(1,min(k,len(a)-1)+1))/a[0]
    return out

def log_series(a,n):
    assert a[0]==1
    der=[Q(k)*a[k] for k in range(1,min(len(a),n+2))]
    quot=mul(der,inv(a,n),n-1)
    out=[Q(0)]
    for k in range(1,n+1):
        out.append(quot[k-1]/Q(k))
    return out

def exp_series(h,n):
    assert h[0]==0
    y=[Q(0) for _ in range(n+1)]; y[0]=1
    for m in range(1,n+1):
        y[m]=sum(Q(k)*h[k]*y[m-k] for k in range(1,m+1))/Q(m)
    return y

# sqrt(1+6t+t^2), checked by exact squaring through t^5.
S=[Q(1),Q(3),Q(-4),Q(12),Q(-44),Q(180)]
sq=mul(S,S,5)
assert sq == [Q(1),Q(6),Q(1),Q(0),Q(0),Q(0)]

# d=(3+t-S)/2 and b=a/t=(1+3t-S)/(4t).
d=[Q(1),Q(-1),Q(2),Q(-6),Q(22),Q(-90)]
b=[Q(1),Q(-3),Q(11),Q(-45)]
ld=log_series(d,4)
lb=log_series(b,3)
assert ld[:5] == [Q(0),Q(-1),Q(3,2),Q(-13,3),Q(63,4)]
assert lb[:4] == [Q(0),Q(-3),Q(13,2),Q(-21)]

# log(M/(2t/e)) = log(a/t)+(log d)/t+1.
h=[Q(0)]*4
for n in range(1,4):
    h[n]=lb[n]+ld[n+1]
assert h == [Q(0),Q(-3,2),Q(13,6),Q(-21,4)]
r=exp_series(h,3)
assert r == [Q(1),Q(-3,2),Q(79,24),Q(-145,16)]

# Numerical corroboration of the crossover and cusp.
def pars(alpha):
    s=math.sqrt(alpha*alpha+6*alpha+1)
    a=(alpha+3-s)/4
    d=(3*alpha+1-s)/(2*alpha)
    return a,d

def logratio(alpha):
    a,d=pars(alpha)
    return math.log(2*a)+alpha*math.log(d)+alpha*math.log(2)
lo,hi=2.25750786,2.25750787
assert logratio(lo)<0<logratio(hi)
for _ in range(80):
    mid=(lo+hi)/2
    if logratio(mid)<0: lo=mid
    else: hi=mid
alpha0=(lo+hi)/2
a0,d0=pars(alpha0)
jump=math.log(2*d0)
assert abs(alpha0-2.257507868922394)<2e-14
assert abs(d0-0.7399006186181092)<2e-14
assert abs(jump-0.3919077795923660)<2e-14
assert jump>0
print('VERIFY_OK')
