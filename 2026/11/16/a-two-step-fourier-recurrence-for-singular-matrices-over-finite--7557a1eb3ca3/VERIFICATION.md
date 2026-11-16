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
The formula was checked by independently transforming the determinant-zero indicator on the complete additive matrix group over the cyclic rings of orders 2, 4, 8, 3, 9 and 27 (ring-element moduli). The six cases have respectively 16, 256, 4096, 81, 6561 and 531441 Fourier frequencies. Every coefficient agreed with the Smith-type recursion; transforms were rounded only after residuals below \(10^{-6}\) were checked. The tests also included exact Walsh transforms in the equal-characteristic chain rings \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) and \(\mathbb F_2[\varepsilon]/(\varepsilon^3)\), with respectively 256 and 4096 Fourier frequencies, matching every coefficient exactly.

The proof uses a primitive-vector factorization, exact character orthogonality, and a two-length induction; it does not infer the general statement from the finite computations. The sharp endpoint norm follows by summing all signs after evaluating every length-three Smith class. To repeat: `python CHECK.py` (Python 3, NumPy installed). Independent mathematical validation and exhaustive historical-priority verification have not occurred.
