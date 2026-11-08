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

# Verification of the tree critical-step theorem

The executable `verify.py` is a self-contained Python 3 script using SymPy and NumPy. Execute it in the same directory with `python verify.py`. Its symbolic tests independently reconstruct the matrices and their unit Perron vectors for the two-, three-, and four-vertex paths; enforce the cubic and quintic transverse center-manifold invariance equations; and compare the coefficients with the exact values \(c=1/8\), \(d=-(1+\sqrt2)/768\), and \(b=(17-\sqrt2)/96\) for the first nonuniform path. It also samples a nonzero center projection over 300,000 steps and compares the logarithmically corrected reciprocal-square expression at four times.

An actual execution returned `VERIFY_OK symbolic_graphs=3 cubic_and_quintic_center_invariance=3 critical_P4_log=17/96 - sqrt(2)/96`, followed by four finite numerical corrected partial values approaching a common limit (approximately 8.0313). This is an algebraic consistency check and finite illustration; the universal infinite-time statement is established by the proof in `RESULT.md`.

The main proof needs the strict scalar cosine remainder at the critical step, compactness of the torus, Perron simplicity for the tree's edge Gram matrix, the hyperbolic stable-set theorem for possibly noninvertible maps, analytic null-set preimage preservation, and the smooth center-manifold/strong-stable-foliation theorem. Verification of these general mathematical steps is analytical and not reducible to finite numerical output. Exceptional initial phases in the strong-stable set do not obey the inverse-square law and were intentionally excluded.
