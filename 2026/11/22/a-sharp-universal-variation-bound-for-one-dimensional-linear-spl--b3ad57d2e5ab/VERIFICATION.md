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

For real BV on the open interval, the signed derivative measure represents f almost everywhere as a constant plus an integral of unit steps. The projector fixes constants and, evaluated at knots, is a finite-dimensional linear map; integration and the triangle inequality reduce the variation seminorm to the largest step gain. Multiplying the hat Gram equations by six gives the displayed tridiagonal coefficients and the endpoint relation 2p_0+p_1=0 on an exterior zero tail. The elimination ratios h_i/[2h_i+(2-rho_(i-1))h_(i-1)] are positive and at most one half, so alternating differences sum to at most three times the edge magnitude. The right tail uses p-1, with zero and empty tails covered. Integrating the hats over the post-jump part of the central cell gives 3(1-u)^2 and 3(1-u^2) after scaling by six and dividing by cell length; subtracting the background one at the right knot yields F,G as stated. The two nonnegative Schur corrections preserve the inequalities used in the four sign cases. In the same-sign cases, s+2t_0<=1 or 2s+t_0>=-1 both certify a nonnegative central increment and bound the weighted sum by three. In the opposite-sign cases the required estimates are s-t_0<=F-G<=1 or t_0-s<=G-F<=1/2. These hold also for u=0,1 and if either exterior tail is absent. For the midpoint on the symmetric graded family, the Schur corrections vanish at fixed m, giving s=-1/4 and t_0=1/4 in the limit; each successive ratio tends to 1/2. Thus the limiting total is 3-3/2^(m+1); taking the stated ordered limits proves sharpness. The package's rational Gram-system checker and logged counts were inspected without execution; those cases support the argument but do not prove the universal inequality.

## originality

PASS

Established for the real, unweighted variation seminorm on arbitrary finite strictly positive meshes and its sharp constant and witness, not for the classical Lebesgue projector norm or for spline stability in general. The strongest primary overlap has the same spline space, number and geometric knot idea in a different operator norm. The closest published same-seminorm result fixes the doubly infinite uniform grid; it is not a dominating mesh theorem. No inspected result implies the claimed arbitrary-mesh sharp variation constant.

## value

PASS

Uniform control of jumps under a continuous reconstruction is a natural endpoint stability question on adaptive or strongly graded meshes. The theorem supplies the exact mesh-uniform variation cost without a mesh-ratio hypothesis, and its explicit one-jump construction explains why three is necessary. It is stronger than finite mesh checks or a nonsharp boundedness assertion, with relevance to BV-preserving approximation rather than simply duplicating max-norm stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
