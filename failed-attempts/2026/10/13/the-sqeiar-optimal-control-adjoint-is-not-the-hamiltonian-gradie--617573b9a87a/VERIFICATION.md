---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Write F=β exp(−U/N) S V/N with U=u1 I+u2 A and V=I+θ A. The exact derivatives are F_S=F(1/S−1/N+U/N²), F_Q=F_E=F_R=F(−1/N+U/N²), F_I=F(1/V−(u1+1)/N+U/N²), F_A=F(θ/V−(u2+1)/N+U/N²). Hence −∂H/∂R=(λ1−λ3)F_R+μλ6, not merely μλ6. The terms −λ1 u3S+λ2u3S contribute (λ1−λ2)u3 to −∂H/∂S, not (λ1−λ3)u3. The source verify.py constructs the full symbolic Hamiltonian and checks all six corrected equations; the discrepancy is structurally nonzero at positive interior states. The terminal Taylor analysis is consistent but not necessary for the counterexample.

## originality

FAIL

FAIL: Exact PRIOR public Resultary finding dated 2026-10-04, “Correct Pontryagin adjoints for a variable-population SQEIAR media-control model,” has the same model, same formulas for all six corrected costates, and the same two decisive discrepancies (missing recovered incidence term and miscoupled quarantine costate). Its complete RESULT.md was read. Current Oct-13 claim is covered regardless of title wording; adding terminal Taylor expansion does not create an independent new core theorem.

## value

FAIL

FAIL: The source-specific Hamiltonian correction has clear mathematical/applied significance but is already supplied by the earlier same-model published result, including generic nonvanishing on interior states. The additional near-terminal Taylor expansion merely illustrates that already-established nonzero term, rather than proving a distinct motivated new invariant or result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
