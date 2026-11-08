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

# Finite independent computational checks

The standalone `verify_wheel_inball.py` was executed using Python 3, NumPy, and SciPy. It independently constructed all cycle-independent-set halfspaces in the rim coordinates and used a general-purpose linear program to optimize the intrinsic Euclidean inscribed-ball radius. Every integer rim length from \(3\) to \(16\) matched the theorem's exact expression to better than \(2\cdot10^{-8}\). It also checked the number of active inequalities, feasibility of the symmetric center, all generating wheel-edge vertices, and the four corner centers of the exceptional rectangle.

Command:

```bash
python verify_wheel_inball.py
```

Expected terminal marker: `WHEEL_ORDINARY_EDGE_INBALL_LP_CHECKS_PASSED`.

The check does not establish facet exhaustiveness, prove optimality for arbitrarily large rim length, or independently verify historical novelty. The universal proof is the vertex-cover duality and exact facet-distance argument in `RESULT.md`. This is a self-review and independent audit has not been performed.
