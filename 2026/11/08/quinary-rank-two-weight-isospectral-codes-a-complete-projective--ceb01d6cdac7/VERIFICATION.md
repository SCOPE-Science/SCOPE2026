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

Run `python3 check.py` from the directory containing the extracted files. The program uses only Python's standard library and exact integer/rational operations.

It verifies the group order, all seven projective cycle types, eleven equality-pattern orbit decompositions, an independent Burnside fixed-point count for each equality pattern, explicit codeword spectra for both length-six examples, non-equivalence through disjoint orbits, orbit sizes \(60\) and \(30\), and an exact minimum distortion of \(36/25\) over all projective changes of message basis. The last printed line is `ALL CHECKS PASSED`.

The infinite-length statement follows mathematically from the proved exhaustive pattern list and adding zero coordinates; executing the finite checker does not by itself prove an infinite theorem. Historical priority and the entire proof have not been independently audited.
