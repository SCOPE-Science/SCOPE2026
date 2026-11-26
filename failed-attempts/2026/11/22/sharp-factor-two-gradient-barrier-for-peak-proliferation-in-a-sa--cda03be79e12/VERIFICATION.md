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

The stationary current is constant and integrable (bounded speeds and integrable densities), hence zero. Solving the flux ODE gives a positive even analytic density with exponential tails. Its derivative on x>0 has the sign of A−H_q(ux). The log derivative of h_q is 2q/sinh(2qy)+3 tanh(y)−coth(y); the first term decreases in q, and h_2=2/(1−tanh^4(y)) strictly increases on the positive half-line. Thus H_q strictly increases to infinity for q≤2, including strict central maximality when A=H_q(0). For every fixed q>2, taking gamma_0=gamma_1=b, v_1=u=1 and v_0=L>max(1,3/[q(q²−4)]) makes H_q/b decrease locally at zero by the quadratic Taylor coefficient. Choosing b between the reciprocals of the two levels forces derivative signs −,+,− on the positive half-line; analyticity makes the sign-changing extrema strict, and reflection gives the additional peak. The q=5/2 witness independently gives H(0)=126/125 and H(atanh(1/3))=(43281−9072√2)/31000<1, by 2·9072²−12281²=13779407>0.

## originality

FAIL

A distinct indexed record states the same sharp factor-two theorem, including the universal one/two-peak classification and the existential converse for each supercritical ratio in this model. The exact q=5/2 worked example differs but is a certificate for the covered theorem, not a distinct final research claim. Both records carry the same date, which does not establish who was first or whether the derivations were independent.

## value

PASS

Assessed on mathematical substance separately from originality: a universal gradient boundary removes the prior unproved ceiling assumption on a full parameter region, and the converse certifies sharpness without claiming all supercritical cases are multimodal. This is a meaningful modality boundary, not just another worked example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
