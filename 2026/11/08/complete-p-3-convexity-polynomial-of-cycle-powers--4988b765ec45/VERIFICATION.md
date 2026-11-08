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

# Reproducible checks

Run `python3 verify.py` (standard library only). The script constructs actual adjacency masks for cycle powers, checks convexity from the definition on every subset for 63 small parameter pairs, verifies two-neighbour closure for 431,136 selected pairs, and reproduces the cyclic-gap counts using integer dynamic programming. Its final output is `VERIFY_OK`.

The mathematical proof is independent of finite exhaustion: the forcing argument works for all integers \(n\ge3\), \(r\ge2\), and exact gap compositions yield all coefficients. No code is used to certify infinitely many graphs, and no independent mathematical audit has been performed.
