# Self-review

**Reviewed claim:** Sharp RK4 positivity on heterogeneous weighted stars and a strict spectral-stability gap.

## Correctness: PASS

The proof starts from the explicitly normalized symmetric weighted Laplacian (one hub, positive spoke weights, completed four-stage explicit RK4). Arrowhead multiplication yields the exact hub-to-leaf cubic and leaf-to-leaf quadratic. A strictly positive quadratic discriminant margin rules out any leaf-to-leaf failure; a sum-of-squares representation makes every diagonal positive. The identity for \(9A_xC_x-4B_x^2\), together with \(v\le b^2\), makes every individual hub-edge cubic strictly decreasing with exactly one positive zero. The same positive leaf-to-leaf quadratic orders all these cubics by weight, making the largest spoke first. The spectral-radius inequality and an irreducibility/Perron–Frobenius contradiction prove strict separation from RK4 \(\ell_2\) stability for nonuniform weights, with equality for uniform stars. The actual bundled checker passed 42,875 exact-rational checks; it is supplemental to the symbolic proof.

## Originality: PASS, conditional on available evidence

The closest same-method claim in accessible prior research covers all **unweighted** bipartite graphs and therefore includes uniform stars, which are expressly credited. A separate previously published all-order Taylor filter result covers all **unweighted** complete multipartite graphs, also including uniform stars. The closest same-graph-class arbitrary-spoke theorem concerns the different **implicit Gauss–Legendre rational** fourth-order stability function, not the classical explicit RK4 polynomial. Comparisons at hypothesis/implication level did not establish that these prior results contain the arbitrary positive-weight cubic bottleneck, permanent largest-edge sign loss or strict/equality spectral-stability classification. General SSP and Runge–Kutta positivity frameworks were inspected in their available materials. The Horváth 1998 full text was unavailable and may imply a stronger result; an equivalent unindexed publication cannot be excluded. A failed search is not a novelty proof.

## Mathematical value: PASS

Heterogeneous diffusion stars are a natural network model with arbitrary positive rates. An otherwise \((m+1)\)-dimensional matrix nonnegativity condition collapses to one explicitly determined cubic root, identifies the precise first failing physical connection, and shows analytically why stability and nonnegativity decouple under any unequal conductances. It replaces numerical parameter sweeps with an all-size exact safety limit, including a rigidity theorem not available from the uniform graph calculation.

## Limits and source comparisons

Only the completed one-step explicit RK4 operator for finite symmetric positively weighted stars is covered. Stagewise positivity, nonlinear systems and general graphs are not proved. Ketcheson–Gottlieb–Macdonald (2011, arXiv:1106.3626v1) addresses SSP time integrators and provides the date-verifiable methodological baseline, not a matching graph-specific formula in inspected sections. Horváth (1998, DOI:10.1016/S0168-9274(98)00050-6) has a highly relevant positivity title but only an accessible abstract. Higueras–Ketcheson–Kocsis (2015, arXiv:1505.04024) was likewise abstract-only. Equal-weight and different-method special cases are not presented as discoveries. Independent publication priority and proof validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
