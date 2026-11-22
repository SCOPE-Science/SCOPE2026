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

## Reproducibility
`verify.py` requires only the Python standard library. Execute `python3 verify.py` from a directory containing this extracted file. The program independently computes the transitions from the state definitions, checks the induced cyclic rotation and predecessor-collapse maps, the exact witness length and absence of three consecutive rotations, and the single-state image for every integer from 3 through 100. It also performs a breadth-first exhaustive search over the finite product of reachable subset images and the no-double-rotation pattern monitor for integer sizes 3 through 15. The expected terminal marker is `BLOCK_RENORMALIZATION_OK n=3..100`.

## Limits
These bounded executions do not certify all integer sizes; the written invariant and induction in `RESULT.md` furnish the general proof. The asserted upper bound is not claimed to be the exact constrained optimum. Independent mathematical audit: not performed.
