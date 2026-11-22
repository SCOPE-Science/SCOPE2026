"""Exact supplementary checks for two-pulse saturation-excess runoff."""
from fractions import Fraction as F

def runoff(C, s, first, second, q):
    overflow1 = max(F(0), s + first - C)
    post1 = min(C, s + first)
    overflow2 = max(F(0), q * post1 + second - C)
    return overflow1 + overflow2

def difference(C, s, A, B, q):
    return runoff(C,s,A,B,q)-runoff(C,s,B,A,q)

def test():
    checks=0
    for C in (F(1), F(3,2), F(5,3)):
      for is_ in range(1,10):
        s = C*F(is_,10)
        for ia in range(1,15):
          A=C*F(ia,10)
          for ib in range(1,ia):
            B=C*F(ib,10)
            for iq in range(1,20):
              q=F(iq,20)
              d=difference(C,s,A,B,q)
              formula = max(F(0),s+A-C)-max(F(0),s+B-C)+max(F(0),q*min(C,s+A)+B-C)-max(F(0),q*min(C,s+B)+A-C)
              assert d == formula
              if s+A<=C: assert d<=0
              elif s+B>=C: assert d>=0
              else:
                qstar=s/(s+B)
                assert (d>0) == (q<qstar)
                assert (d==0) == (q==qstar)
                assert (d<0) == (q>qstar)
              checks+=1
    C,s,A,B=F(1),F(4,5),F(2,5),F(1,10)
    assert s+B<C<s+A
    assert s/(s+B)==F(8,9)
    assert difference(C,s,A,B,F(1,2))==F(1,5)
    assert difference(C,s,A,B,F(9,10))==-F(1,100)
    assert difference(C,s,A,B,F(8,9))==0
    # The crossover is unchanged as the larger storm changes while straddling persists.
    for A in (F(1,4),F(2,5),F(7,10),F(3)):
        assert s+B<C<s+A
        assert difference(C,s,A,B,F(8,9))==0
    print(f'PASS {checks} exact rational parameter checks, boundary and amplitude-independence cases')
if __name__=='__main__': test()
