# Scientific review: Sharp diameter and rigid extremizers of binary rank-two code distortion

## Correctness (C): PASS

The new theorem is proved for every integer \(n\ge2\), with the exceptional \(n=2\) value handled separately. A rank-two binary isomorphism can realize all six matchings of nonzero words; an uncrossing lemma proves the sorted matching optimal. Pairwise ratio bounds give \(\mathcal D\le n\). Equality in the bounds forces a weight-one/all-one pair in one code and equal nonzero weights in the other. Exact generator-column multiplicities establish the claimed \(t\)-range and the complete equivalence-class count. The proof handles zero columns and repeated weights. `verify.py` was executed from the complete package path and returned `CHECK_OK` after 21,096 generator checks and 19,902 exact-rational pair checks. Finite checks are not treated as a proof of the infinite assertion.

## Originality (O): PASS with residual risk

Closest primary literature: H. Bennett, M. Fox, and B. Morrell, *The Code Distortion Problem* (2026, arXiv:2607.26261; DOI:10.4230/LIPIcs.APPROX/RANDOM.2026.24). Its Lemma 15 gives the general \(n^2\) bound, Lemma 27 gives an exact algorithm per input pair, Corollary 28 handles low dimension computationally, and Proposition 19 treats distortion one. The new statement instead determines a sharp maximum over **all** binary dimension-two code pairs for **every** block length and lists the exact extremal classes; none of those prior statements gives this conclusion. The source's example optimizes one pair but does not determine the diameter. Bennett and Win (IACR 2024/782) treat reductions for code equivalence rather than distortion. Search comparisons included alternate weight-spectrum, projective-metric, code equivalence and sharp diameter formulations in published-finding corpus, accessible literature and the previously available mathematical records; no dominating result was found. These comparisons do not certify uniqueness of discovery, and unindexed earlier coverage remains possible.

## Value (V): PASS

A sharp global diameter is a natural invariant of the code-distortion problem, not an arbitrary small instance. The new work improves the general numerical \(n^2\) ceiling to an attained \(n\) bound for all binary rank-two codes and completely classifies the equality families. The Hilbert-projective weight-profile identification supplies a structural explanation for both efficient evaluation and equality rigidity. This is an exact baseline for coding-theoretic metric embeddings and for testing more general distortion bounds.

## Scope and limitations

The result concerns binary linear codes of dimension exactly two with arbitrary zero coordinate positions; it does not address other alphabets, larger dimensions or full-support-only extremizers. Independent audit has not been performed. The checker is only corroborating finite evidence and historical priority has a stated residual risk.

Self-review: passed. Independent audit: not yet performed.
