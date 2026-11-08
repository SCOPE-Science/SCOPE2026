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

# Reproducibility and limits

Run `python3 check_rm_pair.py` from the unpacked file directory. This code generates all affine evaluation vectors and independently computes each cyclic symbol-pair weight from adjacent bits; it does not use the transition formula. It compares the observed weight histogram to the closed formula, and for every threshold from zero through the block length, it obtains the binary rank of all eligible words by elimination and compares it to the proved generation profile. Exhaustive checks cover dimensions \(m=2\) through \(m=8\), or \(1016\) affine words total. The program prints `CERTIFICATE_OK` on success.

The all-dimensions proof is a symbolic argument using carry transitions, a factorization of a finite generating polynomial, and coordinate-span monotonicity; finite enumeration does not certify arbitrarily large dimension. The graph-component statement follows by the Cayley coset argument. Independent mathematical audit has not been performed. Wider literature priority remains open.
