# Scientific review

## Correctness

**PASS.** The numerator of the normalized sigmoid flow is algebraically reduced to a positive denominator times \(2x(e^{1-\delta}Q(x)-1)\). The derivative of \(Q\) has the sign of \(H(x)=2x(1-x^2)-\tanh(2x)\); the strict decrease of \(\tanh(2x)/x\) forces exactly one positive maximum of \(Q\) on \((0,1)\). The resulting horizontal-line intersection count proves the complete equilibrium census for every real initial center opinion and every \(\delta\geq0\). The flow signs prove stability and basins, including the nonhyperbolic boundaries. Numeric verification is supplementary and not an infinite proof.

## Originality

**PASS on the literature inspected, with residual uncertainty.** The original and revised source model, arXiv:2209.07004 and DOI:10.1137/22M1527258, contains local harmonic-state stability results for paths and balanced-exposure graphs, and numerical multistability in larger graphs, but not the exact three-agent five-equilibrium regime or unique scalar saddle-node threshold. The source's Figure 5 treats larger paths and does not imply the claimed global classification merely by specializing parameters. Generic results on bifurcations and different nonlinear-consensus or saturating-response systems do not specify this logistic-kernel root count. A full-text comparison was made to the primary preprint and journal, and relevant related mathematical models were reviewed. An unindexed equivalent statement remains possible.

## Value

**PASS.** The exact coexistence interval \(1<\delta<\delta_*\), its terminating collision, and all attraction basins answer a concrete nonlinear stability-versus-selection question that the source's local harmonic-state criterion does not settle. In particular a linearly stable neutral state coexists with two stable extreme-leaning states on the smallest graph capable of representing two opposed fixed zealots and one flexible opinion. It provides a usable and precisely bounded hysteresis mechanism, not simply a new numerical example or a textbook consequence of linear stability.

## Relationship and limitations

The source's sigmoid dynamics, zealot construction, and linear criterion are credited. The complete classification relies on symmetry, exactly three vertices, and \(\gamma=1\); its extension to unequal edge weights or other steepness values is not claimed. The exact threshold is transcendental and the decimal is approximate. The checker supplies reproducible numerical cross-checks, not independent certification.

Self-review: passed. Independent audit: not yet performed.
