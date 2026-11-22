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

# Reproducibility and limits

The analytic proof in `RESULT.md` establishes the result for all real \(a\ge1\) and \(\theta\in[0,\pi/2]\), including the two threshold aspect ratios and endpoint conventions. The standalone `scripts/check_rectangles.py` script uses the Python standard library only and recomputes the intersection polygon using independent half-plane clipping rather than the retained-side proof.

Run `python3 scripts/check_rectangles.py`. The run conducted before packaging printed `PASS: 21344 checks; independent polygon-half-plane clipping agrees`. Tested inputs included the angle boundaries, both sharp thresholds, 120 randomized shape parameters, dozens of random angles per parameter, and 11 dense grids checking the global lower bound. The checker is an error-detection aid, not an exhaustive enumeration of real angles and aspect ratios; the infinite-parameter theorem depends on the symbolic proof.

The comparison against accessible published sources is a same-model literature analysis, not an independent priority certification. The 2014 convex-body-rotation paper's full text was unavailable; its abstract was read. The first exact calendar date among selected supporting material is July 26, 2012; an older 1986 geometry-book attribution has year-only evidence, not a verified month/day.
