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

The algebra's \(8\)-element monomial basis by squarefree subsets was used to construct all regular multiplication matrices. For each coefficient tuple over \(\mathbb F_q\), the supplied checker computes the matrix-power ranks and reconstructs the nilpotent Jordan partition. Exhaustive enumeration was completed over \(\mathbb F_3\) and \(\mathbb F_5\), with \(2187\) and \(78125\) elements respectively; the results exactly match every listed partition multiplicity. Separate exhaustive \(\mathbb F_2\) and \(\mathbb F_4\) tests verify only the excluded boundary; \(50000\) sampled elements each over \(\mathbb F_7\) and \(\mathbb F_{11}\) produced no partition outside the theorem's support. See `checker.py` and `checker_output.txt` for reproducibility.

The proof's irreducible checks are the unit-normal-form reduction, the kernel of multiplication by \(x+\delta yz\), the determinant \(-2\) of the degree-one-to-degree-two map for \(x+y+z\), the identity \((x+y+z)^3=6xyz\), and the final polynomial-count sum \(q^7\). Each is explicit in `RESULT.md`. Exhaustive finite tests do not prove the theorem for every odd finite field, and they do not certify historical priority. Independent mathematical audit has not been performed.
