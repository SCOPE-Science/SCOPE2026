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

# Verification record

The file `verify.py`, executable with the Python 3 standard library, is a standalone verifier for the exact integral orbit-chain portion of the claim. Execute `python3 verify.py`; it must terminate with `PASS`.

It independently reconstructs all type-B signed partitions at rank five, all strict chains of the proper part, all 120 coordinate-permutation actions, and all rank-ordered orbit cells. It forms the integral cellular boundary and checks each composition is zero. The reported initial orbit-chain ranks are `37,242,471,274`, unit-pivot cancellations are `36,206,265`, and the residual ranks are `1,0,0,9`, with zero differentials. Exact modular ranks at primes 2, 3, and 5 provide separate cross-checks but are not used as a replacement for integral cancellation.

The simple connectivity step is a mathematical application of the ordinary orbit-space fundamental-group theorem and explicit transposition-fixed vertices; it is not asserted from a finite test. The conclusion that the space is a wedge of nine three-spheres then follows from dimension, Hurewicz and homological Whitehead. The verifier does not certify literature priority or any extension to other ranks.
