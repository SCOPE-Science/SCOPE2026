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

# Verification of the adjugate norm identity

The analytical proof is in RESULT.md. The critical steps verified algebraically are the rank-one mixing factorization, the adjugate product identity, separate convexity in stochastic columns, and the three possible deterministic-map ranks. The existence of invertible approximants follows by replacing the repeated deterministic output with a convex combination including the omitted state.

Run `python3 check_markov_adjugate.py`. The checker uses only the Python standard library, constructs cofactors directly from signed permutations, and computes exact rational induced matrix norms. Recorded execution: `MINORIZED_MARKOV_ADJUGATE_EXACT_CHECK_OK 1253`. This is finite corroboration, not proof of the quantified theorem.

The source dated 20 August 2026 motivates the volume-weighted inverse inequality. The theorem proved here neither verifies nor extends the unrestricted asymptotic conclusion from that work. Independence and external certification have not been performed.
