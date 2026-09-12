# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Graded-root lattice-homology branching obstruction
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1061
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Heegaard Floer Homology
- **Method:** Nemethi lattice homology and graded-root plumbing combinatorics

## Problem

Decide whether Nemethi graded roots distinguish Sigma(2,3,7) from Sigma(2,3,11) at lattice-homology level. Construct the graded roots R7 and R11 from the canonical negative-definite star-shaped Seifert plumbing graphs via lattice sublevel sets, compare their stem-trunk branching heights and leaf multiplicities, and certify the cobordism meaning through the lattice-cohomology exact sequence.

## Attempted claim

Let R7 and R11 be the Nemethi graded roots for the canonical negative-definite star-shaped Seifert plumbings bounding Sigma(2,3,7) and Sigma(2,3,11). Then R7 and R11 are non-isomorphic as graded roots with an explicit detectable difference in stem branching heights and leaf multiplicities above the minimal grading, certified through the lattice-cohomology surgery exact sequence as a homology-cobordism obstruction distinguishing the two spheres.

## Research outcome

Corrected certified non-isomorphism R7 vs R11 via S0 run shapes [5,5] vs [1,1] plus d=0 vs 2.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Replayed inputs/artifacts/verify_target.py -> VERIFY_OK and stability.py -> STABILITY_OK; G7 fiber minima cross-checked by independent brute force (B=7 matches all i). K^2+s=0 vs 8 and d=0 vs 2 arithmetic verified. However the essential inference that S0 run widths [5,5] vs [1,1] prove graded-root non-isomorphism is invalid: both reduced roots have 2 vertices at level 0 merging to 1 at level 1, hence are isomorphic as unshifted trees; width/cardinality of {w<=n} fibers and barrier widths are not graded-root invariants. The true distinction is only the absolute grading shift (d), so the headline proof as written rests on a false invariant claim. originality: ADMISSION_DEFECT: Admission/triage claimed no fused source tabulates R7 vs R11 side by side, but Can-Karakurt arXiv:1211.4934 Table 1 (Theorem 1.9) explicitly tabulates Sigma(2,3,7) and Sigma(2,3,11) side by side with kappa=1, d(-Y)=0 vs -2, and HF+(-Y)=T(0)+oplus Z(0) vs T(-2)+oplus Z(-2). Via Nemethi/Ozsvath-Szabo lattice=HF identification for Seifert spheres this substantively implies distinct absolute-graded roots and the d=0 vs 2 separation. Seetharaman-Yue-Zhu 2110.13405 Figure 3 publishes the (2,3,7) root and Can-Karakurt Example 2.4 computes the (2,3,11) tau=[0,1,0] root. The submitted w-ledger is therefore a recomputation/certificate and corollary of a known stronger tabulated fact, not a new comparison. Literal-title absence does not establish priority. value: ADMISSION_DEFECT: Admission value approval rested on the premise that the R7-vs-R11 verdict with d distinction was unrecorded and would advance the lattice-Floer boundary. Objective prior evidence (Can-Karakurt Table 1) shows the d=0 vs 2 separation and the HF+/lattice modules for exactly this pair were already published and compared. A recomputed w(i) ledger with corrected Laufer/DP certificates and observed blow-up stability is certification alone, which per STANDARD does not create value, and the width enumeration without a valid new invariant interpretation is an unexplained/record repackaging. No new citable boundary is contributed.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Relies on cited Nemethi background (one-bad-vertex reduction, almost-rational vanishing, blow-up invariance, lattice-Floer identification); the lattice blow-up/surgery exact sequence is NOT re-proved, only observed blow-up stability of the ledger is claimed; prior one-sided-walk numbers are withdrawn.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
