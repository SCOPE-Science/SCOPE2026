"""Faithful re-implementation of Sage's Yu_bound + Yu_C1_star + Omega' for K=Q,
S={2,3,7,11,50069}, v=(50069), using exact formulas scraped from S_unit_solver.py.
K=Q: dK=1, ep=fp=1, w=2, p=50069. Condition (1.15): p^f=50069 = 1 mod 4? 50069%4=1 -> True.
So no quadratic extension; use direct branch.

mus(SUK,v): multiplicative subgroup generators = S-primes except uniformizer at v.
For K=Q S-unit eq: fundamental units of Z_S^*: -1 plus primes q in S, q != p.
  mu_free_gens = [2,3,7,11] (n-1 = 4 gens), poss mu0 in {+-1} => n = 1+4 = 5.
Omega' = h(mu0) * prod_{mu in mu[1:]} h(mu), h = global Weil height = log max(num,den).
Yu_modified_height(mu0=-1 chain): max(h0, fp*log p/(kappa1*(n+4)*dK)).
Yu_C1_star with n=5: c1 * a1^n * (n^n (n+1)^(n+1)/n!) * p^fp/q^u * (dK/(fp log p))^(n+2)
  * log max(dK,e) * max(log(e^4 (n+1) dK), ep, fp log p); then (n+1)*C1.
p=50069: p%4==1, ep==1 -> c1=1473. a1=8(p-1)/(p-2), kappa1=10. q=2, u=v2(w=2)=1.
c8 = max(e^2/log2, Omega' * C1star); ord_p(Theta-1) < c8 log B.
"""
import math
P=50069; dK=1; ep=1; fp=1; w=2
p=P
# a1,kappa1,c1
a1=8*(p-1)/(p-2); kappa1=10; c1=1473
print(f"a1={a1!r} kappa1={kappa1} c1={c1}")
q=2; u=1  # v2(2)
mus_list=[2,3,7,11]
def h_global(a):
    # Weil height of rational a>0: log max(num,den); for -1: 0
    return math.log(a)
hs=[h_global(a) for a in mus_list]
print("heights:", hs)
n=1+len(mus_list)
print("n =", n)
# modified height of mu0: try mu0 = -1 (h0=0) and mu0=1 (h0=0): take max with h1
h1=fp*math.log(p)/(kappa1*(n+4)*dK)
print(f"h1 = log({p})/(10*{n+4}) = {h1!r}")
h_mu0=max(0.0,h1)
Omega=h_mu0*math.prod(hs)
print(f"Omega' = {Omega!r}  (~{Omega:.4e})")
# C1star
from math import factorial
C1=c1*(a1**n)*(n**n*(n+1)**(n+1)/factorial(n))*(p**fp/q**u)
C1*=(dK/(fp*math.log(p)))**(n+2)
C1*=math.log(max(dK,math.e))
C1*=max(math.log(math.exp(4)*(n+1)*dK), ep, fp*math.log(p))
C1star=(n+1)*C1
print(f"C1star = {C1star!r} (~{C1star:.4e})")
c8=max(math.exp(2)/math.log(2), Omega*C1star)
print(f"c8 = {c8!r} (~{c8:.4e})")
print(f"Sage-doc example scale check: ~9.03e9 for another field; ours ~{c8:.3e}")
# Convert to cap: need logB. Archimedean B0: use K0 pipeline? K0 needs c3_func etc.
# Conservative: K0/B0 from Smart pipeline bounded by 1e30? Report cap for a range of B0.
for B0 in (10**10, 10**15, 10**19, 10**30, 10**100):
    print(f"  B0=1e{int(math.log10(B0))}: ord_p < {c8*math.log(B0):.4e}")
