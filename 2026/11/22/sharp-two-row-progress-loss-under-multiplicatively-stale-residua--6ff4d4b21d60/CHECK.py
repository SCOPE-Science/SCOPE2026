"""Exact-arithmetic and numerical regression checks for the two-row selection-only theorem.

Requires Python >=3.9 and the Python standard library only.
"""
from fractions import Fraction as F
from math import exp, log, isclose
from random import Random

ncheck = 0

def check(cond, msg):
    global ncheck
    ncheck += 1
    if not cond:
        raise AssertionError(msg)


def ratio_closed(z,p,rho):
    U = rho ** (2*p)
    return (1+U*z**(p+2))*(1+z**p)/((1+U*z**p)*(1+z**(p+2)))


def residual_norm2(e):
    return e[0]*e[0]+e[1]*e[1]


def expected_drop(z,p,rho,beta,stale):
    # Rows a1=(1,0), a2=(3/5,4/5), true residuals (1,z).
    e=(F(-1), (F(3)-F(5)*z)/F(4))
    rows=((F(1),F(0)),(F(3,5),F(4,5)))
    residual=(F(1),z)
    weights=((F(1),z**p) if not stale else ((F(1)/rho)**p,(rho*z)**p))
    total=sum(weights)
    drop=F(0)
    for i in (0,1):
        nxt=(e[0]+beta*residual[i]*rows[i][0],e[1]+beta*residual[i]*rows[i][1])
        drop+=(weights[i]/total)*(residual_norm2(e)-residual_norm2(nxt))
    return drop

for p in (1,2,3,4,6,8):
    for rho in (F(5,4),F(3,2),F(2)):
        for z in [F(j,21) for j in range(1,22)]:
            for beta in (F(1,3),F(1),F(7,4)):
                ideal=expected_drop(z,p,rho,beta,False)
                stale=expected_drop(z,p,rho,beta,True)
                check(ideal>0,('ideal',p,z,beta))
                check(stale/ideal==ratio_closed(z,p,rho),('identity',p,z,beta))
                check(0<stale/ideal<=1,('loss',p,z,beta))

# For arbitrary stale multipliers in [rho^-1,rho], the extremal pairing is worst.
for p in (1,2,4):
    for rho in (F(5,4),F(2)):
        for z in (F(1,9),F(1,3),F(2,3),F(1)):
            for d1 in (1/rho,F(1),rho):
                for d2 in (1/rho,F(1),rho):
                    st1=(d1)**p; st2=(d2*z)**p
                    current=z**p
                    ideal=(F(1)+z*z*current)/(F(1)+current)
                    used=(st1+st2*z*z)/(st1+st2)
                    ratio=used/ideal
                    check(ratio>=ratio_closed(z,p,rho),('worst perturbation',p,z))

# Root is unique because the logarithmic derivative is strictly decreasing.
def Fprime(z,p,U):
    return p/(1+U*z**p)-2*z*z/(1-z*z)-(p+2)*z**(p+2)/(1+z**(p+2))

def bisect(p,epsilon):
    U=exp(2*p*epsilon)
    lo,hi=0.0,1.0
    for j in range(95):
        mid=(lo+hi)/2
        if Fprime(mid,p,U)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

for p in (0.5,1,2,4,8,16,32,64,100):
    for epsilon in (.05,.2,log(1.5),1):
        z=bisect(p,epsilon)
        U=exp(2*p*epsilon)
        check(0<z<1,('root',p,epsilon))
        check(abs(Fprime(z,p,U))<1e-8,('stationarity',p,epsilon))
        L=(U-1)*z**p*(1-z*z)/((1+U*z**p)*(1+z**(p+2)))
        for j in range(1,401):
            v=j/401
            Lv=(U-1)*v**p*(1-v*v)/((1+U*v**p)*(1+v**(p+2)))
            check(L>=Lv-1e-12,('global minimizer',p,epsilon,v))

# The high-power limit holds and does not require a numerical limit for proof.
eps=log(1.5)
nums=[]
for p in (4,8,16,32,64,128,256):
    z=bisect(p,eps)
    nums.append(ratio_closed(z,p,1.5))
for a,b in zip(nums[:-1],nums[1:]):
    check(a>b,('high p sampled ordering',a,b))
check(abs(nums[-1]-16/81)<0.035,('asymptotic sample',nums[-1]))
check(ratio_closed(F(1),3,F(3,2))==1, 'equal residuals')
print('PASS:',ncheck,'assertions; exact rational first-step identities and exploratory numerical root/limit checks')
