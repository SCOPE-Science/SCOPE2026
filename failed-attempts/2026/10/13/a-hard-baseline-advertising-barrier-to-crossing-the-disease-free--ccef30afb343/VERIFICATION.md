---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the main claim (R0 > 1), the printed reproduction number agrees with the frozen formula. Let b=(R0−1)c and D=cp+(lambda+c)M0>0. Then D(R1−1)=bp+(b−lambda)M0. This gives the iff for existence of a finite baseline, strict inequality beyond the unique crossing, and the nonattainment of 1 at finite baseline when lambda=b. The derivative is −R0*c*lambda*p/D² and the limit is R0*c/(c+lambda). Exact substitution of the publisher's Table 1 gives R0=7500/4001, M0,c=1698.1028207187…, R1(500)=1.3026792112… and lambda,c(500)=0.0239061895…. The checked threshold is local, as in Theorem 4.1. The aside at frozen RESULT.md line 96 should say 'at or below one' at zero baseline when R0≤1; at R0=1 and M0=0 it equals one, and any positive baseline gives strict inequality. That aside is outside the main R0>1 claim.

## originality

FAIL

The main result is a direct implication of the same model's published exact R1 formula: subtract one and clear the strictly positive denominator to obtain a linear polynomial in M0. Its leading coefficient gives the reachability barrier and its root is the contour already plotted by the source. The source passages read do not state the general barrier in that wording, but the frozen result adds no hypothesis, model, or nontrivial implication beyond the exact published expression. A separate Resultary record exhibits the same boundary and numeric threshold in a different limiting endemic-equilibrium problem; neither identity of the models nor priority follows from that match.

## value

FAIL

The saturation warning is useful as an explanation of the published model, but the frozen work is the one-step inversion of an already explicit linear-fractional contour, with its numerical substitution. It does not establish a new dynamical, empirical, or policy result, and the precise Table 1 crossing is mechanically implied by the motivating equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
