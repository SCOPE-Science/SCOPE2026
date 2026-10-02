---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The linear part has determinant 0.28 and complex conjugate eigenvalues of modulus rho=sqrt(0.28), hence is real-conjugate to a similarity. The inspected certificate gives 16 level-4 words, pairwise separation lower bound 0.20467744730049284 for squared transformed-center distance versus 0.19407316994622348 for (2 r_4)^2, and 16 rho^4>1.25439999999888>1. Thus the level-4 subsystem satisfies strong separation and has similarity dimension log(16)/(4 log(1/rho))>1, so the original attractor has Hausdorff dimension at least 1. The finite certificate has comfortable margins.

## originality

PASS

No checked source or Resultary record was found to state the exact lower bound for this exact affine cell. The primary literature gives much broader conditional dimension theorems, not the level-4 16-word certificate.

## value

FAIL

The exact matrix entries (0.7,0.4), angle 1 radian, triangle translations, and selected level-4 subsystem are not tied in the inspected record or literature to a prior natural classification boundary or independently motivated invariant. The result is a routine finite OSC/Moran lower-bound certificate for one arbitrarily parameterized cell, with no general mechanism, sharpness, or canonical threshold. Correctness and apparent novelty do not by themselves supply the substantive motivation required for a narrow exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
