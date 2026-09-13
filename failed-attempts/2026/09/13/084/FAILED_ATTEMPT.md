# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Single-contact scattering correspondence for (P^2, nodal cubic)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1663
- **Disposition:** AUDIT_1_REJECT
- **Domain:** log Gromov-Witten theory and mirror symmetry
- **Method:** tropical correspondence and wall-crossing with nodal monodromy

## Problem

Let X=P^2 and N be an irreducible nodal cubic, e.g. a plane cubic with one ordinary double point and smooth elsewhere, so N is anticanonical of degree 3. Equip (X,N) with the divisorial log structure from N. For each integer d>=1 let beta=d[H] and let M_d be the genus-zero log Gromov-Witten invariant of (X,N) with one interior point insertion and one relative marking of maximal contact order beta.N=3d supported at the smooth locus of N. Prove or disprove that for every d>=1, M_d equals the coefficient of the corresponding monomial in the consistent completion of the explicit single-initial-wall scattering diagram with monodromy around the node on the dual intersection complex of (X,N), equivalently the weighted count of rigid genus-zero tropical curves with one unbounded leg of weight 3d and the associated broken-line product, via tropical correspondence and wall-crossing. The d=1 flex-line count is non-vacuous. A complete answer is a proof of this equality for all d>=1 or a rigorous counterexample at one explicit d0 with both M_{d0} and the wall-crossing coefficient computed and unequal.

## Attempted claim

Let X=P^2 and N be an irreducible nodal cubic, e.g. a plane cubic with one ordinary double point and smooth elsewhere, so N is anticanonical of degree 3. Equip (X,N) with the divisorial log structure from N. For each integer d>=1 let beta=d[H] and let M_d be the genus-zero log Gromov-Witten invariant of (X,N) with one interior point insertion and one relative marking of maximal contact order beta.N=3d supported at the smooth locus of N. Prove or disprove that for every d>=1, M_d equals the coefficient of the corresponding monomial in the consistent completion of the explicit single-initial-wall scattering diagram with monodromy around the node on the dual intersection complex of (X,N), equivalently the weighted count of rigid genus-zero tropical curves with one unbounded leg of weight 3d and the associated broken-line product, via tropical correspondence and wall-crossing. The d=1 flex-line count is non-vacuous. A complete answer is a proof of this equality for all d>=1 or a rigorous counterexample at one explicit d0 with both M_{d0} and the wall-crossing coefficient computed and unequal.

## Research outcome

Disproved the claimed all-degrees equality by an explicit d=1 counterexample: M_1=0 by virtual dimension while the scattering side is nonzero via an exhibited flex line.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline disproof is mechanically implied by standard tools, not a new theorem. Log-side vanishing M_d=0 follows immediately from textbook log CY virtual-dimension grading taught in Gross-Siebert/Abramovich-Chen theory. Flex line Q,L for this classical nodal cubic is elementary projective geometry. Fused literature search (Graefnitz smooth del Pezzo correspondence, Bousseau smooth (P2,E), Gross-Pandharipande-Siebert tropical vertex, Gross-Hacking-Keel) shows correct correspondence literature always uses unpointed maximal-tangency invariants; no source states this pointed nodal equality, but standard grading plus classical flex substantively implies its falsity without new insight. This is textbook corollary/repackaging, failing originality threshold. value: ADMISSION_DEFECT: negative resolution exposes only a type/normalization error that Admission should have ruled out. Target compares a pointed invariant of virtual dimension 1-2=-1 (identically zero for all d) against an unpointed scattering coefficient (virtual dimension 0), guaranteeing mismatch a priori by elementary dimension count. Per STANDARD and TARGET policy, vacuity, normalization errors, and cheap small-instance mismatches fail value even if literally false. Exhibited flex line only confirms non-vacuity required by topic; it does not create downstream use, new boundary, lemma, or retrievable exact invariant. No future researcher needs this pointed-vs-unpointed mismatch as a record.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: This disproof applies to the claim exactly as stated, with the interior point insertion. Differently pointed log invariants (e.g. a single relative marking with virtual dimension 0) are different numbers and are not addressed. The scattering nonvanishing argument is the structural flex-line/broken-line contribution at order 3 and does not analyze higher-order wall completions. The log virtual-dimension formula used is standard Gross-Siebert/Abramovich-Chen theory.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
