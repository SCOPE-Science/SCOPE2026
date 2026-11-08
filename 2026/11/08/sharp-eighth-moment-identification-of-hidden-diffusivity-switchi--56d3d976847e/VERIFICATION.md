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

# Reproducibility and proof boundary

The accompanying `verify_stationary_moments.py` requires Python 3 and uses only the standard library. From the directory containing the files, run:

```text
python3 verify_stationary_moments.py
```

Observed output from the packaged source file:

```text
PASS 114 exact rational assertions
shared (m2,m4,m6) = [Fraction(3, 1), Fraction(111, 4), Fraction(1755, 4)]
distinct m8 = 79485/8 1749195/176
distinct entropy production = 3/32 8/27
```

The code separately calculates the weighted occupation moments from the two-state transport generator, the position moments from the coupled Markov-switching diffusion generator, and moments from the Gaussian beta-mixture representation. It compares exact fractions for five nondegenerate parameter choices, checks the inverse map, and verifies the two exact lower-moment ambiguity witnesses. No simulation is used as evidence for an all-parameter conclusion.

The mathematical proof in RESULT.md—not this finite diagnostic test—establishes the general stationary representation, strict admissible-data domain, inversion uniqueness, and existence of a continuum of lower-moment ambiguities. The source entropy-production formula is attributed in RESULT.md. Testing does not establish robustness to noisy or finite-sample moments. No independent scientific audit or external certification has been performed.
