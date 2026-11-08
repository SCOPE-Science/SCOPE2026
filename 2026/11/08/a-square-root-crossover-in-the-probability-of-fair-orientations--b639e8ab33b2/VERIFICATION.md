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

# Mathematical verification

Run `python3 verification/check_multistar.py` from this finding's root with Python 3; there are no external dependencies. The script constructs all labeled good orientations on 85 small stars with at least two leaves, computes literal EFX over every ordered pair of agents and every good deletion, and compares to the independent-binomial-count inequalities. It then compares the exact dominant-spoke binomial-slice identity (including odd-parity correction) with exhaustive finite allocation counts for valid small parameters. All included checks pass.

The infinite Gaussian and local-limit claims are justified by the argument in RESULT.md, not by finite enumeration or a numerical test. They require a fixed number of leaves, divergent subsidiary spoke multiplicities, and subsidiary total small relative to the dominant spoke. The EFX convention includes deletion of goods that a particular agent values at zero. The independent audit status is not performed.
