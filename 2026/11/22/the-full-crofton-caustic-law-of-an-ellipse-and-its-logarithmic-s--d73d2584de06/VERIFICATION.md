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

# Reproducibility and checks

Run `python check_caustic.py` using Python 3 with NumPy and SciPy. The checker recomputes the full CDF by direct integration of the conditional line geometry, separately integrates the complete-elliptic-integral density across both regularity intervals, checks the exact focal-crossing probability, and probes the two-sided logarithmic and terminal coefficient. Two independent random sampling constructions—boundary arclength/angle and offset-angle Crofton lines—are compared against analytic probabilities using fixed pseudorandom seeds. The sample counts and tolerances are printed by the script and are numerical diagnostics only.

The proof in `RESULT.md`, not sampling, establishes the continuum formula. The only non-elementary analytic identity is the standard complete elliptic integral reduction and its classical \(K(k)\sim\log(4/\sqrt{1-k^2})\) behavior. The weak point in originality is possible historical publication of this invariant-measure pushforward under another name; this is not an independently certified discovery. Independent audit: not yet performed.
