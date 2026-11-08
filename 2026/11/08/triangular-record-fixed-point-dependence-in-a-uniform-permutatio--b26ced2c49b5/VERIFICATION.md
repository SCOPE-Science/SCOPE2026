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

# Reproducible checks

Run `python3 verify.py` with Python 3 and no additional dependencies. The script performs exact-rational comparisons of every entry of the record/fixed-point covariance matrix after complete permutation enumeration for \(2\le n\le8\), and exact sign/profile checks for \(2\le n\le99\). The tested package produced `TOTAL PASSED: 324079 exact rational assertions`.

The finite diagnostic does not substitute for the universal proof: the latter conditions on fixed-point locations and uses symmetry and pigeonhole arguments. No independent mathematical audit, formal proof assistant check or external certification was performed. The test does not verify historical priority.
