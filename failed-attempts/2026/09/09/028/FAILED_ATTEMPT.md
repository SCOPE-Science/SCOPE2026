# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Graded augmentation-chart separation of orientable Lagrangian fillings of a max-tb Legendrian twist knot
- **Round:** 2026-09-07-first-light-01
- **Lane:** 357
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Symplectic Topology
- **Method:** Floer-theoretic augmentation varieties with microlocal sheaf and cluster-chart mutation analysis

## Problem

Let Λ be the max-tb Legendrian representative of the twist knot 8_1 (even twist family). Do two explicitly constructed orientable exact Lagrangian fillings L, L' of Λ with identical tb/rotation and ruling polynomial induce graded augmentations lying in distinct algebraic-torus charts (cluster seeds) of the graded augmentation variety, and hence fail to be Hamiltonian isotopic relative to boundary?

## Attempted claim

For the max-tb Legendrian twist knot Λ of smooth type 8_1, there exist two orientable exact Lagrangian fillings L and L' with equal classical invariants (tb, rotation) and equal ruling polynomial whose induced graded augmentations ε_L, ε_L' lie in distinct cluster-chart algebraic tori of the graded augmentation variety Aug(Λ), distinguished by an explicit cluster regular function X with X(ε_L) ≠ X(ε_L'); consequently L and L' are not Hamiltonian isotopic relative to boundary.

## Research outcome

Consolidated fallback fragment: machine-verified replay of the twist-knot augmentation variety (ab+1)c=1 with full DGA-equation reduction plus the computational core of the certified torus non-embedding obstruction (separability/Bezout/unit/collision checks, finite-field counts), with the 8_1 two-filling distinction explicitly left open.

## Why this attempt failed

Failed axes: originality, value.

originality: Strongest delivered headline is a machine replay of Gao-Rutherford arXiv:2103.03951 Props 4.1/4.3 for odd Lambda_n: variety (ab+1)c=1, Laurent-unit/separability facts, small-q counts, eps membership. DRAFT itself labels it 'replay of GR Prop 4.1, machine-checked reduction' and 'computational core of GR Prop 4.3'. This is prior-published mathematics, not a new invariant, lemma, or distinction. Finite-field counts q^2-q+1 are mechanically implied by the published equation (q-1 bad pairs). Bezout -g+(s/m)g'=1 is the standard separability witness inside the cited proof. No cluster seed, mutation log, separating function X, 8_1 front/DGA, pinch fillings, transfer lemma, or chart-collision certificate is produced (admitted gap Sec 4). The admitted target's novelty (graded orientable two-filling chart distinction for 8_1) cannot confer originality on an undelivered claim; audit judges delivered content. A timestamp/ALL_PASS log does not establish priority. value: Delivered replay has no independently retrievable new fact: future work on twist-knot augmentations cites Gao-Rutherford for the variety and torus obstruction, not a sympy re-evaluation of 1+c_{j-1}c_j, four small-q brute forces, or tautological (2-1)==1 checks. Admission fallback required (a) graded variety + seed/mutation log for max-tb 8_1 and (b) transfer lemma or certified collision for the candidate pair; neither is present -- variety is for the odd family only, no seed/log, no 8_1 transfer, no pair obstruction. Per value standard, rigorous certification alone does not rescue recomputation of a known equation, and textbook-level corollaries (point-count formula, gcd=1) are not independently worth finding later. Honest gap statement (Sec 4) is commendable but does not create value. Headline 8_1 separation remains open.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['The 8_1 target (two orientable fillings, distinct graded charts, separating X) is not proved; no 8_1 front/DGA/pinch/cluster computation exists in-lane.', 'No cluster seed, mutation log, or separating function X is produced.', 'UFD/finiteness assembly of Prop 4.3 and the algebraic-isomorphism inverse of Prop 4.1 are cited human-checked proof, not machine-proved.', 'Transfer from odd-twist Lambda_n to even-twist 8_1 (gradings, de_1 term, tb/rot) not done; needs Etnyre-Ng-Vertesi analysis.', 'P…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
