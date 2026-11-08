# Scientific review

## Correctness — PASS

The exact transformation from closed SIR to the positive Lotka–Volterra system follows by differentiation for every admissible strictly positive SIR state. The nonnegative conserved energy has strictly convex compact positive levels; each nonzero level is a nonsingular periodic orbit. Prevalence and incidence logarithmic derivatives are respectively \(v-\gamma\) and \(v-h-b\). Restricting the energy to these two stationary-point loci gives a unique minimum in each case, proving the two *if and only if* peak thresholds, including equality tangency and the absence of other extrema. Reconstructing both physical observables yields the exact shift multiplier \(e^{-aP}\). Numerical checks in `check.py` are supplementary and finite, not the basis for an infinite-time claim.

## Originality — PASS (qualified)

The nearest primary 2026 work already states the general incidence stationary-point equation and the log-linear knot representation, and earlier CoSIR work already exploits a different feedback-induced SIR–Lotka–Volterra reduction. Neither inspected source gives the fixed exponentially growing transmission reduction, the two sharp energy threshold curves for original prevalence and incidence, and their exact periodic-geometric peak laws. The standard conservative Lotka–Volterra mechanics are acknowledged. Targeted comparisons found no matching result; this is best-knowledge originality, not an assertion that every unindexed treatment of epidemic oscillations has been excluded. The nearest alternative, adaptive CoSIR control, is materially different and does not supply the asserted implication.

## Mathematical value — PASS

The sharp, explicitly calculable threshold answers a natural complexity/interpretability question from recent peak-preserving SIR literature: even monotone forcing of minimal log-knot complexity can produce an arbitrarily large raw count of strict peaks, while their amplitudes have a precisely specified decay. The difference between raw extrema and observably prominent waves matters mathematically for formulating lower bounds on forcing complexity. The result avoids claiming that two knots preserve arbitrary empirical wave geometry.

## Closest literature and scientific limitations

Rabajante (2026, arXiv:2610.05556v1) covers general time-varying transmission, peak conditions and empirical MPPC; it does not supply the present single-slope exact classification. Shetty–Maheshwari–Bannur–Merugu (medRxiv 2020/2021) identify a Lotka–Volterra structure for a different *state-dependent feedback policy*, not a prescribed exponential transmission function. Classical predator–prey energy geometry is shared and is not presented as new. The exponential growth of transmission makes the conclusion a mathematical phenomenon, not a realistic long-run public-health prediction; the peaks eventually fall below every fixed positive prominence floor. An equivalent specialized result outside searchable sources remains possible.

Self-review: passed. Independent audit: not yet performed.
