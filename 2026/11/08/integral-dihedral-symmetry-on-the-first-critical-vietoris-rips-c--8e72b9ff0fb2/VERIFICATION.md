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
# Reproduction and limits

The provided `critical_cycle_verify.py` is an exact finite checker using Python 3 standard library only. Running `python critical_cycle_verify.py` enumerates the complete flag-complex face sets at parameters `k=2,...,8`, the exact predicted consecutive arcs and exceptional triangles, and all 210 natural dihedral actions. It calculates the signed reduced simplicial Lefschetz number of each action and compares with the theorem's formula. The recorded stdout is `critical_cycle_verify.out`.

For arbitrary parameters the proof, not numerical extrapolation, supplies completeness: a two-case classification of all maximal cliques, a good-cover nerve calculation for the arc subcomplex, a degree-one attaching computation for each additional triangle, and the integral equivariant kernel of the resulting augmentation map.

Limits: this verifier does not enumerate unbounded parameters and does not independently prove the topological nerve theorem. The result is self-reviewed; independent mathematical audit is not performed.
