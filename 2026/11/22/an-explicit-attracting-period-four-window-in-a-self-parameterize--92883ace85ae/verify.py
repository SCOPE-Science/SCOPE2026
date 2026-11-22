"""Exact rational cycle-box verification for the specified cubic interval map.
Run: python verify.py. No external packages.
"""
from fractions import Fraction as Q

q=lambda s: Q(s)
C0,C1=q('0.9978'),q('0.9982')
I=[(q(a),q(b)) for a,b in [
    ('0.03935','0.03955'),
    ('0.14898','0.14975'),
    ('0.50023','0.50244'),
    ('0.989975','0.989991'),
]]

def f(x,c):
    return (q('3.9')+(x+c)/25)*x*(1-x)

def fp(x,c):
    a=q('3.9')+c/25
    return a*(1-2*x)+(2*x-3*x*x)/25

# Regions 0,1 strictly increasing, region 3 strictly decreasing
# for every parameter, so extrema occur at interval and parameter endpoints.
for j in (0,1,3):
    xlo,xhi=I[j]
    if j in (0,1):
        lo,hi=f(xlo,C0),f(xhi,C1)
    else:
        lo,hi=f(xhi,C0),f(xlo,C1)
    ylo,yhi=I[(j+1)%4]
    assert ylo<lo<=hi<yhi, (j,lo,hi,ylo,yhi)
    print('I',j,'image rational bounds',float(lo),float(hi),'margins',float(lo-ylo),float(yhi-hi))

# Region 2 meets the cubic map's critical point. Set t=x-1/2;
# f_C(x)=B(1/4-t^2)+t/100-t^3/25, B=98/25+C/25.
# Since t>0, min is at an endpoint (strict concavity), whereas
# the elementary completion of a square gives the certified upper bound.
t0,t1=[x-Q(1,2) for x in I[2]]
B0=q('3.92')+C0/25
B1=q('3.92')+C1/25
lo=min(B0*(Q(1,4)-t*t)+t/100-t*t*t/25 for t in [t0,t1])
hi=B1/4+1/(40000*B1)
assert I[3][0]<lo<hi<I[3][1], (lo,hi,I[3])
print('I 2 image certified rational bounds',float(lo),float(hi),'margins',float(lo-I[3][0]),float(I[3][1]-hi))

# Across [0,1] and C in [C0,C1], 3.9+C/25<3.94,
# and (2x-3x^2)/25 is in [-1/25,1/75]. Thus |f'|<4.
# On I2, t in [t0,t1] and f'=1/100-2Bt-3t^2/25;
# monotone decreasing in both B,t. Assert absolute derivative<1/100.
dmax=q('0.01')-2*B0*t0-3*t0*t0/25
dmin=q('0.01')-2*B1*t1-3*t1*t1/25
assert -q('0.01')<dmin<=dmax<q('0.01'),(dmin,dmax)
assert Q(4)**3*Q(1,100)<1
print('Critical-stage derivative bounds',float(dmin),float(dmax))
print('Return Lipschitz bound',float(Q(4)**3/100))
# Independent exact-rational algebraic tests from explicit rationals.
for c in (C0, (C0+C1)/2, C1):
    x=sum(I[0])/2
    ys=[]
    for _ in range(4):
        ys.append(x)
        x=f(x,c)
    assert I[0][0]<x<I[0][1]
    assert all(a<xx<b for xx,(a,b) in zip(ys,I))
    d=Q(1)
    for xx in ys:d*=fp(xx,c)
    assert abs(d)<Q(16,25)
    print('c',float(c),'4-stage check (approx)',[float(v) for v in ys],'slope',float(d))
print('PASS: all inequalities exact in rational arithmetic; a primitive attracting 4-cycle for EVERY c in [0.9978,0.9982].')
