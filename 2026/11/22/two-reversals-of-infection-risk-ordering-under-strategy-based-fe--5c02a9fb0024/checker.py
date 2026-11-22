"""Standalone exact and numerical checks for a vaccination Fermi drift counterexample."""
from fractions import Fraction as F
from math import exp

X=F(1,20); E=F(1,20); C=F(1,20); P=F(2,3)
LAM=1-E; QLO=F(3,20); QHI=F(3,5); KSTAR=F(1,40)

def payoffs(q):
    return -C*X-LAM*P*X*q, -(1-X)*q

def logistic(v):
    z=float(v)
    return 1/(1+exp(-z)) if z>=0 else exp(z)/(1+exp(z))

def G(q,k):
    v,n=payoffs(q)
    return (1-float(q))*logistic(v/k)+float(q)*logistic((v+1)/k) - (1-float(LAM*q))*logistic((n+C)/k) - float(LAM*q)*logistic((n+C+P)/k)

def taylor_exp(z,n):
    acc=F(1); term=F(1)
    for j in range(1,n+1):
        term*=z/j
        acc+=term
    return acc

assert payoffs(QLO)==(F(-29,4000),F(-57,400))
assert payoffs(QHI)==(F(-43,2000),F(-57,100))
# Strict logistic bounds via elementary rational bounds on e^z.
assert F(1,1)/(1-F(29,100))<F(3,2) # e^.29 < 1/(1-.29)
assert taylor_exp(F(5),6)>99
assert taylor_exp(F(37,10),7)>39
assert taylor_exp(F(43,50),2)>2
assert F(88,15)>5
lo=F(17,20)*F(2,5)+F(3,20)*F(99,100)-F(343,400)*F(1,40)-F(57,400)
hi=F(2,5)*F(1,3)+F(3,5)-F(57,100)*F(99,100)
assert lo==F(5193,16000) and hi==F(5071,30000)
assert lo-hi==F(37327,240000)>0
# Risk-benefit derivative, exact limiting differences.
assert 1-LAM*P==F(11,30)
assert (1-LAM*P)*QLO-C==F(1,200)
assert (1-LAM*P)*QHI-C==F(17,100)
assert E*(QLO-QHI)==F(-9,400)
slope=2-X-LAM*P*(1+X)
assert slope==F(257,200)
assert (QLO-QHI)*slope==F(-2313,4000)
# All logistic signs for zero-noise limit.
for q in [QLO,QHI]:
    v,n=payoffs(q)
    assert v<0 and v+1>0 and n+C<0 and n+C+P>0
# Numerical cross checks (not used for the infinite proof).
for k in [1e-4,1e-3,1/40,0.1,1,10,100]:
    d=G(QLO,k)-G(QHI,k)
    print('k=',k,'G_low=',G(QLO,k),'G_high=',G(QHI,k),'D=',d)
assert G(QLO,KSTAR)-G(QHI,KSTAR)>float(lo-hi)
assert G(QLO,F(1,10000))-G(QHI,F(1,10000))<0
assert G(QLO,F(100))-G(QHI,F(100))<0
print('PASS: exact rational bounds, exact limit coefficients, endpoint signs, numerical corroboration')
