"""Exact rational replay of the two-parallel-roof two-pulse runoff example.

The piecewise identities follow by elementary branch analysis, not from the grid checks.
"""
from fractions import Fraction as F

A, B = F(1,2), F(1,4)
C1, Q1 = F(1,2), F(1,5)
C2, Q2 = F(2), F(9,10)
W1, W2 = F(1), F(10)
BREAKS = [F(0), F(85,108), F(65,81), F(5,6), F(35,36), F(1)]
ZEROS = [F(5,8), F(635,806), F(45,47)]

def positive(x): return x if x > 0 else F(0)
def runoff(c,q,s,x,y):
    incoming = q*c*s+x
    out1 = positive(incoming-c)
    after1 = min(c,incoming)
    out2 = positive(q*after1+y-c)
    return out1+out2

def delta(c,q,s):
    return runoff(c,q,s,A,B)-runoff(c,q,s,B,A)

def d2_piece(s):
    if s <= BREAKS[1]: return F(0)
    if s <= BREAKS[2]: return F(51,40)-F(81,50)*s
    if s <= BREAKS[3]: return -F(1,40)
    if s <= BREAKS[4]: return F(9,50)*s-F(7,40)
    return F(0)

def total_piece(s):
    return F(2,25)*s-F(1,20)+10*d2_piece(s)

def actual(s): return W1*delta(C1,Q1,s)+W2*delta(C2,Q2,s)

def main():
    for s in sorted(set(BREAKS+ZEROS+[F(i,2000) for i in range(2001)])):
        assert F(0)<=s<=F(1)
        assert delta(C1,Q1,s)==F(2,25)*s-F(1,20),s
        assert delta(C2,Q2,s)==d2_piece(s),s
        assert actual(s)==total_piece(s),s
    # Strict signs and exactly three roots, not merely at sampled points:
    assert F(0)<ZEROS[0]<BREAKS[1]<ZEROS[1]<BREAKS[2]<BREAKS[3]<ZEROS[2]<BREAKS[4]<F(1)
    for z in ZEROS: assert total_piece(z)==0
    for s,sign in [(F(0),-1),(F(3,4),1),(F(7,8),-1),(F(1),1)]:
        assert sign*actual(s)>0,(s,actual(s))
    # The five subinterval formulas are affine and agree at both endpoints.
    # Thus the algebraic branch analysis certifies absence of other roots.
    print('PASS: 2,001 rational-grid states, all exact breakpoints, all three roots, and four alternating sign witnesses.')
    for z in ZEROS: print('root',z)
    for s in [F(0),F(3,4),F(7,8),F(1)]: print('witness',s,actual(s))
if __name__=='__main__': main()
