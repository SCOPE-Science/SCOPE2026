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

# Reproducibility and verification

Execute `python3 verify.py` alongside `RESULT.md`. Python standard library only. The checker evaluates the original GL recurrence and the full four-phase linearized GL recurrence at the claimed root on 24 finite order/memory pairs; independently verifies the quadratic determinant changes sign across the root; checks the classical endpoint; and evaluates the predicted large-memory coefficient on nine combinations. A successful run prints `VERIFY_OK four_phase_cases=24 asymptotic_orders=3 memory_lengths=3 endpoint_q1=1`.

The analytical argument proves for every \(0<q\le1\), integer \(M\ge2\), that exactly one primitive two-cycle negative-unit Floquet resonance exists above its birth parameter. The asymptotic limit and \(M^{-q}\) correction are proved for each fixed \(0<q<1\). Numerical checks do not certify any infinitely quantified statement.

The result does not claim a generic period-four branch, all multipliers inside the unit disk, or an exact periodic orbit of an infinite-memory map. Independent validation has not been performed.
