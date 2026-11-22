# Mathematical review

## Correctness — PASS

The theorem uses real, pairwise-distinct rates strictly between \((\beta-1)/2\) and \(\beta\), a fixed finite number of channels, and nonzero complex coefficients. The transformed Hardy kernel is integrable, so the operators are bounded. The exact adjoint applied to each shifted-Jacobi polynomial has one \(x^{-\delta}\) term plus a polynomial; orthogonality forces each cross-cutoff block to have rank one. Rodrigues and beta integrals give exact coefficients. Two independent rescalings cancel identically and the low/high Gram matrices converge entrywise to the same positive Cauchy matrix. Finite-dimensional singular-value continuity proves all \(m\) limits and eventual rank. The two-rate example follows from exact trace and determinant. The checker provides supplementary finite tests, not the infinite proof.

## Originality — PASS with historical-priority qualifications

Agler–McCarthy (arXiv:2205.01856) treat Hardy eigenvectors, Hilbert-space distances and asymptotic polynomial approximation; their Beurling treatment (arXiv:2206.03462) classifies invariant subspaces. Chalendar–Partington (arXiv:2212.02172; *Archiv der Mathematik*, 2023) address monomial-operator boundedness and compactness. Their inspected results do not provide a multirate simultaneous Gram-limit spectral formula for polynomial projection commutators. Related published work on Hardy commutators with multiplication or diagonal multipliers concerns different operator pairs and asymptotics; it does not imply the rank-\(m\) Cauchy–Gram limit. An unindexed formula or specialized finite-section paper remains a historical-priority risk; absence from searches is not proof of priority.

## Value — PASS

The natural problem is the stability of the polynomial Galerkin representation of a finite linear combination of weighted Hardy averages. The formula gives the **entire** persisting finite-rank singular spectrum, including all interactions and cancellations between arbitrarily many fixed rates. It distinguishes strong convergence from norm convergence and demonstrates a nontrivial smaller leakage channel with an exact second singular value. It is a structural finite-section result, not a small perturbative improvement or a renamed single-rate bound.

## Limits and references

The conclusion is limited to the stated strict real-rate region and fixed finite \(m\). Historical priority is qualified by possible unindexed or inaccessible specialized approximation results. See the three source references and exact proof in `RESULT.md`. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
