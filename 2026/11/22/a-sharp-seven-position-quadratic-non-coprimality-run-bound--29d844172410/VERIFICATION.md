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

The independent-in-the-computational-sense standard-library script `verify.py` enumerates all residue-root masks at eight offsets for primes \(2,5,13,29,53\) and includes three arbitrary single-hit prime-mask placeholders, which cover the possibilities of all remaining prime factors as established by the local lemma. The exhaustive test finds no covering by three distinct local factors. It separately checks the seven values for \(N=1010\), starting at \(a=7\), and twelve CRT examples. The proof, not finite testing of moduli, establishes the unrestricted all-prime upper bound.

This work has undergone only self-review. No independent audit has been performed. Literature priority remains subject to independent verification. The full 2022 and 2017 comparator papers were not read beyond their accessible abstracts.
