# Self-review

## Correctness — PASS

For the precise exponential-age mixture (not a generic nonlinear reset-source PDE), the beta and gamma integrals reconstruct all stated moments. The rational-factor derivatives and increasing digamma yield global strict monotonicity. Values at rational endpoints, computed with interval arithmetic, bracket the unique fourth-moment crossing and rigorously separate its sixth moment from the Gaussian value; `checker.py` also performs independent moment integrations. The proof covers all positive exponents, rates and packet scales, with the ordinary-diffusion endpoint obtained by limits.

## Originality — PASS, qualified

Chełminiak, *Non-linear diffusion with stochastic resetting* (arXiv:2107.14680), already establishes the Barenblatt packet, exponential renewal law and stationary integral; these are not claimed as new. The additional global monotone inverse-kurtosis theorem and unique fourth/sixth-order distinction are not stated in the inspected relevant primary sections. Other index hits about reset kurtosis concern different Markovian or active models. Lenzi et al., *Results for Nonlinear Diffusion Equations with Stochastic Resetting* (2023), could not be inspected completely and remains a priority risk. A general distribution formula determines moments in principle, so originality rests on the complete strict classification and not on a formula substitution alone.

## Mathematical value — PASS

Kurtosis is an experimentally and theoretically natural shape statistic for nonlinear transport. The theorem proves complete ideal-observable identification of the porous-medium exponent independently of the reset time scale, and distinguishes the unique false fourth-order Gaussian signal using sixth cumulant. These are natural shape and identifiability questions, not a chosen finite slice. It makes no assertion about finite-sample estimation errors.

## Limitations and relevant literature

All statements concern a mathematical renewal-aged packet mixture; no direct trajectory-level nonlinear resetting model is asserted. Exact population moments are required. Potential prior coverage in an inaccessible related 2023 full paper and other unindexed sources remains unresolved. Primary references and the reproducible moment calculations are in RESULT.md and checker.py.

Self-review: passed. Independent audit: not yet performed.
