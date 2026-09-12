"""Phase 4d: full Smart-style sieve implementation (K=Q), optimized enumeration.
Per prime q: enumerate exponent tuples mod ORDERS (not mod q-1): total ~ prod orders.
For each: X = prod rho_i^{a_i} mod q; keep if X!=0,1 (Y=1-X != 0) — record (A, X).
Group by X. Complement dict: A -> list of B with Y_B = 1-X_A.
Cross-prime refinement: skip initially (Sage does drop_vector refinement; measure raw first).
Compatible systems: CRT across primes for A-side AND B-side jointly: for combined moduli,
A-systems then for each, B must be compatible... Sage does full (A,B) CRT systems then lifts.
Simplify (rigorously equivalent): CRT-combine A-constraints across primes -> A-systems mod L;
for each A-system, lift A to box (candidates ~ (2B/L)^6 each), compute x, check y=1-x S3-smooth.
Since L>2B, each A-system lifts to <=1 candidate in box... but #A-systems could be huge.
#A-systems mod L ~ L^6 * prod_q(q/L_q...)... measure with q's {5,19,13}: L=lcm(4,18,12)=36.
Then add primes until L>4800, tracking #A-systems growth. Prediction: #A-systems ~ L^6/...
hmm need GoodSet density: per prime, fraction of A-space surviving = #{A: X,1-X in H}/(q-1)^6.
For q=5: total A-space enumerated mod orders: prod=256 entries (with redundancy mod q-1:
256/4^6=256/4096: covers each class 1/16? orders (2,4,4,4,1,2): enumeration mod orders gives
256 combos mapping into 4^6=4096 classes: each combo represents 4096/256=16 classes (fibres of
exponent reduction). Valid combos: those with X,1-X nonzero. Measure everything concretely.
"""
import math, itertools, time
rho=[-1,2,3,7,11,50069]
def order_mod(a,q):
    a%=q
    o=q-1; n=o; fac={}; p=2
    nn=n
    while p*p<=nn:
        while nn%p==0: fac[p]=fac.get(p,0)+1; nn//=p
        p+=1 if p==2 else 2
    if nn>1: fac[nn]=1
    for pr in fac:
        while o%pr==0 and pow(a,o//pr,q)==1: o//=pr
    return o
def sieve_prime_data(q):
    oo=[order_mod(r,q) for r in rho]
    rec={}
    for A in itertools.product(*[range(o) for o in oo]):
        X=1
        for ai,ri in zip(A,rho): X=(X*pow(ri,ai,q))%q
        if X in (0,1): continue
        rec.setdefault(X,[]).append(A)
    return oo,rec
for q in (5,19,13,17):
    t=time.time()
    oo,rec=sieve_prime_data(q)
    nsys=sum(len(v) for v in rec.values())
    import math as m
    prod=1
    for o in oo: prod*=o
    print(f"q={q}: prod_orders={prod} validA={nsys} ({time.time()-t:.1f}s) frac={nsys/prod:.3f}")
