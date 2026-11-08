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

The proof is an elementary recurrence in the field \(\mathbb F_3\) and a periodic/twisted closure analysis; it covers every integer \(n\ge3\) without experimental extrapolation.

Run `python3 artifacts/verify.py` from the package root using Python 3 standard library. The script checks all ternary vertex labelings on both graph types for \(3\le n\le6\), independently evaluates an \(81\)-state local transfer over \(3\le n\le72\), and verifies the proposed finite strip patterns and all neighbor constraints through \(n=120\).

Independent mathematical audit has not been performed. An older injective-coloring article was accessible only through the published abstract and bibliographic record; this limits historical-priority certainty, not the direct recurrence proof.
