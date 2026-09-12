"""Phase 4: Smart sieve for K=Q, S3, x+y=1 — feasibility micro-test.
S-unit gens: rho = (-1, 2, 3, 7, 11, 50069), rank t+1=6 (incl torsion).
x = prod rho_i^{a_i}, y = prod rho_i^{b_i}, x+y=1.
Sieve prime q splits completely in Q trivially; q not in S. rho mod q in F_q^*;
exponents mod (q-1). Condition: X + Y = 1 in F_q for residue images.
compatible systems: exponent vectors mod L=lcm(q_i-1); count ~ ?
For ONE prime q: #valid (X,Y): X in <rho>(subgroup), Y=1-X in <rho>. If rho generate
all of F_q^* (likely since 2 primitive often), #systems ~ q (X any nonzero, Y=1-X
nonzero => q-2 pairs but need X,Y in subgroup; if full group: q-2).
L = q-1. Density of compatible systems: (q-2)/(q-1)^6 per... for 6-dim exponent pair
(A,B)? Actually A,B each 6-vector mod (q-1): (q-1)^12 total, valid ~ (q-2)*(q-1)^... hmm
need [(X,Y)] constrained: X determined by A (6 coeffs), Y by B: valid pairs ~ (q-2) * (q-1)^{...}.
The sieve power: after primes with L = lcm, #compatible systems vs L^6 lift... Sage then
lifts each system (unique lift to |e|<=B if L > 2B) and tests. #systems ~ L^5-ish?? Let's
measure directly for small q: count compatible exponent-pair systems mod (q-1) and
extrapolate to L~4800. If #systems at L=4800 is ~1e9, infeasible; if ~1e5, feasible.
Also NOTE: we only need ord_p cap<=3, NOT full solution set! Weaker target: rule out
ord>=4 within box. Specialized sieve: x = e p^v m/n form... still 5-dim.
Measure now.
"""
import math, itertools, time
from collections import defaultdict
S3=[2,3,7,11,50069]
rho=[-1,2,3,7,11,50069]
def systems_count(q):
    # images of rho in F_q^*
    if any(r%q==0 for r in rho): return None
    g=[r%q for r in rho]
    L=q-1
    # discrete logs: need base; q small: brute force A (6-tuple mod L) -> X. (q-1)^6 too big for q>7.
    # Instead: subgroup H=<g>; X ranges over H (compute reachable set with exponents? just iterate
    # multiplicative subgroup generated). Count pairs (X,1-X) both in H. #compatible (A,B) systems =
    # sum over valid (X,Y) of (#A mapping to X)*(#B mapping to Y) = validpairs * |ker|^2 where
    # ker: exponent tuples mapping to 1: |ker| = L^6/|H|.
    H={1}
    stack=[1]
    while stack:
        x=stack.pop()
        for gi in g:
            z=(x*gi)%q
            if z not in H: H.add(z); stack.append(z)
    valid=sum(1 for x in H if (1-x)%q in H and x!=0)
    ker=(L**6)//len(H)
    total=valid*ker*ker
    return len(H),valid,ker,total
for q in (5,13,17,29,37,97,193):
    if q in S3: continue
    print(f"q={q}: H,valid,ker,total={systems_count(q)}")
