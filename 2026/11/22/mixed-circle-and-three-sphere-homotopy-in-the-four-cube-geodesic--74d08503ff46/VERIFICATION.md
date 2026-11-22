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
# Reproducible verification

Run `python3 q4_gp_verifier.py` using Python 3.10 or later (standard library only). The code exhaustively checks each of \(\binom{16}{3}=560\) vertex triples, each of \(2^{16}-1\) nonempty vertex subsets, the complete matching, all codimension-one incidences, and acyclicity of the entire directed Hasse digraph. A 432-vertex complete topological sort certifies the last assertion. The program also checks the Euler characteristic. A log by itself is not evidence; the included executable enumeration and the explicit matching rule are the certificate.

The mathematical deduction from the verified matching uses Forman's CW reduction: forty 1-cells, zero 2-cells and nine 3-cells imply a wedge of circles and three-spheres. The verification proves only this fixed graph; it does not certify a family of higher-dimensional cubes. This is a self-reviewed result without independent verification.
