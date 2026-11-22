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

Execute `python3 verify.py`. This is a reproducible standard-library computation using exact `fractions.Fraction` intervals, not floating-point testing as a substitute for proof. It checks the ecological root bracket with opposite endpoint signs, the negative derivative on that bracket, positive strategy densities, Jacobian bounds, negative trace and positive determinant, and the existence of exactly two distinct modal-instability boundaries in the stated rational intervals. The two boundary roots are simple because their intervals are disjoint and the determinant polynomial is quadratic.

Proof obligations not discharged by finite computation are in RESULT.md: the nonzero weighted-star Laplacian spectrum is bounded by its ordered conductances using the incidence Gram matrix and the Courant–Fischer principle, and each positive Laplacian eigenmode contributes at most one instability interval for fixed two-species kinetics. Those arguments hold for all positive integers \(m\), not just tested network sizes.

All extrapolation to empirical social behavior, nonlinear patterns, and equality-point stability is explicitly outside the theorem. The scientific review is a self-review; independent audit was not performed.
