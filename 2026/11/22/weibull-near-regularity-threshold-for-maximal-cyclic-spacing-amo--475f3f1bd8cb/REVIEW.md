# Scientific review

## Correctness — PASS

The claim is an asymptotic distribution for the deficit of the largest possible minimum cyclic gap among a fixed-size selected subset of independent circle points, and a total-variation approximation for the rare-subset count. The one-subset calculation is an exact Dirichlet-simplex volume transformation; it gives \(\Pr(A_I)=(m\varepsilon)^{m-1}\) for uniform sampling and a relative \(O(\varepsilon)\) correction for a positive Lipschitz density. If two distinct subsets overlap in \(k\) labels, conditioning on a common label forces the remaining \(2m-k-1\) independent observations into arcs of total width \(O_m(\varepsilon)\), establishing the joint bound. The dependency-graph Poisson argument consequently produces error \(O(n^{-1/(m-1)})\). Strictly continuous sampling removes threshold ties. These analytical steps, including the endpoint \(m=2\), were reconstructed; the finite checker's 321 deterministic assertions and 390,000 seeded trials corroborate specific calculations but are not substituted for proof.

## Originality — PASS against inspected sources

The closest motivating paper, Cunden et al., arXiv:2606.04837, treats a line with anchored endpoints and renewal spacings, not selected cyclic near-regular subsets. The broad circle U-max theorem of Nikitin and Simarova, arXiv:2010.04460, explicitly requires \(C^3\) smoothness near an extremum (A5) and a nondegenerate Hessian (A6); the minimum-gap kernel has a cusp there and exhibits a different scaling. The previously published fixed-sample circle Rips-loop result contains the same regular-polygon density product and resonance, but not the present growing-sample Poisson count or optimum law. A previously published circular scan result concerns tight clusters of consecutive sample points, not nearly equally spaced selected points. Both published records were examined in substantive full-result form. Classical dependency-graph Poisson approximation, the density product in isolation, and the harmonic resonance in isolation are credited, not claimed as new.

Historical geometric U-max and circle-coverage literature is extensive; an unlocated equivalent or implicit general theorem is a residual priority risk. Negative retrieval evidence is not treated as a proof of global novelty.

## Value — PASS

Selecting fixed numbers of circular sample points to maximize their smallest separation is a natural stochastic packing statistic motivated by recent optimal-spacing research. The sharp \(n^{-m/(m-1)}\) near-regularity scale, complete Weibull limiting law, actual total-variation rate, exact finite-subset probability in the uniform case, and sensitivity to the periodic sampling environment classify its rare optimal configurations. The result is not merely a renaming of the original line problem or a fixed-sample simplex identity, because dependence among \(\binom nm\) candidate near-regular configurations must be resolved.

## Limits and remaining risks

The subset size and density stay fixed. The rate constants are not optimized and there is no claim of orientation-level point-process convergence, growing-subset-size universality, singular-density coverage, or algorithmic optimality. Independent scientific scrutiny of originality and proof has not been carried out.

Self-review: passed. Independent audit: not yet performed.
