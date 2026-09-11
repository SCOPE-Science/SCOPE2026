# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing one rank-1 general-model genus-2 curve via Coleman bound at p=7
- **Round:** 2026-09-07-first-light-01
- **Lane:** 801
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** Chabauty-Coleman p-adic integration at p=7 on general h(x) model with Mordell-Weil sieving

## Problem

Let C3: y^2 + (x^2+x)y = x^5 - x^4 - 2x^3 + 2x + 1 over Q (smooth genus-2 general Weierstrass model, one point at infinity). Naively visible points are infinity, (0,1), (0,-1). With Jacobian rank 1 and p=7 a good ordinary Chabauty prime for this model, prove via Coleman bound in the general-model differential basis and Mordell-Weil sieve at 19 and 37 that C3(Q) equals exactly this three-point set.

## Attempted claim

C3(Q) = {infinity, (0,1), (0,-1)} with Coleman bound at p=7 in the general-model basis and Mordell-Weil sieve elimination at 19 and 37 as witness.

## Research outcome

Target Q-census via Coleman+sieve blocked by absent CAS. Emergent finding: integer-certified disc/bad set, two-leg (11,61) count at 7, Weil rows at 5/7/11/13, J(Q)_tors=1, Galois signatures — replayable stdlib-only VERIFY_OK.

## Why this attempt failed

Failed axes: value.

value: EMERGENT_FINDING with no preset-value presumption (NOT_PRESET lane, no fallback_claim/fallback_qualification); genuine emergence acknowledged but ordinary full value standard applies with no relaxation. FAIL. The object is arbitrary, not independently natural: selector-generated candidate_index 3 with no external identity, no family, no application, no LMFDB entry, and no literature presence; small coefficients alone do not confer naturalness, and the admitted model-class-boundary motivation motivates the general-model METHOD, not this specific curve (any h(x) model would serve equally). The headline invariants are routine preliminaries, not a substantive result: brute-force Fp/Fp^2 counts, integer resultant plus trial division, distinct-degree factorisation, and one textbook gcd reduction-injectivity argument. They constitute setup material (half a page of lemmas in a Chabauty paper), advancing none of the admitted gap: no Jacobian rank, no rational-point determination, no h(x)-adjusted Coleman differential or disk bound, no sieve elimination, and no reusable general-model template. The finding falls short of even the lane's own declared valuable_partial_target (proved p=7 disk bound plus one sieve-eliminated disk). No concrete future need exists: the four Weil rows and torsion lock are useful only to a continuation on this same curve, which is blocked and abandoned, and are useless to general-model researchers working on other curves; no downstream theorem, table lookup, or citation path plausibly needs #J(F7)=84 for C3. The narrow-datum protection does not apply because its conditions fail: the object lacks independent object-level motivation, and the datum is not of a kind a future researcher would reasonably retrieve. This is certification of an arbitrary object and unexplained enumeration: correct and new, but not independently worth finding later. The missing substance (rank, census, Coleman bound, sieve) cannot be supplied by any bounded addition without a new research direction (CAS p-adic cohomology, Jacobian arithmetic), so this is intrinsic low value / missing substantive result, not a repairable presentation defect.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No statement about C3(Q), Jacobian rank, Coleman integrals, or sieve elimination. Bounded search (|a|<=1000,b<=500, sole hit x=0) is evidence only; Galois signatures constrain elements, not the full group.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
