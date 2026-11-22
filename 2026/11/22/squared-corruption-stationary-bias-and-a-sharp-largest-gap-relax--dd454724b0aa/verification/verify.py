"""Exact checks for scalar residual-weighted Kaczmarz and its stationary law."""
from fractions import Fraction as Q
from itertools import combinations, product
from math import exp


def weighted_chain(levels, counts, z):
    assert len(set(levels)) == len(levels) and all(n > 0 for n in counts)
    assert Q(0) < z <= Q(1)
    r = len(levels)
    K = [[z ** abs(levels[i]-levels[j]) for j in range(r)] for i in range(r)]
    Z = [sum((counts[j]*K[i][j] for j in range(r)),Q(0)) for i in range(r)]
    P = [[counts[j]*K[i][j]/Z[i] for j in range(r)] for i in range(r)]
    D = sum((counts[i]*Z[i] for i in range(r)),Q(0))
    pi = [counts[i]*Z[i]/D for i in range(r)]
    return P, pi

checks=0
for r in range(2,5):
  for levels in combinations(range(-2,4),r):
    for counts in product(range(1,4), repeat=r):
      for z in [Q(1), Q(1,2), Q(1,3), Q(2,3)]:
        P, pi=weighted_chain(levels,counts,z)
        assert sum(pi)==1
        for i in range(r):
          assert sum(P[i])==1
          for j in range(r):
            assert pi[i]*P[i][j]==pi[j]*P[j][i]
        for j in range(r):
          assert sum((pi[i]*P[i][j] for i in range(r)),Q(0))==pi[j]
        checks+=1

for g in range(2,12):
 for k in range(1,g):
  for z in [Q(1), Q(1,2), Q(1,3), Q(1,5), Q(3,4)]:
   P,pi=weighted_chain((0,1),(g,k),z)
   p=k*z/(g+k*z)
   q=g*z/(k+g*z)
   den=g*g+k*k+2*g*k*z
   target=k*(k+g*z)/den
   lam=1-p-q
   assert P[0][1]==p and P[1][0]==q
   assert pi[1]==target
   assert lam == g*k*(1-z*z)/((g+k*z)*(k+g*z))
   x=Q(0)
   for t in range(20):
     assert x==target*(1-lam**t)
     x=(1-x)*p+x*(1-q)
   checks+=1

for g in range(2,20):
 for k in range(1,g):
  for counts in product(range(1,k+1),repeat=min(k,3)):
   if sum(counts)!=k:continue
   badsq=sum(n*n for n in counts)
   prob=Q(badsq,g*g+badsq)
   assert Q(k,g*g+k)<=prob<=Q(k*k,g*g+k*k)
   checks+=1
print('VERIFY_OK',checks)

# High precision diagnostic for the unique-largest-gap spectral prefactor.
# This numerical test does not substitute for the variational proof.
from decimal import Decimal, localcontext

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

with localcontext() as ctx:
    ctx.prec=85
    v=(0,1,4)
    mult=(4,1,2)
    C=Decimal(21)/Decimal(34)
    deviations=[]
    for eta in (4,6,8,12,18):
        weights=[[(-Decimal(eta)*abs(v[i]-v[j])).exp() for j in range(3)] for i in range(3)]
        Z=[sum(mult[j]*weights[i][j] for j in range(3)) for i in range(3)]
        P=[[Decimal(mult[j])*weights[i][j]/Z[i] for j in range(3)] for i in range(3)]
        B=sum(P[i][i] for i in range(3))-1
        E=det3(P)
        discr=B*B-4*E
        assert discr>=0
        lam2=(B+discr.sqrt())/2
        gap=1-lam2
        assert gap>0
        ratio=gap*Decimal(eta*3).exp()
        deviations.append(abs(ratio-C))
    assert all(deviations[i+1]<deviations[i] for i in range(len(deviations)-1))
    assert deviations[-1]<Decimal('0.000001')
print('SPECTRAL_DIAGNOSTIC_OK', str(ratio))
