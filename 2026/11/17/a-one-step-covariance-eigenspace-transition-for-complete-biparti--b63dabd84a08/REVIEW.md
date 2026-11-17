# Self-review

## Correctness — PASS

For every pair of integers \(a,b\ge2\), the stable-set polytope is the convex hull of the two coordinate cubes and admits a beta-sliced uniform-volume law. Conditional maximum-variable integration gives all seven first/second coordinate-moment types exactly. Permutation symmetry decomposes covariance orthogonally into two within-part contrast spaces and a two-dimensional block-mean space; this reproduces all eigenvalues and their multiplicities. The critical determinant is explicitly evaluated as \(ab(a+1)(b^2-a^2-3a-3)/[48(n+1)^3(n+2)^2]\), whose sign switches strictly between differences one and two, with no integer boundary ties. A separate equal-volume order-chamber construction independently confirms exact-rational moments for 196 parameter pairs. Analytic factorization, not tests, proves the theorem for all sizes.

## Originality — PASS; priority provisional

The first public lead source, Aliniaeifard et al. (arXiv:1804.00360, 2018-04-02), studies the stable-set polytope and one-skeleton; its inspected full text does not evaluate the continuous uniform-volume covariance. Freij-Hollanti and Lundström (arXiv:2312.13890, 2023-12-21), full text examined, treat ordinal sums of antichains and free sums with combinatorial face counts, not this metric covariance spectrum. Davis and Kohl (arXiv:2207.14759, 2022), full text examined, focus on Ehrhart data. Most importantly, full RESULT.md texts of the balanced and unbalanced John ellipsoid results for the **identical two-level order/chain polytope** were inspected at their publicly available GitHub records (2026-10-11): those optimize ellipsoid volume and certify facet contacts, not uniform-volume covariance and not the one-step minimum-eigenmode transition. The new claim is not presented as a generic implication of a classical eigenvalue formula; the exact integer crossing, multiplicities, and contrasting two asymptotic regimes are material. An unindexed equivalent result formulated through order-statistic moment tensors remains a real residual priority risk.

## Mathematical value — PASS

This is a natural full-dimensional polytope family arising in stable-set and ranked-poset geometry. The exact covariance answers a metric shape question for continuous uniform volume that John ellipsoids do not answer. At the universal boundary \(\lvert a-b\rvert=2\), the minimizer changes from a global two-block direction to local within-smaller-block contrasts, while the balanced covariance condition number stays bounded and fixed-minority growth is quadratic. These give a sharp all-parameter qualitative classification, not a randomly chosen finite slice or mere numerical instance.

## Closest sources, limitations, reproducibility

Lead original source: arXiv:1804.00360 (v1 2018-04-02). Poset free-sum source: arXiv:2312.13890. Exact same object but different optimized ellipsoid: publicly recorded full results ending `8659155ecca7` and `c200d8f4f023`. Proof is specifically for \(a,b\ge2\), ordinary Euclidean coordinates and continuous uniform volume; not for uniform vertices or general bipartite graphs. A mathematically equivalent prior moment formula may exist. `check_covariance.py` needs Python 3 only and reproducibly checks 196 exact moment profiles and 8,970 integer threshold signs.

Self-review: passed. Independent audit: not yet performed.
