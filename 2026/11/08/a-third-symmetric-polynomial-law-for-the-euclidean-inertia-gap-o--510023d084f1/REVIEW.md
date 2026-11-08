# Scientific review: Euclidean inertia of maximal ranked poset polytopes

## Correctness — PASS

The proof constructs an explicit invertible piecewise-affine volume-preserving map between the standard order and chain polytopes of an ordinal sum of antichains. Sampling a uniform order-polytope point by independent within-layer permutations of uniform order statistics makes each coordinate pair an order statistic and a local spacing sum. Beta/Dirichlet first and second moments give an exact within-layer covariance difference, and summing it yields the third elementary symmetric polynomial in the layer sizes. Equality in the global and fixed-height bounds follows from counting triples across distinct layers and an exact balancing transfer. Neither computational truncation nor an unsupported positivity assertion is used as proof.

A separate exact rational checker integrates moments over simplices rather than evaluating the proposed Dirichlet formula. It passed 127 layer-size compositions through seven coordinates and 1,813 within-layer covariance-entry checks, 1,981 balancing-profile checks and 21 two-layer reflection checks. The checks are finite; the analytic argument establishes all positive integer parameters. All statements use uniform *volume* distributions and the unweighted canonical Euclidean metric.

## Originality — PASS, provisional historical priority

The 2023 maximal-ranked-poset primary paper by Ahmad–Fourier–Joswig, arXiv:2309.01626 (sections 1–2, theorem 4.1 and computational section), treats face vectors and chain-order polytope interpolants rather than interior quadratic moments. Freij-Hollanti–Lundström, arXiv:2312.13890 (sections 2, 4–6), develops ordinal-sum geometry and face-enumerator inequalities but does not provide the present covariance or inertia identity. Hibi–Li, arXiv:1208.4029, gives unimodular-equivalence/facet criteria; a general affine non-equivalence result cannot supply the exact second-moment gap. Stanley's 1986 transfer map supplies an antecedent tool but no covering metric identity was identified in the accessible material.

Mathematical record comparisons against order/chain inradii, John ellipsoids, signed order polytopes, and the earlier equal-layer mean-width finding revealed different invariants; the width result evaluates a directional support functional, not the volume-uniform covariance. Searches on equivalent language (second moment, mean squared Euclidean distance, inertia, covariance), rank parameters, symmetric-function form and broader affine-equivalence criteria found no strong implication covering this statement. This remains a best-knowledge priority judgment, not independent historical certification. A previously unindexed moment identity or derivation from other full texts is residual risk.

## Mathematical value — PASS

The result gives a sharply quantitative answer to a natural Euclidean question about canonical Ehrhart-equivalent pairs: how far apart are the spatial dispersions of uniformly distributed interior points? The answer depends only on the third elementary symmetric function of level sizes, unexpectedly ignoring the order in which those levels occur. The zero-gap criterion exactly separates one/two-level cases from all higher levels, and the sharp fixed-size and fixed-height extremizers provide complete structural bounds. The full within-layer covariance identity makes the conclusion more informative than an isolated numerical moment. The claim does not rely on a conjectured downstream application, and it does not equate face data with interior second moments.

## Closest work and limitations

Primary sources are arXiv:2309.01626, arXiv:2312.13890 and arXiv:1208.4029, together with Stanley (1986). An accessible earlier claim concerning three equal antichain layers instead studies asymptotic mean width; it does not imply the present all-layer inertia identity. The new result is restricted to maximal ranked posets/ordinal sums of nonempty antichains and their standard coordinate embedding. Historical priority remains provisional, no extension to arbitrary posets is asserted, the full covariance difference is not claimed positive semidefinite, and independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
