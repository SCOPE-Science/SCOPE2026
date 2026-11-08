# Scientific review: Poisson interval-maxima law for associahedral width

## Correctness — PASS

For the precise unweighted Minkowski sum of all consecutive-coordinate simplices in the intrinsic Euclidean hyperplane, each support-function summand is an interval maximum and each width summand is the interval range. Centered Gaussian directions give the exact random-width identity. The first-moment formula follows by the independence of Gaussian radius and direction. For asymptotics, Gaussian upper/lower extremal point processes converge jointly to independent processes; a uniform Gaussian-hazard tail estimate controls every small interval in finite \(L^p\). Macroscopic intervals converge by a truncated Poisson continuous-mapping argument, and a chi-square inverse-radius estimate makes radial normalization negligible. This establishes distributional and second-moment convergence, the mean correction \(\gamma-3/2\), and positive, finite limiting scaled variance. A Poisson mark in the central third yields an exponential lower bound on the upper tail, excluding any Gaussian limit. The standalone finite checker was actually executed and passed; it is corroboration, not an infinite proof.

## Originality — PASS, subject to historical-priority risk

Padrol--Pilaud--Poullot (arXiv:2109.09200) characterize deformation cones of graph associahedra and nestohedra, including interval building sets, but do not assert the random-width limit. The earlier Gaussian-width study of Kabluchko--Litvak--Zaporozhets (arXiv:1511.08479) proves limits for regular simplices, cubes and cross-polytopes, not correlated maxima of all consecutive windows. The later interval-hypergraphic study (arXiv:2606.18376) addresses vertex and face combinatorics. The indexed exact inradius of Loday's polytopes concerns a deterministic inscribed ball, and the indexed stellohedron random-width law concerns a different star-based Minkowski decomposition; neither statement implies the all-interval Poisson integral law. The point-process comparisons check equivalence of the normalization, not merely shared names. Searches did not locate an exact formula for this all-interval width observable. A more general published functional limit for sums of scanning maxima might subsume the result despite not being found; priority therefore remains provisional.

## Mathematical value — PASS

This is a complete asymptotic distribution, not merely a mean-width estimate. The unweighted path graph associahedron is a canonical member of a central polytope family; the limiting functional differs from the Gumbel law for an individual simplex because all subintervals share extremes and retain spatial information. The \(\gamma-3/2\) correction encodes the geometry of all interval lengths, and the variance limit identifies the exact nonvanishing fluctuation scale. The exact finite formula supplies a direct intrinsic-volume observable. No general theorem for arbitrary interval weights or independent publication-sized consequence is claimed.

## Closest literature and limitations

Primary source inspections: arXiv:2109.09200 (relevant introduction, graphical and interval-building-set construction, interval section and theorem statements, including complete PDF pages), arXiv:1511.08479 (relevant regular-polytope mean-width and projection-limit statements and proofs), and arXiv:2606.18376 (interval hypergraphic definition, examples, content outline and relevant searchable text). Earlier Postnikov 2005 simplex-sum work supplies structural background, not the law. Specific indexed findings concerning Loday inradii, stellohedron-width extremes and tree zonotope width variances were checked for logical implication. Source access and nomenclature limitations are detailed in AUDIT.json.

The result is restricted to the explicit unweighted intrinsic Euclidean realization and random line projections. The limiting variance is an exactly defined Poisson-functional variance without a claimed elementary closed form. No uniform convergence rate is given. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
