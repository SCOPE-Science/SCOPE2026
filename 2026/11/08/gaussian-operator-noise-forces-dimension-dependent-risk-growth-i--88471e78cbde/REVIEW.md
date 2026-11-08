# Review of Gaussian fixed-operator risk for a damped scalar Fourier mode

## Correctness — PASS

For the one-row scalar specialization of the stated SD-TRK scheme, geometric-series summation gives the exact iterate \(X_t=(B/A)F_t(A)\). The damping ratio stays strictly between zero and two, establishing almost-sure convergence to \(B/A\). With a zero floor the positive one- or two-dimensional Gaussian density at the origin forces \(\mathbb E|A|^{-2}=\infty\). With a positive floor, a uniform small-denominator estimate gives finite risk at each finite iteration, and elementary Gaussian integral asymptotics produce the real-mode \(\sqrt t\) constant and complex-mode \(\log t\) constant. The target offset is negligible by Cauchy–Schwarz. A standalone verifier tests finite recurrences and the two integral asymptotics; those numerical tests are not substituted for the universal analytic proof.

## Originality — PASS, with historical-priority risk

The most relevant primary source is Lee–Choi, arXiv:2607.13552, Theorem 4.2, Algorithm 1 and Eq. (4.9), read in full HTML form. It analyzes expected row sampling conditional on fixed noisy tensors and supplies a spectral damping prescription. It does not integrate over the Gaussian operator ensemble to obtain the precise real/complex risk growth. Bergou et al., arXiv:2308.16904, analyze observed matrix pseudoinverse sensitivity; Elfving (2024) treats fixed-operator data noise; Ma–Molitor, arXiv:2006.01246, treat noiseless tensor iterations. An equivalent statement might exist in older small-denominator or spectral-regularization theory despite no direct match in the inspected sources. No claim of exhaustive literature novelty or independent validation is made.

## Value — PASS

The published algorithm uses a strictly positive damping floor specifically to stabilize weak Fourier slices. This theorem sharply separates finite-iteration regularization from all-iteration ensemble risk, quantifies the rate of its failure, and distinguishes DC/Nyquist (real) from interior (complex) Fourier modes. It gives a concrete model in which increasing the adaptive scale coefficient cannot cure the leading risk, motivating finite-horizon stopping or a genuinely persistent bias penalty. The theorem is intentionally a structural boundary for a minimal case, not a blanket claim about higher-dimensional tensor solvers.

## Scope and outstanding limitations

Only a fixed-data scalar Fourier mode, Gaussian observed operator with positive density at zero, finite-variance independent right-hand side and constant iteration parameters are covered. Prior probabilistic inverse-problem literature may contain an implicit equivalent, especially for the one-dimensional integral. The explicit two-dimensional Fourier contrast and fixed-floor constants were not identified in the compared primary texts. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
