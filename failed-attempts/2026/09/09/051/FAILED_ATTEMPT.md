# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** SW-versus-d-invariant exoticity test for a small closed twist pair built from a new Stein infinite-order cork
- **Round:** 2026-09-07-first-light-01
- **Lane:** 406
- **Disposition:** AUDIT_1_REJECT
- **Domain:** 4-Manifold Topology
- **Method:** cork-twist surgery with Seiberg-Witten adjunction inequalities and Heegaard Floer correction-term comparison

## Problem

Let (C,f) be the lowest-diagram-complexity member of the infinite-order Stein cork family of Teng arXiv:2608.17462 Theorem 1.1. Embed C in a small closed simply connected 4-manifold X with b2<=3 via the Akbulut-Yasui enlarging/closing recipe and let X^tau be the cork twist by f. Decide whether the twist changes smooth structure.

## Attempted claim

The closed simply connected 4-manifolds X and X^tau defined above are homeomorphic but not diffeomorphic, witnessed by a Seiberg-Witten basic-class versus Heegaard Floer d-invariant mismatch across the twist; in the alternative, the boundary involution f extends to an explicit diffeomorphism X -> X^tau given by a logged handle-slide sequence.

## Research outcome

Certified adjunction exclusion of K0=(-3,1,1) on the closed Teng-cork twist X^tau via connected Sigma(g=2,n=14) with |K0(S)|+S^2=24>2=2g-2 (VERIFY_OK), plus chamber-correct oriented reading and K0^perp chamber-independence; full-target exoticity not closed (X-side basicness needs symplectic-closing detail). Target was pursued for the full gate before switching to the exact preset fallback.

## Why this attempt failed

Failed axes: correctness.

correctness: Arithmetic layer verified: re-ran inputs/artifacts/verify.py -> VERIFY_OK and hand-rechecked Q=diag(1,-1,-1) det=+1 sig=-1, K0=(-3,1,1) characteristic K0^2=7 dim 0, S=(4,-1,-1) S^2=14 K0.S=-10, raw sum 24>2 vs 2g-2=2, oriented demand S^2+K.S=4 vs 2g-2=2 (g=2 fails, g=3 passes), chamber signs Om=(10,-1,-1) Om^2=98 K0.Om=-28 S.Om=38, S-perp Gram [[-15,1],[1,-15]] neg-def, K0-perp Gram [[-8,1],[1,-8]] neg-def, orbit 28 classes, mirror, degree table. Linear algebra for chamber-independence (K0^2>0 => K0-perp misses positive cone) is sound. BUT essential topological inferences unproved: (1) Headline invokes absolute adjunction |K.S|+S^2>2g-2 at b2+=1 where it is invalid -- DRAFT itself admits absolute form needs b2+>1 and host has b2+=1. The exact_success_criterion literally demands this invalid form, so literal fallback criterion is unsound here; oriented fix 2<4 is a different inequality requiring chamber/period hypotheses. (2) X^tau existence with stated Q/pi1/closing not proved: diagram_log gives schematic gamma_i/replay-aid words, no explicit framings/linking proving Q; handle inventory gives Euler 1-1+4-1+1=4 vs claimed chi=5 for closed simply-connected b2=3 (2+3), so Q rank 3 incompatible with logged inventory -- need 5th 2-handle or corrected rank. verify.py asserts chi=2+3 by fiat. pi1-killing and upper-boundary S^3 (Perelman invocation) asserted, not proved. (3) Sigma genus-2 existence in class S on X^tau not proved: surface_log compression narrative (push quartic Sigma_3 g=3 off cork into collar, compress once to g=2 preserving [Sigma]) is explicitly labelled replay-aid/conditional on Fig-level isotopy; no embedded compressing disk exhibited, no transversality/class-preservation proof; DRAFT Limitations states trail complete only conditional on logged existence. verify.py certifies integers only, not embedding. Since existence of g=2 representative in class 4H-E1-E2 on a CP^2#2bar-homology manifold already implies exoticity (standard rational surface needs g>=3 by same bound), the unproved surface carries all content -- result is conditional lemma IF-surface-THEN-exclusion, i.e. partial completion, not exact unconditional fallback. Proof vs computation separated accordingly.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Cited-not-reproved: SW adjunction theorems, Freedman, Gompf/Teng/Akbulut-Yasui inputs. Replay-aid (not finding): Fig-level isotopy for Sigma(g=2) existence; audit trail complete conditional on that logged existence claim. Not claimed: full exoticity (needs X-side basicness), minimal-genus bounds, full basic-set classification, contactomorphism status, C_m transfer.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
