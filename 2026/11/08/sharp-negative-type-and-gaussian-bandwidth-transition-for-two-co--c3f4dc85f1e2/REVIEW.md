# Scientific review

## Correctness
The rank-one character sum follows from the exact multiplicity \(q-1\) of a nonzero outer product and finite-field orthogonality; the rank-two transform is forced by completeness of the character sum. Each eigenvalue and multiplicity is listed in RESULT.md. The strict convexity of \(1-(q+1)z+qz^{2^\alpha}\) proves both the existence/uniqueness of the interior root above the critical exponent and positivity below it. Conditional-negative-type signs and endpoint centered-Gram ranks are obtained from the same two nontrivial Fourier sectors, without extrapolating finite tests. `check_rank_kernel.py` passed exhaustive character checks on three prime-field matrix spaces and one extension-field space and six further parameter inequalities; finite evidence supplements rather than substitutes for the proof.

## Originality
Delsarte (1978), Appendix, already determines the generalized Krawtchouk Fourier characters of rank spheres; Gadouleau–Yan (2007) covers rank-metric MacWilliams transforms. Meckes (2010), Theorem 3.3, establishes the general connection between negative type and positive definite exponentials. These imply the *method* but do not state the two-column sharp field-dependent exponent, entire bandwidth phase diagram and endpoint squared-Euclidean embedding rank as a single exact classification. The result is framed as an explicit specialization, not as a new rank-sphere transform. An unlocated exact corollary in older association-scheme or Schoenberg literature is a residual originality risk.

## Value
The full two-column rank-distance space is the natural diameter-two case of the bilinear-forms association scheme. Gaussian rank-distance kernels are not automatically valid positive-definite kernels. The exact exponent reveals when the entire scale family is valid and the exact positive bandwidth beyond which an otherwise invalid kernel becomes usable. A large drop in minimal squared-Euclidean embedding dimension occurs exactly at the sharp exponent, where an explicit projective-line Hamming decomposition realizes that optimal embedding without spectral numerics. The dimension-independent boundary and nullspace multiplicity describe a motivated geometric invariant for all fields and row counts, not a one-off finite tabulation.

## Scope and integrity
The theorem does not address three or more columns, arbitrary rank-metric subcodes or the positivity of kernels beyond the specified powers. External independent validation has not been performed. Previous general character-table results are credited, and originality is asserted only for the exact specialized phase diagram under the documented bounded comparison.

Self-review: passed. Independent audit: not yet performed.
