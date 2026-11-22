# Scientific review — orientation entropy landscape

## Correctness

**PASS.** The domain is explicitly the canonical affine Markov construction of Oliveira, one map per sign word and branch count. The published Markov matrix and entropy equality are credited premises. The new argument derives a positive Perron eigenvector and the monotone scalar eigenvalue equation, then proves all three word-multiplicity classes, unique minimizing/maximum orientations, asymptotic expansions, a uniform entropy-loss estimate, and the central limit law. The independent finite checker rederives 1,512 exact characteristic-determinant evaluations and enumerates all 32,764 words through fourteen branches. Finite checks corroborate rather than replace the all-size proof. Boundary case two branches is handled separately. The claimed distribution is over orientation words, not orbits or measures.

## Originality

**PASS on the evidence inspected, with residual historical-priority risk.** Oliveira's arXiv:2611.03287v1, especially Theorems 7.1 and 7.2, supplies the minimal-rank affine family and cubic spectral formula. Its Section 7 gives a coarse \(\log(n/(n-1))\) gap bound but does not classify the unique entropy optimizer, enumerate all orientation-word entropies with multiplicity, or derive the Gaussian law. Related previous calculations on the same family establish the invariant physical measure under an equal-ending constraint, or a uniform Parry mixing bound. They are neither equal to nor stronger than the three-part orientation-entropy theorem. Rugh and Tan's earlier kneading framework supplies the general determinant setting, not an explicit all-orientation optimization in this prescribed canonical family. A previously unindexed equivalent derivation remains possible; originality is not externally certified.

## Mathematical value

**PASS.** Entropy dependence on an orientation word is the immediate natural question after the construction of a minimal-jump-rank realization for every orientation word. The theorem gives an exact solution over *all* words at each branch count, not a chosen special example: a unique worst-case orientation, a full multiset with precise multiplicities (including possible algebraic collisions), and a quantitative Gaussian distinction between worst-case and typical orientation choices. It sharpens the source's uniform estimate while explaining why the worst-case leading loss is twice the typical leading loss. The result is intentionally confined to this canonical family; it does not assert minimal entropy among arbitrary maps with the same branch signs.

## Relationship to earlier literature and limitations

Primary source: H. M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1 (2026-11-02), Theorems 7.1–7.2 and Corollary 7.3. Broader source: H. H. Rugh and L. Tan, *Kneading with weights*, J. Fractal Geom. 2 (2015), DOI:10.4171/JFG/24; only its abstract was available for the broad comparison. Further priority search may uncover a preexisting optimization or a stronger general spectral ordering result. No independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
