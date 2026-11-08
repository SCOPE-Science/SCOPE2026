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

# Verification details

The analytic proof is contained in `RESULT.md`. Its nonstandard steps are the exact cyclic-interval description, complete equality analysis of the balanced supporting inequalities, and the convexity-based demonstration that the remaining interval bounds reduce to singleton bounds. Those steps have been reconstructed for arbitrary \(n\ge3\) and include all equality and boundary cases.

Run `python3 verify.py` in a directory containing the standalone checker. It requires Python 3 standard-library `decimal`, `fractions`, `math`, and `itertools`, with no additional modules or network access.

The checker performs (i) every cyclic interval length for every order \(3\le n\le21\); (ii) exact Gaussian-elimination ranks of the systems of tight supporting hyperplanes; (iii) construction and validation of all vertices of the asserted cube slice for even orders through \(n=20\); and (iv) high-precision checks of the convexity bound at each parameter. The observed final output was `CYCLE_GRAPHICAL_ZONOTOPE_INCENTER_CHECKS_PASSED`.

The finite checks are not exhaustive across all graph orders and are not a substitute for the proof. The scientific comparison was performed against the actual relevant primary literature and previously published inradius and cycle-zonotope statements. Historical priority is provisional; no independent mathematical audit has been performed.
