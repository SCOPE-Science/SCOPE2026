---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The coordinate-generator invariant-measure proof is valid for arbitrary compactly supported invariant measures of the stated autonomous polynomial flow: integrating arbitrary antiderivatives of x,y,z gives all three regressions. Conditional-variance Pythagoras gives each squared-speed defect and the covariances; support y<=c follows from E[x^2|y]>=0. Equality rigidity uses bounded complete trajectories and the linear recovery/adaptation equations, not a finite simulation. On non-equilibrium-supported measures each correlation denominator is positive. The supplied standard-library checker independently read and its rational pointwise identities inspected; it does not itself certify the measure-theoretic argument.

## originality

FAIL

A directly published earlier SCOPE theorem on the identical Hindmarsh–Rose equations gives BOTH E[x²|y]=(c-y)/d and E[x|z]=x_R+z/s, BOTH corresponding sharp variance-speed defects, y<=c, and equilibrium-support equality rigidity. Full original RESULT.md was read. Claimed sign-locked covariance identities follow immediately by taking conditional moments, so no independent original substantive recovery/adaptation assertion remains; the additional E[y-z|x] generator identity is the same standard one-coordinate test applied to x. Thus the claimed centerpiece is covered, not merely an overlooked title match.

## value

FAIL

Although the identities are mathematically correct and relevant to bursting statistics, the old same-neuron published theorem already supplies the hard stationary disintegration, support and rigidity; deriving covariances and one further generator regression is routine conditional-expectation algebra and not a motivated new invariant beyond that dominating result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
