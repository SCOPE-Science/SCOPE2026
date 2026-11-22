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

The included `verify_prism.py` is a standalone, standard-library Python 3 verifier for the finite statements used by the proof. Running it directly from the extracted package checks all 256 by 256 entries in the min-plus matrix identity, all base values for orders 5–17, an independent whole-graph exhaustive test for orders 3–8, and direct validation of three explicit witnesses.

The certificate checks 729 allowed transitions, 41,728 finite matrix entries at the eighth and eighteenth powers, and exact weight shift eight at every finite entry. In particular, the certificate is a finite exhaustive identity rather than a finite experiment offered as proof of an infinite claim. Infinite quantification follows from the graph-to-window bijection and min-plus associativity proved in RESULT.md.

Independent mathematical validation and exhaustive publication-priority investigation have not been performed. No claim is made about full configuration-count polynomials or other graph families.
