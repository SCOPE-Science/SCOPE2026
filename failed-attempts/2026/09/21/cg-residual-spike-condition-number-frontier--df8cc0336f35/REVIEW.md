# Review status

Mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: PASS. The package proof is valid: the CG--Lanczos \(LDL^T\) factorization identifies the relevant residual multiplier in a trailing Schur complement, spectral enclosure is inherited through the inverse principal block, and the sharp two-by-two spectral-interval maximization yields the factor \((\kappa-1)/(2\sqrt{\kappa})\). An independent earlier proof based directly on CG orthogonality plus Kantorovich gives the same bound and equality family. The supplied two-dimensional equality cases and numerical artifact are consistent supporting evidence.

Originality: FAIL. A published 20 September 2026 result, one day earlier, states the same sharp all-step Euclidean residual factor, the same exact universal monotonicity threshold \(3+2\sqrt2\), the same endpoint-eigenspace first-step equality construction, and the same fixed-SPD-preconditioner consequence in the \(M^{-1}\) residual norm. It additionally gives a history-dependent refinement. This is direct prior coverage, not merely a similar parameter computation.

Scientific value: PASS. The exact residual-spike frontier and threshold are useful structural facts for conjugate gradients. The scientific rejection is originality only.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
