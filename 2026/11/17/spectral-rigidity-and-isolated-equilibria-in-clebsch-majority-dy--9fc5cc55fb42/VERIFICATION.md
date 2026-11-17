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

# Reproducible finite checks

Execute from the folder containing all packaged artifacts, with Python 3 and no external dependencies:

```sh
python3 verify_finite_dynamics.py > full_dynamics_output.json
python3 verify_independent_symmetry.py > independent_symmetry_output.txt
```

Both commands were actually executed on the standalone programs accompanying this theorem, and their resulting files match the included captured outputs. Both programs check all 65,536 labelled binary configurations. The first constructs the full 65,536-state deterministic graph, removes nonrecurrent states by indegree pruning, identifies every cycle and computes every backward basin and entry layer. The second implements the update using a distinct direct-neighbor-bit expression, checks all trajectories through six rounds, checks the spectral fixed-vector relation and isolation, explicitly enumerates the full affine group of order 1,920, and verifies the fourteen spatial classes. `recurrent_classes.csv` matches the fourteen printed lines in the second program's output.

The main proof uses exact integer arithmetic and a separate analytical spectral argument. The computations establish a **complete finite** fact, not an all-dimensions theorem or an externally certified formal proof. Independent mathematical audit remains unperformed.
