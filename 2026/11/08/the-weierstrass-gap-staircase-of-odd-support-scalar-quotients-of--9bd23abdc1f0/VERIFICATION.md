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

The mathematical argument proceeds from the smooth affine cover's monomial basis and tame invariant-ring decomposition, then computes distinct pole residues and the full Apéry set. The pole valuation and generic scalar quotient are taken with the exact assumptions in the cited 2026 construction.

Run `python3 CHECK.py` in a directory containing this file and the standalone checker. Its assertions check 28 finite \((r,h)\) pairs, including prime powers \(r=9,25\); independent dynamic-programming membership checks are performed for the bounded cases \(r\le11\), \(h\le3\). All integer identities, pseudo-Frobenius classifications and weight sums passed the recorded run.

The finite tests do not establish the universal theorem, exclude alternative historical publications or constitute independent validation. The universal proof is in `RESULT.md`. An independent mathematical audit has not been performed.
