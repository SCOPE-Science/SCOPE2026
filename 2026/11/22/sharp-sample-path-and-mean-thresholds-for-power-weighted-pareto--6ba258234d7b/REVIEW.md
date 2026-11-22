# Scientific review

## Correctness — PASS

The exact Pareto truncated-power moments follow by splitting the density integral at the deterministic saturation point. Tonelli and independence reduce the null expectation to one variance integral, which algebraically simplifies to the rational four-factor formula; positive small-argument equivalents establish the strict critical boundaries. For every finite sample the empirical min-characteristic function is linear sufficiently close to zero, which yields the almost-sure threshold and its boundary divergence. A standard separable-Hilbert CLT justifies the stated Gaussian quadratic limit in the finite-trace regime. The standalone Python checker passed 83 exact and numerical checks. No Monte Carlo or finite computation is used as a substitute for the infinite-range proof.

## Originality — PASS (qualified)

Falk–Stupfler (DOI 10.1007/s13171-019-00184-1), full author-posted text, Example 2.2 and Theorem 3.2, provides the Pareto min-characteristic function and weak convergence on compact intervals, but not the power-singular quadratic discrepancy's two thresholds and rational null trace. Meintanis–Milošević–Jiménez-Gamero (arXiv:2310.12348), full arXiv HTML, Sections 4–5 and Appendix, studies exponentially weighted tests and assumes an integrable weight, whereas the studied power weight is not integrable at zero. Nearby general Hilbert-space covariance and heavy-tail moment theorems supply tools but do not by themselves specify the full almost-sure versus expectation window, pathwise blow-up constants, and exact trace for this statistic. Published scientific records and semantic research-record searches located no equivalent complete assertion. Risk: a general fractional-distance or weighted empirical-process theorem might imply part or all of the claimed classification; historical exhaustiveness is not established.

## Value — PASS

The statistic is a natural scale-sensitive extension of min-characteristic goodness-of-fit methods to heavy-tail-emphasizing power weights. The distinction between observable sample-path existence and finite-null-mean calibration is mathematically material: for every Pareto shape below two, some weights produce finite realized statistics yet infinite expectation. The exact four-factor trace provides finite-null normalization and identifies single- and double-pole transitions, while the strict thresholds define the admissible mean-square Gaussian-calibration regime. This is not a claim that the extension is automatically more powerful. The exact invariant is motivated by the test's ability to calibrate rare-tail weighting, not by selecting an arbitrary finite parameter slice.

## Closest work and limitations

The novel assertion is restricted to a completely known Pareto model, with no parameter estimation. Neither composite-null validity nor alternative power is established. Earlier generic theory, particularly theories of singular weighted processes, remains a genuine priority risk even though no encompassing statement was found in the inspected primary texts.

Self-review: passed. Independent audit: not yet performed.
