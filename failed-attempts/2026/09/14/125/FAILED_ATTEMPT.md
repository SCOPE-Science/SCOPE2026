# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Does weak square plus GCH plus full reflection off the cofinality imply a Souslin tree at the successor of a singular?
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20131
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Set Theory
- **Method:** forcing iteration and morass construction techniques

## Problem

Assume GCH and square-star at aleph_omega. Assume moreover that every stationary subset of E^{aleph_{omega+1}}_{!=omega} = {alpha < aleph_{omega+1} : cf(alpha) != omega} reflects (i.e. for every regular Theta < aleph_omega with Theta != omega, every stationary S subset of E^{aleph_{omega+1}}_Theta reflects at some beta < aleph_{omega+1}). Must there exist an aleph_{omega+1}-Souslin tree?

## Attempted claim

Assume GCH and square-star at aleph_omega. Assume moreover that every stationary subset of E^{aleph_{omega+1}}_{!=omega} = {alpha < aleph_{omega+1} : cf(alpha) != omega} reflects (i.e. for every regular Theta < aleph_omega with Theta != omega, every stationary S subset of E^{aleph_{omega+1}}_Theta reflects at some beta < aleph_{omega+1}). Must there exist an aleph_{omega+1}-Souslin tree?

## Research outcome

Proved YES: GCH plus weak square at aleph_omega implies diamond and hence a Souslin tree at aleph_{omega+1}, so the target hypotheses with added off-omega reflection also imply one.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: B2 misstates Zeman: full-text Theorem 0.3 and Proposition 1.5 prove diamond(T) from 2^kappa=kappa+ + square-star only for T subset of E_cf with stationarily many reflection points. DRAFT applies it unconditionally to E_omega and never establishes reflection there. Target reflection is on the opposite piece E_{!=omega}, so it does not supply the missing premise. Rinot survey Thm 1.12 reports it is consistent that GCH+square-star holds while diamond_S fails for a non-reflecting S in E_cf, so the headline GCH+square-star => full diamond is false as stated. Gluing lemma and stationarity facts are locally valid but premise B2 is unproved. originality: The valid components are prior published theorems: Shelah off-cf diamond (Diamonds 2010 / Thm 1.8) and Zeman reflecting diamond (2010, Thms 1.10-1.11). The only novel step, unconditional diamond on E_omega and hence full diamond from GCH+square-star alone, is invalid and drops the published reflection hypothesis, so it is a repackaging/misattribution, not a new theorem. Schimmerling's question and the Brodsky-Rinot 2019 partial answer (needs a non-reflecting set) predate and subsume the topic. value: The headline YES answer is unproved and in its stated stronger form (GCH+square-star => full diamond) is refuted by the cited consistency result, so no retrievable exact fact is established. Remaining correct fragments (E_theta stationarity, diamond-gluing lemma, textbook diamond=>Souslin sketch) are standard exercises. The target question remains open; no independently valuable invariant, witness, or boundary is contributed.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The proofs of the three cited black boxes (Shelah Diamonds 2010, Zeman Diamond-GCH-weak-square 2010, Jensen diamond-implies-Souslin) are not reproduced; the first two statements were verified at published-abstract level because the full-text acquisition for the Zeman DOI failed, and the third is a standard textbook theorem whose construction is only sketched.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
