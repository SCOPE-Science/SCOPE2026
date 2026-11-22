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

The included `verify.py` was executed using Python with SymPy and NumPy and returned `FIR_HENON_POLYNOMIAL_VERIFY_OK`. Its checks include symbolic coefficient matching of the \((z+r)^n\) construction for \(2\le n\le7\), normalization and strict positivity of the taps, the fixed-point feedback normalization, direct companion-Jacobian characteristic-polynomial checks for \(2\le n\le5\), and floating-point stability diagnostics for selected small-feedback gains. Exact polynomial identities, not the ill-conditioned finite-precision roots of high-multiplicity polynomials, are the critical computational checks.

The proof in `RESULT.md` supplies the all-parameter argument for the spectral-radius lower bound, uniqueness, small-feedback existence and negative-branch instability. The checker does not assert exhaustive numerical sampling, full nonlinear stability at a neutral endpoint, global attraction, or an independent audit.
