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

# Reproduction

Execute `python3 verify.py` using Python 3.10+ (standard library only). The 21-vertex graph uses label \(3i+c\). The script enumerates every face, constructs all signed boundary incidences, checks all oriented Hasse relations for directed cycles, constructs the exact integer Morse boundary, verifies its unit minor and rank, and separately reduces the full mod-two boundary matrices. The supplied `verification_output.txt` records the observed result.

Acyclicity is an exhaustive finite certificate on 5282 faces and 25242 Hasse cover relations, not a non-exhaustive sampling claim. Integral homology follows from the exact signed Morse matrix and its unit minor, not only from mod-two ranks. The homotopy splitting uses the fact that the Morse CW complex has cells only in dimensions zero, three and four and that its attaching maps into a wedge of three-spheres are determined by their integral degrees.

No independent external audit was performed. Reproduction requires ordinary Python execution, not a third-party theorem prover.
