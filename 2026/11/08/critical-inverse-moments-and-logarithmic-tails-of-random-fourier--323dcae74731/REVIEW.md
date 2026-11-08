# Scientific review: critical inverse moments of random Fourier interpolation

## Correctness — PASS

For each realization with distinct nodes, the columns of the inverse interpolation matrix are the coefficient vectors of the classical Lagrange polynomials. Comparing the leading coefficient and elementary-symmetric coefficient bounds proves the deterministic inequalities between the inverse Frobenius gain and the products of reciprocal nodal chords. Conditioning on one uniform node makes its other chord distances independent, which validates the gamma-function Mellin transform. The logarithms of reciprocal chord lengths have exponentially decaying densities with constant \(1/\pi\); the complete simplex convolution argument gives the sharp logarithmic factor, and deterministic comparisons transfer it to the matrix. The layer-cake identity yields the stated moment threshold and critical truncated expectation. Numerical matrix inversions and direct quadrature independently checked the finite algebraic and integral identities. The asymptotic assertions are analytical, not Monte Carlo inferences.

## Originality — PASS relative to inspected sources

The primary 2026 reconstruction-risk article establishes divergence of the usual expected inverse squared singular-value risk under independent random sampling, but does not report the fixed-dimension sharp Pareto-logarithmic tail or the full fractional-moment boundary. The 2012 Tucci–Whiting analysis provides inverse Vandermonde formulas and nonexistence of integer-order inverse Gram moments; these are prior inputs, not claimed as new. The 2019 clustered-node work gives deterministic bounds rather than an independent-uniform-node probability distribution. The present theorem identifies the exact \(1/2\) moment cutoff, the logarithmic exponent \(n-2\) in the tail, and the explicit nodal-product constants. Bass–Gröchenig (2004/05) gives condition-number probability estimates for trigonometric sampling, but only the publisher preview was accessible. A complete mathematical comparison with that work remains unresolved; its abstract alone does not establish coverage of this fixed-square fractional-moment and logarithmic-tail claim. Known equivalent but unindexed results remain possible.

## Value — PASS

Typical spectral bounds do not specify the integrability of noise amplification under rare collisions. The result gives a complete answer for all fractional inverse-risk moments in square trigonometric interpolation and a sharp logarithmic correction that depends on the number of samples. It also provides an exact Mellin transform and leading tail constants for the nodal denominator controlling the matrix; these are useful for understanding robust, truncated or fractional reconstruction losses. This is stronger than the already-known divergence of ordinary mean-square risk.

## Boundaries and residual risk

The conclusions require independent uniform circular nodes, a square consecutive-frequency interpolation matrix, and fixed dimension in the large-tail limit. The exact leading constant is determined only for the Lagrange nodal-denominator surrogate, not the full inverse-Frobenius gain. Relevant work on small-singular-value clustering does not imply the probabilistic logarithmic degree directly. The inaccessible full Bass–Gröchenig treatment is a particular prior-literature uncertainty, and an earlier unlocated random-Vandermonde tail theorem could cover the conclusion. The scientific proof and checker have not received an independent external audit.

Self-review: passed. Independent audit: not yet performed.
