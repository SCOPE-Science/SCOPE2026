# Scientific review

## Correctness — PASS

The affine-coordinate surface measure factors over each facet; independently sampled pair indices have probabilities \(w_iw_j\). Coincident facet classes force a midpoint coordinate in \(\{0,1/2,1\}\), accounting for the entire singular component. Distinct facet classes yield two uniform coordinates and \(d-2\) independent triangular coordinates, producing the displayed mixture density with integral \(1-\sum w_i^2\). The centered function \(\psi=t-1\) has zero uniform mean but triangular mean \(1/3\), isolating each pair's weight by a tensor moment. The algebraic inversion is exact and uses positivity; in dimension two the sole mixture term is constant. An independently executed checker tested 1,320,000 random pairs and exact cube integrals. No numerical experiment is used as an infinite proof.

## Originality — PASS, with residual historical risk

Clement (arXiv:1312.5292, public 2013-12-18) supplies the closest fully inspected text: its Sections 2–4 address trajectory lengths and exit distributions in cuboids, and Section 2.1 explicitly notes independent surface endpoints. It neither states the conditional midpoint density nor establishes the dimension-two/three conditional identifiability threshold. Mathai–Moschopoulos–Pederzoli (1999) addresses distances between points in cubes, including points on different faces; only publisher abstract/metadata were available, so full-document noncoverage is not claimed. Additional exact geometry-record searches for midpoint convolution, tensor moments, shape reconstruction, and aliases did not reveal equivalent or dominating results. Previously available triangle midpoint work concerns triangular boundaries, not products of interval facets. The elementary convolution and pairwise-product inversion devices themselves are standard and are not asserted to be new. Priority is provisional pending broader historical full-text inspection.

## Value — PASS

Separating the singular same-facet midpoint contribution from genuine interior midpoint observations is a canonical operational distinction in surface sampling. The result answers whether the absolutely continuous part retains the surface geometry: it provably loses all planar rectangle aspect ratios, but retains enough statistics to recover every higher-dimensional orthotope side ratio, with an explicit bounded finite-moment inversion. The exact cubical total-variation fractions make the bias quantitative. This is a complete natural inverse classification for the specified observation model, not an arbitrarily chosen finite parameter.

## Scope and limitations

Labeled, dimensionless affine-coordinate observations are assumed, not knowledge of the physical metric; weights of arbitrary skew parallelotopes do not determine all their Euclidean geometry. No stability or finite-sample statistical guarantee is proved. Historical priority is not independently certified because some early face-distance literature was accessible only by abstract.

Self-review: passed. Independent audit: not yet performed.
