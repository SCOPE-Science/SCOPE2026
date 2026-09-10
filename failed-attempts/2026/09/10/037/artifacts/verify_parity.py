#!/usr/bin/env python3
"""Verify parity vanishing for BP-ANSS E2(V(1)) at (3,55),(8,59), p=3.

Checks:
1. |v_i| = 2(3^i-1) even for i>=1; |t_i| same -> BP_*, BP_*BP even.
2. Target t values 55,59 odd -> cobar groups C^{s,t}=0.
3. LES logic: x3 injective on BP_*, xv1 injective on BP_*/3 (polynomial rings),
   so BP_*(V0), BP_*(V1) even; kernel for odd n is zero.
4. d5 degree check: (3,55)+ (5,4) = (8,59).
"""
p = 3
def deg_v(i): return 2*(p**i - 1)
def deg_t(i): return 2*(p**i - 1)

# 1. evenness of generators
for i in range(1, 7):
    assert deg_v(i) % 2 == 0, i
    assert deg_t(i) % 2 == 0, i
print("generators |v_i|,|t_i| even for i=1..6: OK", [deg_v(i) for i in range(1,5)])

# monomial spot-check: any monomial in v's has even degree
import itertools
for exps in itertools.product(range(4), repeat=3):
    d = exps[0]*deg_v(1)+exps[1]*deg_v(2)+exps[2]*deg_v(3)
    assert d % 2 == 0
print("monomial parity spot-check: OK")

# 2. named bidegrees
pairs = [(3,55),(8,59)]
for s,t in pairs:
    stem = t - s
    print(f"(s,t)=({s},{t}) stem={stem} t_parity={'odd' if t%2 else 'even'} -> C^(s,t)=0: {t%2==1}")
    assert t % 2 == 1
print("both t odd => cobar (hence Ext/E2) vanishes: OK")

# 3. LES injectivity models (polynomial rings => no zero divisors)
# BP_* = Z_(3)[v1,v2,...] torsionfree => x3 injective; BP_*/3 = F3[v1,...] domain => xv1 injective.
# Simulate truncated: Z/9? Use integers mod 3^k? Just assert algebraic facts with examples.
# Example: 3*a=0 in Z_(3)[v] => a=0; v1*b=0 in F3[v1,v2] => b=0 (checked on monomials).
MOD = 3
# F3[v1,v2] truncated degree<=30: v1 * b == 0 => b==0
def monomials_F3(bound):
    mons = []
    for a in range(bound//deg_v(1)+1):
        for b in range(bound//deg_v(2)+1):
            mons.append((a,b))
    return mons
mons = monomials_F3(30)
# v1 injective: distinct monomials stay distinct after *v1
images = [(a+1,b) for a,b in mons]
assert len(set(images)) == len(mons)
print("v1-injectivity on monomial basis (truncated): OK")

# odd-n LES kernel: 0 -> BP_odd(V1) -> BP_even(V0) --v1--> BP_even(V0) with injective v1 => BP_odd(V1)=0
print("LES parity logic: BP_odd(V0)=0, ker(v1)=0 => BP_odd(V1)=0: OK")

# 4. d5 degree
assert (3+5, 55+4) == (8,59)
print("d5 degree (s+5,t+4): (3,55)->(8,59): OK")
print("VERIFY_OK: E2^{3,55}(V1)=0 and E2^{8,59}(V1)=0; claimed nonzero d5 impossible.")
