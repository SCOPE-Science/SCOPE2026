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

The exact code `verify_projective_rook.py` constructs the monoid elements as finite partial injections with coefficients represented by residues modulo the phase-group order. Multiplication and exponentiation are implemented from scratch. For each candidate matrix, the program calculates the complete pair of lists of left and right \(n\)-th powers over all possible multipliers, then partitions matrices by equality of those entire signatures. It checks each observed class against a single global phase orbit, verifies the full formula for the quotient cardinality, and compares marginal elements with the class of each diagonal support projection.

The cases \((m,n)=(1,3),(2,3),(2,5),(3,3)\) cover 4, 31, 71 and 352 monoid elements respectively. The resulting quotient counts are 2, 11, 15 and 118, and margin counts are 4, 10, 16 and 22. The program also tests directly that \(I_2\) and \(\operatorname{diag}(i,-i)\) lie in the same \(x^4\)-marginal-equivalence class despite not belonging to one scalar orbit, by checking both power identities against all 49 multipliers in the four-phase degree-two monoid. The recorded program output ends with `VERIFY_OK`.

Verification is exact finite arithmetic, with no floating-point roots of unity. Finite tests are corroborative; the proof in `RESULT.md` establishes the theorem for all odd parameters. The code and output are part of the same complete package, and independent audit is not performed.
