# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Container-plus-spectral stability to the algebraic extremizer for Theta_{4,4,4}-free graphs at n^{5/4} scale
- **Round:** 2026-09-07-first-light-01
- **Lane:** 625
- **Disposition:** NO_RESULT
- **Domain:** Extremal Graph Theory
- **Method:** hypergraph container enumeration with spectral interlacing and pseudorandom stability comparison

## Problem

Pin the Turan-stability window for Theta_{4,4,4}-free graphs at the correct n^{5/4} scale: prove a container-plus-spectral lemma forcing every near-extremal Theta_{4,4,4}-free graph within delta0 n^{5/4} of ex(n,Theta_{4,4,4}) to lie within C delta0^{1/2} n^{5/4} edit distance of the Verstraete-Williford/Conlon-Wenger algebraic extremizer family, or else certify an explicit dense Theta_{4,4,4}-free graph far in edit distance from every member of that family.

## Attempted claim

There exist explicit absolute constants delta0=10^{-5} and C=20 such that for all sufficiently large n, with F={Theta_{4,4,4}} (three internally disjoint paths of length 4 between two endpoints) and A_n a fixed published Theta_{4,4,4}-free algebraic family member (Verstraete-Williford/Conlon-Wenger type) on n vertices with e(A_n) >= 10^{-6} n^{5/4} (rescaled by c_VW/2 with logged rescaling if the published constant is smaller), every F-free graph G on n vertices with e(G) >= ex(n,F) - delta0 n^{5/4} satisfies edit distance d_edit(G,A) <= C delta0^{1/2} n^{5/4} to some isomorphic copy A of A_n on the same vertex set, via one container enumeration bound plus one spectral interlacing inequality.

## Research outcome

Target blocked (no explicit F-free A_n; container K and uniform spectral gap need new research) and preset fallback attempted and blocked (only explicit n^{5/4} family D_4(q) contains Theta_{4,4,4}: 162 LL pairs at q=3; every certified-F-free alternative sits at exponent <5/4). Clean exit with replayable stdlib certificates; no emergent finding (D_4(3) one-sided check is audit evidence only).

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Target two-lemma certificate not proved; no explicit fully F-free A_n fixed (VW existence-only, D_4(q) contains F at q=3). Fallback triple not constructed: legs (i)x(ii) never jointly held across three bounded routes; leg (iii) untested. Computations are small-order (q<=3) witnesses plus exponent arithmetic, not asymptotic proofs. No claim of originality beyond the logged machine checks.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Target two-lemma certificate not proved; no explicit fully F-free A_n fixed (VW existence-only, D_4(q) contains F at q=3). Fallback triple not constructed: legs (i)x(ii) never jointly held across three bounded routes; leg (iii) untested. Computations are small-order (q<=3) witnesses plus exponent arithmetic, not asymptotic proofs. No claim of originality beyond the logged machine checks.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
