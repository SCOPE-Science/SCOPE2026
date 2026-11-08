# Scientific review

## Correctness — PASS

For every stated dimension and sketch size, the core determinant is a nonzero polynomial. The one-column divergence lemma uses a regular zero of an indefinite quadratic form and integration in the normal coordinate, not a finite experiment or a claim that near-singular samples occur with probability one. For multiple columns, a positive-probability neighborhood of eigenvector-selected partial sketches leaves a positive and a negative direction in the Schur-complement residual, and independent final-column sampling yields infinite conditional moments. At one-column undersampling, the rank-one residual identity, spherical regular-value/coarea formula, and beta pushforward establish all tail and integrability statements. All boundary quantifiers \(n\ge2\), \(1\le k<n\), \(p\ge1\), and \(0<p<1\) have been checked; no sharp general-\(k\) tail coefficient is asserted.

## Originality — PASS, qualified

Park–Nakatsukasa (arXiv:2212.01127, Sections 1–3) supply a deterministic unbounded \(2\times2\) indefinite Nyström example and methods for stabilizing/truncating its core; that example is not claimed as new. Their projected-core expected-error theorem does not apply to the **unmodified** random inverse analyzed here, and their deterministic instability example does not alone establish infinite mean for every Gaussian sketch size. Hillier (doi:10.1017/S026646660117101X) already studies spherical quadratic-form density; that density calculus is credited, not presented as a discovery. Schur-complement algebra (Ouellette, 1981) is background. Actual targeted semantic research-record queries produced no equivalent finding, including aliases for indefinite Nyström, Gaussian sketches, reciprocal quadratic forms, moments and all sketch dimensions. Because a density preprint and some specialist published literature were not inspected in their entirety, publication precedence remains a risk; an absence of search hits does not prove novelty.

## Value — PASS

The result closes a natural decision question for **unmodified** indefinite Nyström approximation: does increasing Gaussian sketch size below full rank rescue the mean error? It does not, for any nonsingular indefinite input. This explains why regularizing/truncating the core is mathematically essential for expected-norm error guarantees, rather than merely a finite-precision convenience. The exact near-full distribution quantifies rare catastrophic errors invisible in typical-case experiments: in the one-positive/many-negative spectrum family, the error even converges in probability to a finite value while retaining an infinite mean for each dimension. These are structurally motivated implications for error-risk assessment, not an arbitrary finite numerical slice.

## Closest literature and limitations

Primary motivation: Park and Nakatsukasa, *Randomized low-rank approximation for symmetric indefinite matrices* (2022), https://arxiv.org/abs/2212.01127. Related but differently scoped theory: Hillier, *The Density of a Quadratic Form in a Vector Uniformly Distributed on the n-Sphere* (2001), https://doi.org/10.1017/S026646660117101X; Ouellette, *Schur Complements and Statistics* (1981), https://doi.org/10.1016/0024-3795(81)90232-9. The result does not treat finite-precision computed cores, regularized/truncated methods, non-Gaussian embeddings, singular matrices, or exact lower-sketch tail coefficients. The cited density work was compared through its 1999 institutional preprint introduction and coarea sections; no claim of exhaustive specialist publication screening is made.

Self-review: passed. Independent audit: not yet performed.
