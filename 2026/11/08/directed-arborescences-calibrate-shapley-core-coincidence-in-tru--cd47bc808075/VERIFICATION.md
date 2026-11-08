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

# Reproducibility

Run `python verify_trust.py` with Python 3 and its standard library. The test uses exact fractions, direct evaluation of every coalition's worth, and direct permutation averaging for each Shapley value. The comparison formula is then checked independently. Enumeration of rooted out-arborescences is separate from the algebraic identity. Fixed pseudorandom sampling for five- and six-vertex instances has seed `271828`.

Expected output:

```
EXACT_CHECKS_OK graph_parameter_checks=1528 calibrated_strongly_connected=369 tree_identities=257
4-vertex calibration: ['2/3', '2/3', '2/3', '4/9'] core/Shapley: ['4/3', '4/3', '4/3', '4/3']
```

The verifier exhausts all directed graphs of orders three and four meeting the indegree restriction, testing four additional positive score vectors per graph; the larger graph checks are sampled. The 257 arborescence cases are exhaustive at orders three and four within that restricted graph class. The verifier also checks core feasibility against all coalitions in its sampled/exhaustive cases. None of these computations constitutes a proof for arbitrary order; the standalone proof in `RESULT.md` is decisive.

No independent audit has been performed.
