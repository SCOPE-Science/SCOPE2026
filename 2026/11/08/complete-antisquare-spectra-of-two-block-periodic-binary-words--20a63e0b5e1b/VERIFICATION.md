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

# Verification and reproducibility

Run `python3 verify.py` in a directory containing the extracted standalone script. The script checks all positive pairs \(1\le a,b\le22\), and all \(1\le k\le4(a+b)\). For each triple it independently builds enough of the periodic host to extract every starting-phase length-\(2k\) factor, checks equality of the second half to the binary complement of the first, deduplicates actual strings, and compares with the theorem's formula. It also checks the circular mismatch criterion independently and sums every possible order in 462 unequal-run cases. The saved `checks.txt` gives the actual run output: 44,528 triple comparisons and 462 total-count comparisons, all passed.

A finite verifier does not establish the unbounded part of the theorem, nor does it certify novelty. The general proof uses interval geometry on a circle and a primitive-period argument; it covers arbitrary positive integers without reliance on numerical extrapolation.
