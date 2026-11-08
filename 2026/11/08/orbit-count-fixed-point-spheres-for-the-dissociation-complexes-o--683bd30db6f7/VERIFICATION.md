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

The standalone `VERIFY.py` checks the defining connected-component condition for every expanded fixed simplex, forms the augmented mod-two simplicial boundary matrices, and verifies reduced homology for all integer partitions of arm counts 2–5. It checks 17 orbit partitions and 28,959 faces and prints `ALL_FIXED_SPIDER_CHECKS_OK`. Re-run with `python3 VERIFY.py` and compare to `verification_output.txt`. These calculations do not establish an infinite theorem or integer torsion claims by themselves. The integral and equivariant conclusions are proved in `RESULT.md`.
