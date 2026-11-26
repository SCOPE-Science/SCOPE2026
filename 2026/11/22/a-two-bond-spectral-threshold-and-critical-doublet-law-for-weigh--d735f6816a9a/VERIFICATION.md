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
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification and scope

The analytic sign brackets and exact product identity in `RESULT.md` prove both limits. A finite check of the detuned approximation can use monotone bisection in \(t>0\) for \(m\operatorname{expm1}(2t)/[-\operatorname{expm1}(-(m-1)t)]=2+s/m\) whenever \(2+s/m>2m/(m-1)\). Compute the gap as \(2\sinh^2(t/2)\) to avoid cancellation. For \(m=32,128,512\), respectively, the fourth-order scaled gaps at \(s=3\) are approximately \(0.382313,0.468264,0.491914\) (limit \(0.5\)), and at \(s=5\) are \(3.686888,4.282403,4.444656\) (limit \(4.5\)). The exact criterion rules out the branch at \(s=2\). These finite values illustrate convergence; the arbitrary-detuning assertion is proved by the uniform Taylor remainder, not the finite checks.
