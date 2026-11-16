# Review: first-order Walsh sampling on one-edge-excluded Hamiltonian tours

## Correctness — PASS

The theorem covers every integer \(n\ge6\) and every forbidden edge of \(K_n\), for **uniform** undirected tours and probability-normalized *centered* first-order Walsh characters. Contracting disjoint path components gives every requisite one-, two- and three-edge moment. Conditioning on excluding the edge yields the exact covariance blocks. Vertex-star degree constraints provide an \(n\)-dimensional nullspace. Two explicit endpoint-contrast spaces have the **same** positive covariance eigenvalue, while the incidence-kernel internal-edge sector has the other positive eigenvalue. The three sectors and degree stars fill all coordinates, proving completeness and multiplicities. Multiplication by four converts incidence covariance to Walsh Gram, giving the stated sharp ratio. Exact standard-library rational tests cover all allowable tours for \(n=6,7,8,9\). Numerical or finite evidence is not used as an infinite proof.

## Originality — PASS (provisional historical priority)

The closest published overlap is *Equal-volume Walsh coordinate bases on directed Hamiltonian tours*: its complete published statement and proof concern **directed** tours with unrestricted arc variables. Its two-point covariance does not supply the three-edge moments required by our **undirected**, edge-excluded conditional ensemble. The published exact Walsh spectrum of uniform connected unicyclic graphs has a different sampling measure, includes arbitrary tree attachments, and only one deterministic dependence; it cannot be specialized to uniform Hamiltonian tours with a forbidden edge. Gutekunst–Williamson establish symmetric-tour-polytope inequalities and cite its classical dimension; this prior rank information is not an eigenvalue spectrum. Fickus–Schmitt provide the broader harmonic-frame context, but their difference-set construction does not imply the restricted tour Gram. Searches for spectral, incidence, and conditioned-tour aliases located no equivalent formula. Older combinatorial-design/covariance tables remain an explicit priority risk; this is not a claim of externally certified novelty.

## Mathematical value — PASS

The result gives sharp low-order reconstruction stability for a natural family of constrained tour signals in every dimension and identifies a structural eigenvalue degeneracy not forced by the remaining vertex symmetry alone. The relative conditioning \((n-2)/(n-3)\) tends to one with an exact leading defect, even after losing an allowed edge. Its explicit extremal sectors and exact kernel provide more than a dimension count or a routine finite parameter substitution.

## Limitations and validation state

The theorem is not asserted for arbitrary weights, multiple forbidden edges, noncentered features, or higher Fourier degrees. Exact rational finite checks corroborate the proof but are not an independent mathematical audit. Historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
