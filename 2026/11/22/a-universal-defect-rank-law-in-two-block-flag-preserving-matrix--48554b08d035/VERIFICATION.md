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

# Verification

The exact formula was separately replayed with the self-contained `checker.py`, which enumerates all \(q^{a^2+ab+b^2}\) matrices for each selected small case, performs modular Gaussian elimination and checks every \((r,s,t)\) stratum. Cases and observations are recorded in `checker_output.txt`. The checker also independently searches all potential von Neumann inner inverses for \(a=b=1\) over three fields. The Python checker uses prime fields and is not a proof of the prime-power or unbounded-size assertion; those follow from the linear-algebraic count, the section construction and dominated convergence. Other automated algebra or independent review is not claimed.
