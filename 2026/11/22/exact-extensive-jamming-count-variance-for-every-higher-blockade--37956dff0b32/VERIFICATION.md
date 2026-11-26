---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the original-distance conflict graph the first accepted site leaves two noninteracting pieces with the stated A/B indices, including the zero-index B singleton. Conditional on the first choice (and its priority value), each surviving piece sees a uniform relative priority order, independently; these order laws do not depend on the first priority value. Total variance therefore adds the child variances and the nonnegative variance of the child-mean sum. Averaging gives the stated scalar ODE with homogeneous factor exp(-P_b(z))/(1-z)^2. The affine part of each child mean yields the same summed baseline for every root. In each row the deviations are one rapidly decaying sequence from each end, with finitely many terms for negative indices; their overlap and missing tails are supergeometrically small. Thus the first and second raw deviation sums each tend to a constant at supergeometric speed, giving kT_k=K_b+D_b/k plus a supergeometric error. Multiplying H_b' by (1-z)^2 leaves a polynomial from K_b and absolutely summable coefficients with finite first absolute moment from the second differences of 1/k, as well as the analytic remainder. Entire factors and integration preserve the needed summability for the numerator. Convolution with (1-z)^(-2) then gives V_k=nu_b k+O(1). The variance difference obeys the stated delayed contraction with O(1/k) toll difference, so both shapes have the same slope. At k=b the toll is (b-1)/(2b^2)>0, proving strict positivity in the convergent integral. Coupling A and the open ladder changes only two end vertices; any acceptance discrepancy propagates along strictly increasing priorities, with a factorial path-length bound despite exponentially many paths. On a two-row finite-range strip this gives a uniform second moment for the number of discrepancies, hence an O(sqrt L) variance transfer. Independent high-precision evaluation for b=2 gives 0.0267945787085631864907625185535257686419051279 at both cutoffs 80 and 160 after subtracting and integrating the endpoint tail terms; this supports the stated decimal without certifying rounding by intervals.

## originality

PASS

The supported distinction is the exact convergent variance coefficient for every fixed higher blockade and its b=2 evaluation, not the existing first-moment recurrence, nearest-neighbor fluctuation law, or general stabilization and Gaussian fluctuation framework.

## value

PASS

The dynamic second moment is a natural gap between exact higher-blockade mean results and nearest-neighbor counting laws. A positive variance per rung measures fluctuation amplitude, separates it from the density, and gives concrete numerical input for comparisons across blockade ranges. The positive quadrature also makes the coefficient accessible without trying to extrapolate finite ladder simulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
