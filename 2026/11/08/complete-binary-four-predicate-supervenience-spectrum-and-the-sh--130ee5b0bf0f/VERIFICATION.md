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

Run `python3 checker.py` using Python 3 standard library. The full computation enumerates 32,768 anchored nonempty binary teams and 65,535 nonempty binary teams, computes each complete dependence closure in two logically equivalent but separately implemented ways, counts isomorphism classes under all 24 predicate permutations, and enumerates 32,768 candidate Moore families. Each claimed numerical result is checked with assertions; the reviewed run terminated successfully with the exact `BOOLEAN_FOUR_SUPERVENIENCE_CERTIFICATE_OK` output recorded in `RESULT.md`.

The enumeration is exhaustive for four Boolean attributes. It does not certify claims about unbounded predicate arity, nonbinary value domains, or historical novelty. The mathematical reason that every possibility occurs in the search is the XOR anchoring lemma, and the semantic correctness of each computed map is the pairwise difference criterion (both proved in `RESULT.md`). There is no external or independent audit certificate.
