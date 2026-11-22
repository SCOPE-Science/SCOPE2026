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

# Exact verification

Run `python3 check.py` using standard Python 3. The test independently enumerates spanning trees of six complete bipartite graphs, checks exact degree-parity profile counts, computes direct signed sums and an independent Walsh--Hadamard transform, verifies complete Fourier support and exact rational projection norms, and tests the Krawtchouk identities through shore order sixteen. Its expected output is `PASS: 672 integer/rational assertions; direct labelled-tree enumeration, Walsh-Hadamard transforms, Krawtchouk identities, projection kernels`. The full all-order claim is proved by the symbolic argument in RESULT.md; enumeration is not used as an infinite proof. No external independent audit has been performed.
