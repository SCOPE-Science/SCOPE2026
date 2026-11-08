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

The standalone finite calculation is provided by `check.py`. Run `python3 check.py` in this directory. It exhaustively generates binary matrices of orders 2, 3, and 4, tests full rank by exact binary Gaussian elimination, and computes the stabilizer of each matrix under all coordinate permutations. Separately, for order 5 it enumerates every matrix in the fixed subspace of a transposition by its 17 cell orbits and confirms 21,504 invertible members. It verifies the exact formula \(2^{2n-3}|\operatorname{GL}_{n-2}(\mathbb F_2)|\) for a transposition centralizer, counts transposition incidences, and computes isomorphism-class counts using Burnside's lemma. The resulting exact numerical record is in `verification_output.txt`.

The proof in `RESULT.md` separately verifies the monomial reduction, the conditional transposition count, the orbit-codimension estimates, and the error bound for every \(n\ge32\). The script's finite enumeration is **not** a proof of any assertion for all dimensions. No external audit or independent proof certification was performed.
