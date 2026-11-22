# Scientific review

**Correctness — PASS.** The target is a strictly convex positive KL projection; the underlying isotonic block Jacobian is given in Blondel et al. (2020), Proposition 3, Lemma 2 and Proposition 4. Every block derivative row has absolute sum \(2(1-\mu_i/\sum_{k\in I}\mu_k)\), bounded using \(m\le\mu_i\) and \(\sum_{k\in I}\mu_k\le B\). Interiority near a vertex makes the bound sharp. The script tests 7 dimensions, 7,000 random pairs and 7 sharpness constructions; numerical tests are ancillary to the proof. Nonconstant weights and the constant-weight exception are explicit.

**Originality — PASS, with historical-priority risk.** Full texts inspected: Blondel et al., *Fast Differentiable Sorting and Ranking*, ICML 2020 (especially §§4–5 and the displayed Jacobian); Lim–Wright, *Efficient Bregman Projections onto the Permutahedron and Related Polytopes*, AISTATS 2016 (especially the algorithms and relative-entropy pooling). Both establish precursor methods and local computations, but neither inspected main text contains the global maximum-coordinate coefficient, vertex-limit extremality/nonattainment, or quantitative quadratic/entropy separation. Searches for permutahedron KL projection sensitivity, aliases and sharp Lipschitz constants found no equivalent theorem; search absence does not establish priority.

**Mathematical value — PASS.** The exact robustness budget depends on only the smallest vertex mass and total, not the full permutahedron's shape. It identifies near-hard rankings as asymptotically worst conditioned, gives a precise \(1/\varepsilon\) smoothing law, and establishes a strict quantitative stability gap between entropy- and quadratic-regularized ranking for every number of labels. These are motivated operator quantities for differentiable ranking, not arbitrary numerical slices.

**Limitations.** The main result requires strictly positive nonconstant weights, concerns log-KL output, and does not address norm changes or performance of entropic optimal transport ranking. Earlier equivalent results in another vocabulary cannot be ruled out definitively.

Self-review: passed. Independent audit: not yet performed.
