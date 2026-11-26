---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Strict convexity of squared distance in each coordinate forces every maximizing pair to consist of vertices. Compactness gives a deficit away from fixed disjoint pair neighborhoods. At each ordered pair the positive inward projections give s >= c(|u|+|v|), hence |w| <= C s. In the local cone neighborhoods the exact deficit is (2Ds-s^2-|w|^2)/(D+distance) >= s/2 for sufficiently small s. Thus the scaled tail is bounded uniformly in epsilon and the finite polytope truncations are irrelevant. The local radial threshold near t=1 on the compact level S=1 is 1+epsilon H/(2D)+O_K(epsilon^2); the radial inequality is decreasing on the entire bounded range for small epsilon. The quadratic may have a distant second root, so uniqueness is local, not global in t. Radial integration and degree-two homogeneity give the factor (2d+2)/(2D) multiplying the integral of H over S<=1. Beta integration of measures with cumulative moments A t^d, M t^(d+1), Q t^(d+2) gives both Gamma ratios and the negative transverse cross term. Reversing the ordered pair leaves the integral unchanged. Each A is positive and H is nonzero off a proper linear subspace in dimension at least two, giving strict positivity. As an independent check, cube coordinate deficits have density 2x on [0,1]; setting x_i=epsilon sqrt(d) t u_i with simplex angles u gives Dirichlet(2,...,2) and the first two coefficients in ratio d(d-1)/(sqrt(d)(2d+1)), with C0=2^d d^d/(2d)!. This matches the cone formulas and in d=2 gives 2/3 and 4/(15sqrt(2)).

## originality

FAIL

The full frozen law has demonstrable equivalent catalogue coverage for d>=2, including both coefficients, their signs, the error order and nonunique longest segments. The invariant cone-moment packaging eliminates explicit triangulation from the notation but is the sum of the same simplex-piece integrals and yields no distinct theorem. This is a determination of coverage in the inspected catalogue, not a claim that its later-dated entry has historical priority over the frozen text.

## value

PASS

The general fixed-pair asymptotic quantifies a natural geometric probability problem. The second positive coefficient detects transverse displacements not captured by just the first cap volumes, and summing across all maximizers makes the result useful even when longest segments are not unique. This is structural mathematical value; the audit does not credit the equivalent rewrite as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
