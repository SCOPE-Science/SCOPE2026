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

The theorem follows for all cycle orders from the Dirichlet Green function and Sherman–Morrison identity, with the boundary cases stated explicitly. The standalone checker `verify_chord_sandpile.py` requires Python's standard library only. Execute `python verify_chord_sandpile.py` to replay rational matrix comparisons for all 120 nonsink chord insertions with 4 through 11 vertices, plus independent burning-test and avalanche enumeration for 20 chord insertions with 4 through 7 vertices. Its finite checks include exact stationary means and number of recurrent configurations; they are not an infinite proof. The near-doubling ratio is additionally evaluated for four large sizes and proved symbolically in RESULT.md. Self-review has been performed, but no independent audit has been performed.
