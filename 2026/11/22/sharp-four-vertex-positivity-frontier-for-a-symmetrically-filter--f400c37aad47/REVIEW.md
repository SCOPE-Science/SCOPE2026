# Scientific review

## Correctness — PASS

For the stated first-order matched filter, the response is exactly \(I-hL(I+hL/2)^{-2}\), consistent with the specified first-order filtered branch in Wu and Shu, arXiv:2611.02282v1, Equations (3.5), (3.6), (3.38). Spectral calculus gives eigenvalues in \([1/2,1]\), preserving constants. Every simple undirected graph of at most three vertices is covered by the explicit checks of \(K_1,K_2,P_3,K_3\). On \(P_4\), four independent rational off-diagonal formulas have a common strictly positive denominator; all but the endpoint-neighbor class are positive, and Descartes' rule gives exactly one positive root of the sign-controlling cubic. Effective-resistance double centering and finite-dimensional functional calculus prove the general fixed-order stiff expansion and its path obstruction for every \(n\ge4\). The delivered Python/SymPy checker passes; no finite enumeration is treated as proof of all graph orders or timesteps.

## Originality — PASS, with residual priority risk

The motivating full text introduces the filter and its unconditional energy stability, but does not state the exact graph positivity frontier. Fontan–Altafini already establishes that Laplacian pseudoinverses need not be \(M\)-matrices; this general sign phenomenon is credited, not newly claimed. The full published weighted-path Gauss result concerns the distinct multiplier \((z^2-6z+12)/(z^2+6z+12)\), not the filtered-Euler multiplier \((1+z^2/4)/(1+z/2)^2\). The complete-multipartite scalar-filter criterion is restricted to that graph class, which excludes the path \(P_4\). Targeted mathematical-record and primary-literature comparisons found no statement implying the specific sharp cubic cutoff and minimal witness order. Unindexed literature and other implementations of the same rational filter remain residual risks, so this is not an independently established priority claim.

## Value — PASS

A sharp four-state obstruction in a norm-contracting, mass-conserving heat integrator distinguishes spectral stability from the discrete maximum principle on a physically natural diffusion network. The exact onset and the general pseudoinverse obstruction explain why arbitrarily stiff steps can remain energetically safe while producing negative nodal values. The result helps identify when a positivity constraint or limiter is mathematically necessary; it does not promise improved accuracy, cost, or nonlinear convergence.

## Closest literature and limits

- Yue Wu and Chi-Wang Shu, arXiv:2611.02282v1, especially Equations (3.5)–(3.12), (3.38), and related proofs, https://arxiv.org/abs/2611.02282.
- Angela Fontan and Claudio Altafini, arXiv:2109.14587v1, Laplacian pseudoinverse sign structure, https://arxiv.org/abs/2109.14587.
- *Unconditional fourth-order Gauss positivity on weighted paths: a four-vertex cutoff*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unconditional-fourth-order-gauss-positivity-on-weighted-paths-a--73910250a06c.
- *A scalar criterion for unconditionally positive rational graph-heat steps on complete multipartite networks*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-scalar-criterion-for-unconditionally-positive-rational-graph-h--335027f86795.

Self-review: passed. Independent audit: not yet performed.
