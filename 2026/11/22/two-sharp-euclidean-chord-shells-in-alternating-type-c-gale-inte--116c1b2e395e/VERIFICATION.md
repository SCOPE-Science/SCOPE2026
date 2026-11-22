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

Run `python check_chords.py` with Python 3.9 or later. The program enumerates feasible zero-one vectors via all suffix bounds and computes exact squared distances by bitwise Hamming counts. It compares all pair distances with the analytic top-two-shell multiplicities for \(1\le r\le6\); the dimension-two case is an extra boundary check. A second ordered-pair walk-state dynamic program checks the same formulas for \(1\le r\le15\) without enumerating full vertex pairs. The certificate is finite corroboration of the explicit unbounded combinatorial proof in `RESULT.md`, not an exhaustive proof across all dimensions. No external validation has been performed.
