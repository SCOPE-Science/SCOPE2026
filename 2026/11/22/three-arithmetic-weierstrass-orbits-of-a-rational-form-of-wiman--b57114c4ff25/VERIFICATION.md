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

# Reproducibility and scope

Run `python3 verify_cyclotomic.py` in the same folder as this file and the scientific result. The program requires only Python's standard library. It checks the coefficientwise Fourier trace identities modulo the fifth cyclotomic polynomial, the golden-ratio relation, all five branch products and rotations, the three exact radical square identities, and the combinatorial orbit sizes for the two independent Kummer involutions. It prints `HUMBERT_FIVE_EXACT_IDENTITIES_OK` on success.

The geometric and arithmetic proof additionally uses exact standard facts independently explained in the result: smoothness from a rank-three Vandermonde Jacobian, canonical adjunction for a complete intersection of three quadrics, the nonzero jet Vandermonde, the total genus-five canonical Weierstrass weight, irreducibility and signature of the quartic \(U^4-U^2-1\), and the Galois action on the chosen cyclotomic square root of five. The script does not stand in for these arguments; it is a reproducible check of their algebraic identities and finite group-action bookkeeping. No independent audit or external validation is asserted.

An optional, separately supplied finite-field sanity program `check_good_reduction_examples.py` performs direct enumeration of the projected forty-point support for a few specified good primes. It is a finite spot-check, not a proof of the characteristic-zero field-degree theorem or an assertion about all prime reductions.
