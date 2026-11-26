"""Exact integer checks for finite-copy passivity of a three-level oscillator.

The finite cases below are independent arithmetic tests of the analytic theorem.
They do not certify the universal quantifier over copy number or populations.
"""
from itertools import combinations_with_replacement


def count_states(n, a, b, c):
    # Weight is unnormalized; the common partition denominator cancels.
    return [(i + 2*j, a**(n-i-j)*b**i*c**j, (n-i-j,i,j))
            for i in range(n+1) for j in range(n-i+1)]


def exhaustively_passive(n, a, b, c):
    rows=count_states(n,a,b,c)
    return all(not(Ea>Eb and pa>pb)
               for Ea,pa,_ in rows for Eb,pb,_ in rows)


def exact_criterion(n,a,b,c):
    r=n if n%2 else n-1
    k=(r+1)//2
    return a**(k-1)*c**k<=b**r<=a**k*c**(k-1)


def run():
    examples=[(16,2,1),(8,2,1),(32,4,1),(128,16,1),
              (4,4,1),(4,1,1),(256,16,1),(9,3,1),
              (15,6,2),(30,12,7)]
    comparisons=0
    for a,b,c in examples:
        assert a>=b>=c>0
        for n in range(1,12):
            actual=exhaustively_passive(n,a,b,c)
            expected=exact_criterion(n,a,b,c)
            assert actual==expected,(n,a,b,c,actual,expected)
            comparisons+=1
    # Entire bounded family of integer populations, not just chosen examples.
    for a in range(1,10):
      for b in range(1,a+1):
       for c in range(1,b+1):
        for n in range(1,9):
          assert exhaustively_passive(n,a,b,c)==exact_criterion(n,a,b,c),(a,b,c,n)
          comparisons+=1
    # First activation at 3, 5, 7, 9 for exact adjacent log-ratio powers.
    for (a,b,c),first in [((16,2,1),3),((8,2,1),5),
                            ((32,4,1),7),((128,16,1),9)]:
      assert all(exact_criterion(n,a,b,c) for n in range(1,first))
      assert not exact_criterion(first,a,b,c)
    # At five copies, one explicit energy-gap-one population inversion.
    a,b,c=8,2,1
    low=b**5
    high=a**2*c**3
    assert high==64 and low==32 and high>low
    assert exhaustively_passive(4,a,b,c)
    assert not exhaustively_passive(5,a,b,c)
    print(f'VERIFY_OK exact_count_vector_cases={comparisons} activation_onsets=3,5,7,9 witness_5=(64,32)')


if __name__=='__main__':
    run()
