# Self-review

## Correctness

**PASS.** The theorem is a fully quantified exact-arithmetic statement about all integer block sizes at least two, strict positive equicorrelation, positive regularization and replicated training centers. The three orthogonal subspaces exhaust the ambient dimension, give every generalized eigenvalue with multiplicity, and permit a direct min-max proof of a lower bound valid for *every* positive semidefinite rank-one denominator correction. A scalar global update attains the lower bound on the proven closed tuning interval. The example and parametric formulas were checked by the standalone verifier (4,216 assertions, including exact symbolic spectra). Finite tests do not serve as an infinite proof.

## Originality

**PASS, with priority uncertainty.** The motivating BLOKS paper provides the block-sketch construction and proposes future coarse corrections; its relevant algorithm and Appendix B do not state the exact sharp one-rank positive correction classification. General coarse-space methods and block-Jacobi scaling results address related but nonidentical optimization operators. Existing spectral interlacing is a known ingredient, and an older general theorem may subsume a portion of the derivation. No claim is made that rank-one correction or the min-max principle itself is new.

## Value

**PASS.** The all-parameter optimum directly addresses inter-block coupling in a newly proposed memory-bounded kernel preconditioner. A fixed-rank, constant-cost correction changes a growing condition number into a fixed-block-width bound; the proof establishes sharpness among arbitrary positive semidefinite rank-one additions, not just within a convenient tuned family. This is a structured spectral benchmark, not a claim about broad runtime improvements.

## Closest literature and limits

Vitale et al., arXiv:2610.13382; Xu–Zikatanov, arXiv:1611.01917; Demmel, DOI:10.1137/22M1504901. The comparison with the latter two is constrained by the full material accessible from their abstracts and summaries. The theorem does not cover heterogeneous blocks, partial random sketches, numerical roundoff, general kernels or actual prediction error. Independent mathematical audit is not performed.

Self-review: passed. Independent audit: not yet performed.
