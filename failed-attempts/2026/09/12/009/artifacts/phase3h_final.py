"""Phase 3h: push Smart iteration further — the stall at B0=2405,u=5 needs diagnosis.
At u=5: does a SMALLER u fire? u=5 fired with B0=2405 -> Bnew=(5+1)/c5=2404.7 <2405 barely.
Try: with B0=2404.7, maybe u=4 fires? thr=4*2404^2=2.3e7. u=4 lattice det=p^4~6e18,
lambda1~det^{1/5}~ 6e18^0.2 ~ 90?? sqrt: shortest^2 ~ 90^2 ~ 8000 < 2.3e7. No fire at u=4
unless actual shortest big. The iteration found u=5 fires (shortest^2 > 2.3e7? det=p^5,
lambda1 ~ (p^5)^{1/5} = p = 50069, ^2 ~ 2.5e9 > 2.3e7 YES fires).
Fixed point: B*=(u+1)/c5 with u minimal firing. To get B* smaller need u=4 to fire, needs
thr < shortest(u=4)^2. Compute exact shortest at u=4: if S4^2 ~ e.g. 1e6, then B0 < 500
would fire at u=4 -> Bnew=(4+1)/c5=2004. Still ~2000. u=3: Bnew=1603; u=2: 1202; u=1: 801.
Floor ~800 even in best case?! Because B2=(u+c9)/c5 >= 2/c5 = 801. So Smart p-adic LLL at
v=(50069) can NEVER give exponent bound below ~800 (c5^-1 scale). And ord_p cap <=3 needs
valuation bound, a different quantity!

KEY INSIGHT (Smart Ch.IX / Sage pipeline): the p_adic_LLL_bound returns bounds on
EXPONENTS assuming extremal place finite. The FINAL ord_v caps come from a different
lemma: once exponents <= B_final (~800), ord_p(x(1-x)) is bounded by... still need
valuation-specific argument. Options:
 (a) Direct: |exponents| <= 800 for ALL S-unit exponents? Then x = prod p_i^{e_i},
     and x-1 = ... ord_p(x-1) via LIFTING: if x=1 mod p^k... With exponents bounded by
     800, is ord_p(x(1-x)) <= 3 provable? NO — x could still be 1 mod p^4 with exponents
     <= 800 (e.g. x = 1+p^4*m has huge height generally, but some S-unit could coincide).
     Need: enumerate/check all exponent combos? 1600^5 ~ 1e16 — infeasible directly, but
     SIEVE (Smart Ch.X, Sage 'sieve') finishes. Sieve over 5-dim box of side 1600 with
     split-prime lcm conditions: feasible in Sage (minutes-hours), NOT in 1-hour stdlib lane.
 (b) The target claims cap<=3 DIRECTLY from "logged p-adic LLL at stated precision".
     Our computation shows the RAW pipeline stalls at exponent bound ~800-2400, and the
     valuation cap<=3 requires the SIEVE stage (Smart Ch.X/XI: sieve + final enumeration),
     which for rank 5 with B~800 needs serious computation (Sage-level, estimated hours).
 (c) ALTERNATIVE direct valuation attack: suppose ord_p(x(1-x)) >= 4. Then x = 1+p^4 t or
     x = p^4 t (up to denom). Use S-unit structure + size bounds: archimedean Baker bound
     B0arch on exponents (~1e19 raw, reducible by REAL LLL to ~hundreds), then p-adic de Weger
     lemma in VALUATION form (Smart Lemma VI.5 applied to get ord bound directly): the
     returned B2=(u+c9)/c5 for SMALLER c5... hmm.

Actually WAIT. Reconsider what the target asks: 'ord_{50069}(x(1-x)) <= 3 ... tightened by
the logged p-adic LLL reduction at stated precision'. The reduction needed: show that
assuming ord >= 4 leads to contradiction via approximation lattice. Our lattice test with
y=0/b0=0 was the EXPONENT-bound form. The VALUATION form: assume v=ord_p >= 4 fixed, derive
linear form small p-adically, get lattice condition that FAILS for v>=4 (i.e., run the de
Weger lemma with u ~ v + something and show no exponent vector with |b|<=B0 can achieve
ord>=4 because the lattice min exceeds). That's EXACTLY what our loop does at threshold:
firing at u means: no |b|<=B0 vector gives ord >= u+c9-ish. Our loop fired at u=5 with
B0=2405: meaning NO solution with exponents<=2405 has ord_p >= 6?? (u+c9=6?). Hmm: B2 =
(u+c9)/c5 is a bound on B (exponents), and the lemma says: EITHER exponents <= B2 OR...
no wait, the lemma concludes B <= B2 (new exponent bound) — the u is auxiliary.

Let me restate Smart Lemma VI.5 (p.90): given B0 (exponent bound), lattice param u: if
ell(L,y) [our c10^2] > n B0^2 then B <= (u+c9)/c5 [if ...] — it's an exponent reduction.
The valuation NEVER appears directly. So indeed: p-adic LLL reduces EXPONENTS, and the
final valuation cap comes from ENUMERATION/SIEVE of the reduced box.

CONCLUSION: cap<=3 requires sieving box |e_i| <= ~2400 in rank 5 (4800^5 ~ 2.5e18 points
before sieve). Smart's sieve (sieve with split primes, Smart Ch.X) cuts this drastically
but implementing a full certified sieve in remaining ~25 min in stdlib Python is infeasible
to push to valuation <=3 with AUDIT-grade rigor... BUT maybe the sieve collapses fast:
for S-unit equation rank 5, Sage typically finishes in seconds-minutes. Our stdlib sieve:
use split primes q (q-1 | ... ) to sieve exponent lattice mod (q-1): standard Smart sieve:
x+y=1 mod q => for each split prime q not in S, exponent vectors mod (q-1) restricted to
~ (q+1)/... small set. With lcm(q_i - 1) > 2B, unique lift. Implementable! Estimate:
B~2400, need lcm(q-1)>=4800: q's like 17, 97... lattice points 4800^5=2.5e18 -> sieve mods
reduce by factor ~ q per prime... need product ~ 2.5e18/ feasible-enumeration(~1e7) = 2.5e11
=> many split primes; each sieve step is vectorized numpy over... 2.5e18 impossible to
iterate directly; Smart sieve works RECURSIVELY (sublattices), not by full enumeration.
Implementing recursive lattice sieve correctly + certified in 25 min: VERY RISKY.

PRAGMATIC RE-CHECK: is the TRUE fixed point actually lower? Our c3_cert=0.027 used a FLOAT
estimate 0.0277 truncated. True c3 needs exact regulator computation. If true c3 bigger,
c5 bigger, floor lower — but floor ~ 2/c5 ~ 800*c3ratio; c3 can't exceed ~1 (c1>=1, rank 5:
c3<=0.2). So exponent floor >= ~10. Valuation cap<=3 still needs sieve. UNAVOIDABLE.

DECISION INPUT: pivot to implementing Smart sieve (recursive) in stdlib+numpy? Time check.
Alternative: direct computational proof of cap<=3 via 'valuation-4 implies huge height':
 use LOWER bounds for linear forms (archimedean): if ord_p(x(1-x))>=4 with x S-unit of
 height H, then... no direct link between p-adic closeness and archimedean height without
 Baker. Baker gives: ord_p <= c8 log B (~2.3e12 * log B) — an UPPER bound, useless for cap 3.
 The cap 3 comes ONLY from reduction+sieve. So: sieve or nothing.

Estimate sieve feasibility honestly (test micro-implementation), then decide TARGET EXIT vs push.
"""
print(__doc__)
