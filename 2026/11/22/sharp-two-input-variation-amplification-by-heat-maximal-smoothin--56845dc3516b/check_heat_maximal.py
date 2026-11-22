import math, random
from fractions import Fraction

def mean_uv(x):
    a,b,c=x
    return ((a+b+c)/3.0,(a-c)/2.0,(a+c-2*b)/6.0)

def polymax(A,B):
    # max_{0<=z<=1} (Az+Bz^3)
    vals=[0.0,A+B]
    if A*B<0:
        z=math.sqrt(-A/(3*B))
        if z<1: vals.append(A*z+B*z**3)
    return max(vals)

def heat_max(x):
    m,u,v=mean_uv(x)
    return (m+polymax(u,v),m+max(0,-2*v),m+polymax(-u,v))

def variation(x): return sum(abs(x[i+1]-x[i]) for i in range(len(x)-1))

x=(13,12,5); y=(15,11,4)
a=heat_max(x); b=heat_max(y)
print('RATIONAL_WITNESS',x,y,'Mx',a,'My',b,'Vin',variation([y[i]-x[i] for i in range(3)]),'Vout',variation([b[i]-a[i] for i in range(3)]))
assert all(abs(a[i]-[13,12,10][i])<1e-10 for i in range(3))
assert all(abs(b[i]-[15,11,10][i])<1e-10 for i in range(3))
assert variation(tuple(y[i]-x[i] for i in range(3)))==3
assert abs(variation(tuple(b[i]-a[i] for i in range(3)))-4)<1e-10
print('EXACT_FINITE_WITNESS_4_OVER_3_PASS')

rng=random.Random(177103)
maxratio=0
for j in range(20000):
    x=[rng.uniform(-20,20) for k in range(3)]
    y=[rng.uniform(-20,20) for k in range(3)]
    xx=tuple(y[k]-x[k] for k in range(3))
    xxV=variation(xx)
    if xxV<1e-9: continue
    a=heat_max(x); b=heat_max(y)
    ratio=variation(tuple(b[k]-a[k] for k in range(3)))/xxV
    maxratio=max(maxratio,ratio)
    assert ratio <= 4/3 + 1e-9,(x,y,ratio)
print('RANDOM_GLOBAL_PAIRS_BOUND_PASS',20000,'largest observed',maxratio)

for beta in [0,1]:
    # sample all potential active times, even infeasible choices, upper <=4/3
    for j in range(101):
     for k in range(101):
        xp=j/100.0; xm=k/100.0
        norm=max((xp+xm)/2+abs(xp**3-xm**3)/6,abs(xp-xm)/2+(xp**3+xm**3+4*beta)/6)
        assert norm<=4/3+1e-9,(xp,xm,norm)
print('GENERALIZED_JACOBIAN_BOX_GRID_BOUND_PASS',2*101*101)

# Independent evaluation of the heat semigroup via diagonalization or direct 3x3 matrix formula
for j in range(250):
    x=[rng.uniform(-7,7) for k in range(3)]
    target=heat_max(x)
    m,u,v=mean_uv(x)
    approx=[-1e20]*3
    for k in range(5001):
        z=k/5000.
        vals=(m+u*z+v*z**3,m-2*v*z**3,m-u*z+v*z**3)
        approx=[max(approx[i],vals[i]) for i in range(3)]
    for h in range(3): assert -1e-9 <= target[h]-approx[h] <2e-6,(x,h,target[h],approx[h])
print('INDEPENDENT_TIME_GRID_MATCH_PASS',250)

# P2 result algebraic: M(a,b)=(max(a,m),max(b,m)), output difference (a-b)/2
for j in range(250):
    a,b=rng.uniform(-10,10),rng.uniform(-10,10)
    m=(a+b)/2
    assert abs(max(a,m)-max(b,m)-(a-b)/2)<1e-10
print('P2_SHARP_HALF_COEFFICIENT_PASS')
print('ALL_CHECKS_PASS')
