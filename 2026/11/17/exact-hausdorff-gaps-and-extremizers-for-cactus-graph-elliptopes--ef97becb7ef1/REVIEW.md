# Mathematical assessment: Euclidean elliptope–cut gaps for cactus graphs

## Correctness — PASS

The precise claim is restricted to standard Euclidean edge-correlation coordinates and to finite, connected, simple cactus graphs. The single-cycle proof is complete without computational extrapolation. A parity argument gives the exact support function of the even-sign cut body. The signed-cycle adjacency matrix has antiperiodic Fourier eigenvalues, with largest eigenvalue \(2\cos(\pi/n)\) of multiplicity two. The unit-diagonal PSD trace bound is tight at planar Gram points. The equality case is **unique in edge coordinates**, since a quadratic form constant at three or more distinct points of the half-circle must be isotropic. Decomposing an arbitrary functional into a minimum-weight odd signing plus coordinate residuals proves the global Euclidean support gap, with strictness for nonconstant absolute weights. The metric-projection variational identity then proves that the displayed farthest points and their nearest cut projections are exhaustive. One-vertex gluing gives literal Cartesian products, so the sum-of-squares distance and the free bridge coordinates follow for arbitrary cactus graphs, including trees.

The finite standard-library checker returns `PASS: 9057 finite numerical and combinatorial assertions`; this is corroboration only, not the logical proof. Every cited equality and normalization is checked for the triangle boundary case and the empty-cycle tree case. In \(0\)-\(1\) cut coordinates all distances halve, as disclosed.

## Originality — PASS, subject to historical priority

**Closest mathematical precedent:** Laurent and Varvitsiotis (2011), Theorem 3.3, evaluates the multiplicative Grothendieck constant of a cycle and already establishes the special signed uniform semidefinite optimum. These two results are explicitly credited. Their full text does not state or classify the Euclidean *additive Hausdorff gap*, all maximizing unit directions, all farthest elliptope points, or the closest cut projections. Although the special support value is enough to motivate the new calculation, its ratio bound alone does not supply a global \(\ell_2\)-normalized additive optimization and equality classification.

**Direct recent motivation:** Avis, Devroye and Deza (first posted April 17, 2026) determine volumes of graph cut/elliptope bodies and establish one-vertex product decompositions. Those volume and product statements are known inputs, not claimed as new. Laurent, Mascarin and Telen (May 4, 2026) classify algebraic boundary pieces, not Hausdorff extremizers. Published work on sparse positive-semidefinite cone extreme rays concerns a related but different invariant. The novel scope assessed here is the *combined exact metric gap, complete equality/projection classification, and Pythagorean cactus composition*.

Targeted searches compared aliases such as support-gap, additive SDP integrality gap, Euclidean relaxation distance and convex-body Hausdorff distance, as well as stronger graph and polytope classes. No inspected primary source or indexed mathematical finding was found to cover the whole claim. This is not an exhaustive priority guarantee: another preexisting derivation of additive distances may be indexed differently. The 2016 sparse-PSD source was only accessible at abstract level and is treated as a residual coverage risk rather than as evidence of noncoverage.

## Mathematical value — PASS

The exact additive Euclidean error of the semidefinite elliptope approximation is a natural geometric invariant distinct from volume and multiplicative objective ratios. The theorem supplies the complete extremal geometry and closest feasible cut points, not just a scalar. In particular, one cycle has gap of order \(2/\sqrt n\), whereas adding independent cycle blocks combines their squared gaps, with arbitrarily many copies producing growth proportional to the square root of the number of blocks. This contrasts with the maximum rule for multiplicative Grothendieck constants under one-vertex sums. The theorem therefore quantifies the metric error of a 2026-motivated family of relaxations and explains exactly where the error is attained.

## Sources, comparisons, and remaining scope

Primary documents inspected: Laurent–Varvitsiotis (2011), https://optimization-online.org/wp-content/uploads/2011/06/3060.pdf , in particular Sections 2–3; Avis–Devroye–Deza (arXiv:2604.16735), https://arxiv.org/abs/2604.16735 , in particular Sections 2–3 and the cycle-volume corollary; Laurent–Mascarin–Telen (arXiv:2605.02484), https://arxiv.org/html/2605.02484v1 , especially the introduction, preliminaries and geometric-boundary sections. The more remotely related Solus–Uhler–Yoshida (arXiv:1506.06702) was compared at abstract level, not claimed to have been fully inspected.

Limitations: the theorem does not address general graphs containing overlapping cycle blocks, anisotropic edge metrics, arbitrary correlation projections, or historical priority in unindexed literature. The finite verifier is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
