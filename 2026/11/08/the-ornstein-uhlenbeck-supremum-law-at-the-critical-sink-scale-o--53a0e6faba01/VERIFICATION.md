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

# Verification scope and reproducibility

The accompanying `check_finite.py` is standalone Python 3 source using only standard-library exact rational arithmetic. Run:

```bash
python check_finite.py
```

The observed output from the saved file is:

```text
PASS: 69812 exact finite assertions
```

Checks cover exact transition probabilities in the \(p\)-biased Bernoulli-refresh chain, normalization, conditional drift and second moments, binomial detailed balance and stationary moments, product-measure invariance under each fixed-coordinate refresh, and the integer no-overshoot boundary property. Parameters include many small state-space sizes and rational sleep/sink probabilities.

The infinite theorem depends additionally on the independent-Gaussian/stationary-OU functional limit, maximal early-contact exclusion, late-contact tightness, regularity of the OU first-crossing map, and the conditional stationary time-shift calculation. Those steps are reasoned in `RESULT.md`; finite testing is not a substitute for their proofs. No separate mathematical audit or external replication was performed. The claimed limiting distribution has not been asserted to imply finite-model moment convergence.
