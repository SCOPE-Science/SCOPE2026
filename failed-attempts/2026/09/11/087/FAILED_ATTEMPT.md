# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Diamond-sealed three-way far family in the rho1-coherent special cell
- **Round:** 2026-09-07-first-light-01
- **Lane:** 910
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Infinite Combinatorics and Set Theory
- **Method:** diamond-sealed coherent-tree diagonal construction

## Problem

Assume diamond on omega1 (or the Brodsky-Rinot proxy instance implying it for this construction). Build three rho1-coherent special Aronszajn trees R0, R1, R2 by sealing potential club-isomorphisms along a diamond guess. Decide whether they are pairwise far: no one contains a subtree club-isomorphic to a subtree of another.

## Attempted claim

Assuming diamond on omega1, the three explicitly diamond-sealed rho1-coherent special Aronszajn trees R0, R1, R2 are pairwise far: for distinct i,j, no subtree of Ri is club-isomorphic to a subtree of Rj; hence the rho1-coherent special cell has club-isomorphism basis number at least 3 and no member is club-universal for the cell.

## Research outcome

Proved diamond-sealed rho1-coherent special triple R0/R1/R2 pairwise far with basis>=3, supported by sealing proof and VERIFY_OK finite ledger.

## Why this attempt failed

Failed axes: correctness.

correctness: Headline far claim (no uncountable downward-closed subtree club-isomorphic to another) is not proved. (1) Sealing omits entire mod-finite class of v: any two one-step extensions of same node differ in one value hence are mod-finite equivalent, so killing whole class can kill entire cone above a predecessor, and prunedness preservation induction is missing. Omitting single v would suffice but is not what is proved. (2) Verification assumes S contains limit u=union(b) because S is downward-closed uncountable. Downward-closed means predecessor-closed, not limit-closed: e.g. Ri minus cone above u (including u) is downward-closed, contains b, misses u. No argument shows genuine S must contain the sealed u. (3) Menu {b_p} picks one branch per node p, but U^i of countable height can have uncountably many cofinal branches; construction cannot cover the branch of an arbitrary future S, so one seal per alpha cannot block a fixed Q=(S,T,phi,C). Whole-tree non-club-isomorphism would follow from single-node omission, but far (subtree) does not. (4) Corollaries A/B apply farness to images of whole-tree embeddings, but images need not be downward-closed, so hypotheses of far do not apply even if far held. Finite verify.py at depth 10 checks keep-source/kill-cone shape only and does not address transfinite closure, prunedness, or limit containment.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Proof assumes diamond on omega1 essentially and cites Todorcevic walk/coherence closure facts as black boxes rather than re-deriving them. The finite script validates only the combinatorial shape of sealing at depth 10, not any uncountable statement; transfinite prunedness induction and limit-in-S arguments are mathematical. Basis bound is for whole-tree club-embeddings as defined in DRAFT.md, not upper-universals outside the triple.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
