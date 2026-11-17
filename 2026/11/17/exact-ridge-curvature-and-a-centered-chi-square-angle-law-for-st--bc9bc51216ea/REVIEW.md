# Review: star symmetric-edge ridge curvature

## Correctness — PASS
The claimed domain is every integer \(d\ge2\), for the canonical Euclidean zero-sum embedding. The proof reconstructs all outward normals by solving \(B^{\mathsf T}h=\sigma\), computes the two-normal Gram determinant, and independently obtains ridge volumes from the actual signed-root Gram matrix. Every ridge is counted exactly once. The exterior-angle normalization of \(V_{d-2}\) is validated at \(d=2\). The central-limit and Taylor steps prove the distributional limit; the binomial tail bound and fourth-moment control justify averaging the second-order expansion. Exact enumeration verified \(768\) ridge instances in dimensions \(2\) through \(7\). Risk: no general computer-aided formalization; analytical proof, not finite enumerations, carries the infinite statement.

## Originality — PASS, subject to historical priority risk
The 2018, 2019 and 2021 primary manuscripts describe symmetric-edge-polytope facets, tree crosspolytope equivalence and facet subgraphs, not exact **area-weighted ridge** angle curvature. Published companion results on the same canonical star compute normal lengths/incenters, and another study of tree polytopes computes **facet** areas and surface area. A related \(K_{2,q}\) ridge-angle calculation includes the same centered chi-square angular limit: that distribution alone is not claimed new or sufficient for novelty. Its graph family and calculations do not furnish this star's ridge measures and exact second Steiner intrinsic volume. Additional metric-polytope sources could still contain an equivalent result.

## Mathematical value — PASS
The complete ridge-angle/area distribution answers a natural extrinsic Euclidean geometric question that is lost under the known unimodular crosspolytope equivalence. The exact \(V_{d-2}\) formula extends beyond facet area or inradius and provides a precise first curvature correction despite order-one (rescaled) non-Gaussian angular fluctuations. This is a natural invariant and structural cancellation, not an arbitrary parameter slice or bare numerical record.

## Limitations and source comparison
The result is confined to star symmetric-edge polytopes. It does not assert a general tree theorem, independent priority certification, or originality of the same chi-square law in a related bipartite family. Full-text comparisons are described scientifically in `AUDIT.json` and the references of `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
