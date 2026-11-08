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
The proof is analytic-algebraic and uses a genuine rank-matched projector subfamily, pole control, two-block incidence transversality, generic smoothness, cut-resultant avoidance and Riemann–Hurwitz. `verify.py` is a standalone symbolic checker requiring Python 3 plus SymPy (`python verify.py`). It recomputes the objective from block vectors rather than accepting precomputed critical polynomials, and checks polynomial degrees and greatest-common-divisor conditions, including the cut equation. The finite checks are not a substitute for the proof for unrestricted parameters. Independent audit has not been performed.
