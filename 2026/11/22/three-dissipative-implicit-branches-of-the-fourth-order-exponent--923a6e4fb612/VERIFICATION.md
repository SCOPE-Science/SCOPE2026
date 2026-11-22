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

`verification.py` uses only Python's standard library. Execute `python3 verification.py` to check the two degree-six Möbius substitution coefficient arrays by exact rational expansion, both sign endpoints of the polynomial, the exact rational lower bound \(606579/544000>1\), and three independently bracketed roots at \(t=20\) with 190-digit Decimal arithmetic.

The root brackets serve as a reproducibility sanity check, not a replacement for the intermediate value theorem, Descartes' rule, Rolle's theorem or the asymptotic comparison argument in `RESULT.md`. The true exact statement concerns all \(t\ge20\). The theorem does not prescribe a numerical implicit solver, prove that any particular initialization chooses a particular root, or assert a sharp onset threshold. Independent audit has not been performed.
