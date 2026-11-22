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

The included standalone program `check_idempotent_derivations.py` was run using Python 3 with no third-party dependencies. It exhaustively constructs each admissible coefficient vector and checks the original Leibniz rule, composition idempotence, normal-form equivalence, and matrix rank in 16 finite-field/truncation cases. Every case passed and the program printed `IDEMPOTENT_TRUNCATED_DERIVATIONS_VERIFIED`.

The argument for arbitrary field and truncation length is a symbolic valuation proof, not an extrapolation from those checks. The reduced solution-locus description does not imply the unreduced parameter scheme is smooth. Publication priority is provisional.
