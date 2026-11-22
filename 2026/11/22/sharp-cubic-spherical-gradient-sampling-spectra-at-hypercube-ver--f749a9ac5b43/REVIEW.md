# Scientific review: cubic spherical-gradient sampling spectra

## Correctness — PASS

The claim uses degree-three homogeneous **harmonic** polynomials, normalized probability area measure on the unit sphere, a Dirichlet source norm with factor \(3(d+1)\), and equal-weight tangent-gradient observations at all \(2^d\) signed cube vertices. Three explicit subspaces have verified harmonicity, are invariant and mutually orthogonal under sign flips and coordinate permutations, and their dimensions exhaust the entire harmonic-cubic space. They are irreducible signed-permutation sectors, or equivalently direct symmetry calculations show that all three sampled-gradient and spherical norm forms diagonalize in these blocks. Exact sixth-order spherical moments and cube sign averages give the three scalar ratios. Their positivity and pairwise rational ratios prove the sole \(d=3\) null mode, injectivity for every \(d\ge4\), and the exact spectral upper-branch switch at \(d=9\). All dimensions are proved algebraically; computation is not substituted for infinite proof. Independent exact rational Gram reconstruction passed every basis-pair identity for \(d=3,4,5,6,7\).

## Originality — PASS, with residual priority risk

The checked point-value hypercube Walsh theorem (research record in References) characterizes only scalar evaluation ranks. Its strongest relevant assertion explicitly omits positive singular values and makes no claim about tangential derivatives. Moore–Russell's Gegenbauer–Krawtchouk coefficient formula similarly concerns point-value sampling after random rotation, not the fixed-frame derivative spectrum; its full arXiv HTML was examined through its main evaluation-map and Appendix A arguments. Bigi–Fraux–Browning–Ceriotti derive efficient Cartesian derivative recurrences, but not a discrete frame lower bound. Xiao–Zhuang's gradients are those of a spherical-design optimization objective rather than observation of harmonic gradients. Allasia–Cavoretto–De Rossi construct geodesic radial cardinal Hermite–Birkhoff interpolants rather than the exact pure-degree Dirichlet spectral classification. A related cubed-sphere numerical interpolator's full text was inaccessible; accessible material indicates a different geometry and point-value data, but this does not eliminate all priority risk. Database searches of gradient-only frames, aliases and three-sector spectra did not identify a dominating theorem; absence of a search match alone is not proof of originality.

## Mathematical value — PASS

This is a complete all-dimensional sharp first-order observation classification on a canonical cubical spherical design. Unlike scalar values, tangent derivatives determine the entire cubic harmonic in every dimension at least four; dimension three has a concrete, irreducible exceptional blind mode. Explicit singular values quantify noise amplification and exhibit a nontrivial change of the worst-amplified/most-observed symmetry class at dimension nine. These are motivated exact recovery facts for derivative data, not merely a renamed moment identity or arbitrary fixed-parameter enumeration. No all-degree frame or perturbation theorem is asserted.

## Boundaries and checks

The normalization and multiplicities in `RESULT.md` were compared directly against the extracted exact checker; every new package path is standalone. The numerical tests are finite and serve as reproducibility corroboration. The novelty comparison is limited by indexing and the unavailable full text mentioned above. Independent mathematical validation has not taken place.

Self-review: passed. Independent audit: not yet performed.
