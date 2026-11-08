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

The stationary-equation proof is analytic. The critical conditions are positivity of \(F_\ell'\) and \(F_g'\), unboundedness of the dense flux, the logarithmic divergence of the dilute inverse-coordinate integral at zero, and the interface/source flux matching.

Run the included executable with `python check_flux_core.py` using Python 3.10+ and SciPy. It gives 570 passed deterministic scalar assertions for density exponents \(1/2,3/4,1\), twelve reset-scale choices, a linear and a distinct rational dilute flux, core and gas coordinate inversions, exact mass identities and the sharp optimizer. The checker is supportive and does not constitute a proof for all functions or infinitely many scales.

The principal source arXiv:2610.26149, first publicly released 19 October 2026, was read through its accessible full HTML, including Sections 2–5 and Appendices A–B. Related 2011 and 2021 sources were examined at abstract level. These limits remain relevant to scientific priority; the separate review records them.

No external independent validation has been performed.
