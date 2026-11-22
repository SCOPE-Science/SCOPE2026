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

Run from the directory containing this document:

```text
python3 verification/check_lo_poset.py
```

Requires Python 3 only. The program recomputes the closed-channel counts from exact finite double sums for chain sizes \(0\) through \(16\), enumerates all finite transitive relations compatible with each possible placement of two distinctly named points into a linear extension of old chains of sizes \(0\) through \(7\), and compares the orientation channels. This second implementation does not rely on cut conditions. It also checks exact ratios. The accompanying `verification/output.txt` is actual recorded program output and ends with `ALL_LO_POSET_CHECKS_OK`.

The infinite statements are not consequences of finite enumeration alone. Their proof is the classification of possible cuts, the exact finite double-sum expressions, the degree-six polynomiality argument, seven initial-value identities, and elementary algebra for the limiting and monotone ratios. The two-term rational polynomial expressions have been checked against the exact sums. Unproved limitations: no arbitrary-base extension or higher-arity result is asserted, and historical uniqueness is not established.
