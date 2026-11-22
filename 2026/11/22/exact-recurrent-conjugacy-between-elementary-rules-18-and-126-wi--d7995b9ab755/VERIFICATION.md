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

The proof is a truth-table factorization of the two global finite-ring maps and a constructive inverse on every fixed-iterate set. It does not rely on extrapolation from a finite search. The basin identity follows from the two-element fibers of cyclic XOR differences and equivariance of the dynamics.

Run `python3 verification/structural_check.py` from the package root to reproduce the local-factorization truth tables, periodic-core correspondence for every ring through circumference sixteen, and the per-orbit basin transfer identity; the final line is `STRUCTURAL_OK`. Run `python3 verification/direct_orbit_check.py` for an independent bitwise simulation and temporal-cycle census through circumference fifteen; the final line is `DIRECT_ORBIT_OK`. Both programs were executed from the package contents, with their actual outputs embedded. The finite examples do not constitute an infinite proof; the factorization and fixed-iterate bijection do.

Full transient functional graphs and individual basin sizes on arbitrary rings are not asserted equal. The result concerns finite rings, not an unqualified conjugacy of infinite-configuration cellular automata. Independent external validation has not been performed.
