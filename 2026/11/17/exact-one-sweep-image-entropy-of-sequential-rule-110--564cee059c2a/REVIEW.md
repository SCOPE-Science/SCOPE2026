# Self-review: exact one-sweep Rule 110 image entropy

## Correctness — PASS

The claim is precisely one in-place left-to-right sweep on a labelled binary ring of length at least three, with no subsequent dynamics assumed. The scan equations fix the two unusual boundary updates. The candidate-set automaton is necessary and sufficient because it existentially tracks the original last bit while successively eliminating each hidden old interior bit; the equality \((a,a)\) at the final state enforces the seam. Distinct output prefixes follow unique deterministic labelled paths, so terminal weights correctly enumerate distinct words rather than predecessors. The exact 26-state closure and 26 consecutive degree-five recurrence residuals are regenerated from the truth table; Cayley--Hamilton converts these finite exact equalities into an all-length recurrence. Polynomial arithmetic gives the stated rational series. Exhaustive independent forward simulation on all configurations through length 16 and independent acceptance testing through length 13 pass. The asymptotic root separation follows from rational sign and derivative arguments.

Scientific limits: the proof depends on the explicit, reproducible finite-state closure, not on finite experiments as an infinite argument. No repeated-sweep or arbitrary-update-order assertion is made.

## Originality — PASS, subject to historical-priority uncertainty

The closest published Rule-110 full results examined count distinct cyclic outputs **after a simultaneous update**, with an explicitly different local dependency, formula, and entropy. One is the 2026-11-02 exact synchronous Rule-110 enumeration, whose image counts at lengths four and five are 10 and 22; the new sequential counts are 11 and 20. A second independently published 2026-11-08 synchronous enumeration has the same synchronized scope. These do not imply a scan-specific enumerator. The 2007 *Order Independence in Asynchronous Cellular Automata* classifies invariant periodic-point sets, not the image of a particular sweep. The 2025/2026 *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, especially Theorem 16, concerns isolated fixed points and convergence, not the distinct one-sweep image counts. Cook's Rule-110 computational construction is explicitly simultaneous. Searches for the exact coefficient sequence, the new quartic and one-sweep preimage language yielded no matching prior statement. No search exhausts unindexed historical material.

## Value — PASS

The exact full-image count and constructive predecessor recognition address a natural information-loss invariant of a canonical nonlinear automaton under an experimentally and theoretically important change of update schedule. The strict inequality between simultaneous and sequential exponential image growth is structural and not determined by the known fixed-point or periodic-set results. The theorem covers all ring lengths, not an arbitrary finite slice, and provides an exact recurrence, rational series, and entropy rather than isolated numeric gains. It does not claim improved computational universality or novelty of finite automata as a method.

## Closest scientific references and residual risks

- Wolfram, *Statistical mechanics of cellular automata*, Rev. Mod. Phys. 55 (1983), DOI 10.1103/RevModPhys.55.601; founding synchronous model.
- Macauley, McCammond and Mortveit, arXiv:0707.2360; periodic-point order independence.
- Cook, arXiv:0906.3248; synchronous Rule 110 computation.
- Donoso-Leiva et al., arXiv:2509.07797; sequential convergence and fixed-point isolation.
- *Exact one-step image counts for cyclic elementary cellular automaton Rule 110* (public 2026-11-02) and *Exact cyclic one-step image enumeration for cellular automaton Rule 110* (public 2026-11-08); both simultaneous dynamics.

Residual risks: a previously unindexed scan-specific image enumeration may exist; no independent mathematical audit has been conducted. This review does not certify historical priority.

Self-review: passed. Independent audit: not yet performed.
