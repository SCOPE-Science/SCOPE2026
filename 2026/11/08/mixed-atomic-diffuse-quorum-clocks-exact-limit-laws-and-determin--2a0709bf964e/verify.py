"""Reproducible finite checks for mixed atomic--diffuse quorum clocks.

Standard library only. Finite calculations are diagnostics, not a proof of convergence.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb, exp, log

checks = 0

def confirm(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def rational_survival(weights, threshold, q):
    """Independent exponential clocks: q = exp(-t), all normalized clocks."""
    n = len(weights)
    total = Q(0)
    for mask in range(1 << n):
        mass = sum((weights[i] for i in range(n) if mask & (1 << i)), Q(0))
        if mass <= threshold:
            k = mask.bit_count()
            total += (1-q) ** k * q ** (n-k)
    return total


def exact_chain_tail(weights, threshold, k):
    """Subset Markov recursion for k independent uniform coupon draws."""
    n=len(weights)
    p = {0: Q(1)}
    for _ in range(k):
        new={}
        for mask, mass in p.items():
            for i in range(n):
                dest=mask | (1<<i)
                new[dest]=new.get(dest,Q(0))+mass/n
        p=new
    return sum((mass for mask,mass in p.items()
                if sum((weights[i] for i in range(n) if mask & (1<<i)),Q(0)) <= threshold), Q(0))


def words_tail(weights, threshold, k):
    """Directly enumerate strings; distinct from the subset recursion."""
    n=len(weights)
    favorable=0
    for word in product(range(n),repeat=k):
        observed=set(word)
        if sum((weights[i] for i in observed),Q(0)) <= threshold:
            favorable+=1
    return Q(favorable,n**k)

# Exactly enumerate every finite word for small unequal quorum weights.
print('starting words',flush=True)
for n in range(2,6):
    print('n',n,flush=True)
    for tup in list(product(range(1,4), repeat=n))[:min(12,3**n)]:
        weights=[Q(x,sum(tup)) for x in tup]
        for t in (Q(1,4),Q(1,2),Q(3,4)):
            for k in range(0,5 if n==5 else 6):
                a=exact_chain_tail(weights,t,k)
                b=words_tail(weights,t,k)
                confirm(a==b, ('finite word',n,tup,t,k,a,b))

print('words complete',flush=True)
# Exact Poissonization identity as a polynomial in q at N=2,3,4.
# P(all discoveries of chosen subset by t)=products of Bernoulli probabilities.
for n in range(2,6):
    weights=[Q(i+1,n*(n+1)//2) for i in range(n)]
    for theta in (Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4)):
        for q in (Q(1,7),Q(1,4),Q(1,2),Q(3,4),Q(6,7)):
            s=rational_survival(weights,theta,q)
            # Independent inclusion--exclusion over undrawn sets, not over drawn sets.
            s2=Q(0)
            for missing in range(1<<n):
                missing_mass=sum((weights[i] for i in range(n) if missing&(1<<i)),Q(0))
                if missing_mass>=1-theta:
                    z=missing.bit_count()
                    s2+=q**z*(1-q)**(n-z)
            confirm(s==s2,('complement',n,theta,q))
            confirm(Q(0)<=s<=Q(1),('probability bounds',n,theta,q))

print('rational complete',flush=True)
# One persistent type of weight 2/5, diffuse residual 3/5, threshold 1/2.
a,d,theta=Q(2,5),Q(3,5),Q(1,2)
q_low = 1-(theta-a)/d  # e^{-x_{present}} = 5/6
q_high = 1-theta/d    # e^{-x_{absent}} = 1/6
confirm(q_low == Q(5,6), 'first deterministic crossing')
confirm(q_high == Q(1,6), 'second deterministic crossing')
confirm(1-q_low == Q(1,6), 'first point mass')
confirm(q_high == Q(1,6), 'second point mass')
confirm(q_low-q_high == Q(2,3), 'continuous mass')

# Exact binomial calculation for the finite one-atom family at selected rational times.
def finite_one_atom(N, q):
    j=N-1
    p=1-q
    # conditional on the macroscopic type undiscovered / discovered
    s=Q(0)
    for flag,pr in ((0,q),(1,p)):
        for k in range(j+1):
            mass=a*flag + d*Q(k,j)
            if mass<=theta:
                s+=pr*comb(j,k)*p**k*q**(j-k)
    return s

print('binomial start',flush=True)
for N in range(2,10):
    weights=[a]+[d/Q(N-1)]*(N-1)
    for q in (Q(1,8),Q(1,6),Q(1,3),Q(1,2),Q(5,6),Q(7,8)):
        confirm(finite_one_atom(N,q)==rational_survival(weights,theta,q),('binomial',N,q))

print('binomial complete',flush=True)
# At q=1/2, the limiting survival is q, away from deterministic discontinuity times.
for N in (51, 101, 151, 201):
    val=float(finite_one_atom(N,Q(1,2)))
    confirm(abs(val-0.5)<0.04,('stable two-regime probability',N,val))

# The survival function of the limiting example is 1 below x_present,
# exp(-t) between its two deterministic jump locations, and 0 thereafter.
for q,expected in ((Q(9,10),Q(1)),(Q(1,2),Q(1,2)),(Q(1,5),Q(1,5)),(Q(1,10),Q(0))):
    x=log(1/float(q))
    f=Q(1)-q
    limit=q if d*f < theta <= a+d*f else (Q(1) if a+d*f<theta else Q(0))
    confirm(limit==expected,('limiting survival',q))


# Sharp 2^r deterministic-atom count: binary macroscopic weights total 1/4.
for r in range(1,9):
    atoms=[Q(2**i,4*(2**r-1)) for i in range(r)]
    dust=Q(3,4)
    threshold=Q(1,2)
    roots=set()
    for mask in range(1<<r):
        a_sum=sum((atoms[i] for i in range(r) if mask&(1<<i)),Q(0))
        confirm(Q(0)<threshold-a_sum<dust,('all drift crossings',r,mask))
        q=Q(1)-(threshold-a_sum)/dust
        confirm(Q(0)<q<Q(1),('finite exponential time',r,mask))
        roots.add(q)
    confirm(len(roots)==2**r,('maximal distinct deterministic times',r))

print(f'{checks} exact-rational / finite diagnostic assertions passed')
print('Exact limiting two-atom masses: 1/6 and 1/6; continuous remainder: 2/3')
print('Limiting example mean = log(6/5) + 2/3 =',log(6/5)+2/3)
