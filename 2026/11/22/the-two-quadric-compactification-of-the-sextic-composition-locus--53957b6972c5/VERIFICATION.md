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

## Reproducible checks

Run `python CHECK.py` using Python 3 and SymPy. It expands the coefficient parametrization of the quadratic-after-cubic family, proves the two polynomial syzygies used to derive the projective union ideal, verifies the two elimination formulas giving the normal-crossing local equations (one chart at infinity), checks two Jacobian-rank witnesses, and independently compares the complete-intersection Hilbert-series coefficients with the Hilbert polynomial in a finite diagnostic range.

## What these checks do not establish

The finite diagnostics do not prove radicality of an arbitrary ideal, smoothness of the projective cubic scroll, or a statement valid for all degrees. Those assertions are proved in `RESULT.md` from the displayed determinantal model, height-two complete-intersection structure, generic reducedness, and local charts. The exact checks have no external service dependence other than SymPy.
