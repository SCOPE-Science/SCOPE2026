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

The portable Python verifier is `verify_triangular_matching.py`; use `python3 verify_triangular_matching.py`. It uses only the Python standard library, derives every input from the explicit graph definition and prints the expected lines in `verification_output.txt`.

It checks the face vector and graph definition, exhaustively topologically sorts the oriented 2,460-face Hasse graph, reconstructs 1,146 integral unit cancellations, checks the precise two determinant minors and characteristic-three rank, then enumerates the 120 graph automorphisms and computes complete rational irreducible multiplicities. The rank/minor evidence is sufficient to determine the **whole integral homology** of the reduced complex and, with the critical-cell dimensions and two-skeleton argument, its homotopy type.

The verifier establishes mathematical finite identities, not publication novelty or independent external certification. It does not calculate the integral action on three-torsion, the quotient's integral cohomology or any higher \(T_n\) cases.
