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

Checked the rephrased normalized theorem: rate rescaling gives iid unit exponentials, squared profile mass is at most one, and the characteristic-function tail remainder is controlled by the next ranked coefficient times the tail squared mass. The Bernoulli series is an L²-bounded martingale. The local centered mass increment has variance O(s_n³), leaving deterministic slope 1−θ on the s_n scale; the exact strict-crossing event gives weak convergence even for atomic limits. Nonzero third cumulant, or negative fourth cumulant when θ=1/2, distinguishes every nonzero profile. Power-sum and zeta evaluation at the harmonic endpoint and the single-heavy-weight example follow from the displayed coefficients. No time-moment limit is inferred. CHECK.py was inspected as finite corroboration, not executed.

## originality

PASS

The narrowed arbitrary ranked-profile theorem, including a Bernoulli series plus an independent Gaussian remainder of nonzero variance, survives the demonstrated Zipf overlap on the inspected evidence. This is not a finding of publication priority.

## value

PASS

The repaired result explains why diffuse weights give first-order universality but not necessarily Gaussian second-order fluctuations. Arbitrary profiles classify a mixed regime which cannot appear in the earlier Zipf family; this is substantive beyond the known endpoint transition and classical fixed-time limit tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
