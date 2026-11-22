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

The package contains `verify.py` and `smith_ops.json`. Running `python3 verify.py` with Python 3 standard library enumerates the full geometric incidence model, replays all 2,710 elementary unimodular operations, compares every entry of the resulting 45-by-120 matrix with the claimed diagonal, and checks the order of each of 45 formal coordinate classes. It also checks the 120-pair support count and the 16, 4, and 1 incidence valencies. No finite-field sampling is used. The geometry-to-combinatorics reduction is explained in `RESULT.md`; the executable verifies the resulting finite integral calculation, not the entire textbook classification of smooth cubic surfaces. No independent scientific audit was performed.
