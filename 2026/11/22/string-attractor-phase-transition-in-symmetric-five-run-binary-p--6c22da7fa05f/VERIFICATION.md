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

# Computational verification and logical boundaries

The all-length theorem follows from the factor-gap argument and three disjoint unique-factor witnesses in RESULT.md. The scripts are intentionally finite consistency checks and do not claim to prove infinitely many cases by enumeration.

`python3 verify_exhaustive.py` computes the exact union of occurrence masks for every factor of each word for all 216 triples with \(1\le a,b,c\le6\). It checks the proposed constructive witnesses, rejects every one-point attractor, rejects every possible pair in the three-point regime, and confirms a pair in the two-point regime. Its recorded output is `verify_exhaustive.out`.

`python3 verify_independent.py` uses an independently coded literal-occurrence scan, not the occurrence-mask method. It checks all displayed constructive positions on 305 triples, verifies that each of the three certificate factors occurs exactly once and their occurrence intervals are disjoint in every tested obstructed triple, and recomputes the exceptional generating-function coefficients by direct compositions for all lengths 5 through 110. The pseudorandom parameter sample uses a fixed seed. Its recorded output is `verify_independent.out`.

The result is restricted to binary, linear, exactly five-run symmetric palindromes with positive parameters, and does not establish an exhaustive bibliographic novelty guarantee. Neither script reports external independent validation.
