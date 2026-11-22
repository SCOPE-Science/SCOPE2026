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

The `checker.py` file is a standalone Python 3 program requiring only the standard library. Invoke it as `python3 checker.py`. Its finite checks reconstruct both integral quotient polynomials from their cyclotomic factors and verify their evaluations against the original twelve-term repunits at 25 sample bases. The exact Sylvester determinant is computed by fraction-free integer elimination and checked against \(2^{10}5^2 7^2 13^8\). Every residue modulo \(2\), \(5^2\), \(7^2\), and \(13^2\) is examined, proving the relevant finite root lists and absence of any simultaneous square-power lift. All \(455\) CRT residues are compared with the claimed local product, and the exact frequency vector is checked. For a separate direct evaluation check, both lengths six and twelve are tested for all integer bases from \(2\) to \(4001\), producing 8,000 direct GCD comparisons.

The proof of the infinite family rests on classification of pairs of unit-circle roots and the nonzero-resultant Bézout bound; the finite program checks the exact twelve-digit arithmetic certificate and cannot by itself prove the all-length assertion. In particular, this program does not determine full spectra at any length greater than twelve, nor does it certify publication priority.
