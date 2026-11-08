# Scientific review: exact Gaussian two-sided tangent risk

## Correctness — PASS

The deterministic identity \(E=QN+NR^{\mathsf T}-QNR^{\mathsf T}\) is verified by exact matrix algebra. Its three terms are orthogonal under the Frobenius inner product. Independent Gaussian regression reduces their squared expectations to an inverse-Gram trace; an explicit chi-square regression argument gives \(r/(\ell-r-1)\), with divergence at smaller sketch dimensions. The product contribution follows by independence and successive conditioning. Finite and infinite moment statements are distinguished, and exact rational tests plus seeded simulations reproduce the noncritical cases. The simulations are not a proof of the universal result.

## Originality — PASS (best-knowledge, qualified)

The closest primary numerical-method source is Carrel–Grigori (arXiv:2607.03402, the oblique tangent projection and low-rank-compatible analysis). It provides the target projector and qualitative normal-residual mechanism, but not the stated sharp Gaussian second moment, exact integrability threshold, or fixed-ratio nonvanishing limit. Niu et al. (arXiv:2605.24955, Section 3) treat *sampling*-induced one-sided projection bias and variance, rather than independent Gaussian sketches applied to two sides of a tangent projection. Halko–Martinsson–Tropp (2011, Proposition 10.2) provide the classical Gaussian pseudoinverse moment, which is a necessary ingredient but not the two-sided orthogonal error decomposition. published-finding corpus, accessible historical records, and targeted literature searches did not identify an already stated stronger result. This is not a priority guarantee; an older implicit or published derivation remains possible.

## Value — PASS

The exact law turns a qualitative instability warning for oblique dynamical low-rank projection into a sharp, quantitatively interpretable local risk test. It separates integrability failure at minimal oversampling from a persistent variance floor at fixed sketch/rank ratios. The fact that this floor already appears for a rank-one normal component matters to choosing sketch dimensions: low normal-component rank by itself does not imply diminishing Gaussian mean-square projection error when \(\ell/r\) stays bounded. The result does not assert an integrated dynamics theorem.

## Scope and limits

All assertions are instantaneous, fixed-state, exact-arithmetic, and for independent Gaussian sketches. General sketch distributions, adaptivity and global solver stability are not addressed. The elementary inverse-Wishart ingredient is classical; priority against an older two-sided projector-risk formulation is not fully resolved.

Self-review: passed. Independent audit: not yet performed.
