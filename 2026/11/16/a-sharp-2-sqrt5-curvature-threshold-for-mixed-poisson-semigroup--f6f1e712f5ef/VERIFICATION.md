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

# Verification details

The proof establishes all real-parameter cases by reduction of the second derivative to a rational level equation. The nontrivial quotient derivative factors by a quadratic with discriminant \(t^2-18t+1\), giving a complete root-collision classification. The positive witness uses an integer quartic and three disjoint rational brackets; Descartes' sign rule proves the brackets exhaust its positive roots.

Run `python3 check.py` in the directory with this file and RESULT.md. The checker requires only the Python standard library. It independently constructs the witness quartic from its factors, verifies six exact bracket signs and the Descartes sign pattern, performs **239** separate rational quotient-derivative comparisons, and evaluates discriminant signs on both sides of the critical threshold. These finite computations corroborate the exact identities but do not replace the general argument. No independent audit has been carried out.
