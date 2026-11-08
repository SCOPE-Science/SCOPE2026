# Scientific review

## Correctness — PASS

The theorem applies to finite connected unweighted complete multipartite graphs with at least two parts, known order, arbitrary observed vertex, and a uniform spanning tree. The classical multivariate weighted-tree identity yields the normalized one-vertex degree generating polynomial (2). The distinguished root \(1-N\) determines the number of parts; each other integral zero records the sizes and multiplicities of all unobserved parts, after removing the mandatory factor at zero. The remaining part size follows by subtraction. The reconstruction handles singleton parts, stars, complete graphs, and \(N=2\). Exact independent Kirchhoff-cofactor computations passed 2,892 scalar comparisons and 336 decoding checks. The finite checker is corroboration, not an infinite certificate.

## Originality — PASS, with historical-priority risk

General weighted tree enumerators (Remmel--Williamson 2002), general uniform-spanning-tree joint degree laws (Rapoport 2023), and general covariance formulas (Fita Sanmartín--Schnörr--Hamprecht 2024) are acknowledged as stronger *forward-computation* frameworks. The new assertion evaluated here is not a formula for a fixed host, but the injectivity of the mapping from all complete multipartite host graph isomorphism classes of fixed order to **one arbitrary rooted marginal law**, with explicit recovery even when the root's part is unknown. None of the inspected source statements establishes that inverse property. A prior unlocated treatment may exist; some publisher full text was not accessible.

## Value — PASS

One-vertex stochastic graph reconstruction is an intrinsically motivated local-to-global inference problem. The finding identifies an entire natural infinite family from a single scalar random variable's exact law, and gives an inexpensive algebraic decoder without enumeration of spanning trees. The known-order assumption is mathematically necessary in general: a leaf of every star has deterministic degree one regardless of the star's size. No finite-sample inference guarantee is claimed.

## Related work and limitations

Closest sources: Remmel--Williamson (2002), DOI 10.37236/1650, for multivariate generating functions of multipartite spanning trees; Rapoport (2023), arXiv:2312.14992, for uniform-spanning-tree joint degree probabilities; Fita Sanmartín--Schnörr--Hamprecht (2024), arXiv:2409.13472, for the general node degree framework; Li--Chen--Yan (2023), DOI 10.1002/jgt.22954, for complete multipartite fixed-forest counts. The theorem depends on the classical enumerator, requires the known vertex count and an exact rooted distribution, and is not a claim of identification for arbitrary graphs. Prior work with a direct inversion statement remains a possible historical risk.

Self-review: passed. Independent audit: not yet performed.
