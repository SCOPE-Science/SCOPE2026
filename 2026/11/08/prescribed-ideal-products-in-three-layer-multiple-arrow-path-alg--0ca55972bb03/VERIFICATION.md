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

The unrestricted claim follows by Peirce decomposition of radical ideals and finite-field subspace counting. It does not rely on finite experiments.

Run `python3 check_ideal_products.py` to exhaustively enumerate ideals and all ordered products over the prime fields of orders 2 and 3. The output should agree exactly with `check_ideal_products.out` and terminate with `ALL_THREE_LAYER_IDEAL_PRODUCT_FIBERS_PASS`. The program checks total ideal counts, zero fibers, commuting ideal pairs, and every nonzero prescribed-product fiber in six small configurations.

Run `python3 check_mass_identities.py` to check the Gaussian-coefficient mass and symmetry identities across 175 parameter configurations; its output should match `check_mass_identities.out` and terminate with `ALL_THREE_LAYER_IDEAL_MASS_IDENTITIES_PASS`. For nonprime prime-power arguments, this second program checks integer polynomial identities, not an extension-field multiplication table.

The complete proofs of tensor support uniqueness and of the commutativity partition are in `RESULT.md`. External review and independent mathematical validation have not been performed.
