# Scientific review: weighted two-clique covariance conditioning

## Correctness — PASS

The stated object is the centered graphical zonotope of two complete graphs joined at precisely one articulation vertex; the random variable is uniform on distinct vertices and both positive edge lengths are constant *within* their respective blocks. Acyclic orientations split uniquely into a pair of transitive clique tournaments. Uniform sampling therefore gives independent uniform permutations, whose exact rank covariance is \((r+1)L_{K_r}/12\). This yields the matrix \(C=uL_{K_a}+vL_{K_b}\) with \(u=(a+1)t^2/12\) and \(v=(b+1)s^2/12\). The contrast decomposition and a three-variable quotient give all eigenvalues, including the single zero eigenvalue. Evaluating the quotient quadratic at \(au\) and \(bv\) proves the strict extremal ordering, including cases where an internal eigenspace has zero multiplicity. The identity \(\kappa+2+\kappa^{-1}=4ab/n+(ay-b)^2/(ny)\) proves existence, uniqueness and sharpness of the minimizer. The fixed-clique imbalanced limit follows from the exact quadratic's sum and product. A replayable exact-rational program separately enumerated the small graphical-zonotope vertices and matched every tested covariance entry. Its finite computations supplement, rather than replace, the all-parameter proof.

## Originality — PASS, with a bounded historical-priority risk

Padrol–Pilaud–Poullot (arXiv:2111.12422, initial public date November 24, 2021) analyze graphical-zonotope deformations. Pilaud (arXiv:2111.12387, initial public date November 24, 2021) establishes the correspondence with acyclic reorientations and develops graph-fan and lattice methods. Neither inspected source derives the unique covariance-conditioning weight ratio. Kling (2023), Theorem 4, treats exactly the same unweighted underlying clique-coalescence graph but gives its **unweighted graph-Laplacian spectrum**. This covers the equal-clique, equal-weight special case after applying the standard permutation-covariance identity, so no originality is asserted for that subcase. For arbitrary positive clique weights, the covariance matrix is instead a distinct two-coefficient Laplacian, and the sharp unique scale ratio and bounded-versus-quadratic anisotropy law require an additional calculation not stated in the inspected work. Searches also included graph-spectral and network-design formulations as potential alternative routes to the same optimization. An unidentified earlier equivalent weighted-Laplacian conditioning calculation remains the principal risk; publication priority is not independently established.

## Mathematical value — PASS

The question has a natural geometric object and invariant: the spectral condition number of uniformly sampled zonotope vertices quantifies shape anisotropy under edge-length choices. The exact global optimum is not a mere normalization: it selects a uniquely determined **relative** clique weight and changes the asymptotic anisotropy of highly unequal cliques from quadratic divergence to a finite explicit limit. The full eigenvalue multiplicities and strict optimality gap rule out hidden competing modes or weight plateaus. The result is a complete natural family classification, with relevance to weighted zonotope design and rank-statistic covariance. It makes no claim to solve arbitrary graph weighting or general polytope preconditioning.

## Closest literature and scientific limits

- Padrol, Pilaud, Poullot, *Deformed graphical zonotopes*, 2021 preprint: geometric framework and deformation cone, no claimed covariance optimization.
- Pilaud, *Acyclic reorientation lattices and their lattice quotients*, 2021 preprint: orientation–vertex interpretation and simplicial graph fan, no claimed covariance optimization.
- Kling, *On the uniqueness of the Laplacian spectra of coalescence of complete graphs*, 2023, Theorem 4: exact unweighted Laplacian spectrum of the same graphs; weighted covariance minimization is not addressed.

Acyclic orientation correspondence, permutation covariance, and equitable quotient methods are established ingredients, not novel lemmas. Earlier weighted graph spectral work may contain a logically equivalent optimization under other terminology. The result excludes volume-uniform samples, varying weights within a clique, and graphs with more than two blocks. Code and proof have been assessed only by the self-review process.

Self-review: passed. Independent audit: not yet performed.
