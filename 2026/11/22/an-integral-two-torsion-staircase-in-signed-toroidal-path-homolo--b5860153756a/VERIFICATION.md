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

The core proof in `RESULT.md` supplies the unique-midpoint alternating-path argument, an integral unit-pivot contraction compatible with translations, the natural product-chain isomorphism over \(\mathbb Z\), and the signed-incidence Smith reduction. These steps are necessary to extend the finite checks to all cycle lengths and dimensions.

Run `python3 verify_signed_toroidal.py` with Python 3 and SymPy. The output must agree byte-for-byte with `verification.log`. The program uses exact integer Smith normal forms of signed incidence and cubical tensor boundaries and mod-two elimination of all allowed paths through degree six in the indicated finite cycles. A finite mod-two rank is not an integer homology calculation or an exhaustive proof for every length.

All outputs refer to the defined chain-before-homology anti-invariants. The anti-invariant subgroup of ordinary cover homology is not calculated by the signed chain model.
