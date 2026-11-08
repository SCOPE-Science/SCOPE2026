# Mathematical assessment

## Correctness — PASS

For the rooted metric tree with one unit stem, \(d\ge2\) identical second-level stems, and \(e\ge2\) terminal unit edges per second-level hub, the root-to-point integration map is unitarily equivalent to the compact Sobolev embedding with energy norm. Its inverse squared singular values are the rooted Dirichlet–Kirchhoff Laplacian eigenvalues. Solving the edge ODEs for \(0<k<\pi/2\) leaves the exact hub conditions \(B_j(c^2-es^2)=U(e+1)sc\) and \(Cc=\sum_j B_j\). The nonresonant case has exactly one frequency \(\arctan(1/\sqrt{de+d+e})\), with one-dimensional eigenspace; the resonant case has exactly \(\arctan(1/\sqrt e)\) with eigenspace dimension \(d-1\). These two disjoint cases exhaust all lower frequencies, establishing the first two singular values, exact multiplicities, and all inverse deductions. A local symbolic determinant and finite-element discretization on the actual graph independently check the critical formulas, without being substituted for proof.

## Originality — PASS, qualified

The general tree-Hardy approximation-number framework is Evans–Harris–Lang (arXiv:math/0003215v1, 2000); the regular metric-tree Laplacian decomposition is Naimark–Solomyak (2000, especially Theorem 7.2); general spectral estimates are Solomyak (arXiv:math/0201015v1, 2002). Pivovarchik (arXiv:2301.05939, especially Theorem 2.2) establishes a general equilateral-tree Dirichlet characteristic-polynomial framework and reconstruction from two complete spectra. These are substantial antecedents and cover the general method of calculating eigenvalues, but their inspected primary text does not state the complete **two leading singular-value** collision law and single-boundary-problem two-value inverse rigidity on the present two-level branching family. Another paper by Pivovarchik–Rozhenko on inverse regular trees studies different pendant-boundary conditions; its full text was inaccessible. Full duplicate-coverage searches across the accessible findings index and relevant primary sources returned no stronger directly covering specialized statement. This is not an exhaustive novelty proof, and literature under equivalent terminology remains a residual risk.

## Value — PASS

The problem has an intrinsic operator-theoretic and inverse-spectral motivation: the first singular value is a sharp root-to-point integration constant, but a sharp constant generally need not identify the underlying geometry. This theorem classifies *all* equal-norm collisions on a natural infinite regular-tree family and shows that the second singular value (and even its value plus multiplicity alone) resolves them. An explicit pair with different total metric length but equal norm demonstrates nontrivial ambiguity. This yields a complete finite-dimensional inverse spectral fingerprint, not just a numerical special case or an arbitrary restricted parameter computation.

## Verification and limitations

The bundled checker reports `EXACT_SECULAR_DETERMINANTS_OK 8`, `INDEPENDENT_CONFORMING_FE_LOW_SPECTRUM_OK 8`, `BRANCH_PRODUCT_COLLISIONS_AND_TWO_VALUE_INVERSION_OK`, and `ALL_TWO_TIER_HARDY_CHECKS_OK`. It checks finitely many instances only; the all-parameter proof is the explicit eigenfrequency exhaustion. An unindexed prior closed-form specialization of the general regular-tree spectral theory remains possible. Claims do not extend to arbitrary trees, higher eigenvalues, or heterogeneous lengths or weights.

Self-review: passed. Independent audit: not yet performed.
