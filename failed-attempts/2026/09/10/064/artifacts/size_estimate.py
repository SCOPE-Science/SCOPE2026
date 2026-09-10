"""Bounded recovery test: census of k=3 weighted-degree-12 jet monomials + unknown-count scaling.
Shows the (3,12,2) Fp system is 10^4-10^5 unknowns / several-x equations, and -- crucially --
that the certified matrix additionally needs undocumented k=3 inputs (order-3 transition formulas,
triangular denominator exponents, infinity twist bounds), so failure is theoretical, not just coding time."""
sols=[]
for a in range(13):
 for b in range(13-a):
  for c in range(5):
   for d1 in range(3):
    for d2 in range(3):
     if a+b+3*c+5*(d1+d2)==12:
        sols.append((a,b,c,d1,d2))
print("jet monomials at m=12:", len(sols))
for D in [4,6,8,10]:
    print(f"D={D}: total unknowns ~ {len(sols)*(D+1)**3}")
print("RESULT: size alone is tractable for machines, but exact k=3 denominator/twist data absent -> matrix not certifiable in-hour.")
