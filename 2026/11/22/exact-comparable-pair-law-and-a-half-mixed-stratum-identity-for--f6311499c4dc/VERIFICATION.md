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

Run `python3 checker.py` from the extracted file directory. This uses only the Python standard library and is deterministic (seed 161127). The observed output is:

```
SIGNED_POSITIVE_PAIR_COMPARABILITY_PASS exact_dimensions=79 ambient_rejection_pairs=240000
```

For each integer \(n=2,\ldots,80\), `checker.py` evaluates the beta integrals as exact rational numbers and verifies the three unconditional sign-stratum masses, total probability, conditional sign-composition law, and strict comparison with the cube probability. Its separate randomized diagnostic samples the defining inequalities by ambient-cube rejection, without conditioning on the proof's cap decomposition, for \(n\in\{2,3,4,5,6\}\). It checks 48,000 independent point pairs per dimension, and the mixed-stratum frequency for \(n\le5\).

The complete general proof is the sign-stratum integration in `RESULT.md`; the exact-rational finite checks and random diagnostics are not themselves a proof for unbounded \(n\). The ambient-cube rejection method is also not intended as an efficient high-dimensional sampler; the exact cap-mixture sampler follows analytically from the proved decomposition. Originality is based on inspected literature and may require a later historical-priority assessment.
