# Self-review

## Correctness — PASS

For every positive initial occupancy, the reciprocal \(y=1/p\) obeys \(y'=-r(t)y+2\). The symmetric smooth ramps have exactly unit homogeneous multipliers and additive increments bounded between \(2\eta e^{-\eta}\) and \(2\eta e^{\eta}\). Composing the four intervals yields \(y_{n+1}=q_n y_n+b_n\), with \(q_n=e^{H_n-F_n}\to e^{-\delta}\) and \(b_n\to2(1+e^{-\delta})\). Contraction for positive \(\delta\) yields the claimed peak; expansion for negative \(\delta\) and positive forcing at zero \(\delta\) imply extinction. Long monotone segments and shrinking ramps transfer the discrete limits to the full trajectory. Both Bohl extremes are attained on increasingly long opposite-signed plateaux. For the balanced linear-length calendar, summable \(b_n-4\) implies \(y_n=4n+O(1)\). The separate finite checker passed; it does not prove the infinite limits.

## Originality — PASS (literature-bounded)

Full accessible source comparisons identified the prior reciprocal formula, the mixed-sign zero-lower-occupancy theorem, and a specially tuned piecewise weak-persistence example, all credited. The precise contribution is a smooth fixed-colonization calendar with an all-initial-condition necessary-and-sufficient season-length offset classification, exact upper peak and critical law. Searches of published research records on the originating paper, equivalent inverse-occupancy recurrences, Bohl spectra, smooth ramps and critical rates found no dominating claim among the returned matches. A failed search is not a proof of historical novelty.

The closest source is Robledo and Bustamante, arXiv:2504.20396v1, specifically Appendix B's single engineered piecewise example. That work proves possible weak persistence but not the all-offset phase classification claimed here. Amster, Robledo and Sepúlveda, arXiv:2412.02952v1, analyze almost-periodic environments without these diverging blocks. The specific retrieved research records are documented in AUDIT.json; the closest concern finite-period Floquet matrices or discrete biomass models. Risk remains that a broader nonautonomous logistic theorem could subsume part of the result.

## Value — PASS

Mixed-sign Bohl exponents do not settle persistence in the general model. Here, even though the favorable and hostile seasons both diverge and the Bohl extremes stay fixed, an asymptotic duration imbalance of order \(1\) switches extinction into weak persistence. The peak \(\tfrac12\tanh(\delta/2)\) and the special balanced season-boundary rate \(1/(4n)\) quantify an ecologically motivated information gap rather than a merely numerical observation.

## Verification and limitations

Run `python3 CHECK.py`. It passes eight finite seasonal-offset trajectories and thirty ramp comparisons. Finite checks do not replace the analytical proofs. This deterministic fraction-of-patches theorem does not predict finite-population survival, and the critical rate is not claimed for all zero-offset schedules. Historical priority and scientific validation have not been independently established.

Self-review: passed. Independent audit: not yet performed.
