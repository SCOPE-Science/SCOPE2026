# Review of the two-stage algebraic-stability negativity frontier

## Correctness
**PASS.** For every admissible two-stage order-three tableau, positive weights and the first three order conditions force a unique pair of nodes for each weight \(p\in[1/4,3/4]\). The positive semidefinite algebraic-stability matrix forces \(a_{11}\ge p/2\), hence \(a_{12}\le-f(p)\). A monotone quartic equation proves the unique global minimum of \(f\). The explicit symplectic family has all four classical third-order conditions, achieves equality, and the positive-semidefinite equality conditions prove uniqueness. The standalone exact-rational arithmetic tests and sampled checks passed. No numerical finite test is used for the infinite quantifier.

## Originality
**PASS, qualified.** The comparison is of implications, not titles: the phase-type study arXiv:2610.37425v1 optimizes SSP radii and positive coefficients; Ketcheson–Macdonald–Gottlieb 2007 discusses why negative Butcher entries rule out a positive SSP radius; Gottlieb et al. arXiv:2611.07981v1 (Section 5) proves a general qualitative nonnegative-coefficient/algebraic-stability incompatibility. None of the inspected relevant passages determines the exact two-stage, bounded-stage-time minimax negative-entry magnitude or equality tableau. published-finding corpus and accessible prior-claim checks gave no directly covering result. A hidden equivalent two-stage coefficient optimization remains a priority risk, especially because the proof is elementary.

## Value
**PASS.** The problem naturally measures the strength of the incompatibility between inner-product contractivity through algebraic stability and nonnegative Butcher coefficients required by SSP. The normalized stage-time interval permits a dimensionless, finite, sharp quantitative separation, and the unique realizing symplectic integrator identifies the precise least-negative design. This is a complete extremal classification at the minimum stage count capable of order three, rather than an arbitrary example; it does not claim practical superiority or a general-stage theorem.

## Limits
Only two stages, positive weights, normalized stage abscissas and exact real coefficients are covered. The result does not establish positive SSP radius, unconditional monotonicity, or numerical superiority. The historical-priority comparison is limited to identified and inspected sources.

Self-review: passed. Independent audit: not yet performed.
