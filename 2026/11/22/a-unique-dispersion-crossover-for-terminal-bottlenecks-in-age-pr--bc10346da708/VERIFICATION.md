---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At birth j+1 the prescribed edge gives the factor (1-q)/(1-q^(j+1)); the later lag caps telescope, giving b_j=rho P_j^(-m). Conditioning on a terminal cut independently truncates each later lag to the age relative to the new root. This gives the pair laws b_j b_(d-1) for finite start and rho b_(d-1) in the two-sided extension. For mixing, replace the whole past indicator vector by one computed from births through L; the two vectors can differ only if a later birth sends an edge through the boundary at 0, an event of probability at most m q^L/(1-q). The truncated past is independent of the far future. Bounded indicators and exponential mixing suffice for the stationary CLT. In the finite-start coupling each mismatching birth at t can change at most t indicators, and the L2 norm of the resulting total bound is at most sqrt(m) sum(t q^(t/2)); this transfers both the CLT and the linear variance coefficient. Summation of b_j-rho gives the stated mean and covariance sum; the stationary variance coefficient is strictly positive. S_m is continuous by locally uniform geometric tail control, strictly increasing in q and m, zero in the limit q down to 0 and already greater than 1/2 at q=1/2. For q=O(1/m), the first log-product starts q+3q^2/2, the second starts q^2, and the remaining terms total O(m q^3). Substitution at c/m+d/m^2 leaves residual O(m^-2) for c=log(3/2), d=-13c^2/6; the j=0 term alone gives S_m'(q)>=m, so the root error is O(m^-3). Independent bisection with backwards accumulation of -log(1-q^h) for h through 101 reproduces the three printed roots. Uploaded code was inspected, not executed; its finite exact checks are not the basis of the limit proofs.

## originality

PASS

Pass is for the explicit dispersion classification and its two-term frontier, not for Gaussianity in isolation. The same model, renewal structure, gap moments, and cut probabilities are already covered. Those facts give a standard implicit renewal variance and are enough to start a covariance calculation; their inspected statements do not give the model's Fano sign classification or the large-m location of its sign switch.

## value

PASS

The nontrivial output is a complete, strictly ordered dispersion frontier for the natural terminal renewal count. It tells when Poisson variance is too large or too small and quantifies the sensitivity of that boundary to multiplicity. The correction term is not a generic renewal CLT prediction: it depends on the first two different tail products. This is useful without treating the count as an online observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
