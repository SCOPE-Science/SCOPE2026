# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Fifty-eight-line angle-1/5 record pursuit in R18 via three-point SDP duality
- **Round:** 2026-09-07-first-light-01
- **Lane:** 734
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Algebraic Combinatorics
- **Method:** Bachoc-Vallentin three-point semidefinite programming duality with exact rational certificate rounding

## Problem

Decide the live fixed-angle edge N_{1/5}(18) in [57,59]: does a 58-line angle-arccos(1/5) system exist in R18? Attack from a documented 57-line R18 record parent via triple-correlation-constrained extension guided by three-point SDP duality, seeking either a beating 58-line Gram witness or a global exact-dual certificate that no 58-line 1/5-system exists.

## Attempted claim

There exist 58 unit vectors in R18 with pairwise inner products in {+1/5,-1/5} (equiangular lines with angle arccos(1/5)); equivalently, there exists a 58x58 symmetric Gram matrix G with diagonal 1, off-diagonal +/-1/5, positive semidefinite of rank <= 18, extending the triple-correlation profile of a documented 57-line R18 angle-1/5 record parent.

## Research outcome

No 58-line system found; instead proved all four documented 57-line angle-1/5 systems in R18 are exactly unextendable to any real 58th line (complete integer proofs, VERIFY_OK), after showing the preset three-point-dual fallback is infeasible against the published optimum 61.

## Why this attempt failed

Failed axes: originality, value.

originality: EMERGENT_FINDING route: genuinely arose from target 58-extension work (triple-correlation route) per report; absence from topic.json not adverse; judged under ordinary full standard with no presumption. Headline per-parent R18 non-extendability of the four Greaves-Syatriadi-Yatsyna 57-sets is substantively covered by a known stronger theorem. Lin-Munemasa-Taniguchi-Yoshino arXiv:2503.06377 (Mar 2025, published LAA 2025) proves every maximal affine equiangular set in X is strongly maximal (Thm 8.4 via Lemmas 2.6,7.2,8.3) and Appendix explicitly lists I1..I4 whose omega(Ii) induce the four sets corresponding to Seidel matrices Si from Fi in Greaves et al. [13] for i=1..4. Introduction states Yoshino [24] already proved the four sets are strongly maximal and not contained in the 276-set. Strong maximality (no extension even in higher dimension) strictly implies submitted R18 maximality (no real 58th vector in R18). Hence claim is a corollary/repackaging of a known stronger fact under different (switching-root/affine) encoding. New proof method (direct 2^18 integer enumeration) and basis-dependent unit-pattern counts do not establish priority. FAIL, never repairable. value: As an abstract fact, per-parent maximality of the R18 record parents would be motivated, but retrieval value fails here: (1) The core fact is already retrievable via a strictly stronger prior (Lin et al. Thm 8.4 + Appendix: F1..F4 strongly maximal), so an independent record for the weaker R18-only corollary has no incremental retrieval need. Report's 'first maximality data' premise is materially false. (2) The only arguably new data — unit-norm pattern counts 304/174/224/154 — are basis-dependent (fixed bases [35..51,54] etc.), unexplained enumerations with no canonical meaning, no interpretation, and no demonstrated downstream use; certification alone does not rescue them per policy. Fails the exact-invariant clause which requires the value be not known: here it is known and implied by stronger prior. FAIL.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Per-parent maximality only; does not prove global N_{1/5}(18) ≤ 57.', 'Says nothing about 58-systems avoiding F1..F4 57-subsets.', 'Munemasa-family 57-sets not tested (no machine-readable matrices).']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
