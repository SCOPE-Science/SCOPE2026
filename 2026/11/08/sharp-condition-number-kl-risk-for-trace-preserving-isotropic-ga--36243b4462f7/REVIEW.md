# Scientific review

## Correctness — PASS

The claim is the exact finite-dimensional supremum of the **forward** Gaussian KL divergence for a trace-matched isotropic covariance. Its spectral formula is the standard Gaussian identity. A new one-variable derivative polynomial has one positive zero because its derivative is strictly positive, via \(BT\ge(n-1)^2\), so each maximizing covariance eigenvalue must lie at a condition-number endpoint. The finite discrete maximization then follows exactly. The continuous optimizing fraction is unique by a single sign change of its derivative. The large-condition-number coefficient and the simple envelope follow from direct finite-sum asymptotics and the Kantorovich/Jensen inequalities. Deterministic reproducibility tests passed. Risks: an error in the cubic derivative or the KL orientation would be critical; both were explicitly recomputed and tested. Finite tests are not a proof.

## Originality — PASS, subject to priority uncertainty

The closest source is Fifen–Karambal–Hennig, arXiv:2609.10080, Section 4.3 and Theorem 13. It supplies the trace-preserving isotropic covariance and a general quadratic-in-condition-number KL bound but not the exact endpoint-spectrum optimizing multiplicities, the finite-dimensional sharp function or the linear large-contrast coefficient. The Kantorovich inequality controls one term of the exact divergence formula but does not determine the competing logarithmic term, so it cannot directly imply the discrete sharp bound. General Gaussian KL approximation literature has different variational targets. Searches of relevant published claims and accessible prior records did not reveal a covering theorem; priority uncertainty in classical spectral-entropy inequalities and inaccessible full texts remains.

## Value — PASS

The trace-preserving isotropic covariance is a natural computational surrogate in Krylov-complement uncertainty models. A sharp error certificate for a fixed condition-number budget, with equality spectra and the dimension-dependent high-contrast coefficient, is materially stronger than a loose quadratic estimate. It identifies precisely which spectral mixtures make isotropization worst and supplies a reproducible benchmark for numerical approximations. This is a standalone numerical-linear-algebra conditioning result, not a proposed complete Lanczos solver or a general stochastic convergence theorem.

## Limitations

The theorem concerns the unrestricted class of SPD complement covariances, not the smaller set realizable by any fixed Lanczos process. The forward KL orientation and trace-preserving scalar are fixed. Historical priority remains subject to broader published Gaussian information-geometry literature. Only the accompanying self-review was performed; no independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
