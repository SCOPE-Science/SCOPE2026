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
# Finite exact checks

The complete theorem, assumptions, references, and proof appear in `RESULT.md`. Run `python3 verify_exotic_richelot.py` and compare its \(22\) orbit entries against `orbit_profiles.json`. Both use ordinary finite exact integer arithmetic. Expected first status line:

`GENUS_THREE_30_NONTRACTABLE_22_FROBENIUS_TYPES_VERIFIED`

The program enumerates \(135\) distinct isotropic three-dimensional subspaces of the \(64\)-element even-subset quotient, and separately enumerates \(30\) affine hyperplane families from all \(8!\) label bijections. It verifies equality of the \(30\)-element sets and equality of the two independently calculated orbit spectra for all \(22\) partitions. It also checks all \(105\) pairing kernels, the order-seven subgroup count, absence of rational two-torsion and polynomial irreducibility in the concrete \(\mathbb F_5\) example.

**Limits:** No infinite-field pattern is deduced from finite sampled field sizes; finite combinatorics already exhausts every possible degree-eight Frobenius permutation. Does not certify that an explicit isogeny to a Jacobian over the base field exists. The verification is not an independent audit.
