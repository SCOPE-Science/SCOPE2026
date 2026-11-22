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

The standalone `verify.py` computes scattered `01` counts directly from each literal rotation, without relying on the claimed gap formulas, for all binary necklaces having exactly three ones through length eighteen. It compares those values to the three-root polynomial identity and the formula generated from zero gaps.

An independent enumeration of cyclic zero-gap triples through length eighty-four checks all spectrum fibers against the reflected-complement partner construction. The exact observed run output is:

`VERIFY_OK: independently evaluated 276 binary necklace spectra at n<=18; checked 31780 gap necklaces at n<=84; exact fiber law, direct trace identity, rational partner, and the n=9 example all passed.`

These computations are finite. The infinitely quantified theorem is established by the proof in `RESULT.md`, not by extrapolation from the counts. No independent external audit is asserted.
