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

The exact linear-algebra identity was checked with a standalone standard-library Python program `check.py` distributed beside the main result. Run `python3 check.py`. It independently compares rational Gaussian elimination against a parity-union-find criterion, exhaustively enumerating eight small hash/sign models and five reproducible finite-sample simulation settings. Successful execution prints `EXHAUSTIVE_RANK_OK` and `VERIFY_OK`.

The eight exhaustive ranks yield \(2/2,2/4,0/8,8/8,56/64,336/512,306/324,4896/5832\) for the parameter pairs specified in RESULT.md. The sample checks compare only finite sizes and have intentionally generous tolerance. The asymptotic probability and critical transition are **proved analytically**, not asserted on the strength of simulations.

No external or independent validation was conducted. The remaining conceptual risk is historical priority within signed-graph enumeration and bipartite 2-XOR models. The full-rank law says nothing about a positive minimal singular value.
