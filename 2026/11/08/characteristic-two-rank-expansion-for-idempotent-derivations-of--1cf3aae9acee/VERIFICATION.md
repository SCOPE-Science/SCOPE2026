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

The standalone `verify.py` generated and checked all derivation matrices for generator dimensions \(n=2\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), and \(n=3\) over \(\mathbb F_2\). It reconstructs the induced map on \(\bigwedge^2 V\) from the derivation identity, independently tests full-matrix idempotence and ranks, and matches all predicted counts. Executed output ends in `VERIFY_OK`.

These are finite exact computational tests. The general theorem for all prime-power finite fields and all \(n\ge2\) is proved symbolically in `RESULT.md`. Independent audit has not been performed.
