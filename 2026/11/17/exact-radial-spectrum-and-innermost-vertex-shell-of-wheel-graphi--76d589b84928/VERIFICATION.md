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

# Reproducibility checks

Run `python3 verify_wheel.py` next to this file. This is a standalone Python 3 standard-library program; no external mathematical packages or downloaded data are required.

The checker tests every orientation of the wheel with \(m\) rim vertices, for \(m=4,5,6,7,8,9\). It independently builds the directed graph edge by edge, computes indegrees and squared Euclidean vertex norms, and determines acyclicity by Kahn's topological ordering. A separate four-state polynomial dynamic program computes coefficients of the stated \(F_m(u,v)\). The checker then compares both complete bivariate distributions, the inner radial shell, the \(m k(m-k)\) equality counts, the all-orientation count, and boundary conditions.

Verified console summary:

```
m=4: oriented_edge_assignments=256, vertices=78, first_squared_norm_times_4=20, first_shell_size=16, radial_shells=5
m=5: oriented_edge_assignments=1024, vertices=240, first_squared_norm_times_4=22, first_shell_size=60, radial_shells=4
m=6: oriented_edge_assignments=4096, vertices=726, first_squared_norm_times_4=22, first_shell_size=54, radial_shells=11
m=7: oriented_edge_assignments=16384, vertices=2184, first_squared_norm_times_4=24, first_shell_size=168, radial_shells=8
m=8: oriented_edge_assignments=65536, vertices=6558, first_squared_norm_times_4=24, first_shell_size=128, radial_shells=19
m=9: oriented_edge_assignments=262144, vertices=19680, first_squared_norm_times_4=26, first_shell_size=360, radial_shells=13
VERIFIED: 349440 directed-edge assignments, 29466 acyclic orientations, 231 polynomial and boundary assertions
```

These computations are finite consistency checks. The written triangle-path argument, run decomposition and extremal comparison supply the proof for all \(m\ge4\). The self-review is not independent mathematical verification.
