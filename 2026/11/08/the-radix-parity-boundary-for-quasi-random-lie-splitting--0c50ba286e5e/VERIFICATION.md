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

The statement and derivation are in `RESULT.md`. The attached `verify.py` uses only the Python standard library and exact rational arithmetic. It evaluates independent radical-inverse digit tests for radices \(2\) through \(13\), the source's half-interval sign prefixes, even-base periodicity and cancellation, odd-base recursive blocks, exact discrepancy subsequences, and the coefficient of \(E_{13}\) in the complete numerical three-by-three product. Running `python verify.py` yielded `VERIFY_OK exact rational tests: 4128`.

The nonstandard critical facts are proved without relying on the program: the recursive central digit in odd radix, the explicit logarithmic imbalance, the Abel bound with uniformly varying propagated defects, and the nilpotent matrix-product identity. Numerical enumeration cannot prove the infinite cases. The proof assumes bounded generators, exact exponentials, two split operators and a fixed finite terminal time. Novelty is assessed against accessible primary literature and published research records, not independently certified.
