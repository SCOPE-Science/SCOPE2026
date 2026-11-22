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
The complete proof is in RESULT.md. To reproduce the finite independent examples, run `python3 checker.py` from the directory containing the embedded files. The checker uses Python standard library only and verifies rational grid cases in four arities, 27,000 sampled rational vectors for rational shifts, and 99 numerical lower-bound identities. The expected terminal marker is `VERIFY_OK`.

## What has been checked
The all-vector scalar envelope and universal lower bound are proved analytically for all integer arities at least two. The rational-root theorem certifies nonattainment for every arity from three onward, conditional only on the specified rational-constant finite syntax. Evaluating all modal operators on a singleton unit loop is exact and gives the depth-independent restriction. No finite sampling is used to assert impossibility on infinite models.

## Remaining limitations
Numerical tests are corroborative, not independent mathematical certification. The motivating uniform-interpolation paper's full text was inaccessible for direct comparison, and potential older general approximation statements remain an originality risk. Independent audit: not yet performed.
