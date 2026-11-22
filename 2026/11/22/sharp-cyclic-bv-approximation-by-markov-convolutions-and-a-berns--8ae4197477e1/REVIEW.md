# Scientific review

## Correctness — PASS

The statement specifies real signals, counting-\(\ell^1\), cyclic edge variation, convolution orientation, and the unnormalized heat generator. Stepwise cyclic telescoping gives an upper bound for any probability kernel; every balanced arc simultaneously attains every displacement term. The cut equality argument uses the displacement \(\lfloor n/2\rfloor\) and the exact cardinality barrier to force one run, while strict positivity prevents equality across distinct nested level sets. The Fourier transform of cyclic distance is derived directly from its discrete second differences, giving nonnegative exponential weights and the complete Bernstein derivative sign law. The actual embedded checker passes exact small-size cut tests and independent heat matrix-exponential comparisons. Neither finite enumeration nor floating-point tests are treated as universal proof. Residual mathematical risk: normalization errors outside the declared generator convention or overlooked equality cases would contradict the explicit analytical steps, not merely the diagnostics.

## Originality — PASS (qualified)

The complete heat-kernel formulas in Karlsson–Neuhauser (2006) and Dowker (2012) predate this calculation; they are acknowledged, not claimed as new. The published cycle heat-Lipschitz computation optimizes the edgewise \(\ell^\infty\) difference of \(H_t f\), the unicyclic graph-variation theorem governs \(V(H_tf)\), and the cyclic two-tap Gini result governs complete-pair dispersion. None of their inspected statements implies the arbitrary-kernel equality family, its sharp \(\mathrm{TV}\to\ell^1\) approximation coefficient, or the finite positive spectral law in the declared norm. The finite-path and reflecting-interval heat approximation results have different boundary and cut geometry. These are statement-and-implication comparisons, not novelty claims inferred from a negative text search. Risk remains from unindexed literature or stronger general cyclic convolution theorems not inspected.

## Value — PASS

The invariant is the exact maximum integrated distortion per unit adjacent variation for a natural, broad class of cyclic filters. Its evaluation as expected geodesic displacement yields an immediately computable design criterion for arbitrary nonsymmetric filters, and equality rigidity identifies every worst-case signal under full support. The heat specialization adds nontrivial shape information at every time—complete monotonicity of the derivative—which is stronger than ordinary monotone convergence and useful for diffusion-time error budgeting. This is a structural norm theorem for all finite cyclic orders, not a single sample calculation or restatement of kernel spectral theory. Limitations are finite unweighted cycles, with full-support only for uniqueness; no weighted or higher-dimensional claim is made.

## Literature and limitations

Primary inspected works: Karlsson–Neuhauser (2006), https://www.unige.ch/math/folks/karlsson/heatcyclicfinal.pdf (theorems and cyclic heat-kernel derivation); Dowker (2012), https://arxiv.org/abs/1207.2096 (author-uploaded full-text sections on cyclic heat kernels). Closest published related claims were inspected in the three linked results cited in RESULT.md. The 2006 primary work uses a degree-normalized generator, so its time variable must not be silently identified with the combinatorial generator in this theorem. No assertion of exhaustive publication priority or independent certification is made.

Self-review: passed. Independent audit: not yet performed.
