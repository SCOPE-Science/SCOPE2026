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

Execute `python3 verify_bv_broken_affine.py` with Python 3 standard library only. The checker uses exact `fractions.Fraction` arithmetic and tests: local \(L^2\) moment equations for \(98\) rational jump positions; exact sharp step witnesses for one, two and three or more cells; \(1{,}790\) additional rational jump positions on four meshes including nonuniform examples; and \(2{,}400\) randomized rational signed-multijump pairs across one to eight nonuniform cells.

Expected output:

```text
EXACT_PROJECTION_NORMAL_EQUATIONS_AND_WITNESSES_PASS
EXACT_SINGLE_JUMP_MESH_SWEEP_PASS 1790
EXACT_MULTIJUMP_NONUNIFORM_TESTS_PASS 2400
ALL_SHARP_BV_BROKEN_AFFINE_PROJECTION_CHECKS_PASS
```

The mathematical proof is the jump-representation reduction and exact maximization of two endpoint-trace polynomial profiles in `RESULT.md`. Computation is finite confirmation, **not** proof for infinitely many meshes or \(BV\) inputs. This record contains no external independent validation; unindexed overlapping prior literature remains a priority risk.
