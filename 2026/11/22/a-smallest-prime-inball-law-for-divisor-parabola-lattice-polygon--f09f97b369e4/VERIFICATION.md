---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The packaged `verify_inball.py` implements independent 65-digit decimal distance and tangency calculations using the closed-form formula, over \(2\le h\le2000\), with 15,517 lower-facet comparisons. Its successful output was reproduced from the assembled JSONL record after decoding the embedded checker. A separate numerical LP calculation directly optimized unrestricted center coordinates for 149 polygons and 591 selected deletion polygons; those supplemental experiments are not necessary dependencies.

The universal proof is analytic: exact facet equations, strict monotonicity of \(R_h(a,b)\), uniqueness from three support constraints, and the arithmetic identity with a uniform error less than \(1/(2h)\). The finite checks are not a proof of infinite quantification. The supplied program is standalone and needs only Python's standard library. No external audit has been performed.
