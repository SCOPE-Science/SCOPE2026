# Scientific review: A minimal four-state arrow of time in a binary stochastic sensor

## Correctness

PASS. The exact stationary generator and its stationary row vector give an analytic four-word matrix product. Its Taylor expansion has zero constant, linear and quadratic antisymmetry terms and the stated cubic coefficient. The general three-state obstruction follows from regeneration at a singleton observed class. A complete census of nonconstant binary partitions of the four-cycle reduces to a singleton, adjacent-pair, and opposite-pair partition. In the opposite-pair case the stationary run-entry Palm calculation has the explicit asymmetric neighboring-run covariance; when either rate contrast vanishes, phase exchange proves full time reversibility. A fixed positive-lag witness survives sufficiently small strictly positive backward rates by continuity of stationary finite-state Markov laws. The symbolic algebra and numerical cross-checks in `checker.py` passed. No numerical enumeration substitutes for these proofs.

## Originality

PASS, qualified. The 2026 Ghosal–Bisker review and Biddle state-sequence estimator motivate partial observation and explicitly do not present the exact two-color directed four-cycle threshold. Lucente et al. (2022) establish the singleton-class semi-Markov no-go mechanism (and examine four-state rings with singleton observation), so that component is credited. Arola-Fernandez and Lacasa (2023) prove the general three-symbol binary obstruction, which is credited. Martínez et al. (2019) and subsequent cautions on waiting-time entropy concern broader inference, not the stated iff rate-contrast and four-snapshot coefficient. The originality scope is therefore confined to the **complete minimal ring/coloring classification and its two explicit signal diagnostics**. Residual risk: a less visible application of general hidden Markov or semi-Markov reversibility conditions may imply the classification without identical wording.

## Value

PASS. A binary observable is a realistic limitation in two-color fluorescence, occupancy and conformational state sensors. The theorem gives a sharp hidden-state complexity lower bound and a necessary-and-sufficient contrast criterion on the smallest realizable cycle; it also specifies the shortest equally spaced word length and a directly measurable adjacent-dwell asymmetry. A small positive backward rate shows that the effect is not limited to unphysical unidirectional transitions. The theorem does not estimate entropy production, and its short-time cubic witness is practically weak at finite sample size; those limits are explicit.

## Closest literature and limits

The closest strong antecedents are Lucente et al., *Physical Review Research* 4 (2022), 043103, Section V (singleton coarse-graining is renewal); Arola-Fernandez and Lacasa, arXiv:2303.11868, Section III (short binary word no-go); Ghosal and Bisker, *PCCP* 28 (2026), 9840–9866 (review of coarse-grained irreversibility). The proof applies to stationary finite Markov jump models with a deterministic state readout and assumes no hidden time-odd parity variables. Full four-state topology classification beyond the ring remains unproved. An equivalent unindexed treatment is possible.

Self-review: passed. Independent audit: not yet performed.
