# Scientific review

## Correctness

**PASS.** The underlying invariant is the minimal length of a deterministic unrestricted feedback map for an infinite periodic sequence, not a linear-register length. Two factors with equal previous context and unequal next symbols obstruct that length, and conversely a feedback map may be defined on all contexts with consistent successors. If the two nonzero labels are distinct, a repeated context cannot contain a nonzero label and zero-run lengths give the exact obstruction. If they agree and the two gaps differ, at most one spike can align under a nontrivial rotation; there are exactly two sharp competing obstruction lengths. Equal gaps have separate behavior because matching nonzero symbols halve the primitive period, while distinct symbols do not. Position-pair orbit counts give the polynomial coefficients without multiplicity loss. The executable checker independently evaluated 28,280 words and 60 complete histograms, plus 210 pairwise-phase cases. It does not replace the general proof.

## Originality

**PASS under available evidence; historical-priority risk remains.** The closest recent primary paper, Yuan–Li–Zeng (arXiv:2602.01134), counts all binary periodic sequences only in a high-complexity regime. Yuan–Li–Zeng–Helleseth–He (arXiv:2404.16313) provides algorithms for generating binary sequences with prescribed nonlinear complexity. Neither inspected statement supplies the explicit two-spike multi-alphabet color dichotomy or its generating polynomial. The standard general successor-conflict criterion, used in both, is acknowledged as prior. The 2024 survey reports general maximum-order-complexity criteria and bounds; the available excerpt was inspected, while the full publisher text could not be retrieved. Generic computability of the invariant is not itself an explicit distance/color classification or the counting law. No definitive global priority assertion is made; the strongest risk is an unindexed low-weight specialization in older shift-register literature.

## Value

**PASS.** Hamming-weight-two periodic sequences are a canonical sparse test family for shift-register complexity, and minimal register length is a natural invariant of these sequences. The answer is not a single trivial gap formula: coincident nonzero labels create a second obstruction \(2d\), distinct labels eliminate it, and antipodal equal labels reduce the primitive period. The exact all-parameter polynomial quantifies the entire restricted complexity distribution, allowing comparisons with unconstrained periodic-sequence complexity distributions and furnishing sharp test instances. This does not claim cryptographic strength or a new general bound for arbitrary sequences.

## Closest literature and limits

- Q. Yuan, C. Li, X. Zeng, *The structure and enumeration of periodic binary sequences with high nonlinear complexity*, arXiv:2602.01134 (first submitted February 1, 2026), especially the definitions and high-complexity enumeration in Sections 2, 4 and 5.
- Q. Yuan, C. Li, X. Zeng, T. Helleseth, D. He, *Further Investigations on Nonlinear Complexity of Periodic Binary Sequences*, arXiv:2404.16313 (2024), on generating binary periodic sequences by nonlinear-complexity class.
- *A Survey on Complexity Measures for Pseudo-Random Sequences*, Cryptography 8 (2024), article 25, for the general \(q\)-ary successor-conflict characterization; the available publisher excerpt does not support a whole-document exclusion claim.

The formula classifies exactly two nonzero positions under unrestricted deterministic feedback. It is not a statement about LFSRs, feedback-with-carry registers, or arbitrary Hamming weight. Finite tests do not verify the infinite quantifiers; no independent audit or definitive priority determination has been performed.

Self-review: passed. Independent audit: not yet performed.
