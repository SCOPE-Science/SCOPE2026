"""Phase 4c: implement TRUE Smart sieve for K=Q case and MEASURE.
Per-prime dictionary: exponent vectors A mod (q-1) [6-dim, rho=(-1,2,3,7,11,50069)]
-> residue X in F_q. Complement: B with Y=1-X. Keys: A with X,1-X both nonzero (and in H).
Size per prime: #keys ~ q-2 times ker, ker=(q-1)^6/|H| ~ (q-1)^5.
BUT the sieve refinement across primes (drop_vector): A survives only if compatible
with other primes' dicts. Final: compatible_systems across primes via CRT on L=lcm(q-1),
then lift each system to box |e|<=B (unique if L>2B) and test x+y=1 EXACTLY.
Total work ~ #final CRT systems. Estimate: implement for 2-3 small primes, count systems,
extrapolate. The (q-1)^6 enumeration per prime is the bottleneck: q=13 -> 12^6=3M ok;
q=17 -> 16^6=16.7M (slow in py, ok in numpy); bigger q needs smarter enumeration
(iterate over X-subgroup instead: for each X in GoodSet (~q values), fibre = coset of ker;
ker enumeration still (q-1)^5 each!). Hmm — Sage faces same: product_rho_orders huge.
Sage handles via residue-field-vector grouping (rfv_to_ev): enumerate exponent vectors only
mod ORDERS (product of rho orders), not mod q-1. For K=Q, rho orders divide q-1; product
can still be ~ (q-1)^6. For the SIEVE to be efficient need SMALL rho orders: choose q with
small orders of {2,3,7,11,50069} mod q! E.g. q=5: orders divide 4. q=17: divide 16.
Smart sieve prime selection: split_primes_large_lcm picks primes minimizing product of
orders presumably. Enumeration cost per prime ~ prod orders; #systems ~ related.
Let me: find primes q (not in S3) with small order-product for rho, implement full sieve
with L>2B~4800, count final systems, time it. If final systems ~ millions and each lift
cheap: FEASIBLE. Go.
"""
import math, itertools, time
rho=[-1,2,3,7,11,50069]
def orders(q):
    return [pow(r,q-1,q) and order_mod(r,q) for r in rho]
def order_mod(a,q):
    a%=q
    if a==0: return None
    from math import gcd
    o=q-1; d=o; f={}
    n=d; p=2
    fac={}
    while p*p<=n:
        while n%p==0: fac[p]=fac.get(p,0)+1; n//=p
        p+=1 if p==2 else 2
    if n>1: fac[n]=1
    for pr in fac:
        while o%pr==0 and pow(a,o//pr,q)==1: o//=pr
    return o
cands=[]
for q in range(5,2000):
    if q in (2,3,7,11,50069): continue
    # prime check
    if any(q%p==0 for p in range(2,int(q**0.5)+1)): continue
    if any(r%q==0 for r in rho): continue
    oo=[order_mod(r,q) for r in rho]
    import math as m
    prod=1
    for o in oo: prod*=o
    cands.append((prod,q,oo))
cands.sort()
print("best order-product primes:")
for prod,q,oo in cands[:15]:
    print(f"  q={q} orders={oo} prod={prod:.2e} q-1={q-1}")
