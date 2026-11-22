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

Run `python checks/verify.py` from the root of these extracted files with Python 3. No third-party libraries are needed. `checks/output.txt` contains the recorded successful output from the exact code embedded here.

The checker computes the group commutator by explicit coordinate operations and compares its full target-frequency table with the independent formula using generated subgroups and their coset sums. It tests lamps \(C_2\), \(C_3\), \(C_4\), and \(C_2\times C_2\); cyclic complements \(C_2,C_3,C_4,C_5\); and the noncyclic complement \(C_2\times C_2\). It also compares a separate cyclic divisor implementation against subgroup counts on four additional configurations.

These are finite checks. The arbitrary-group result depends instead on the spanning-tree proof of the image of a difference map and uniform fiber size. A finite search cannot establish originality, historical uniqueness, or independent certification. The largest exact comparisons are bounded by the enumerated configurations.
