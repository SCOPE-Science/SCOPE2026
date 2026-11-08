# Scientific review

## Correctness — PASS

The mathematical claim covers exactly integer bases \(b\ge3\) and lengths \(n\ge2\). It is derived by an exact marker reconstruction, not extrapolation: each substitution block has only its terminal position variable, so a factor with prescribed endpoint one has a forced residue and its full length-\(m\) parent word is recovered by reading markers. This proves both equivalences of occurrence sets. The construction of the two unbordered factors is justified by the already-published reversal and unborderedness lemmas, and their uniqueness is explicitly attributed to Goč–Mousavi–Shallit's full generalized-base theorem. Exact valuation-class densities justify the asymptotic frequency; absence of adjacent ones justifies the entire short/long gap sequence. Boundaries \(n=2\), \(n=b\), \(d=0\) and \(d=b-1\) are included. The independent finite verifier passed 537764 counted occurrence comparisons and 56 complete short-length classifications. The code is corroboration, not a substitute for proof.

## Originality — PASS (with residual bibliographic risk)

Goč–Mousavi–Shallit (2012), Section 5, directly covers the same word family and proves exactly two unbordered factors per length, but not their all-position affine sets, first starts, densities or return gaps. Their factor recurrence is a prerequisite rather than the new conclusion. Huang–Wen (2016) is a stronger **binary-base** return-word result, so no claim is made to new coverage at base two; their results as read do not supply a multibase theorem. Spiegelhofer's (2021) gap result is about Thue–Morse rather than the generalized period-doubling family, and Currie (2023) treats forbidden binary patterns. Semantic mathematical-record searches found a period-doubling attractor theorem and a period-doubling subshift-lift theorem with different objects or invariants, not equivalent coverage. Full-text comparison focused on explicit implication; an unindexed generalized-base return-word classification remains the main risk.

## Mathematical value — PASS

A complete exact occurrence-position and return-gap spectrum for both unbordered factors at **every length and every generalized base** is a natural refinement of the established two-factor count. The result identifies a single normalized gap sequence independent of length or orientation, gives all first positions constructively, and computes exact natural densities and long-gap proportions. These structural identities provide testable recurrence information not contained in the cardinality statement. The base-three-and-up restriction deliberately avoids the already studied binary case.

## Limitations and comparisons

The 2012 count and key unborderedness lemma are borrowed and credited. Finite diagnostics do not establish infinite uniqueness or prove novelty. The theorem is not a classification of arbitrary bordered factors, and no independent scientific validation has been performed. Related primary full text and precise provenance are recorded in the companion result and audit.

Self-review: passed. Independent audit: not yet performed.
