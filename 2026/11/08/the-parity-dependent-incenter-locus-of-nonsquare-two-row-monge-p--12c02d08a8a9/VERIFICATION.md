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

# Verification record

The analytic proof in `RESULT.md` establishes the all-parameter claims. The supplementary `verify_monge_two_row.py` is independently runnable with Python 3, `fractions` from the standard library and (for LP tests) NumPy/SciPy. Run `python verify_monge_two_row.py` in the extracted package directory. On the reported execution it returned `PASS: 12661 exact/LP assertions, m=2..18 LP, m=2..50 exact`.

The exact-arithmetic checks verify row-difference formulas, total excess mass, adjacent slacks, and predicted zero-coordinate counts. A separate finite integer enumeration exercises the lower bound for dimensions two through five over the explicitly limited range used by the script. Numerical linear programs search the **full** polytope for dimensions two through eighteen and compare both inradii and center-coordinate extremes.

Finite checks do not prove infinitely many cases. No computational algebra black-box is needed for the discrete total-variation inequality or its equality characterization. No independent audit was performed.
