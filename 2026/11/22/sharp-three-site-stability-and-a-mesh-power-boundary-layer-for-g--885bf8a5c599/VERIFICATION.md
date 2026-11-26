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

Cancelling the common signed factor makes the blend positive for every allowed parity. On each open cell there is exactly one negative cardinal weight, so the unrestricted norm equals 1+2 max(H_gamma(a),H_gamma(1-a)). For nondecreasing data the left cell lies at or below y_1 and the right at or above it, and the exact lower and upper defects are respectively H_gamma(a) for (0,0,1) and H_gamma(1-a) for (0,1,1); the common worst-sign bound is attained, not necessarily by both signs away from the midpoint. The interior maximum yields strict increase of H_gamma with a, hence unique minimax at 1/2. The midpoint derivative gives the stated unique t_gamma and strict decrease with gamma. Independent bisection at gamma=2 gave t=0.5436890126920764 and norm 1.134884497736246. The outer limit follows by splitting the weight at 1/2 +/- eta. In inner variables compact convergence is uniform; for z<=0, log((1+2z/gamma)/(1-2z/gamma))<=4z/gamma gives an exponential tail, and near z=beta the prefactor vanishes. The limiting maximum at 4(beta-z)=1+exp(4z), followed by reflection, gives the stated Lambert W formula and includes the centered limit.

## originality

PASS

Passed for the exact arbitrary-placement three-site optimization, including odd and even powers and the fixed/off-center and moving-mesh laws. The classical midpoint constant at gamma=1 is background, and the even-power midpoint monotone defect overlaps a distinct same-day Resultary finding; neither is given independent novelty credit. The available comparison does not establish coverage of arbitrary three-site placement or the coupled power/placement limit. No order is inferred from the shared date.

## value

PASS

The smallest grid with extrapolatory local blending is a useful sharp model: the norm exactly measures worst-sign monotone range loss, and the midpoint high-power improvement is unstable at fixed off-center placement. The moving-mesh limit resolves which displacements retain O(1/gamma) amplification and gives its exact crossover coefficient on that scale, beyond the classical constant or the uniform-grid overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
