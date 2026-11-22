"""Exact finite checks for a collective-risk quorum signal comparison.
This checks finite identities and samples; it does not prove large-N asymptotics.
Run: python checker.py
"""
from fractions import Fraction as F
from math import comb


def tail(n,k,p):
    return sum((F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(k,n+1)), F(0))


def common_mass(n,j,x,s):
    if j == 0:
        return (1-s) + s*(1-x)**n
    return s*F(comb(n,j))*x**j*(1-x)**(n-j)


def private_mass(n,j,x,s):
    p=x*s
    return F(comb(n,j))*p**j*(1-p)**(n-j)


def direct_enumeration_common(n,k,x,s):
    # Enumerate all AP/defector type configurations (not reuse binomial tails).
    achieve=F(0); prevent_weight=F(0); expect_contrib=F(0)
    for mask in range(1<<n):
        count=mask.bit_count()
        probability=x**count*(1-x)**(n-count)
        # public common risk interval [tau,1] makes the AP agents cooperate
        # integral of 1 dr = s, integral of r dr = (1-tau**2)/2.
        tau=1-s
        if count>=k:
            achieve += probability*s
            prevent_weight += probability*(1-tau*tau)/2
        expect_contrib += probability*s*count
    return achieve,prevent_weight,expect_contrib


def direct_enumeration_private(n,k,x,s):
    # Each agent contributes with probability x*s independently of disaster risk.
    achieve=F(0); prevent_weight=F(0); expect_contrib=F(0)
    for mask in range(1<<n):
        count=mask.bit_count()
        # Sum probability from independently realized (AP and signal) actions.
        probability=(x*s)**count*(1-x*s)**(n-count)
        if count>=k:
            achieve+=probability
            prevent_weight+=probability/2
        expect_contrib += probability*count
    return achieve,prevent_weight,expect_contrib

cases=0
for n in range(2,9):
 for x in [F(1,5), F(1,3), F(1,2),F(3,4)]:
  for tau in [F(1,7),F(1,3),F(1,2),F(4,5)]:
   s=1-tau; q=s*x
   common=[common_mass(n,k,x,s) for k in range(n+1)]
   private=[private_mass(n,k,x,s) for k in range(n+1)]
   assert sum(common)==sum(private)==1
   assert sum(k*common[k] for k in range(n+1)) == n*q
   assert sum(k*private[k] for k in range(n+1)) == n*q
   e2_pub=sum(k*k*common[k] for k in range(n+1))
   e2_priv=sum(k*k*private[k] for k in range(n+1))
   assert e2_pub-e2_priv==n*(n-1)*s*tau*x*x
   ratios=[]
   for k in range(1,n+1):
    a_pub=s*tail(n,k,x); a_ind=tail(n,k,q)
    direct_c=direct_enumeration_common(n,k,x,s)
    direct_p=direct_enumeration_private(n,k,x,s)
    assert direct_c==(a_pub,(1-tau*tau)*tail(n,k,x)/2,n*q)
    assert direct_p==(a_ind,a_ind/2,n*q)
    assert sum(common[k:])==a_pub and sum(private[k:])==a_ind
    ratios.append(a_pub/a_ind)
    cases += 1
   assert ratios[0]<1 and ratios[-1]>1
   assert all(a<b for a,b in zip(ratios,ratios[1:]))
   assert all(common[j]/private[j]<common[j+1]/private[j+1] for j in range(1,n))

n=6;k=2;x=F(1,2);tau=F(1,2);s=1-tau;q=s*x
pub=s*tail(n,k,x); ind=tail(n,k,q)
pub_w=(1-tau*tau)*tail(n,k,x); ind_w=ind
assert pub==F(57,128) and ind==F(1909,4096)
assert pub-ind==-F(85,4096)
assert pub_w-ind_w==F(827,4096)
assert (pub_w-ind_w)/2==F(827,8192)
print('PASS:',cases,'exact rational quota tests; mass, mean, variance, tail-ratio ordering, and independent enumeration.')
print('N=6,k=2, achievement difference',pub-ind,'; normalized welfare difference', (pub_w-ind_w)/2)

# General finite-support risk distributions, including nonuniform priors.
priors = [
 [(F(1,4), F(1,2)), (F(3,4), F(1,2))],
 [(F(1,10), F(1,4)), (F(1,2), F(1,4)), (F(9,10), F(1,2))],
 [(F(1,8), F(1,3)), (F(2,5), F(1,3)), (F(7,8), F(1,3))],
]
checks=0
for risk_prior in priors:
 assert sum(w for r,w in risk_prior)==1
 for threshold in [F(1,3), F(1,2), F(2,3)]:
  s=sum((w for r,w in risk_prior if r>=threshold),F(0))
  if not (0<s<1):continue
  mu=sum(r*w for r,w in risk_prior)
  h=sum((r*w for r,w in risk_prior if r>=threshold),F(0))/mu
  assert 0<s<h<1
  for n in range(2,8):
   x=F(2,5)
   q=x*s
   for quota in range(1,n+1):
    # Direct independent enumeration of all types and discrete environmental states.
    common_success=F(0); common_prevent=F(0)
    private_success=F(0); private_prevent=F(0)
    for r,w in risk_prior:
     for mask in range(1<<n):
      a=mask.bit_count()
      types_probability = x**a*(1-x)**(n-a)
      if r>=threshold and a>=quota:
       common_success+=w*types_probability
       common_prevent+=w*r*types_probability
      # In the private benchmark independently randomized actions have p=q.
      private_probability = q**a*(1-q)**(n-a)
      if a>=quota:
       private_success+=w*private_probability
       private_prevent+=w*r*private_probability
    assert common_success==s*tail(n,quota,x)
    assert private_success==tail(n,quota,q)
    assert common_prevent==mu*h*tail(n,quota,x)
    assert private_prevent==mu*tail(n,quota,q)
    checks+=1
print('PASS:',checks,'general-risk exact enumeration tests of both performance measures.')
