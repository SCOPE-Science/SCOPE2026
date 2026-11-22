"""Exact rational verification of a continuous two-heatwave sliding-window theorem.

No finite test is used as a proof of the all-parameter statement.
"""
from fractions import Fraction as F
from itertools import product

def overlap(a,b,c,d):
    return max(F(0), min(b,d)-max(a,c))

def heat(t,W,d,g):
    return overlap(F(0),d,t-W,t)+overlap(d+g,2*d+g,t-W,t)

def exact_level_intervals(W,d,g,q):
    knots=sorted({F(0),d,d+g,2*d+g,W,W+d,W+d+g,W+2*d+g})
    intervals=[]
    for a,b in zip(knots,knots[1:]):
        x,y=heat(a,W,d,g)-q,heat(b,W,d,g)-q
        if x>=0 and y>=0:
            intervals.append((a,b))
        elif x<0 and y<0:
            continue
        elif x<0 and y>=0:
            cut=a+(b-a)*(-x)/(y-x)
            intervals.append((cut,b))
        elif x>=0 and y<0:
            cut=a+(b-a)*x/(x-y)
            intervals.append((a,cut))
    # discard isolated equality points; only positive-duration intervals count.
    intervals=[(a,b) for a,b in intervals if b>a]
    merged=[]
    for a,b in intervals:
        if merged and a<=merged[-1][1]:
            merged[-1]=(merged[-1][0],max(merged[-1][1],b))
        else:
            merged.append((a,b))
    return merged

def prediction(W,d,g,q):
    critical=W-q
    if q<=d:
        if g<=critical:
            return W+2*d+g-2*q,1
        return 2*(W+d-2*q),2
    if g<=critical:
        return W+2*d-g-2*q,1
    return F(0),0

def run():
    cases=0
    for d0,W0,g0,qnum in product(range(1,8),range(2,12),range(0,26),range(1,19)):
        d=F(d0,2);W=F(W0,2)
        if W<2*d:continue
        g=F(g0,2);q=F(qnum,4)
        if q>=2*d:continue
        intervals=exact_level_intervals(W,d,g,q)
        actual=(sum((b-a for a,b in intervals), F(0)),len(intervals))
        expected=prediction(W,d,g,q)
        assert actual==expected, (d,W,g,q,actual,expected,intervals)
        cases+=1
    # Explicit threshold equalities in a realistic 12-week window.
    for d,W,q in ((F(3),F(12),F(2)),(F(3),F(12),F(4)),(F(3),F(12),F(3))):
        g=W-q
        actual=exact_level_intervals(W,d,g,q)
        assert (sum((b-a for a,b in actual),F(0)),len(actual))==prediction(W,d,g,q)
        cases+=1
    print('PASS:',cases,'exact-rational analytical-scope diagnostic cases')
    print('4-degree-week normalized example: W=12,d=3,q=2,g*=10; duration=24 at threshold and 22 beyond')
    print('8-degree-week normalized example: W=12,d=3,q=4,g*=8; duration=2 at threshold and 0 beyond')

if __name__=='__main__':run()
