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

Run `python verify.py` with Python 3 standard library. It independently enumerates all \(t\)-subsets of each labeled cycle union obtained from each nondecreasing cycle-length partition for \(3\le n\le11\) and \(0\le t\le n\), then compares first three exact falling-factorial moments with the analytical expressions. It additionally verifies the exact \(6\)-vertex probability distributions, the shared variance, and the coefficient identity for all enumerated cases with \(n\ge6\). Expected output includes `PASS 239 exactly enumerated (cycle partition, deletion count) cases`.

The proof of all-order validity is combinatorial; finite enumerations are cross-checks and cannot establish an infinite family by themselves. No independent review or external certificate is asserted.
