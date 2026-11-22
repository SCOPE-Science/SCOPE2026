# Self-review

## Correctness: PASS

The conditional absorption time and mark distribution are defined for every \(p\in(0,1)\), \(\lambda_0,\lambda_1>0\), and \(B>0\). The completed event density \(a_je^{-\lambda_jt}\) and censoring mass partition total probability one. Using \((a_0,a_1,p)\) as local parameters, the score-block expansions and the \(2\times2\) Schur complement yield the explicit \(B^3/12\) coefficient. The known-rate benchmark includes the censor term; it has leading order \(B\). Strict identifiability follows from intercepts and slopes on any nonempty time interval. The Hellinger expansion includes both event channels and the censor atom, and tensorized affinity gives a necessary \(MB^3\to\infty\) condition for consistent two-point discrimination. Recalculation of the expansions and direct high-precision integration checks from the bundled script agree. The theorem does not mistake simulations for an infinite proof.

## Originality: PASS, with literature-coverage qualification

The complete available text of Reia--Fontanari (arXiv:2611.12692v1) specifies the underlying censoring model and raises the unknown-duration inference problem, but does not give an efficient Fisher-information cubic asymptotic or a matching global Hellinger indistinguishability limit. Larson--Dinse (1985) and Choi--Huang (2014) give competing-risk mixture likelihood context; their accessible summaries do not resolve this specific comparison. The 2026 hybrid-censoring Bernstein--von Mises paper was inspected in full-text HTML: it provides general operational information for a different marked-hazard parametrization, not this explicit cubic nuisance-profile and fixed-intensity comparison. Searches for short-horizon censored exponential mixtures, competing-risk Fisher information, and exact cubic lower bounds did not reveal a covering statement. Generic likelihoods alone do not establish the new sharp coefficient without the nuisance Schur calculation, and generic information formulas do not establish the matched-alternative global indistinguishability. Remaining risks include relevant inaccessible full texts and unindexed equivalent work.

## Value: PASS

The sharp cubic loss explains quantitatively why parallel first-trajectory simulations with severe censoring cannot infer eventual absorbing-state proportions reliably when both outcome-dependent mean times are unknown. The exact coefficient identifies the information penalty relative to calibrated rates, and the two-point Hellinger bound extends it to every estimator by proving that fixed total simulation time spread over arbitrarily short trajectories loses the ability to distinguish some physically distinct models. This resolves a specific observability concern of the motivating statistical-mechanics model; it is more than a restatement of censoring bias or a one-point numerical observation.

## Limitations and comparison risks

The physical model is exactly the binary exponential absorbing-outcome model with independent first trajectories, not a general interacting-system theorem. No claims of priority beyond inspected sources, no sufficiency result for estimators, and no full-text assessment of paywalled articles are made. Finite checks supplement exact algebra.

Self-review: passed. Independent audit: not yet performed.
