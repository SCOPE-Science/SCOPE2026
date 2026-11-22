from decimal import Decimal,getcontext,ROUND_HALF_EVEN
from fractions import Fraction
getcontext().prec=140

def jacobi_certificate(a,b,L,parity,Niter=1000):
  ns=list(range(-L,L+1,2)) if parity==0 else list(range(-(L-1),L,2))
  n=len(ns);d=Decimal(b)/Decimal(a)
  ws=[d**((ns[i]+1)**2) for i in range(n-1)]
  v=[Decimal(1)]*n
  for _ in range(Niter):
    w=[v[i]+(ws[i-1]*v[i-1] if i>0 else 0)+(ws[i]*v[i+1] if i<n-1 else 0) for i in range(n)]
    scale=max(w)
    v=[x/scale for x in w]
  ints=[int((x*Decimal(10)**100).to_integral_value(rounding=ROUND_HALF_EVEN)) for x in v]
  assert min(ints)>0
  ratws=[Fraction(b,a)**((ns[i]+1)**2) for i in range(n-1)]
  ratios=[]
  for i in range(n):
    numerator=(ratws[i-1]*ints[i-1] if i else 0)+(ratws[i]*ints[i+1] if i<n-1 else 0)
    ratios.append(numerator/ints[i])
  low=min(ratios);high=max(ratios)
  tail=2*Fraction(b,a)**((L+1)**2 if parity==0 else L**2)
  print((a,b),('even' if parity==0 else 'odd'),'l',L,'low',format(float(low),'.14f'),'high',format(float(high),'.14f'),'tail',float(tail),'spread',float(high-low),'len',len(ns))
  return low,high+tail,ints

# Rational thresholds are deliberately coarse; every comparison is checked in Fraction arithmetic.
cases=[(24,23,24,"odd", Fraction(15254155,10000000),Fraction(15254140,10000000)),
       (12,11,14,"even",Fraction(13750732,10000000),Fraction(13748651,10000000)),
       (5,4,10,"odd",Fraction(11464312,10000000),Fraction(11393045,10000000))]
for a,b,L,winner,winner_lower,loser_upper in cases:
 e=jacobi_certificate(a,b,L,0)
 o=jacobi_certificate(a,b,L,1)
 if winner=="odd": hi,lo=o,e
 else: hi,lo=e,o
 assert hi[0] > winner_lower, (a,b,"winner lower")
 assert lo[1] < loser_upper, (a,b,"loser upper")
 assert winner_lower > loser_upper, (a,b,"not separated")
 print("EXACT PASS",(a,b),winner,"rho winner >",str(winner_lower),"rho loser <",str(loser_upper))
print("Three rational certificates verified; continuity forces at least two parity switches.")
