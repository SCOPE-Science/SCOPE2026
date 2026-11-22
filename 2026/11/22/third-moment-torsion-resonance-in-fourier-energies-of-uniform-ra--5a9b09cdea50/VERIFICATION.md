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

The standalone `check.py` requires Python 3 only and checks all three rational sixth-moment identities by building the 203 set partitions of six indices and evaluating each complete coarsening sum as an integer polynomial. It clears a common falling-factorial denominator and checks the resulting polynomial coefficient arrays for exact equality. These checks certify the finite combinatorial reduction, rather than relying on interpolation from finitely many sample sizes.

As a separate check, the script enumerates all 5,040 permutations for size 7 and all 362,880 permutations for size 9, directly computing their Fourier energies and comparing the first three centered moments with the formulas. Complex arithmetic is used only for this numerical cross-check. The derivation of the character-orthogonality reduction, the low-order identities, and the positive difference factors is set out in `RESULT.md`.

No inference is made for even sizes, nonuniform pairing laws, mixed higher-order moments, or power of a combined independence test. Independent audit remains unperformed.
