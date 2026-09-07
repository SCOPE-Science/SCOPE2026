# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact Davenport constant of C3 x C3 x C6 with certified extremal witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 40
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Additive Combinatorics
- **Method:** SAT/ILP extremal-sequence search with Olson-type invariant pruning and explicit zero-sum verification tables

## Problem

Determine the Davenport constant D(G) for G=C3 x C3 x C6 (presented as Z3 x Z3 x Z6, order 54, exponent 6, invariant factors 3|3|6, D*=1+(2+2+5)=10) exactly: exhibit an explicit zero-sum-free sequence S of length D-1 and a machine-checkable certificate that every sequence of length D over G contains a nonempty zero-sum subsequence.

## Attempted claim

D(C3 x C3 x C6)=10 (=D*): the canonical 2+2+5 basis sequence of length 9 is zero-sum-free (with full subsequence-sum verification table), and no zero-sum-free sequence of length 10 exists, certified by a SAT/ILP UNSAT log (DRAT) with Olson-type pruning that replays deterministically in minutes on one core.

## Research outcome

Closed the flagged rank-3 mixed entry: D(Z3xZ3xZ6)=10 with explicit length-9 witness (full 511-row verification table) and complete machine-checkable proof that no length-10 zero-sum-free sequence exists (84.9M-node sorted-multiset exhaustion in ~3 s, replayable in one command).

## Why this attempt failed

Failed axes: originality.

originality: Live retrieval defeats novelty. Nearest prior Bhowmik & Schlage-Puchta (2007) 'Davenport's constant for groups of the form Z3(+)Z3(+)Z_{3d}', CRM Proc. 43 pp.307-326, DOI 10.1090/crmp/043/17, studies the exact infinite family containing the candidate: d=2 gives Z3xZ3xZ6. Biswas & Mazumdar arXiv:2402.09999 (2024, published Math Notes 118:23-34, 2025) 'Davenport constant for finite abelian groups with higher rank', which itself studies G=(Cp)^{d-1}xC_{pq} (p=3,q=2,d=3 is exactly the candidate), states verbatim 'It is already known that D(G)=D*(G) for the groups C3xC3xC_{3s} for any positive integer s ([BP2])' where [BP2] is Bhowmik 2007. With s=2, C3xC3xC_{6} has D*=10, i.e. exactly the candidate theorem D=10=D*. DRAFT Sec.6 omits this family, listing only Olson p-groups, rank-two formula, surveys, and EGZ rank<=2, and claims 'no citable exact entry' and 'flagged open' and 'first certified exact' — false in light of the 2007 family result as summarized in 2024-2025 literature. Substantive comparison: same group, same invariant, same equality D=D*=10 with same canonical witness type; candidate's 84.9M-node DFS is at most an independent recomputation, not a new object, gap, or method. Therefore originality FAIL.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: ['Computer-assisted upper bound depends on enumerate.c correctness and sorted-multiset/pruning lemmas; mitigated by tiny auditable source, independent brute cross-checks, deterministic reruns, single-command replay.', 'No SAT/DRAT log: pivoted to direct enumeration certificate (program + branch-count log) which reruns faster and is simpler to audit; no proof-assistant formalization.', 'No length-9 extremal classification beyond witness and multiset count 9723168; no EGZ constant s(G) determinat…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
