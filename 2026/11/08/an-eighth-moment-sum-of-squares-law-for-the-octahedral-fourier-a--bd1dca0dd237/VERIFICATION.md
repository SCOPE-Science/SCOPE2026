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

# Verification of exact Fourier eighth-moment identity

Run `python3 octahedral_eighth_check.py` from a directory containing the checker, using Python 3 standard library only. The checker computes the coefficients of the square, cube and fourth power of \(1\cdot(z_1+z_1^{-1})+v(z_2+z_2^{-1})+w(z_3+z_3^{-1})\) as integer Laurent polynomials in \(v,w\), constructs their absolute-square coefficient energies, and verifies exact equality to the predicted expressions by matching every Laurent coefficient. It also counts fourth-power frequency sums, verifies integer values of the all-equal eighth moment and checks cubic-root product-pattern combinatorics for three alphabet sizes. Its final success marker is `OCTAHEDRAL_EIGHTH_EXACT_PASS`.

The exact symbolic check supports the finite expansion. The mathematical proof separately shows that the identity holds for all six original unimodular coefficient phases, that three unit products sum to zero precisely in the equilateral case, and that the alphabet-count and finite-sampling conclusions hold for every declared integer. No numerical sampling, external certificate or independent audit is asserted.
