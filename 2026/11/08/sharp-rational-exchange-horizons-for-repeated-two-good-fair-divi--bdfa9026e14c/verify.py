"""Exact finite corroboration of two-good repeated-allocation horizon theorem.

Plain Python 3, no external packages. All arithmetic is integer/exact.
"""
from math import comb
from fractions import Fraction
from itertools import product


def direct_ef1_one_round(a,b,c,d,choice):
    # choice=(owner of A,owner of B), indexed 0,1
    for i in (0,1):
        own=[j for j in (0,1) if choice[j]==i]
        other=[j for j in (0,1) if choice[j]!=i]
        val=(a,b) if i==0 else (c,d)
        uown=sum(val[j] for j in own)
        uother=sum(val[j] for j in other)
        if uown>=uother: continue
        if not any(uown-(val[j] if j in own else 0)>=uother-(val[j] if j in other else 0) for j in (0,1)):
            return False
    return True


def direct_pareto(a,b,c,d,k,x,y):
    base1=a*x+b*y
    base2=c*(k-x)+d*(k-y)
    for xx in range(k+1):
        for yy in range(k+1):
            new1=a*xx+b*yy
            new2=c*(k-xx)+d*(k-yy)
            if new1>=base1 and new2>=base2 and (new1>base1 or new2>base2):
                return False
    return True


def fraction_trade(a,b,c,d,k):
    if a*d == b*c: return False
    low,high=sorted((Fraction(a,b),Fraction(c,d)))
    m=k//2
    return any(low<=Fraction(t,s)<=high for s in range(1,m+1) for t in range(1,m+1))


def test():
    assert all(direct_ef1_one_round(4,2,5,3,choice)==(choice[0]!=choice[1]) for choice in product((0,1),repeat=2))
    checks=0
    for a in range(2,8):
      for b in range(1,a):
       for c in range(2,8):
        for d in range(1,c):
         for choice in product((0,1),repeat=2):
          assert direct_ef1_one_round(a,b,c,d,choice)==(choice[0]!=choice[1])
         for k in range(1,13):
          predicted=(k%2==0 and not fraction_trade(a,b,c,d,k))
          if k%2==0:
           actual=direct_pareto(a,b,c,d,k,k//2,k//2)
           assert actual == (not fraction_trade(a,b,c,d,k)), (a,b,c,d,k)
          # If k odd, EF impossible; if even, the sequences are forced to be balanced
          assert predicted == (k%2==0 and direct_pareto(a,b,c,d,k,k//2,k//2)),(a,b,c,d,k)
          checks+=1
    print('OK',checks,'exact PO-vs-Farey exhaustive integer-profile/horizon comparisons')
    for h in range(1,35):
       a,b,c,d=h+1,h,h+2,h+1
       for k in range(2,2*(h+3)+1,2):
          assert fraction_trade(a,b,c,d,k)==(k>=2*(h+1)),(h,k)
       assert comb(2*h,h)>0
    print('OK 34 parametric sharp-horizon instances')
    # Truly direct enumeration of all 4^k round-by-round sequences for selected profiles
    total=0
    for a,b,c,d in [(2,1,3,2),(3,2,4,3),(4,3,6,2),(5,1,3,2),(4,2,8,4)]:
      for k in range(1,8):
       observed=0
       round_choices=[(0,1),(1,0),(0,0),(1,1)]
       for choices in product(round_choices,repeat=k):
        if not all(direct_ef1_one_round(a,b,c,d,z) for z in choices): continue
        x=sum(z[0]==0 for z in choices)
        y=sum(z[1]==0 for z in choices)
        u1=a*x+b*y
        u2=c*(k-x)+d*(k-y)
        if 2*u1 < k*(a+b) or 2*u2 < k*(c+d): continue
        if direct_pareto(a,b,c,d,k,x,y): observed+=1
       target=comb(k,k//2) if k%2==0 and not fraction_trade(a,b,c,d,k) else 0
       assert observed == target,(a,b,c,d,k,observed,target)
       total+=4**k
    print('OK',total,'direct round-sequence classifications')

if __name__=='__main__':test()
