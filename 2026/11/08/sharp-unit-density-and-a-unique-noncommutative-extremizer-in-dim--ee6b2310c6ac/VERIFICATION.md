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

# Verification and limits

Execute `python3 verify.py` using Python 3 standard library only. The recorded output is stored in `verify-output.txt`.

The checker constructs the Frobenius-skew extension explicitly over the quadratic fields of orders \(4,9,25\), checks the noncommuting multiplication witnesses and unit/nonunit counts, checks explicit two-sided inverses in the smaller examples, verifies associativity of the smallest ring exhaustively, and enumerates all semisimple field-degree profiles with degrees at least two and a nonzero radical within vector-space dimension seven. Each of the latter tests is a necessary dimension criterion, not a constructed classification of all rings.

The exact bound and uniqueness for **all primes** follow from the proof using Artin–Wedderburn, the separable semisimple complement theorem, field-module dimension divisibility, and classification of the two possible automorphisms of the quadratic finite field. No computation here establishes a universal algebra classification on its own.

Historical-priority limitation: the 1986 Kobayashi–Koh classification was identified but not read in full. Independent scientific audit has not been performed.
