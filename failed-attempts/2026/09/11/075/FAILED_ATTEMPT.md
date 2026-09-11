# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Nontrivial nested Whitehead bracket on a 10-vertex stacked moment-angle complex
- **Round:** 2026-09-07-first-light-01
- **Lane:** 880
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Topology
- **Method:** BBCG decomposition with Iriye-Kishimoto fat-wedge filtration and Whitehead-bracket calculus

## Problem

Let W10 be the 10-vertex stacked 2-sphere whose missing-face set contains two disjoint missing edges e1,e2 and a missing triangle supported on their neighbourhood (explicit stacking word fixed at start). Prove that the iterated higher Whitehead product [[mu1,mu2],mu3] of the canonical inclusions of the corresponding BBCG wedge summands is a nontrivial element of pi_N(Z_W10) for the resulting N, realized as the top fat-wedge attaching map.

## Attempted claim

For the named 10-vertex stacked sphere W10, the iterated higher Whitehead product [[mu1,mu2],mu3] supported on the two disjoint missing edges and the stacked missing triangle is defined and nontrivial in pi_N(Z_W10), and equals (up to sign) the top BBCG fat-wedge attaching map, with summand label exhibited.

## Research outcome

Target blocked: iterated Whitehead [[mu1,mu2],mu3] on 10-vertex stacked W10 lacks both its inner S^1 support (chordality forbids the C4 join on any stacking word) and its detecting Hochster/BBCG summand (every disjoint J* acyclic; 0/370 triples viable). Bounded recovery census absent-pattern. No independently auditable alternative; CLEAN_EXIT per output/target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Exact rational full-subcomplex homology and Hochster census (output/artifacts/verify.py -> VERIFY_OK) prove absence of the required supports on the fixed chain W10 and in bounded random stacking-word censuses; the C4 impossibility is argued via stacking-as-triangle-clique-sum preserving chordality. No proof of the positive bracket claim; no emergent finding claimed (candidate lemma = known folklore).

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Exact rational full-subcomplex homology and Hochster census (output/artifacts/verify.py -> VERIFY_OK) prove absence of the required supports on the fixed chain W10 and in bounded random stacking-word censuses; the C4 impossibility is argued via stacking-as-triangle-clique-sum preserving chordality. No proof of the positive bracket claim; no emergent finding claimed (candidate lemma = known folklore).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
