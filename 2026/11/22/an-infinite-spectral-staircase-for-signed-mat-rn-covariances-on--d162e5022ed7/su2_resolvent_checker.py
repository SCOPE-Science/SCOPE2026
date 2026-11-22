"""Exact-rational supplementary checks for a signed SU(2) resolvent.
The unrestricted theorem requires the analytic argument in RESULT.md.
Run: python su2_resolvent_checker.py
"""
from fractions import Fraction as F


def a(y, q):
    return F(0) if y == 0 else F(y, 1) / (F(y*y, 1) + q)**2


def R(y, q):
    return (a(y - 1, q) + a(y + 1, q)) / a(y, q)


def tc(y):
    m = y*(y-1)*(y+1)*(y+2)
    return [
        -m*(6*y**8+24*y**7+30*y**6+6*y**5-21*y**4-24*y**3+y*y+10*y+4),
        -2*m*(6*y**6+18*y**5+12*y**4-6*y**3+18*y*y+24*y+13),
        30*y**8+120*y**7+256*y**6+348*y**5+354*y**4+268*y**3+242*y*y+146*y+1,
        6*(20*y**6+60*y**5+92*y**4+84*y**3+70*y*y+38*y+1),
        3*(50*y**4+100*y**3+120*y*y+70*y+21),
        4*(21*y*y+21*y+19),
        18,
    ]


def T(y, q):
    return sum(c*q**i for i,c in enumerate(tc(y)))


def denominator(y, q):
    return ((q+y*y)**2*(q+(y-1)**2)**2
            *(q+(y+1)**2)**2*(q+(y+2)**2)**2)


def check():
    tests = 0
    for y in range(2, 65):
        cs=tc(y)
        assert cs[0]<0 and cs[1]<0 and all(c>0 for c in cs[2:]);tests+=1
        for q in [F(0),F(1,10),F(1),F(7,3),F(10),F(67)]:
            lhs=R(y+1,q)-R(y,q)
            rhs=F(2*(2*y+1))*T(y,q)/denominator(y,q)
            assert lhs==rhs, (y,q,lhs,rhs)
            tests+=1
    for ell in range(0,50):
        for la in [F(1,10),F(1,2),F(1),F(3),F(10),F(200)]:
            q=la-1
            y=ell+1
            for b in [F(-1,7),F(0),F(1,3)]:
                coeff=a(y,q)+b*(a(y-1,q)+a(y+1,q))
                assert coeff==a(y,q)*(1+b*R(y,q));tests+=1
    for q in [F(-9,10),F(-1,2),F(0),F(1,10),F(1),F(5),F(25),F(100),F(1000)]:
        vals=[R(y,q) for y in range(1,250)]
        idx=max(range(len(vals)),key=lambda z:vals[z])+1
        assert idx>=2 and vals[idx-1]>2
        if q<=0: assert idx==2
        assert all(vals[k]<=vals[k+1] for k in range(idx-1))
        assert all(vals[k]>=vals[k+1] for k in range(idx-1,len(vals)-1))
        tests+=1
    bounds=[(2,F(1380,1000),F(1381,1000)),
            (3,F(3371,1000),F(3372,1000)),
            (4,F(6034,1000),F(6035,1000)),
            (5,F(9365,1000),F(9366,1000))]
    for y,lo,hi in bounds:
        assert T(y,lo)<0<T(y,hi); tests+=1
    for la in [F(1,10),F(1),F(2),F(5),F(12),F(100)]:
        q=la-1
        rs=[R(y,q) for y in range(1,400)]
        maxr=max(rs)
        critical=-1/maxr
        for y in range(1,400):
            assert a(y,q)+critical*(a(y-1,q)+a(y+1,q))>=0
            tests+=1
        assert critical>F(-1,2)
    print(f'PASS {tests} exact rational checks; analytic proof covers all parameters')

if __name__=='__main__': check()
