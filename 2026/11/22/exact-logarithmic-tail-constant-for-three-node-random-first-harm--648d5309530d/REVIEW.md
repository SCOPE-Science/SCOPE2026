# Self-review

## Correctness — PASS

The exact sine formula for the normalized trigonometric interpolatory weights follows from the three moment equations and the triple-half-angle identity. The independent-uniform cyclic gaps have constant density \(1/(2\pi^2)\) on their simplex. On each of its three pair-collision corners, the leading homogeneous weight norm is \(2\sqrt{2(x^2-x+1)}/[r^2x(1-x)]\). The Jacobian integration yields the sharp corner area coefficient \(2\sqrt2\) for \((\log T)/T\); three identical corners and the density give \(3\sqrt2/\pi^2\). Away from the corners the probability is only \(O(T^{-1})\). The squeeze is uniform at the corner endpoints and the cutoff tends to zero after the large-threshold limit. The moment and noise conclusions follow by exact identities. Finite diagnostics are supplemental, not an infinite proof.

## Originality — PASS with stated residual risk

The claimed contribution is the exact leading coefficient for the **normalized three-weight quadrature functional** under independent full-circle sampling. Existing published results establish a logarithmic order bound for the **entire Fourier inverse-Frobenius norm**, not its exact coefficient; that published proof explicitly does not claim a leading constant for its own full-matrix norm. Another published first-harmonic quadrature result treats independently perturbed *stratified* points and yields a distinct endpoint-noise regime. The 2026 randomized least-squares quadrature paper concerns high-probability weight concentration with adequate sampling, not the fixed three-point unsafeguarded rare-tail constant in its accessible introductory summary. The Xu–Shen paper studies expected full-spectrum risk divergence rather than the exact scalar quadrature-functional coefficient in its accessible abstract. Broader inversion results do not imply the constant because norm comparisons have nonsharp multiplicative factors. Equivalent unindexed special-purpose formulas remain a priority risk. The first primary paper's later sections and the Xu–Shen full text were not accessible for exhaustive comparison.

## Value — PASS

Three angles are the minimal nontrivial interpolation design exact on a constant and both first harmonics. The exact tail coefficient, not merely a divergence assertion or polynomial tail exponent, gives a quantitative asymptotic probability for catastrophic observation-noise gain in the natural unstratified design, allowing sharp comparison with stable, jittered, or oversampled rules. It is a structurally motivated exact invariant of a common numerical quadrature construction, not an arbitrary parameter slice. The result is not an all-sample-size random quadrature theorem.

## Limitations and literature

References and full derivation are in `RESULT.md`. The comparison is bounded by available text, particularly for arXiv:2609.09506 and arXiv:2609.29286. The core proof is mathematical; the attached diagnostic script has no exhaustive or asymptotic-certification role. There has been no independent audit.

Self-review: passed. Independent audit: not yet performed.
