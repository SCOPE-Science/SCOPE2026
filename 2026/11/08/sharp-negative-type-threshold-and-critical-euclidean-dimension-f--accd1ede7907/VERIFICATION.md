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
# Reproducibility and limits

The theorem follows from exact Grassmann intersection numbers, the four-sector eigenvalue recurrence, and elementary sign comparisons written in RESULT.md. Run `python3 check.py` in the extracted package. The checker uses only the Python standard library. It independently enumerates all \(1395\) binary Grassmannian vertices at \(n=6\) and tests intersection parameters, checks exact sector eigenvalues and multiplicities for multiple \(q,n\), then approximates the critical root by bisection.

The finite tests are corroboration, not proof of all prime powers or all dimensions. The proof for all parameters is supplied separately; it does not depend on extrapolating the finite tests. Independent mathematical auditing has not been performed, and priority comparisons are bounded by source availability and search scope.
