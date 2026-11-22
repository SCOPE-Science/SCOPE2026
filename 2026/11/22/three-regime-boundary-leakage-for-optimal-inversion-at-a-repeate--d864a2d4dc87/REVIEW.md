# Scientific assessment: three-regime boundary leakage at a repeated root

## Correctness — PASS

The result quantifies the residual of the unique minimum-norm polynomial in a fixed finite codimension subspace. The coefficient representation and finite moment system are exact and taken from an explicitly credited prior theorem. After diagonal scaling, the inverse weighted Hilbert matrix is well defined and converges entrywise by fixed-dimensional Gram positivity; rational interpolation determines both first and last coefficient limits with signs and constants. The proof gives separate uniform estimates: an Abel two-step difference bound when the coefficient weight is nondecreasing, and Dirichlet uniform convergence plus a bounded-variation estimate for positive weight. The interior profile follows from absolute convergence. Explicit nonzero endpoint constants establish sharp orders. `verify.py` reconstructs the source Gram matrices and tests finite cases, but is not used to justify the infinite limit.

**Risk/limits:** The asymptotics are fixed-parameter and exclude the boundary root itself. The estimates do not control a boundary layer whose distance to the root shrinks with degree. No effective finite-degree threshold is stated.

## Originality — PASS, best-knowledge

The closest article is Bénéteau–Manolaki–Seco, arXiv:1901.00694 (first public 2019-01-03). Its Theorem 7.1 gives the exact coefficients, Theorem 7.3 the squared residual norm, and its discussion following Corollary 7.4 expressly leaves uniform closed-disk convergence for higher multiplicity for later study. The 2022 Acuaviva–Seco theorem on uniform off-zero convergence assumes distinct simple zeros; a repeated zero is not a special case. The published mixed-multiplicity Hardy research record (2026-10-18) gives a uniform coefficient profile at weight zero; that covers or implies some of the Hardy endpoint algebra, **which is credited and not separately claimed as novel**. It does not cover the two non-Hardy boundary regimes or their weight transition. The new joint theorem supplies these along with the sharp interior-to-boundary comparison. Searches of the accessible historical collection and relevant research index identified no statement with stronger weighted repeated-zero boundary coverage.

**Risk/limits:** A published older treatment in confluent Christoffel-kernel or Fourier endpoint language may state equivalent formulas under another normalization. The checked published index is not an exhaustive originality guarantee. One 2021 background article on generalized inner functions was inspected at the abstract and bibliographic level only; its subject differs, but this limited material is not represented as full-text coverage.

## Value — PASS

The result addresses an explicitly identified missing case in the main motivating paper: norm convergence for a repeated unit-circle zero does not alone determine closed-disk boundary convergence. The complete regime distinction shows that the leading error changes mechanism at the Hardy exponent. The sharp constants capture a terminal oscillatory coefficient for negative weights and the Dirichlet-series coefficient tail for positive weights; the all-multiplicity classification provides exact pointwise rates and a stronger interior profile. The sharp distinction is meaningful for uniform approximation by polynomial inverse filters in Bergman and Dirichlet-type spaces, not just for an isolated finite computation.

**Risk/limits:** This does not solve general polynomials with multiple distinct boundary zeros, nor any moving-weight or moving-root problem. No downstream theorem or independent external validation is claimed.

Self-review: passed. Independent audit: not yet performed.
