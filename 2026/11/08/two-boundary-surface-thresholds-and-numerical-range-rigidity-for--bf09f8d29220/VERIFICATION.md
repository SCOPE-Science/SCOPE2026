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

The proof in RESULT.md gives all analytical assertions without invoking the diagnostics as an infinite-dimensional proof. The operator family is explicitly normalized as a forward shift on complex \(\ell^2(\mathbb N_0)\); the quantitative threshold concerns the top surface eigenvalue of its selfadjoint real part, and the final numerical-radius formula divides this eigenvalue by two.

The supplied `CHECK.py` uses only the Python standard library. Running it independently prints `PASS: 971 finite diagnostic assertions`; its tests cover the periodic-tail Weyl quadratic and edge limit, root residuals, presence and absence of isolated top eigenvalues, inertia-based largest eigenvalues of finite sections, the quadratic onset coefficient and fixed-energy monotonicity. These finite checks do not establish essential-spectrum statements or uniqueness of the infinite-dimensional root, which follow from the analytical proof.

Publication-priority limitations are recorded in REVIEW.md and AUDIT.json. No independent mathematical audit has been performed.
