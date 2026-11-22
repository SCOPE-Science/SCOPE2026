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

# Reproducibility

Place `verify_tm3.py` and `tm3_coefficients.json` in one directory and run `python3 verify_tm3.py` with a standard Python 3 interpreter. The program asserts rational polynomial identities for both parity classes, base cases, row extraction, and independently verifies small instances. Successful completion prints `VERIFY_OK`.

The stored 128 coefficient-polynomial entries are read as exact numerator/denominator rational pairs; the arithmetic uses `fractions.Fraction`. The matrix identities are checked symbolically as ordinary polynomial coefficient equality and therefore certify all integer morphism depths after the direct two base cases. Finite enumerations through length eight for every binary input, explicit deletion enumeration on morphic inputs through length 32, and a distinct last-occurrence dynamic program through length 16384 are corroboration, not infinity claims.

The proof does not assert results for non-dyadic lengths or different deletion counts. Earlier equivalent work remains an originality risk; independent audit has not been performed.
