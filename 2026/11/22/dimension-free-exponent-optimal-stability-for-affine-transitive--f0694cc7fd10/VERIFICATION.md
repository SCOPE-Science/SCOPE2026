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

The proof is self-contained after citing the standard Clarkson and Ball–Carlen–Lieb inequalities and the previously published exact affine-transitive synthesis constant. The orbit-average identity, invariance under affine Fourier change of variables, pairwise midpoint bounds, Jensen reduction, Hilbert equality, and two fixed-group sharpness examples are explicitly checked in RESULT.md.

To reproduce the finite sanity tests, run `python checker.py` with Python 3. The checker uses only the standard library. It tests the claimed inequality for complex Fourier signals on full cyclic groups, reflection-transitive two-point sets, and even-residue subgroup supports, across eight exponents; it separately checks two analytical deficit asymptotics. These tests cannot certify the theorem for unbounded group orders or all affine-transitive subsets; that scope is established by the written argument.

Source comparisons distinguish the existing exact symmetry theorem from the new near-equality estimate. The claimed novelty remains conditional on the inspected literature; earlier results about general uniformly convex projections may contain equivalent abstract implications. Exact numerical constants in non-Hilbert estimates are not asserted optimal.
