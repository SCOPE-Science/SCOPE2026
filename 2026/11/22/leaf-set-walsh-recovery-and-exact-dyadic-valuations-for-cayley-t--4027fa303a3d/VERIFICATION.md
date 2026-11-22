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

The exact-integer verifier `verify.py` was run successfully on the current package contents. It returned 18,541 passing assertions.

The checks comprise direct enumeration of Prüfer strings through eight vertices, a full Walsh transform of the resulting leaf-set counts, a separate calculation using Stirling-number prescribed-leaf-set counts for every character weight through size 34, and exact divisibility and nonzero checks for every character weight through size 128. The exhaustive finite calculations alone do not establish the infinitely many cases; the proof in `RESULT.md` supplies the all-order argument.

No independent audit has been performed. The claimed exact dyadic eigenvalue valuations are not claimed to be 2-primary Smith invariant factors.
