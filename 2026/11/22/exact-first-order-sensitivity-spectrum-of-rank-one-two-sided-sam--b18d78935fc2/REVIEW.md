# Scientific review

## Correctness
PASS. The map is taken directly from the fixed-increment definition in Zhang [1, Eq. (2.1)]. Differentiation of normalized sampled projectors gives formula (1); an orthogonal rank-one tangent/normal decomposition gives (2). The adjoint-product eigenanalysis proves every multiplicity, including degenerate alignment by continuity, and furnishes an exact worst perturbation. The derivative is smooth under nonzero overlaps. A standalone deterministic program completed 1,563 corroborating checks. The formal proof, not numerical sampling, establishes the universal quantifiers.

## Originality
PASS, subject to residual literature risk. Zhang [1, Theorem 2.2] supplies the broader finite-error estimate, but does not determine the exact local derivative or singular spectrum. The familiar two-sided projector itself is prior art: Epperly [2, Section 10.1], citing Stewart, explicitly defines it. Nobile–Riffaud [3] and Hauck–Kusch–Schotthöfer [4] treat integration and robustness rather than the infinitesimal two-sided sampling condition numbers. Published-record semantic searches for the same map, aliases, principal angles, and condition numbers found no specific covering spectrum. The result is therefore a narrow refinement of a known algorithm, not a new algorithm or a priority guarantee.

## Value
PASS. The exact singular spectrum separates tangent errors (unmodified), normal errors (which can leak into tangent channels), and tangent-normal input combinations that cancel at first order; it quantifies a dimension- and singular-value-independent accuracy budget for a newly analyzed same-increment low-rank update. The sharp angular norm improves the source's rank-one finite-error prefactor only for infinitesimal defects, from \(\sqrt{2+\alpha^2+\beta^2}\) to \(\sqrt{1+\alpha^2+\beta^2}\). Its sharpness witnesses rule out any better universal local guarantee at fixed alignments. This matters for selecting numerical increment tolerances when old bases drift; it does not imply a new global integration order or general dynamic stability.

## Closest literature and limitations
Primary sources: Zhang, arXiv:2611.15175, Section 2; Epperly's 2025 thesis, Section 10.1; Nobile–Riffaud arXiv:2502.07040; Hauck–Kusch–Schotthöfer arXiv:2608.27749. Unindexed earlier matrix perturbation derivations may contain equivalent formulas. Rank \(r>1\), roundoff, singular reference overlaps, and finite-error global optimization are unproved. No independent audit or external certification is claimed.

Self-review: passed. Independent audit: not yet performed.
