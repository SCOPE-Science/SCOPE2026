# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharpened explicit Burgess r=2 constant for prime moduli with lowered threshold and improved least-nonresidue corollary
- **Round:** 2026-09-07-first-light-01
- **Lane:** 128
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Analytic Number Theory
- **Method:** explicit Burgess r=2 amplification with optimized auxiliary estimates and interval-certified constants

## Problem

Prove a general explicit Burgess r=2 inequality for nonprincipal quadratic characters modulo primes with a certified constant at least 10% below the pinned prior implemented constant and validity threshold P0<=1e6, and derive the improved least-quadratic-nonresidue corollary n(p)<=C_n p^{1/4} log p with correspondingly improved C_n and lowered nontriviality threshold.

## Attempted claim

Let chi be any nonprincipal quadratic Dirichlet character modulo a prime p and S(M,N)=sum_{M<n<=M+N} chi(n). With the log-factor shape pinned to the prior Trevino/Booker r=2 form at runtime, prove |S(M,N)| <= C* N^{1/2} p^{3/16} L(p) for all p >= P0, where C* <= 0.90*C_prior (>=10% below the pinned prior implemented r=2 constant recomputed from cited formulas before optimization), P0 <= 10^6 (finite range discharged by logged verification), and hence n(p) <= C_n p^{1/4} log p for all p >= P0 with C_n improved >=10% over the pinned Trevino corollary and a lowered nontriviality threshold. All auxiliary constants are interval-certified and the margin is verified by a comparison script.

## Research outcome

Fallback-(a) general theorem: quadratic r=2 Burgess constant 2.56 at p0=1e7, 6.68% below pinned Trevino prior 2.7381, interval-certified, with n(p)<=26.3 p^{1/4} log p corollary (12%+ cut). Scoped to all large primes; no finite prime table is the contribution.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Three independent essential-inference failures. (1) Unproved/incorrect Weil-moment coefficient: DRAFT asserts quadratic-only W<=3B^2p+2B^4sqrt(p) ('2r-2=2 instead of 2r-1=3' via 'Trevino Remark 1') with no proof. Pointwise Weil analysis contradicts the derivation: the all-distinct 4-tuple pattern (1,1,1,1) gives odd-part degree d=4, hence per-tuple bound (d-1)sqrt(p)=3sqrt(p), not 2sqrt(p). Pattern-counted bound is W<=3B^2p+[4B(B-1)+6B(B-1)(B-2)]sqrt(p)+3B(B-1)(B-2)(B-3)sqrt(p) ~2.83B^4sqrt(p) at B~68.8, which does NOT imply the claimed 2B^4sqrt(p). Small-p brute-force checks (p=7..10009, various B) show no numerical violation, but that is evidence, not proof, and the per-tuple justification as written is false. Recomputing the fixed point with the correct coefficient 3 (same B,k) gives F0~1.87 vs claimed 1.769 and C~2.69 vs 2.56, i.e. only ~1.8% below prior 2.7381, below the 5% fallback margin; re-optimizing B=p^{1/4} gives ~2.67 (~2.3% cut). So the 6.68% margin depends on the unproved lemma. (2) Corollary exponent algebra error: from |S|<=C*N^{1/2}p^{3/16}(log p)^{1/2} < N/2 one gets N>(2C*)^2 p^{3/8} log p, not p^{1/4} log p. The claimed n(p)<=26.3 p^{1/4} log p does not follow from the r=2 theorem; the 'N>(2C*)^2p^{1/4}log p' step drops a power (p^{3/8} vs p^{1/4}). The Vinogradov-trick paragraph ('prime-density loss absorbed') does not repair the dimensional mismatch. (3) Global monotonicity unproved: coverage of all p>=1e7 is asserted from spot floats at 1e7,3e7,1e8,1e9,1e12, not from a proved monotone majorant; t1/ef/inner/den monotonicity for all p>=p0 is not established with rigorous enclosures. The interval script itself replays (C_UPPER=2.555118, A_low=29.398, den>=0.786) conditional on the formula, and enclosures were verified to contain true log/sqrt/powers values, but that only certifies the closed-form evaluation, not the lemmas above. Prior-baseline replay (2.73807) is asserted without a replay artifact. Hence the headline theorem+corollary are not proved as stated. value: Judging the strongest headline package as stated (6.68% r=2 cut at same threshold p0=1e7 plus n(p)<=26.3 p^{1/4} log p corollary): it is not independently worth retrieving. (i) The advertised downstream payoff is absent because the corollary exponent is wrong (r=2 yields p^{3/8}, not p^{1/4}); with the corollary invalid, the residual is a same-threshold constant tweak. (ii) The residual tweak is obtained by re-tuning two scalars (B multiplier sqrt(3/2), k=1/22 vs prior 2/45) while quoting all other lemmas unchanged; the only claimed new lemma (quadratic W coefficient) is unproved and attributed to a prior remark. That is a mere parameter substitution with a single-digit unmotivated gain at no threshold improvement (main target P0<=1e6 unmet), not a new general boundary, exact invariant of a motivated object, or benchmark advance of the kind the literature publishes with threshold reduction. Certification of a closed-form evaluation alone does not r…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Fallback (a) only: 6.68% cut, not the 10% main target; threshold p0=1e7 equals (not beats) prior; quadratic characters only (uses Remark-1 improved Weil moment); lemmas quoted from Trevino, not re-proved; interval script uses hand enclosures + 0.5% margin rather than formal interval arithmetic library.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
