"""Exact finite-path checks for boundary color response in one-shot antagonistic adsorption.
Standard library only. Run: python verify_seed_response.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial

def finite_halfline(m, a, b):
    # Each polynomial is a list of exact coefficients, constant first.
    aa = [[F(0)]]
    bb = [[F(0)]]
    for k in range(1, m+1):
        def integrate(poly, factor):
            out = [F(0), factor]
            for j,c in enumerate(poly):
                while len(out)<=j+1:out.append(F(0))
                out[j+1] -= factor*c/F(j+1)
            return out
        aa.append(integrate(bb[-1],a))
        bb.append(integrate(aa[-2],b))
    return aa, bb

def formula(n, d, t, a):
    b=1-a
    _,bb=finite_halfline(n-d,a,b)
    tail=bb[-1]
    integ=t**d/F(d)
    for j,c in enumerate(tail):
        integ -= c*t**(d+j)/F(d+j)
    return a**((d+1)//2)*b**(d//2)*integ/F(factorial(d-1))

def exhaustive_tensor(n):
    # Tensor indexed by distance, number of attempted sites, and A-mark count.
    out = [[[0 for i in range(k+1)] for k in range(n+1)] for d in range(n)]
    cases=0
    for k in range(n+1):
      for subset in combinations(range(n),k):
        for marks in product((1,-1),repeat=k):
          na=sum(z==1 for z in marks)
          for order in permutations(range(k)):
            splus=[1]+[0]*n
            sminus=[-1]+[0]*n
            for h in order:
                site=subset[h]+1
                mark=marks[h]
                if splus[site-1] != -mark and (site==n or splus[site+1] != -mark):
                    splus[site]=mark
                if sminus[site-1] != -mark and (site==n or sminus[site+1] != -mark):
                    sminus[site]=mark
            for i in range(n):
                out[i][k][na]+=(splus[i+1]==1)-(sminus[i+1]==1)
            cases+=1
    return out,cases

def main():
  comparisons=0;cases_total=0
  biases=(F(1,3),F(1,2),F(2,3))
  times=(F(1,3),F(1,2),F(1))
  for n in range(1,8):
    tensor,cases=exhaustive_tensor(n)
    cases_total+=cases
    for a in biases:
      b=1-a
      for t in times:
        for d in range(1,n+1):
          lhs=F(0)
          for k in range(n+1):
            for na,c in enumerate(tensor[d-1][k]):
              lhs+=F(c,factorial(k))*t**k*(1-t)**(n-k)*a**na*b**(k-na)
          rhs=formula(n,d,t,a)
          assert lhs==rhs,(n,d,a,t,lhs,rhs)
          comparisons+=1
  print('PASS exact finite-path exhaustive tests:',comparisons,
        'comparisons over',cases_total,'marked-order cases; n=1..7')
  # Entire response generating function at balanced colors gives exact t/2.
  # Test first 20 terms against certified positive factorial tail bound.
  import math
  from decimal import Decimal, localcontext
  with localcontext() as c:
    c.prec=45
    t=Decimal('1')
    exact=Decimal('0.5')
    summ=Decimal(0)
    for d in range(1,21):
      # Integrate exponential by a stable Taylor series using exact decimals.
      z=Decimal(0)
      for m in range(70):
        add=Decimal(-1)**m / (Decimal(2)**(d+m)*Decimal(math.factorial(m))*Decimal(math.factorial(d-1)) * Decimal(d+m))
        z+=add
      summ+=z
    tail=exact-summ
    assert tail>0
    assert tail < Decimal('0.5')**21/Decimal(math.factorial(21)) * Decimal('2')
    print('PASS balanced susceptibility sum rule: t/2 with 20-term tail',tail)
  return comparisons,cases_total
if __name__=='__main__':main()
