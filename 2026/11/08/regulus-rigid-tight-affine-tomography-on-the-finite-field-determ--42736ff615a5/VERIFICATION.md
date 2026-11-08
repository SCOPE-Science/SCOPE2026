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

# Verification record

The primary proof consists of the determinant-rank-one parametrization, the two ruling incidence relations, nondegeneracy of the determinant polar form in every characteristic, finite-field character orthogonality on coset sums, and a complete grid-kernel argument. These steps establish the results for all prime powers without extrapolating finite enumeration.

For computational corroboration, run `python null_regulus_checker.py` with Python and NumPy. The script constructs \(\mathbb F_2\), \(\mathbb F_3\), and the extension field \(\mathbb F_4\); checks every generator has \(q^2\) elements and every cross-ruling pair meets in exactly \(q\) elements; constructs full affine incidence normal matrices; tests four unweighted direction sets and three nonuniform positive-weight sets; and diagonalizes the entire integer normal matrix for each design. Full eigenvalue multiplicities must agree exactly with the theoretical table, after a numerical eigenvalue-to-integer tolerance of \(10^{-7}\). The verification does not treat all fields computationally and does not constitute independent validation.

Remaining limitations include unknown publication priority within inaccessible older finite Radon literature and excluded measurements with selectively missing individual cosets.
