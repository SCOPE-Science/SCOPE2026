# Review of the sparse slow-class crossover

## Correctness — PASS

The assumptions put both Gamma tails in a uniform strict large-deviation regime. The backward-geometric representation of the Poisson lower tail and Stirling's formula yield a logarithmic prefactor and its exact half-log threshold. Independent thinned Poisson streams establish the colored extremal process, whose two intensity measures give both the limiting completion CDF and the last-class probability. Conditional clock variance and a deterministic stopping-index truncation transfer the joint result to discrete draws. The proof includes the essential floor effects and the competing-class phase alternatives. The included numerical checker passes 46 finite diagnostics; infinite results are proved analytically, not inferred from these diagnostics.

## Originality — PASS (provisional)

Castro–Marinho (2026), arXiv:2610.33199, treats the uniform-probability growing-multiplicity cutoff; its Theorem 2.3 is a one-slope Gumbel result. Long (2026), arXiv:2604.25108, Theorem 4.1, already proves a broad terminal-defect limit transfer for arbitrary unequal probabilities, so the scalar completion CDF is covered **as an application** and is explicitly credited. The assessed additional claim is the power-and-logarithmic scarcity threshold and joint last-type color law from two colored extremal point processes. Ilienko (2019), arXiv:1904.12954, proves uncolored point-process convergence for fixed multiplicity under uniform draws. Doumas (2025), arXiv:2510.25900, studies other two-class sampling and first-order expectations, while Neal (2008), Section 4, extends Poisson counts to fixed \(K\) copies. None of the inspected theorem statements gives this growing-quota sparse-class threshold and marked critical limit. A broader unpublished or differently presented marked extreme-value theorem could still imply it. Published priority has not been independently certified.

## Mathematical value — PASS

The number of rare types can be sublinear and still have strictly positive limiting probability of containing the last completed coupon. The theorem quantifies precisely how scarcity competes with arrival-rate disadvantage: the exponent \(\delta\) controls polynomial population size and the necessary exponent \(\eta\) supplies a nontrivial logarithmic correction. At the boundary, two distinct exponential slopes yield a non-affine-Gumbel completion law and a tractable last-class probability. This is a natural heterogeneous extension of recently studied growing-quota collectors, not an arbitrary finite instance; the sharp color phase adds information absent from general unmarked transfer results.

## Limits and comparison risks

The boundary \(ry=c\) and the regime \(ry<c\) are excluded. A precise leading multiplicative factor for the critical population depends on the floor-induced phase, and hence quantile calibration is retained. The result does not claim new general Poissonization, generalized terminal-defect, or Erlang extreme-value principles. Priority among all broad marked-extreme-value theorems remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
