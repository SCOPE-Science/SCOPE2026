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

# Verification of the alternating-grid BDF3 result

Run `python verify_bdf3.py` using Python 3 (standard library only). The included `verification_output.txt` contains the output from the checked script. It carries out 163 exact rational or interval assertions on eleven positive rational step ratios and several shape parameters. It also isolates the unique positive quartic root by bisection with 70-digit decimal precision; uniqueness and all-ratio spectral stability are proved in the manuscript, not inferred from a finite sweep.

The check reconstructs the first-derivative stencil as the exact solution of a four-node rational Vandermonde system, verifies the exact recurrence parameters and transfer invariants, tests phase-reversal invariance, checks the three rescaled Jury numerators, and confirms the bracket for the sharp optimum.

The proof's global steps requiring mathematical review are the polynomial identities for the Floquet invariants, the strict Schur/Jury implication, Descartes' unique-positive-root argument, and strict monotonicity on either side of the discriminant root. These are worked explicitly in `RESULT.md`.

No claim of an independent or external audit is made. A more general adaptive mesh with nonperiodic ratios, nonlinear stiffness, or uniform-in-r transient bounds has not been verified.
