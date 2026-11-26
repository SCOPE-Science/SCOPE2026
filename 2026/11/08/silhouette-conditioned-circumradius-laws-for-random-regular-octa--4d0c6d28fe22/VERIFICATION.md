---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Central symmetry gives a least enclosing disk centered at zero; the largest projected coordinate-vector norm gives R²=1−t², t=min |U_i|. In the chamber a≥b≥c, the projected-vector relation makes the a-pair redundant exactly for a≥b+c, apart from null degeneracies. With c=t and the other two coordinates sqrt(1−t²)(cos φ,sin φ), the spherical Jacobian is one and the 48 chambers give 12/π. The lower angle is α(t), the chamber upper angle π/4, and the quadrilateral cap is φ≤β(t), closing at (2,1,1)/sqrt(6). Therefore L_4=(β−α)_+ and L_6=L−L_4 give the asserted joint tails of t; the change of variable to R reverses the tail. Computing the solid angle of the triangle-ray cone for the six-vertex event gives numerator |det|=2 and denominator 5 sqrt(2) in the half-angle formula, hence 4 arctan(sqrt(2)/5)/π across the eight octants. L_4/L strictly decreases to zero, so the normalized density ratio crosses one once; both sides have positive interval mass, giving strict interior stochastic order. The lower-width slopes at t=1/sqrt(6) and 1/sqrt(3) are sqrt(6) and 3 sqrt(3)/2, with t-to-radius slope magnitudes sqrt(5) and sqrt(2). The upper widths at zero are π/4+O(t) and t/sqrt(2)+O(t³). Integration gives all four joint coefficients and opposite jumps ±60 sqrt(6)/π. Inclusion–exclusion of the three coordinate bands yields the stated marginal; integrating its t-density against t² reduces to (2/π) times the integral of (1−q²)/(1+q²) over q∈[1/sqrt(3),1], giving the stated expectation. Read RESULT.md lines 62–100, VERIFICATION.md and the checker. Recorded Monte Carlo, convex-hull checks and quadrature were inspected, not rerun; the analytic argument proves the full Haar law.

## originality

PASS

Accept the joint circumradius/silhouette law and its derived conditional comparison and split endpoint behavior. The silhouette criterion and frequency and the unconditional minimum-coordinate law are not new. A distinct same-day record gives the identical unconditional n=3,q=1 CDF; no same-day priority order is inferred. The closest earlier joint law uses a different size statistic, and its actual coarea slices prove why it does not transfer to the minimum-coordinate joint law by a change of scalar variable.

## value

PASS

A classical rotationally random projection has two shape classes at the same upper radius endpoint. Their strict conditional ordering, different lower supports, and distinct linear versus square-root upper-tail orders give information no marginal reveals. The cancellation of opposite second-derivative jumps identifies a real transition in the split law that the marginal hides. This is an exact motivated coupling, not priority for single-statistic evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
