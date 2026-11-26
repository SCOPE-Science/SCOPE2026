# Independent mathematical audit

## correctness

PASS

For a deterministic SPD problem and a nonterminal Lanczos step, the Gaussian images of the basis and residual direction are independent. The sketched matrix is T plus a last-column rank-one update. Its terminal coefficient solves (1+D)Q=c with c the nonzero signed product of the Lanczos subdiagonals divided by det T. After a column rotation toward T^{-1}e_k, projecting out k-1 columns leaves s-k+1 Gaussian directions; the scalar regression is eta times an independent standard normal divided by a chi variable of those degrees of freedom. The resulting scaled Student density is continuous and positive at -1. The symmetric small interval defining |Q|>R has length 2|c|/R; integrating its density gives the stated constant and the moment cutoff. The vector error is at least the absolute error in that coordinate, and subtracting its deterministic exact-solution value does not cure divergence. At beta=0 full sketch rank gives the original invariant-subspace inverse. This checks the proof also at s=k (one residual degree of freedom); it does not extend to conditioned sketches, finite arithmetic, or harmonic projection. Read VERIFICATION.md and verify.py; their reported rational tests and scalar quadrature are corroboration, not a fresh replay or a proof of the Gaussian law.

## originality

FAIL

A distinct indexed October 26 finding gives the complete same-method random vector, including the Gaussian-regression law and the same rank-one pole. Projecting its formula on e_k gives exactly the frozen law for all admissible k,s; a one-dimensional density limit yields the stated coefficient. Its stronger energy-error moment cutoff implies the Euclidean divergence by SPD norm equivalence. This is demonstrated current coverage, not evidence that the October 26 record preceded the October 13 record. The October 13 one-step record alone does not cover k>=2.

## value

PASS

As a mathematical statement the error barrier is informative: it isolates why even a well-conditioned SPD problem can have infinite unconditional mean inverse error at every finite oversampling despite high-probability guarantees. The decision against the frozen finding is due to existing coverage, not lack of a meaningful stability question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
