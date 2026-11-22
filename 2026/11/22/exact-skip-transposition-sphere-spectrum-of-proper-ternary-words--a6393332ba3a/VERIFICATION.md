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

The attached `checker.py` runs using the Python standard library. It enumerates every proper ternary word of lengths \(2\) through \(13\), performs all position-distance-two swaps directly, tests the outputs for properness, and compares each result with maximal sign-run counts. Separately, it constructs the exact degree distribution by the integer ordered-composition recurrence implied by \(A(z,u)=z+uz^2+z^3/(1-z)\). The resulting \(24{,}570\) word instances, complete degree distributions, extremal multiplicities, and moment formulas pass all assertions.

The proof in `RESULT.md` establishes the all-length theorem. Finite enumeration is not an infinite certificate, and this verification is not an independent mathematical audit.
