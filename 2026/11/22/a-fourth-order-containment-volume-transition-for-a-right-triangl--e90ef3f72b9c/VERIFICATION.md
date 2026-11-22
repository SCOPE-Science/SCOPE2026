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

The analytic proof derives the exact translated-fiber widths and integrates them over all oriented scale-rotation multipliers; no asymptotic or infinite conclusion is inferred from finite samples. The symbolic vertex computation in `checker.py` examines every four-element subset of the twelve defining inequalities. The script solves nonsingular active systems over rational numbers, computes exact feasible aspect-ratio intervals, proves that their only boundaries at ratios at least one are one and two, and counts distinct solutions on each interval and at each boundary.

The same script verifies the piecewise volume identities using exact rational arithmetic. Each branch is a polynomial of degree at most four and five distinct input values per branch suffice for an identity check. Independent four-dimensional convex-hull computations at aspect ratios \(1/2,3/4,1,1.001,1.25,1.9,2,2.001,2.4,4,10\) matched the stated volumes and vertex counts; these floating-point computations are not used to certify the theorem.

Run `python3 checker.py` using Python 3.8 or newer. No external data downloads, symbolic algebra packages or proprietary software are required. Historical novelty remains subject to the cited literature-coverage limitations. Independent external mathematical verification has not been performed.
