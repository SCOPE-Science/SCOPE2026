---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The unchanged companion `verify_extended_hasse.py` is a Python 3 standard-library checker. Run `python3 verify_extended_hasse.py` in the directory containing it. The expected final line is `EXTENDED_CIANI_HASSE_OK`. The script checks equality of the vectors from three coefficient computations at the primes \(5,7,11,13,17,19,23,29\): the original plane quartic, the transformed Deuring polynomial, and the square-completed genus-one equation. The original accompanying notes report a successful run. These checks concern normalization in an explicit finite test set, not an independent proof of the uniform claim.

The all-prime argument in `RESULT.md` uses the central coefficient of a monic quadratic to extract the discriminant power and then applies two binomial identities over \(\mathbb F_p[a]\). It does not infer the last root from a comparison of root sets on the smooth locus. After the polynomial identity is established, the classical simplicity and field of definition of the Legendre–Deuring roots imply the exact multiplicity and the smooth root count.
