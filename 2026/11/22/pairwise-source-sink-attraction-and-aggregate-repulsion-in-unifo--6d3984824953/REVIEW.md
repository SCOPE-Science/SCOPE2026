# Scientific review

## Correctness — PASS
The proof starts from the explicit random-tree and independent fair-edge model, verifies the marked pair probability with and without a shared edge, and proves the weighted edge-restricted Cayley identity using the matrix-tree derivative and a solved electrical potential. These exact evaluations yield the full pairwise covariance profile, strictly positive off-diagonal and strictly negative aggregate covariances (except the deterministic size-two boundary). Source-source probabilities establish marginal variance, and controlled expansions yield the limiting correlation. `verify.py` independently enumerates all labeled trees and edge orientations through six vertices with exact rational arithmetic. Finite checks are not substituted for an infinite proof.

## Originality — PASS, historical priority qualified
The closest published deterministic-tree theorem already supplies the fixed-tree covariance identity and exact path/star extrema. The 2012 Bernardi–Morales paper supplies the classical multidegree enumerator; both are credited as substantive ingredients. The additional marked-edge Cayley calculation gives the annealed two-label sign profile and its opposite-sign aggregate, which are not in the inspected statements. Okoth's label-directed orientation model is distinct. The separate ingredients are elementary enough that unnoticed prior synthesis remains a real priority risk.

## Value — PASS
The natural signed covariance question for source and sink locations changes qualitatively on aggregation: all off-diagonal local correlations are positive, yet the totals are negatively correlated at every nontrivial order. The uniform spanning-tree ensemble gives a canonical comparison with fixed paths, and the explicit limiting correlation is informative at macroscopic scale. This is a concrete structural dependence result rather than a small numerical improvement.

## Closest literature and limits
Bernardi and Morales, *Counting trees using symmetries* (2012), arXiv:1206.0598, give the multidegree enumerator. *Sharp path–star bounds for source–sink covariance in randomly oriented trees* (2026) establishes the fixed-tree identity and positive path example. Okoth's 2015 dissertation concerns label-directed edges. This result asserts no joint central limit theorem or biased orientation extension, and historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
