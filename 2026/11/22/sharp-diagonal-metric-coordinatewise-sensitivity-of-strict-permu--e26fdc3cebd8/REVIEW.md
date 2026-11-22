# Scientific review: diagonal-metric permutahedral projection

## Correctness — PASS

For strictly decreasing generating coordinates, every face is a product of ordinary permutahedra indexed by an ordered partition. The proof reconstructs the diagonal weighted projection on each face affine hull and its exact induced coordinate-maximum operator norm, then maximizes across all realizable faces. Replacing the maximizing inverse weight by the global maximum and selecting the smallest remaining inverse weights gives the closed finite formula. Every maximizing face has a nonempty open projection cell, ensuring a finite sharp pair. The exact-rational checker separately compares 600 finite cases and verifies two explicit finite optimality witnesses against all 120 vertices. The full infinite claim rests on the stated analytic argument, not on the experiments.

## Originality — PASS, with priority risk

The closest projection literature is Lim–Wright (2016), whose uniform-separability hypothesis excludes nonuniform diagonal quadratic objectives; Moondra–Mortagy–Gupta (2021), which gives face-stability and projection algorithms without this sharp anisotropic coordinatewise coefficient; and Padrol–Pilaud–Poullot (2023), which supplies ordered-partition face geometry but not sensitivity. The available search of earlier mathematical records and published results found no equivalent sorted-prefix formula. Existing unweighted permutahedron, entropy soft-rank, weighted simplex, and \(\ell_p\) cross-polytope coefficients concern different maps and do not imply this weighted-metric maximum-norm result without additional work. A broader older treatment of separable convex optimization over polymatroids could still contain equivalent stability information, and no exhaustive publication-priority claim is made.

## Mathematical value — PASS

The theorem determines an exact robustness budget for anisotropically weighted least-squares ranking projection, independent of the rank magnitudes. It reveals that the worst error amplification can arise on a proper face, which makes estimates based only on the global sum constraint wrong, and identifies uniform diagonal weights as the unique optimal metric family for this endpoint robustness objective. The sharp coefficient is computable by sorting and a prefix scan; these conclusions are specific structural information, not just an application of generic Euclidean nonexpansivity.

## Scope and independent validation

The proof applies only to strictly decreasing generating ranks, positive diagonal quadratic metrics, and ordinary coordinate maximum norms. The supplementary finite checker does not constitute an infinite-dimensional or third-party proof. An earlier equivalent theorem, particularly within nonuniform separable polymatroid projection literature, remains possible.

Self-review: passed. Independent audit: not yet performed.
