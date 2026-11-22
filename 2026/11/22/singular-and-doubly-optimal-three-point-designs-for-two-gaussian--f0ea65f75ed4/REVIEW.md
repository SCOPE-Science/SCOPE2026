# Scientific review: singular and doubly optimal three-point designs

## Correctness — PASS

The response matrix for two shifted Gaussian profiles and a constant sky column yields the determinant \(\Delta_d(x)=(a-b)(a+b-2c)\). With independent Gaussian errors of known variance, its square controls the Fisher determinant. Strict monotonicity of \(\tanh u/u\) gives the exact singular-radius classification, while the analytic finite-root expansion gives square-root onset. Both sign lobes have attained positive maxima, and the inner-versus-outer crossing follows from continuous maxima with opposite limiting dominance. The numerical checker passes 323 representative diagnostics and is not a substitute for the universal proof.

## Originality — PASS relative to inspected evidence

The closest primary work on photometric crowds (Primini and Kashyap, 2014) provides a general simultaneous source/background likelihood matrix, but its inspected analysis uses fixed apertures, Poisson counts and posterior errors, not the precise three-point Gaussian D-design rank curve or global tie. Méndez and colleagues (2013) focus on one unknown source position. Prasad (2014) considers one-versus-two source hypothesis testing. A closest published Gaussian-plume sensing theorem uses one signal and an unknown center, whereas this has two unknown shifted fluxes and a constant sky level. The accessible original texts were compared by mathematical implications. Historical risk remains from broader experimental-design theory and an observational crowded-field paper with inaccessible full text; novelty is not claimed certified by database searches.

## Value — PASS

Limited readout resources, blended astronomical sources, and uncertain background naturally motivate identifying all three coefficients. The sharp rank-defect threshold and nonunique global optimum demonstrate both a failure configuration to avoid and competing efficient sampling geometries. The finding is deliberately confined to a symmetric three-point, homoscedastic read-noise idealization; it is not an all-pixels or all-noise astronomy design rule.

## Closest literature and limitations

Relevant inspected literature: https://arxiv.org/abs/1304.6361 ; https://arxiv.org/abs/1403.4919 ; https://arxiv.org/abs/1410.2564 . Crowded-field 2013 observational report https://arxiv.org/abs/1309.4487 was read only in accessible abstract and journal extracts. The exact critical global-tie separation is not proved unique. No field validation or independent historical survey is asserted.

Self-review: passed. Independent audit: not yet performed.
