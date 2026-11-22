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

# Finite verification and limits

The attached `verify_census.py` runs without external packages and enumerates every unlabelled strict poset through eight vertices, via one-maximal-element additions, all ideals and exact backtracking for isomorphism. It calculates every complete compatible ideal/filter pair at each size. Independent checks use explicit ternary one-point extensions of all posets of size at most five and 25 deterministic representatives at each larger size, plus both witness posets. `verification_output.txt` is the output of a successful execution, and `census.json` holds all 31 collision fibres. The classical unlabelled class counts are matched exactly; no probabilistic evidence or extrapolation is needed for the sharp eight-point classification.

Mathematical limits: higher-order posets are not classified; prior publication priority remains provisional; and an independent audit of the code and reasoning has not been performed.
