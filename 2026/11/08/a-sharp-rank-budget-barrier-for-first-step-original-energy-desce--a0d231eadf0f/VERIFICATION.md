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

# Verification of the mathematical statement

The proof in `RESULT.md` is analytic. The attached `verify.py` requires NumPy and uses a fixed pseudorandom seed. Run with `python verify.py` to reproduce the 17,663 recorded numerical checks. It tests random positive-definite quadratic forms, arbitrary positive-semidefinite curvature operators (including noncommuting pairs), numerical Loewner-equivalence boundaries, objective descent inside the allowable range and arbitrarily small objective-increase witnesses outside it. It also checks that spectral truncation achieves the Courant–Fischer rank limit.

The exact illustrative example has \(H=\operatorname{diag}(9,4,1)\). For rank one choose \(L=\operatorname{diag}(9/2,0,0)\); for rank two choose \(L=\operatorname{diag}(9/2,2,0)\). Their residual largest eigenvalues are respectively \(4\) and \(1\), yielding universally safe first-step bounds \(h\le1/2\) and \(h\le2\).

**Limits of verification:** Finite floating-point tests cannot prove the infinite-dimensional or universal statements; these follow from the explicit algebra and Courant–Fischer proof. No independent mathematical audit has been performed. The theorem does not assert objective decrease in subsequent steps after the auxiliary scalar has been relaxed.
