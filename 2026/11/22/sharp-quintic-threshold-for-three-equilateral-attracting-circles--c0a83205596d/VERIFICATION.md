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

# Verification evidence and limits

The standalone `checks/check.py` uses SymPy to check exact equalities for the explicit quintic field and the equilateral special case of Cao--Llibre's full quartic normal form. It verifies degree exactly five, the coefficient \(-\sqrt3/20\) of \(x^5\) in the first component at \(y=0\), divisibility of \(X(f_i)\) by \(f_i\), exact center angular values, and all three symbolic small-radius Floquet coefficients. It also checks cancellations of the quintic and sextic terms in the quartic normal form. The analytic sign lemma for quartic fields, its exclusion of three negative Floquet logarithms, and uniform existence of a sufficiently small radius range are established in `RESULT.md` and are not replaced by the checker. No optimal radius threshold, global phase portrait, or independent audit is claimed.

To reproduce, run `python checks/check.py` in an environment with SymPy installed. No network access is needed by the checker.
