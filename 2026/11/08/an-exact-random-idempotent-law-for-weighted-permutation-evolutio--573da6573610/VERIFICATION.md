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

# Finite exact-arithmetic verification

Execute `python3 verify.py` in the directory containing this document and the companion script. Python's standard library suffices. The script enumerates all nonzero weights and all permutations for each listed field/dimension pair and computes every idempotent by independently checking the defining quadratic equations over each field. Fields of order four and eight use explicit binary irreducible polynomials.

The independent predicted frequency table is obtained by enumerating permutation cycle types and applying the power-map root count. Expected probabilities are rational numbers; the comparison to exhaustive observed counts uses exact integer and `Fraction` equality. The tests also check that the unconditional expected total number of idempotents is \(n+1\) in every case, and, for the quaternary field, confirm the zero-idempotent probability, that every total count is a power of two, and the coefficients of the claimed second-moment rational function.

The actual executed result concluded with `VERIFY_OK cases=21 matrices=6559`. The verification output is included verbatim as `verification_output.txt`.

The proof of the general theorem, the probability-zero assertion in odd dimensions, and the asymptotic statements are symbolic. The finite checks are corroborative, not infinite certificates or independent validation. No independent audit has been performed.
