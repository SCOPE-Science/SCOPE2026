# Self-review

## Correctness — PASS

The exact Gaussian-plus-compound-Poisson cumulant formula and the size-square/Beta-remainder transform give the right variational objective. The endpoint-tail hypothesis is strong enough to prove both the Laplace asymptotic and the first logarithmic derivative asymptotic without assuming a density. A comparison point gives the sharp order \(1/L\); elementary global upper bounds exclude all arguments outside the \(L\)-scale. Every interior global maximizer therefore satisfies a stationary equation, which yields both the \((\beta+3)\log L\) shift and the constant \(1-\log K\) in the reciprocal optimal scale. All hypotheses, normalization factors and the no-uniqueness limitation were checked. The standalone checker passed 262 diagnostics for two continuous-endpoint families; it is supplementary only.

## Originality — PASS, with residual historical risk

The closest primary texts are Chen (arXiv:2610.00032v1), which supplies the broad variational representation but not a continuous endpoint-tail expansion, and Chen--Wang (arXiv:2609.02590v1), which derives the coefficient three for a Skellam model with an atom at the positive endpoint. The new theorem excludes that atom case and proves that the logarithmic coefficient varies continuously with the non-atomic endpoint exponent. An accessible previous claim for Gaussian plus *fixed* Poisson jumps has the same atom-case limit, not the present \(\beta>0\) family. The nearby sub-Poisson work of Leskelä--Välimaa optimizes a different envelope. Targeted literature and semantic research-record searches found no explicit or dominating continuous-endpoint result. This is a best-knowledge assessment, not proof of global priority.

## Value — PASS

The optimal Bernstein-type scale is a natural quantitative invariant of a Gaussian-smoothed jump model. Its leading inverse-logarithmic decay is insensitive to jump-endpoint regularity, making the first correction essential for distinguishing classes of distributions. The theorem supplies that correction, including its constant, for arbitrary non-atomic regular-variation exponents and identifies a universal change of log-log coefficient. The two naturally normalized continuous examples \(\operatorname{Uniform}(0,1)\) and \(\operatorname{Beta}(1,2)\) have different and precisely predicted coefficients. This is more than a parameter substitution in a single fixed-jump model: the full endpoint Laplace ratio and an all-global-maximizers argument are needed.

## Closest literature, scope and limitations

The main source and the earlier directional result were examined in their relevant theorem, proof, example and discussion sections. The sub-Poisson paper was checked at its definitions and central concentration results, not claimed as exhaustively excluded on every page. Residual historical risk remains from broader analytic Tauberian optimization results or later versions of these preprints. The theorem is limited to fixed bounded nonnegative jump laws with a pure-power endpoint, positive fixed Gaussian variance and rare Poisson intensity. No maximizer uniqueness, multivariate extension or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
