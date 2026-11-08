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

# Reproducible mathematical checks

Use Python 3 standard library only, in the same directory as `verify_two_cluster_metric.py`:

```sh
python verify_two_cluster_metric.py
```

The checker independently enumerates Pruefer-coded spanning trees, tight-edge signs and all feasible extreme potentials on 18 small rational metrics, comparing their exact rational centered variances with the stated two-integer formula. It checks the \(s=3/2\) law for all 1,089 pairs of cardinalities from 2 through 34 and both endpoint formulas for all 529 pairs from 2 through 24. The program produces four success lines or stops with an assertion. Finite enumeration cannot certify the general infinite parameter statement; the tight-edge graph lemma and exact square completion in RESULT.md are the universal proof.

No independent mathematical audit has been performed.
