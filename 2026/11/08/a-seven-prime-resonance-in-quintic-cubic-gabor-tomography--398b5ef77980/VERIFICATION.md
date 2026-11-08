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
# Reproducible checks

Run `python3 check.py` using Python's standard library. This script builds a complete exact table of the root-count criterion for ambiguity zeros for every phase-coefficient pair at primes \(2,3,5,7,11,13,17,19\), then tests five further nontrivial instances at primes \(23,29,31,37\). It compares complete zero sets, not only total ranks, and therefore checks the precise exceptional Weyl directions at \(p=7\). The success marker is `QUINTIC_CUBIC_GABOR_RANK_CLASSIFICATION_PASS`.

The proof establishes all primes using cyclotomic minimality, power-sum constraints, and explicit small-field verification, while finite computations corroborate it. A direct numerical singular-value test, separately performed for the small primes, agrees with the integer zero-set ranks; it is not relied on for infinite quantifiers. The full text of one earlier polynomial-phase correlation source was unavailable for comparison, and no independent mathematical audit or external certification has been performed.
