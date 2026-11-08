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

# Reproduction of the finite-step certificate

Run `python verify.py` with SymPy. The script checks exact identities over \(\mathbb Q(\sqrt2)\), including the three signed scalar contact points, the closed-form quadratic residual certificate, its strictly positive leading minor and determinant, and the zero at its unique minimizer. It also performs 3,000 seeded auxiliary numerical checks on random spectral measures; these finite tests do **not** prove the all-dimensional theorem.

The analytic bound is obtained from concavity of \(t-1/p(t)\) on \([0,1]\) and functional calculus for real symmetric matrices. The matching lower bound follows from positivity of the two-by-two quadratic coefficient matrix, with determinant \((3\sqrt2-4)/8\). No floating-point simulation or outside software is needed for the infinite-dimensional quantifiers beyond the explicitly stated elementary proof. There is no independent mathematical audit.
