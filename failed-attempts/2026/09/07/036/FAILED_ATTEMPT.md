# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Triple-verified insertion-encoding census to n=9 and a new insertion-code certificate for the Le-hard length-4 pair (1342,2143)~(3142,2341)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 55
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** insertion-encoding generating-tree enumeration with transfer-matrix cross-check and brute-force pattern-matching replay

## Problem

For canonical representatives of unordered pairs {p,q} of classical patterns of length 4 (276 pairs modulo reverse/complement/inverse), compute a_n(p,q)=|Av_n(p,q)| for n<=9 by three independent deterministic counts (truncated insertion-encoding generating tree; truncated transfer-matrix over insertion codes; brute-force pattern matching over n! perms), cluster pairs by vectors (a_0..a_9), and certify the Le-hard equivalence (1342,2143)~(3142,2341) by an explicit insertion-code active-site isomorphism sketch that is machine-checked bijective and avoidance-preserving for n<=9.

## Attempted claim

Triple-verified census to n=9 shows a_ n(1342,2143)=a_n(3142,2341) for all n<=9 by three agreeing methods, and an explicit insertion-code relabeling preserving active-site profiles gives a bijection Av_n(1342,2143)->Av_n(3142,2341) checked bijective and avoidance-preserving to n=9, yielding a new insertion-encoding proof sketch of this Le-hard Wilf-equivalence distinct from Le's block bijection.

## Research outcome

Delivered fallback census: first triple-verified (tree vs code vs brute) deterministic table a_n for all 56 symmetry-distinct length-4 pairs to n=9 with replay, confirming Le-hard (1342,2143)~(3142,2341) to n=9 (31192) and second Le pair to n=9 (25252) by a disjoint method; documented failure of simple max-insertion active-site isomorphism (trees non-isomorphic). Honest finite-n claim only.

## Why this attempt failed

Failed axes: originality, value.

originality: Live retrieval decisively anticipates the mathematical content. Le (Electron. J. Combin. 12(1) R25, 2005) proves for ALL n that |S_n(1342,2143)|=|S_n(3142,2341)| and |S_n(1342,3124)|=|S_n(1243,2134)| by block bijections plus a generating function for the former, completing the Wilf-classification of length-4 pairs. The DRAFT fallback finite-n equalities to n<=9 (31192=31192, 25252=25252) are strict corollaries of Le's infinite theorems, not new facts. The 38-vector clustering to n=9 is an empirical truncation implied by Le's classes (DRAFT itself calls coincidence a conjecture, not a theorem). Kremer-Shiu (Discrete Math. 268, 2003) already gives finite transition matrices for a subset of length-4 pairs, the direct predecessor of the transfer-matrix/Code-enumeration cross-check. Vatter (arXiv:0911.2683) and Bean et al. (arXiv:2312.07716) establish the regular-insertion-encoding framework and its limits (height<=2 POPs rational; classical length-4 pairs generally irregular), so the DRAFT's truncated n<=9 use without rationality claim is a deliberately weakened application, not a new encoding theorem. The originally promised novelty (ii) -- an explicit insertion-code profile-preserving isomorphism for the Le-hard pair -- is documented in DRAFT Section 5 as failing (rank maps fail at n=4, max-insertion trees non-isomorphic to depth 6, no general bijection claimed). What remains as arguably new is only the provenance artifact: a triple-agreement CSV+code bundle. A new replay bundle for already-proved equalities is verification, not a substantively new combinatorial result under live-literature comparison. value: Even taking correctness for granted and treating the CSV bundle as new provenance, the result is not independently worth finding later. Le already closed the infinite classification with proofs, bijections, and a generating function; a finite truncation to n<=9 adds no formula, no infinite bijection, no rationality/automaton, and no extension to n>=10 or longer patterns (n=10 explicitly not run). The 38 finite-n clusters are unexplained enumerations by DRAFT's own admission (conjecture, no proof that they equal Wilf-classes; equality to n=9 does not imply equality for all n). The envisioned reusable insertion-encoding certificate failed for max-insertion and other encodings were not searched, so no transferable bijection method is delivered -- the reusable remainder is textbook brute-force enumeration regenerable in seconds (~15s on 32 cores per DRAFT). This falls squarely under the reject categories: unexplained enumeration, tiny unmotivated finite gain over a closed classification, and mere parameter-substitution-style recomputation, which must be rejected even if correct and new. A future researcher seeking Wilf-equivalence would cite Le's theorems, not a n<=9 table.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Finite-n only (n<=9); n=10 (3.6M perms) not run. Equality to n=9 does not prove Wilf-equivalence for all n (that remains Le 2005). No general insertion-code bijection delivered; max-insertion relabeling proved to fail as documented; other encodings unsearched. Correctness rests on three code paths (distinct generators/checkers) not formal proof; common-spec error possible but mitigated. 38 clusters are finite-n, may in principle split later (though stable 8->9). No automaton/rationality claim (…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
