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

Execute `python3 verify_f4.py` with standard Python 3. The program has been run successfully against the packaged source. It reconstructs all \(1,152\) Weyl matrices, checks simple-reflection involutions, computes all \(48\) roots and the \(24\) positive roots, verifies the length-inversion equality for every group element, and reconstructs every lower Bruhat interval by a complete reduced-subword recurrence. It checks the longest-interval Poincaré polynomial against the exponent product \([2]_q[6]_q[8]_q[12]_q\). It then checks the maximum \(252\), the two equality cases, their length \(18\), diagram automorphism, involutivity, common Betti coefficients, lower-half opposite differences, and runner-up value \(249\).

All arithmetic and comparisons are exact integers. The proof uses an exhaustive finite enumeration and is not a general all-rank theorem. The package does not claim independent review or an independently implemented second enumerator.
