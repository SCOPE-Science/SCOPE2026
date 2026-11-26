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

The integrand is Lipschitz in sigma with an integrable bound proportional to |Z|; the moving clipping point is a Gaussian null event. Pairing Z and -Z separates D' into a positive integral on (0,A-epsilon) minus a negative contribution from (A-epsilon,infinity). As a function of inverse variance lambda=1/(2 sigma^2), the derivative of log(N/P) is the mean u^2 under P minus the mean under N and is strictly negative. For small sigma one may lower-bound P on any fixed compact subinterval strictly inside its support; this dominates the exponentially smaller negative tail. For large sigma, P is bounded while N diverges monotonically, since its unweighted integrand is asymptotic to 1/(tu). Thus the unique zero is strict. Dominated convergence gives the half-floor limit, and strict decrease after the maximum gives the zero-noise comparison including equality. The mean-field velocity has sign rho-d, whose sole zero is 2-sqrt(2); both endpoint signs and the intermediate opposite sign are certified. Independent rational Machin, alternating-series and Jensen bounds gave D(1)>0.59426664>0.59, and independent quadrature gave roots 0.1477881754700885 and 6.480171581268562. The two-root proof does not depend on numerical quadrature.

## originality

PASS

The supported distinction is the exact global peak and crossing classification of the floored reciprocal-Gaussian expectation, and its rigorous two-crossing application to a specified existing mean-field closure. The mortality rule, lower floor, closure, and the generic reentrance phenomenon are not new. The nearest inspected annealed-noise calculation is a local Taylor approximation; it does not give the exact tail or sign pattern at all intensities.

## value

PASS

A small-noise expansion cannot answer what happens at large fluctuations or how many times the formal viability sign changes. The exact mortality theorem identifies when a return below the baseline exists, and the certified example shows an actual pair of distinct mean-field thresholds instead of relying on an extrapolated phase diagram. The value is in the provable model-level boundary, not an asserted biological or spatial survival consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
