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

Run `python3 CHECK.py` in a standard Python 3 environment. It checks all binary strings at lengths 1 through 16, reconstructs minimal forbidden words from absent words with legal one-letter-shorter prefix and suffix, compares exact Fibonacci language complexity, and enumerates quadratic sparse-generator families for 12 indices. The actual execution printed:

```text
PASS: 135165 exact finite strings checked; lengths 1..16 and sparse-family levels 0..11.
These finite checks are not proofs of infinite-language, entropy, or novelty assertions.
```

The proof in RESULT.md establishes the infinite extension criterion, the all-length factor identity, completeness of the minimal forbidden list, and the entropy asymptotics. Exhaustion at fixed finite lengths cannot prove those statements and is not used as their justification. General priority and independent validation remain open.
