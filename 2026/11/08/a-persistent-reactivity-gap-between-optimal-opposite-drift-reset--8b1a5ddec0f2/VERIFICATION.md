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

# Verification scope

Run `python3 CHECK.py` in the same directory; it uses only Python 3's standard library. The deterministic test checks the derivative series, the unique-root stationarity residual and signs, all-speed paired inequalities on sampled parameters, and approach to the sharp strong-drift rate difference. The expected final status is `PASS 590 deterministic numerical and coefficient checks`.

The infinite-parameter statements are proved in `RESULT.md` by an absolutely convergent positive-coefficient series and an implicit root expansion. The finite computations are not an exhaustive mathematical certificate. The proof uses a prior published exact mean absorption time for the specified delta-killing normalization. All remainder estimates take fixed finite positive \(D,L,k\). Independent external audit was not performed.
