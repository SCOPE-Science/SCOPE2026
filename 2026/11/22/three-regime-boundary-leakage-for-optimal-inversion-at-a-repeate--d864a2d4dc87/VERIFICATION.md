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

# Verification notes

The general claim is proved in `RESULT.md` by a finite Gramian representation, a weighted Hilbert-moment limit, rational interpolation of the limiting moments, uniform Abel/Dirichlet summation estimates, and exact nonzero endpoint constants. The uniformity required by the theorem is on a compact subset of the closed unit disk separated from the boundary zero; the estimates in the proof have constants depending on this separation, the fixed weight, and the fixed multiplicity.

`verify.py` is a standalone finite diagnostic for the formula. It requires Python 3 and `mpmath`, and checks the exact moment constraints for finite degree, the limiting Cauchy-matrix endpoint constants, and the three normalized boundary profiles at several degrees, repeated-root multiplicities, and two complex boundary points. Its finite checks are illustrative and do not establish infinite-degree uniform convergence or historical priority.

The exact coefficient formula and norm asymptotic are credited to Bénéteau–Manolaki–Seco, arXiv:1901.00694, Section 7. The present additional statements concern the off-zero boundary and interior profiles, with the previously published Hardy coefficient profile acknowledged explicitly.
