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

# Reproducibility

Run `python3 artifacts/verify.py` using only the Python 3 standard library. The command prints `CYCLE_SECOND_RADIAL_SHELL_CHECKS_PASSED exhaustive_vertex_profiles=71768 gap_formula_profiles=1334 orders=12` on success. It uses `fractions.Fraction` throughout, enumerates all cyclic facet step words for every order 4 through 15, checks both distinct leading norm levels and their exact multiplicities, and tests the exact deficit identities for representatives through half-order 30. The all-order strict-concavity and integer-endpoint arguments in `RESULT.md` supply the proof; a finite check alone does not prove them. No independent audit or external certification has been conducted.
