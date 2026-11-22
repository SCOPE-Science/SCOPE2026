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
Run `python3 verify.py` using a standard Python 3 installation and compare with `verification_output.txt`. The direct calculation enumerates first and second superdiagonals and multiplies the relevant paths. A second calculation counts the rank of the linear form conditional on the first band; it avoids the direct second-band enumeration. The independently implemented finite tests cover \((n,q)=(3,2),(4,2),(4,3),(6,2)\) directly and \((4,2),(4,3),(6,2),(6,3),(8,2)\) by the linear-form method. This is finite experimental corroboration, not an independent audit or a proof of the all-parameter statement. The symbolic combinatorial proof is in `RESULT.md`.
