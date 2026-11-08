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

Run `python verify.py` with Python 3 standard-library modules only. The checker uses exact rational midpoint coordinates for odd deck sizes from 3 through 63, verifies first/last cut formulas, inversion parity at the second cut, and checks the commutator supports for all positive powers. It also exhaustively builds the finite generated groups for deck sizes 3, 5 and 7. The observed output is `PASS finite exact midpoint/group checks: 31378`.

The proof for every odd size is the algebraic argument in `RESULT.md`, not an induction inferred from the finite checker. No quantitative mixing bound is claimed, and no independent audit has been performed.
