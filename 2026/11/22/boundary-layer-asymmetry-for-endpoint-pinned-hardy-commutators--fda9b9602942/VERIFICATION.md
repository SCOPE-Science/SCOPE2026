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

# Reproducibility and verification

Execute `python3 verify.py` with Python 3. No third-party packages are needed. The script uses rational arctanh-series bounds with explicit remainder control, establishes the positive/negative signs needed to locate the single three-ramp maximum, verifies a strict rational witness against the tent, and directly quadratures the original double-kernel Hilbert–Schmidt integral as an independent consistency check.

The infinite continuum maximum is proved analytically from the exact formula for the third derivative, the signs of the second derivative and the endpoint derivative data; finite quadrature has no role in certifying an infinity of parameters. The rational bounds certify the reported strict comparisons and the root interval. The root and energy decimals are approximations, not exact algebraic identities. The unrestricted endpoint-pinned Lipschitz optimization and historical priority beyond the inspected sources remain open to further investigation.
