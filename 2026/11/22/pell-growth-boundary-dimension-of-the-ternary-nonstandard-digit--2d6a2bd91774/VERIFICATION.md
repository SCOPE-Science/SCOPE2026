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
# Reproducibility checks

Run `python3 verify_boundary.py` with Python 3 and only its standard library. The checker returns the exact string beginning `TERNARY_BOUNDARY_CERTIFICATE_OK` on success.

The code independently constructs the three-state carry transitions from the actual digit mapping \(0\mapsto0,1\mapsto1,2\mapsto5\), forms all six reachable mixed preimage states, checks both absorbing outcomes are attainable, verifies the six-by-six matrix, enumerates all ternary words up to length seven by direct carry composition, and checks the matrix count recurrence up to length 110. The verified values through length nine are \(1,3,8,20,49,119,288,696,1681,4059\).

The finite checks are corroboration, not a proof of a universal identity. For the infinite argument, inspect `RESULT.md` Steps 1–4: the rational-function inversion of \(I-zT\), the exact characteristic polynomial \((t-1)^3(t+1)(t^2-2t-1)\), the shrinking exceptional cylinders, and the Perron–Frobenius Frostman measure. No independent external mathematical validation is claimed.
