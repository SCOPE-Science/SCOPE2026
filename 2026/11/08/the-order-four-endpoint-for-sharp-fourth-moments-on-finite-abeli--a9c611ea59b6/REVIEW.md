# Review of the sharp coordinate-cross fourth-moment theorem

## Correctness — PASS
The stated Fourier normalization was checked by character orthogonality. The centered fourth-moment lemma is proved through a complex Lagrange-multiplier reduction and a two-value extremum; its skewness consequence uses centered Cauchy–Schwarz. Independent-variable expansion yields the displayed fourth-moment bound. The large-order case has an exact factored polynomial and a positive mixed-axis remainder. The order-four proof treats the sign reversal explicitly: the cross-axis energy enters through \(v=\sqrt{\sum_j(X_j/T)^2}\), and its two minimization regimes prove strictness unless one axis survives. A one-coordinate fourth-moment equality criterion completes rigidity. The counterexamples for orders two and three were checked by exact pair-sum counting. The bundled checker verified 480 finite sample cases and two exact witnesses; this does not replace the analytic proof.

## Originality — PASS, with residual literature risk
The closest published result is *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses* (2026), which was read in full. Its theorem is restricted to two axes and cardinalities at least five; it explicitly excludes order four, and its sign-based concentration argument cannot establish that case. The accepted claim resolves the missing order-four boundary for every number of axes and classifies the sharp group-order threshold. Separate searches for product-space fourth moments, coordinate crosses with three or more axes, and order-four group endpoints found no prior statement covering the exact endpoint and rigidity together. The finite-field restriction literature from 2018 and 2024 covers other geometries. A general sharp tensor-product or first-order Fourier-chaos theorem is the principal possible subsumption risk.

## Mathematical value — PASS
The smallest nontrivial group order for which all axis unions have one-axis-rigid sharp fourth moments is a natural structural cutoff. At order four the scalar fourth-moment estimate loses the helpful positive pairwise-energy term used above that threshold; the new argument restores sharpness by coupling the cubic energy profile to the quadratic energy profile. The conclusion is uniform in the number of axes and independent of group structure, with an explicit concentration remainder above threshold. It is a complete sharp classification for this natural family rather than an arbitrary finite test.

## Limitations
The order-four stability coefficient is not optimized, and the smaller-order counterexamples do not classify the sharp constants there. A general published product-space theorem could imply the endpoint; no claim of exhaustive historical novelty is made. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
