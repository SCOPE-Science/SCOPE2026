# Scientific review: two-pool RNA:DNA ratio threshold

## Correctness — PASS

The final theorem is a closed first-order, coeval two-pool model with all six parameters positive. The transformation \(x=e^{-\Delta t}\) gives an exact logarithmic derivative; algebra yields a quartic \(P_q\) with strictly negative derivative for every \(0<x<1\). Endpoint signs prove its sole root, and the sign of \(F_q-s\) establishes a complete zero-, one-tangent-, or two-turning-point classification. The range of the three monotone branches implies exactly three age solutions at every level between the two extrema. The displayed counterexample has strict certified integer-power inequalities; the checker additionally passes 12,609 supplementary checks. There is no claim that finite numerical tests prove the theorem.

## Originality — PASS on accessible comparisons; priority provisional

Marshall et al. (2021), Jo et al. (2022), and Kagzi et al. (2023) establish physical motivation for differential degradation but do not state the parameter-specific theorem. Mixture reversals are an old phenomenon and are not asserted to be novel. Bar-Lev and Letac (2010) treat increasing mixture hazard under a different objective; classical exponential-polynomial theory already provides a generic three-level-root ceiling but not the parameter-specific criterion or matching-rate example. Scarsini and Spizzichino (1999) address Simpson-type ageing paradoxes at a broader level, but the available abstract does not decide priority for this exact special case; complete article access was not obtained. Thus historical priority requires further examination even though no decisive covering implication arose in the accessible comparison.

## Value — PASS

The measurement interpretation problem is concrete: estimating molecular age from a higher-or-lower eRNA:eDNA ratio is motivated by published experiments. The result identifies a counterintuitive nonmonotonicity despite faster RNA degradation *within each component*, supplies an explicit necessary-and-sufficient boundary using only pool weight and relative excess rate, and specifies how many compatible ages may result. The two-pool minimum and exact certified example show that the issue is structural, not merely a numerical fit. This is neither a field-calibrated statistical procedure nor a conclusion about measured samples.

## Principal scientific risks and limitations

The precise inter-pool rate coupling and equal initial RNA:DNA proportions are essential. Measurements with noise, detection limits, replenishment, transport or additional pools are outside the theorem. The two extrema can be close; practical identifiability requires experiments. The broad survival-analysis literature may contain a mathematically equivalent specialized result not located by the available comparisons.

Self-review: passed. Independent audit: not yet performed.
